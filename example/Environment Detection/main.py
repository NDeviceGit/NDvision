"""
USB 카메라를 사용한 실시간 눈 깜빡임 검출 AI 예제
- 눈이 감겼을 때: 빨간색으로 표시
- 눈이 떴을 때: 초록색으로 표시
- OpenCV Haar Cascade 사용 (dlib 없이도 동작)
"""

import cv2
import numpy as np
import time

class EyeBlinkDetector:
    def __init__(self):
        # Haar Cascade 분류기 로드
        self.face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
        self.eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
        
        # 눈 상태 추적 변수
        self.previous_eye_count = 0
        self.closed_frame_count = 0
        self.blink_count = 0
        self.last_blink_time = 0
        
        # 임계값 설정
        self.min_eye_area = 200  # 최소 눈 영역 크기
        self.blink_threshold = 5  # 깜빡임으로 인정할 최소 프레임 수
        
    def detect_eye_area_ratio(self, eye_region):
        """
        눈 영역에서 열린 정도를 계산하는 함수
        흰색 픽셀의 비율로 눈이 열려있는지 판단
        """
        # 그레이스케일로 변환
        gray_eye = cv2.cvtColor(eye_region, cv2.COLOR_BGR2GRAY) if len(eye_region.shape) == 3 else eye_region
        
        # 적응적 임계값 적용
        thresh = cv2.adaptiveThreshold(gray_eye, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 2)
        
        # 흰색 픽셀 비율 계산
        white_pixels = np.sum(thresh == 255)
        total_pixels = thresh.shape[0] * thresh.shape[1]
        white_ratio = white_pixels / total_pixels
        
        return white_ratio
    
    def detect_eyes_state(self, frame):
        """
        프레임에서 눈의 상태를 검출하는 함수
        """
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # 얼굴 검출
        faces = self.face_cascade.detectMultiScale(gray, 1.3, 5)
        
        eyes_open = True
        detected_eyes = []
        
        for (x, y, w, h) in faces:
            # 얼굴 영역 표시
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            
            # 얼굴 영역에서 눈 검출
            roi_gray = gray[y:y + h, x:x + w]
            roi_color = frame[y:y + h, x:x + w]
            
            # 눈 검출 (얼굴 상단 2/3 영역에서만)
            eyes = self.eye_cascade.detectMultiScale(roi_gray[:int(h*0.6), :], 1.1, 4)
            
            current_eye_count = len(eyes)
            detected_eyes = eyes
            
            # 눈이 검출되지 않았거나 개수가 급격히 줄어들면 감긴 것으로 판단
            if current_eye_count < 2:
                eyes_open = False
            else:
                # 각 눈의 열린 정도 확인
                eye_ratios = []
                for (ex, ey, ew, eh) in eyes:
                    if ew * eh > self.min_eye_area:  # 충분히 큰 눈 영역만 처리
                        eye_region = roi_color[ey:ey + eh, ex:ex + ew]
                        if eye_region.size > 0:
                            ratio = self.detect_eye_area_ratio(eye_region)
                            eye_ratios.append(ratio)
                            
                            # 눈 영역 표시
                            cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 255), 2)
                
                # 평균 비율이 낮으면 눈이 감긴 것으로 판단
                if eye_ratios:
                    avg_ratio = np.mean(eye_ratios)
                    if avg_ratio < 0.15:  # 임계값
                        eyes_open = False
        
        return eyes_open, detected_eyes, faces
    
    def update_blink_count(self, eyes_open):
        """
        깜빡임 횟수를 업데이트하는 함수
        """
        current_time = time.time()
        
        if not eyes_open:
            self.closed_frame_count += 1
        else:
            if self.closed_frame_count >= self.blink_threshold:
                # 충분한 시간 간격이 있는 깜빡임만 카운트
                if current_time - self.last_blink_time > 0.3:
                    self.blink_count += 1
                    self.last_blink_time = current_time
            self.closed_frame_count = 0
    
    def draw_status(self, frame, eyes_open):
        """
        눈 상태에 따라 화면에 표시하는 함수
        """
        if eyes_open:
            # 눈이 뜸 - 초록색
            status = "OPEN"
            color = (0, 255, 0)  # BGR에서 초록색
            cv2.putText(frame, "Eyes: OPEN", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 2)
            # 화면 테두리를 초록색으로
            cv2.rectangle(frame, (5, 5), (frame.shape[1]-5, frame.shape[0]-5), color, 5)
        else:
            # 눈이 감김 - 빨간색
            status = "CLOSED"
            color = (0, 0, 255)  # BGR에서 빨간색
            cv2.putText(frame, "Eyes: CLOSED", (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1.0, color, 2)
            # 화면 테두리를 빨간색으로
            cv2.rectangle(frame, (5, 5), (frame.shape[1]-5, frame.shape[0]-5), color, 5)
        
        # 깜빡임 횟수 표시
        cv2.putText(frame, f"Blinks: {self.blink_count}", (10, 70), 
                   cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255, 255, 255), 2)
        
        # 연속 감긴 프레임 수 표시 (디버깅용)
        cv2.putText(frame, f"Closed Frames: {self.closed_frame_count}", (10, 110), 
                   cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        return frame

def main():
    """
    메인 함수 - USB 카메라로 실시간 눈 깜빡임 검출
    """
    print("USB 카메라 눈 깜빡임 검출 프로그램을 시작합니다...")
    print("OpenCV Haar Cascade 기반 검출 사용")
    
    # 눈 깜빡임 검출기 초기화
    detector = EyeBlinkDetector()
    
    # 카메라 초기화
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("오류: 카메라를 열 수 없습니다.")
        print("USB 카메라가 연결되어 있는지 확인해주세요.")
        return
    
    # 카메라 설정
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
    cap.set(cv2.CAP_PROP_FPS, 30)
    
    print("카메라가 성공적으로 연결되었습니다!")
    print("사용법:")
    print("- 초록색: 눈이 뜬 상태")
    print("- 빨간색: 눈이 감긴 상태")
    print("- 'q' 키를 눌러 종료")
    print("- 'r' 키를 눌러 깜빡임 횟수 리셋")
    
    fps_counter = 0
    start_time = time.time()
    
    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽을 수 없습니다.")
            break
        
        # 프레임 뒤집기 (거울 효과)
        frame = cv2.flip(frame, 1)
        
        # 눈 상태 검출
        eyes_open, detected_eyes, faces = detector.detect_eyes_state(frame)
        
        # 깜빡임 카운트 업데이트
        detector.update_blink_count(eyes_open)
        
        # 상태 표시
        frame = detector.draw_status(frame, eyes_open)
        
        # 얼굴이 검출되지 않은 경우 메시지 표시
        if len(faces) == 0:
            cv2.putText(frame, "No Face Detected", (10, 150), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        # FPS 계산 및 표시
        fps_counter += 1
        if fps_counter >= 30:
            elapsed_time = time.time() - start_time
            fps = fps_counter / elapsed_time
            fps_counter = 0
            start_time = time.time()
        else:
            fps = 0
        
        if fps > 0:
            cv2.putText(frame, f"FPS: {fps:.1f}", (frame.shape[1] - 150, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        
        # 프레임 표시
        cv2.imshow('Eye Blink Detection - NDvision (OpenCV)', frame)
        
        # 키 입력 처리
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('r'):
            detector.blink_count = 0
            print("깜빡임 횟수가 리셋되었습니다.")
    
    # 정리
    cap.release()
    cv2.destroyAllWindows()
    print(f"프로그램을 종료합니다. 총 깜빡임 횟수: {detector.blink_count}")

if __name__ == "__main__":
    main()