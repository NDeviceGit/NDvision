NDvision 인공지능 개발 키트 예제
이 저장소는 NDevice(엔디바이스)에서 개발한 NDvision 인공지능 개발 키트 사용자를 위한 공식 예제 코드와 가이드를 제공합니다. 모든 예제는 NDevice에서 제공하는 VS Code 확장판을 기준으로 작성되었습니다.

🚀 1. 빠른 시작
1.1. 필수 요구 사항
본 예제 코드를 사용하기 위해서는 다음 항목들이 PC에 설치되어 있어야 합니다.

- NDvision 개발 키트 하드웨어
- Visual Studio Code (VS Code, https://code.visualstudio.com/download): 개발 환경
- ND Controller VS Code 확장판: 장치 제어 및 시각화 도구
- Python 3.x: (가상 환경 권장)

1.2. 저장소 복제 (Clone)
- ND Controller 확장판에서 예제 복사
- VS Code 터미널 또는 Git Bash를 사용하여 이 저장소를 로컬 PC로 복제하십시오.

```powershell
git clone https://github.com/Jaeyoung-Lee/NDvision.git
cd NDvision
```

📦 2. 예제 코드 디렉토리 구조
핵심 기능별로 디렉토리가 구분되어 있습니다. 각 폴더 내부의 README.md 파일에서 자세한 실행 방법을 확인하십시오.

- **[01_Basic Python](https://github.com/Jaeyoung-Lee/NDvision/blob/main/example/Basic%20Python/main.py)** : 파이썬의 기초를 다질 수 있는 예제
- **[02_Edge Detection](https://github.com/Jaeyoung-Lee/NDvision/blob/main/example/Edge%20Detection/main.py)** : 이미지의 에지를 검출하는 예제
- **[03_Object Detection](https://github.com/Jaeyoung-Lee/NDvision/blob/main/example/Object%20Detection/main.py)** : 이미지에서 물체를 검출하는 예제
- **[04_Environment Detection](https://github.com/Jaeyoung-Lee/NDvision/blob/main/example/Environment%20Detection/main.py)** : 실시간 영상에서 상황을 검출할 수 있는 예제
- **[05_Data Training](https://github.com/Jaeyoung-Lee/NDvision/blob/main/example/Data%20Training/main.py)** : PyTorch 모델 학습 후
- **06_Upload to NDvision** : NDvision제품에 업로드를 하고 PC에서 처리하는 것과 비교를 해볼 수 있는 예제


🔧 3. 고장진단  
파이썬 코드를 실행시 모듈들이 설치되지 않았을 수 있습니다. 그러한 경우에는 아래의 명령어를 실행해 주십시오.

```powerhsell
pip install -r requirements.txt
```