"""
Object Detection using YOLOv8
이미지에서 객체를 탐지하고 바운딩 박스와 텍스트 레이블로 표시하는 프로그램
"""

import cv2
import numpy as np
from ultralytics import YOLO
import os
import matplotlib.pyplot as plt

def load_model():
    """
    YOLOv8 사전 훈련된 모델을 로드합니다.
    """
    try:
        # YOLOv8n (nano) 모델 로드 - 가장 빠르고 가벼운 모델
        model = YOLO('yolov8n.pt')
        print("YOLOv8 모델이 성공적으로 로드되었습니다.")
        return model
    except Exception as e:
        print(f"모델 로드 중 오류 발생: {e}")
        return None

def detect_objects(model, image_path):
    """
    이미지에서 객체를 탐지합니다.
    
    Args:
        model: 로드된 YOLO 모델
        image_path: 입력 이미지 경로
    
    Returns:
        results: 탐지 결과
        image: 원본 이미지
    """
    try:
        # 이미지 로드
        image = cv2.imread(image_path)
        if image is None:
            print(f"이미지를 로드할 수 없습니다: {image_path}")
            return None, None
        
        # 객체 탐지 수행
        results = model(image)
        print(f"객체 탐지가 완료되었습니다. {len(results[0].boxes)} 개의 객체가 탐지되었습니다.")
        
        return results, image
    
    except Exception as e:
        print(f"객체 탐지 중 오류 발생: {e}")
        return None, None

def draw_detections(image, results):
    """
    탐지된 객체에 바운딩 박스와 레이블을 그립니다.
    
    Args:
        image: 원본 이미지
        results: YOLO 탐지 결과
    
    Returns:
        annotated_image: 어노테이션이 추가된 이미지
    """
    try:
        # 이미지 복사본 생성
        annotated_image = image.copy()
        
        # 탐지 결과가 있는지 확인
        if len(results[0].boxes) == 0:
            print("탐지된 객체가 없습니다.")
            return annotated_image
        
        # 각 탐지된 객체에 대해 처리
        for box in results[0].boxes:
            # 바운딩 박스 좌표 추출
            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
            
            # 신뢰도 점수
            confidence = box.conf[0].cpu().numpy()
            
            # 클래스 ID와 이름
            class_id = int(box.cls[0].cpu().numpy())
            class_name = results[0].names[class_id]
            
            # 신뢰도가 0.5 이상인 경우만 표시
            if confidence >= 0.5:
                # 바운딩 박스 그리기 (초록색)
                cv2.rectangle(annotated_image, (x1, y1), (x2, y2), (0, 255, 0), 2)
                
                # 레이블 텍스트 생성
                label = f"{class_name}: {confidence:.2f}"
                
                # 텍스트 크기 계산
                font = cv2.FONT_HERSHEY_SIMPLEX
                font_scale = 0.6
                thickness = 2
                (text_width, text_height), _ = cv2.getTextSize(label, font, font_scale, thickness)
                
                # 텍스트 배경 사각형 그리기
                cv2.rectangle(annotated_image, (x1, y1 - text_height - 10), 
                             (x1 + text_width, y1), (0, 255, 0), -1)
                
                # 텍스트 그리기 (검은색)
                cv2.putText(annotated_image, label, (x1, y1 - 5), 
                           font, font_scale, (0, 0, 0), thickness)
                
                print(f"탐지된 객체: {class_name} (신뢰도: {confidence:.2f})")
        
        return annotated_image
    
    except Exception as e:
        print(f"어노테이션 그리기 중 오류 발생: {e}")
        return image

def save_output(image, output_path):
    """
    처리된 이미지를 저장합니다.
    
    Args:
        image: 저장할 이미지
        output_path: 출력 파일 경로
    """
    try:
        success = cv2.imwrite(output_path, image)
        if success:
            print(f"결과 이미지가 저장되었습니다: {output_path}")
        else:
            print("이미지 저장에 실패했습니다.")
    except Exception as e:
        print(f"이미지 저장 중 오류 발생: {e}")

def main():
    """
    메인 함수 - 객체 탐지 파이프라인을 실행합니다.
    """
    print("=== 객체 탐지 프로그램 시작 ===")
    
    # 파일 경로 설정
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_image = os.path.join(current_dir, "2477308902_443e5baf08_z.jpg")
    output_image = os.path.join(current_dir, "output.jpg")
    
    # 입력 이미지 존재 확인
    if not os.path.exists(input_image):
        print(f"입력 이미지를 찾을 수 없습니다: {input_image}")
        print("https://github.com/Jaeyoung-Lee/NDvision/tree/main/example/Object%20Detection 에서 샘플 이미지를 다운로드하세요.")
        return
    
    # 1. 모델 로드
    print("1. YOLOv8 모델 로드 중...")
    model = load_model()
    if model is None:
        return
    
    # 2. 객체 탐지
    print("2. 객체 탐지 수행 중...")
    results, original_image = detect_objects(model, input_image)
    if results is None or original_image is None:
        return
    
    # 3. 결과 시각화
    print("3. 탐지 결과 시각화 중...")
    annotated_image = draw_detections(original_image, results)
    
    # 4. 결과 저장
    print("4. 결과 이미지 저장 중...")
    save_output(annotated_image, output_image)
    
    # 5. 결과 이미지 표시
    print("5. 결과 이미지 표시 중...")
    # OpenCV BGR을 RGB로 변환
    annotated_rgb = cv2.cvtColor(annotated_image, cv2.COLOR_BGR2RGB)
    
    # 결과 이미지 표시
    plt.figure(figsize=(12, 8))
    plt.imshow(annotated_rgb)
    plt.title('Object Detection Results', fontsize=16, fontweight='bold')
    plt.axis('off')
    plt.tight_layout()
    plt.show()
    
    print("=== 객체 탐지 프로그램 완료 ===")
    print(f"입력 이미지: {input_image}")
    print(f"출력 이미지: {output_image}")

if __name__ == "__main__":
    main()