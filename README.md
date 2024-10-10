# 과자 브렌드 구별자 만들기 실험#1 (부끄럽지만 가장 설레는 순간이 아닌가 싶다 ^^)
과자 브랜드를 구별하는 모델을 만들고자 하지만..종류별 마다 과자 봉투들이 너무 다양하다 O.O!
분류 할 과자 봉투들: 
<br>
1.바나나킥 
<img src="https://github.com/user-attachments/assets/4e7ef37c-b161-44bf-80fa-5f3e8247cd68" width="25%" height="25%"/>

2.블루베리 포키 
<img src="https://github.com/user-attachments/assets/422bd663-1621-4154-a004-c152f0404a4e" width="25%" height="25%"/>

3.콘초
<img src="https://github.com/user-attachments/assets/0cd6f470-fd5b-46a8-8652-4980eb468fad" width="25%" height="25%"/>

4.꼬깔콘 
<img src="https://github.com/user-attachments/assets/b6b918a8-eaea-497b-9113-e4e21dbf7c0a" width="25%" height="25%"/>

5.자이리톨 
<img src="https://github.com/user-attachments/assets/7445a3d9-0fb3-4bcd-be00-a0e0e921b5c3" width="25%" height="25%"/>

6.오징어집 
<img src="https://github.com/user-attachments/assets/067cf819-c54b-4a3d-be20-f0fd5dd7662e" width="25%" height="25%"/>

7.새우깡
<img src="https://github.com/user-attachments/assets/d41ffa0e-81f4-4300-9370-8c7c78aac2d2" width="25%" height="25%"/>

하지만, 포키 과자 브랜드만 보아도, 과자 박스 색깔이 너무 다양하다:
<img src="https://github.com/user-attachments/assets/9b8a4f52-676f-4b91-98f0-3d2139c7bf79" width="50%" height="50%"/>

현재 AI허브에 제공 되는 데이터로는 과자 브랜드를 정확히 구별하기에는 부족하다(포키 블루베리 버전만):
<img src="https://github.com/user-attachments/assets/0eea72ba-f60d-48e8-b84b-647c91995ecf" width="100%" height="100%"/>

인공지능 과자 브렌드 구별 오류:
(바나나킥은 노랑색, 포키는 파랑 및 보라색으로 인식해서 나는 오류)


## 문제
과자 봉투 분류기 만들기 도전! 좋은 인공지능 모델에 핵심은 적어도 깔금한 데이터라고 한다. 하지만, 현재 AI 허브 데이터 샘플만 보아도, 각 과자 브렌드의 무궁진한 봉투들을 포함하지 않았다.

## 가설
기존 데이터셋에, 구별 해야 할 과자 브렌드에 서로 상반되는 마스크를 씌우면, 과자 구별 인지도가 높아 질 것이다

## 결론
1. - 강점
       - 적고 깔끔한 데이터(일치한 배경, 일정한 각도 변경)로 학습이 빠름
           - 4 epoch 후 100% 정확도 도달
   - 단점
       - 바나나킥 우유를 블루베리 포키로 오해
       - 보라색 포장지로 감싼 바나나킥 브랜드 과자를 블루베리 포키로 오해, 하지만 노란색 봉지로 감싼 포키는 정확히 인식함
       - 학습하지 않은 과자들을 보여주어도, 학습한 과자는 인식 한다?
2. - 강점
       - 기타 간식 5개 (1번과 유사한 데이터) 학습도 1번만큼 빠름 (1번과 유사하게 4 epoch 후 100% 정확도 도달)
   - 단점
       - 노란색 봉지로 감싼 포키와 학습하지 않은 과자들 사이 학습한 스낵은 정확히 인식 하는 것 같지만, 설명이 어려운 오차가 의심된다
       - 바나나킥 우유를 파랑색 포장지로 감싼 자이리톨로 오해 (자이리톨 원둥형 통을 닮아서 그런가?)
       - 보라색 포장지로 감싼 바나나킥 스낵을 파랑색 포장지로 감싼 자이리톨로 오해 (이유를 짐착이 되지 않음ㅠ)
       - 과자 봉투에 꺼낸 포키는 자이리톨 검으로 오해 (진짜 모르겠음 ㅠㅠㅠ)
