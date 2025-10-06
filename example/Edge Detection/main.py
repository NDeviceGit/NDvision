"""
AI-powered Edge Detection Algorithm
이미지에서 에지를 검출하는 AI 알고리즘 구현
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os

class EdgeDetector:
    def __init__(self, input_image_path, output_image_path):
        """
        에지 검출기 초기화
        Args:
            input_image_path (str): 입력 이미지 경로
            output_image_path (str): 출력 이미지 경로
        """
        self.input_path = input_image_path
        self.output_path = output_image_path
        self.image = None
        
    def load_image(self):
        """이미지를 로드합니다."""
        if not os.path.exists(self.input_path):
            raise FileNotFoundError(f"입력 이미지를 찾을 수 없습니다: {self.input_path}")
        
        self.image = cv2.imread(self.input_path)
        if self.image is None:
            raise ValueError("이미지를 읽을 수 없습니다.")
        
        print(f"이미지 로드 완료: {self.image.shape}")
        return self.image
    
    def preprocess_image(self, image):
        """이미지 전처리를 수행합니다."""
        # 그레이스케일 변환
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        # 가우시안 블러를 적용하여 노이즈 제거
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        
        return gray, blurred
    
    def canny_edge_detection(self, image, low_threshold=50, high_threshold=150):
        """
        OpenCV Canny 알고리즘을 사용한 에지 검출
        Args:
            image: 입력 이미지
            low_threshold: 하위 임계값
            high_threshold: 상위 임계값
        Returns:
            에지가 검출된 이미지
        """
        gray, blurred = self.preprocess_image(image)
        
        # Canny 에지 검출
        edges = cv2.Canny(blurred, low_threshold, high_threshold)
        
        return edges
    
    def adaptive_canny_edge_detection(self, image, sigma=0.33):
        """
        적응형 Canny 에지 검출 (자동 임계값 설정)
        Args:
            image: 입력 이미지
            sigma: 임계값 계산을 위한 시그마 값
        Returns:
            에지가 검출된 이미지
        """
        gray, blurred = self.preprocess_image(image)
        
        # 중간값을 기반으로 자동 임계값 계산
        median = np.median(blurred)
        low_threshold = int(max(0, (1.0 - sigma) * median))
        high_threshold = int(min(255, (1.0 + sigma) * median))
        
        print(f"자동 계산된 임계값: Low={low_threshold}, High={high_threshold}")
        
        # Canny 에지 검출
        edges = cv2.Canny(blurred, low_threshold, high_threshold)
        
        return edges
    
    def sobel_edge_detection(self, image):
        """
        Sobel 연산자를 사용한 에지 검출
        Returns:
            에지가 검출된 이미지
        """
        gray, blurred = self.preprocess_image(image)
        
        # Sobel X와 Y 방향 그래디언트 계산
        sobel_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        sobel_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        
        # 그래디언트 크기 계산
        sobel_magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
        sobel_magnitude = np.uint8(sobel_magnitude / sobel_magnitude.max() * 255)
        
        return sobel_magnitude
    
    def laplacian_edge_detection(self, image):
        """
        Laplacian을 사용한 에지 검출
        Returns:
            에지가 검출된 이미지
        """
        gray, blurred = self.preprocess_image(image)
        
        # Laplacian 필터 적용
        laplacian = cv2.Laplacian(blurred, cv2.CV_64F)
        laplacian = np.uint8(np.absolute(laplacian))
        
        return laplacian
    
    def morphological_edge_detection(self, image):
        """
        형태학적 연산을 사용한 에지 검출
        Returns:
            에지가 검출된 이미지
        """
        gray, blurred = self.preprocess_image(image)
        
        # 형태학적 그래디언트
        kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
        morph_gradient = cv2.morphologyEx(blurred, cv2.MORPH_GRADIENT, kernel)
        
        return morph_gradient
    
    def enhanced_edge_detection(self, image):
        """
        여러 방법을 결합한 향상된 에지 검출
        Returns:
            향상된 에지가 검출된 이미지
        """
        # 다양한 방법으로 에지 검출
        canny_edges = self.adaptive_canny_edge_detection(image)
        sobel_edges = self.sobel_edge_detection(image)
        laplacian_edges = self.laplacian_edge_detection(image)
        
        # 가중 평균으로 결합
        combined = cv2.addWeighted(canny_edges, 0.5, sobel_edges, 0.3, 0)
        combined = cv2.addWeighted(combined, 0.8, laplacian_edges, 0.2, 0)
        
        # 결과 향상을 위한 후처리
        # 가우시안 블러로 부드럽게 처리
        enhanced = cv2.GaussianBlur(combined, (3, 3), 0)
        
        # 임계값 적용으로 이진화
        _, enhanced = cv2.threshold(enhanced, 50, 255, cv2.THRESH_BINARY)
        
        return enhanced
    
    def save_edge_detection_results(self):
        """모든 에지 검출 방법의 결과를 저장합니다."""
        if self.image is None:
            self.load_image()
        
        # 다양한 에지 검출 방법 적용
        methods = {
            'Original': cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY),
            'Canny': self.canny_edge_detection(self.image),
            'Adaptive Canny': self.adaptive_canny_edge_detection(self.image),
            'Sobel': self.sobel_edge_detection(self.image),
            'Laplacian': self.laplacian_edge_detection(self.image),
            'Morphological': self.morphological_edge_detection(self.image),
            'Enhanced': self.enhanced_edge_detection(self.image)
        }
        
        # 결과 시각화
        fig, axes = plt.subplots(2, 4, figsize=(20, 10))
        axes = axes.ravel()
        
        for i, (method_name, result) in enumerate(methods.items()):
            axes[i].imshow(result, cmap='gray')
            axes[i].set_title(f'{method_name} Edge Detection', fontsize=12)
            axes[i].axis('off')
        
        # 마지막 subplot 숨기기
        axes[7].axis('off')
        
        plt.tight_layout()
        
        # 비교 결과 저장
        comparison_path = self.output_path.replace('.jpg', '_comparison.jpg')
        plt.savefig(comparison_path, dpi=300, bbox_inches='tight')
        plt.show()
        
        # 최고 품질의 결과 (Enhanced) 저장
        cv2.imwrite(self.output_path, methods['Enhanced'])
        
        print(f"에지 검출 완료!")
        print(f"메인 결과 저장: {self.output_path}")
        print(f"비교 결과 저장: {comparison_path}")
        
        return methods
    
    def process(self):
        """전체 에지 검출 프로세스를 실행합니다."""
        print("=== AI 기반 에지 검출 시작 ===")
        
        # 이미지 로드
        self.load_image()
        
        # 에지 검출 및 결과 저장
        results = self.save_edge_detection_results()
        
        print("=== 에지 검출 완료 ===")
        return results

def main():
    """메인 함수"""
    # 파일 경로 설정
    input_image = "2148664187_be75e2c40b_z.jpg"
    output_image = "output.jpg"
    
    try:
        # 에지 검출기 생성 및 실행
        detector = EdgeDetector(input_image, output_image)
        results = detector.process()
        
        print("\n=== 에지 검출 알고리즘 분석 ===")
        print("1. Canny: 가장 널리 사용되는 에지 검출 알고리즘")
        print("2. Adaptive Canny: 자동 임계값 설정으로 더 나은 결과")
        print("3. Sobel: 그래디언트 기반 에지 검출")
        print("4. Laplacian: 2차 미분 기반 에지 검출")
        print("5. Morphological: 형태학적 연산 기반")
        print("6. Enhanced: 여러 방법을 결합한 최적화된 결과")
        
    except Exception as e:
        print(f"에러 발생: {e}")

if __name__ == "__main__":
    main()