3. - 강점
       - 마스크 씌워도, 학습은 1번만큼 빠름 (1번과 유사하게 4 epoch 후 100% 정확도 도달)
       - **1,2번과 다르게 바나나킥 우유와 보라색 포장지로 감싼 바나나킥 간식을 정확히 인식!!!**
   - 단점
       - 하지만 여전히 과자 봉투 꺼낸 포키는 과자봉투에서 묘사한데도 불구하고 인식하는 것에 어려움이 있는 듯 (왜 일까???!!)
4. - 단점
       - overfitting 의심
           - 7 epoch 후 100% 정확도에 도달 한 후, 학습 도중 정확도가 3번 떨어짐
       - 1-3번 보다 학습 속도가 거의 두배 이상 (4 epoch vs 7 epoch 이후 100% 정확도 도달)
       - **마스크를 씌워도, 비슷한 봉투 색갈을 구분하지 못한다: 노랑색 봉투로 감싼 바나나킥 과자를 8번이나 노랑색으로 감싼 오징어집으로 오해**
       - **7번이나 빨강색 봉투로 감싼 꼬깔콘 과자를 노랑색으로 감싼 오징어집으로 오해 (왜 그런지 전혀 짐착이 가지 않음!!!!!!!)**
       - **시범 예측 예제 5개 모두 틀림 !!!!!!!!**
           - 2번과 유사하게 노란색 바나나킥 우유와 보라색 봉투로 감싼 바나나킥 과자를 자이리톨로 오해 (2번과 똑같은 오류인 것이 중요한 단서일까?)
           - **여태까지 한번도 틀린 적 없는 문제도 실패!!!! 학습하지 않은 과자 봉투들 사이 학습한 과자 인식하기도 구분도 실패 ㅠㅠㅠㅠㅠ**
5. - 단점
       - **느린 학습률 (25epoch 이후에도 정확도가 75% 정확률)**
       - **마스크를 씌운 뒤 마스크를 씌우든 씌우지 않든, 노랑색 바나나킥 과자를 구분 하지 못함**
       - **바나나킥 봉투를 구분하기 어려운 이유가 있는 듯!!!! 모델과 연관 시킬 수 있을까?**
       - **실험상 학습하지 못한 다양한 스낵 브랜드를 보여주자, 하나만 예측하고 모두 구분 할 것을 거부 함**
           -  유일하게 에측한 것도 틀림 ㅠ

## 아쉬운 점
- 학습 할 데이터가 문제 난의도에 비해 너무 적다??
- efficientnetb0는 resnet50모델에 비해 더 많은 학습 시간 혹은 데이터가 필요함
- 렌덤 값을 고정하지 않아 정확한 비결 불과

## 다음
- 틀린 것 학습하고 *분석하고* fine tuning
- 마스크를 씨우지 않고, 실제 여러 색감 과자 포장지로 데이터 학습하면?
- 노이즈가 많지만 풍부한 데이터 VS 및 깔금하지만 적은 데이터
- 촬영 각도에 따라 학습 증가율 올리기 VS 데이터 가공(예:affine)로 각도 바꾸기
- 빛 필터 및 다른 필터들로 (예:equalize, contrast 등등) 학습 증가율의 영향

### 실험 상황
- learning rate, batch size, epoch 모두 유사
    - learning rate=0.001, batchsize=32, epoch=25
    - 데이터 사이즈는 마스크 씌우지 않은 데이터셋과 비교해 train, valid, test 각각 한계 더 추가
        - fyi: 마스크를 씌우지 않은 데이터셋트를 전체 사용하는 것과 달리 마스크로 씌운 데이터셋트는 마스크로 씌우지 않은 데이터셋트와 반반으로 섞는다. 여기에 전체 데이터 갯수가 홀수이어서, 반반으로 섞은 데이터셋트는 반올림으로 인해 데이터셋트 하나 더 추가 됨.

## 결과
### 1. 바나나킥 vs 포키 구별하기
  ![o2res train](https://github.com/user-attachments/assets/076400f4-9669-4f8c-9f90-c93f80419229)
  ![o2res fitGraph](https://github.com/user-attachments/assets/464742e3-b33e-46ca-ae20-659db74d085b)
  ![o2res fit](https://github.com/user-attachments/assets/09047c55-35ca-474d-b325-fea0a128eb63)
  ![o2res cfmatrix](https://github.com/user-attachments/assets/06b7ed9d-bc12-4574-9a4d-4c76684c7f74)
  ![o2res predict](https://github.com/user-attachments/assets/4a4088ab-9162-4ed0-988f-c1c3b1f92932)
### 2. 5가지 과자 브렌드 데이터 추가, 바나나킥 vs 포키 구별하기
  ![o7res train](https://github.com/user-attachments/assets/b44fdc79-bfbc-4e15-8b1f-ca485c342c65)
  ![o7res predict](https://github.com/user-attachments/assets/125be216-876f-4dfa-b388-a3277574cc53)
  ![o7res fitGraph](https://github.com/user-attachments/assets/52d253b3-4660-4571-be53-27155c608193)
  ![o7res fit](https://github.com/user-attachments/assets/af8a3431-e39a-4e42-8275-aa8d9a93544f)
  ![o7res cfmatrix](https://github.com/user-attachments/assets/6f0efde6-9b10-4194-8430-8623c1f23339)
  ![o7res predict](https://github.com/user-attachments/assets/43ec1010-faf6-44b5-a3dc-dfb1cb2f639f)
### 3. 마스크를 씌우고, 바나나킥 vs 포키 구별하기 (efficientnetb0) 
  ![o7res_da train](https://github.com/user-attachments/assets/c2fbf671-c9a4-41c8-bde7-39fab6692404)
  ![o7res_da fitGraph](https://github.com/user-attachments/assets/aec8a00a-7fe8-4b3d-84c9-9cc2a17782da)
  ![o2res_da fit](https://github.com/user-attachments/assets/4b9bb5d0-2aa4-4285-92a3-f4a3fcff1527)
  ![o2res_da eval](https://github.com/user-attachments/assets/f9c4098b-2c5e-4346-8703-11fd93864e15)
  ![o7res_da predict](https://github.com/user-attachments/assets/d87e034b-a2aa-4715-9af6-1221e07b48ca)
### 4. 마스크를 씌우고 + 5가지 과자 브렌드 데이터 추가, 바나나킥 vs 포키 구별하기 (resnet50)
  ![c7res_da train](https://github.com/user-attachments/assets/ef8a37be-bfb0-41f4-8991-a850e390b44a)
  ![c7res_da fitGraph](https://github.com/user-attachments/assets/0a6e43fd-7eca-4cc2-bcc0-09f6149c142f)
  ![o7res fit](https://github.com/user-attachments/assets/8bcbb5d1-6c3f-417a-a7d1-8db38154cfd0)
  ![c7res_cfmatrix](https://github.com/user-attachments/assets/430abc6a-cd8c-42ad-b044-5669606083a7)
  ![c7res_da eval](https://github.com/user-attachments/assets/4b827fce-3987-4008-b290-dc530b0e2aac)
  ![c7res_da predict](https://github.com/user-attachments/assets/52cc6218-69ff-45e2-adcb-49f8f75bc721)
### 5. 4번 조건(resnet50 모델 적용)에 efficientnet50 모델 적용
   ![c7eff_da train](https://github.com/user-attachments/assets/c99451e4-3e8b-42d5-add4-eb877888f65f)
   ![c7eff_da fitGraph](https://github.com/user-attachments/assets/8050f192-04fb-4862-a14c-091091a27566)
   ![c7eff_da fit](https://github.com/user-attachments/assets/38f664b4-d218-43ac-b517-8643562fb01b)
   ![c7eff_cfmatrix](https://github.com/user-attachments/assets/2658ed8d-b29a-4b7e-b5a5-2ce9d2575ebd)
   ![c7eff_da eval](https://github.com/user-attachments/assets/d305f50c-24eb-43c8-857f-cd200ab02336)
   ![c7eff_da predict](https://github.com/user-attachments/assets/6538c606-4ada-4f7c-a1fe-6a628c26f082)

### 6. Coming Soon!! hyperparameter tuning 

# 개념 및 코딩 리뷰
## 피처 
## 데이터 가공
## 마스크를 씌우기 코드
