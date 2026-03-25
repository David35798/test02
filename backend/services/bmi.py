class BMICalculator:
    """
    BMI 계산 및 분류를 담당하는 서비스 클래스
    - 입력값: 체중(kg), 신장(cm)
    - 출력값: BMI 값 및 비만도 카테고리
    """

    def __init__(self, weight: float, height: float):
        """
        BMI 계산기 초기화

        :param weight: 체중 (kg)
        :param height: 신장 (cm)
        """
        self.weight = weight
        self.height = height / 100  # cm → m 변환


    def calculate_bmi(self) -> float:
        """
        BMI 계산

        공식:
            BMI = 체중(kg) / (신장(m) ^ 2)

        :return: BMI 값 (float)
        """
        return self.weight / (self.height ** 2)


    def get_bmi_category(self) -> str:
        """
        BMI 값을 기준으로 건강 상태 분류

        기준 (대한비만학회):
        - 18.5 미만: 저체중
        - 18.5 ~ 22.9: 정상
        - 23 ~ 24.9: 과체중
        - 25 ~ 29.9: 비만
        - 30 이상: 고도비만

        :return: BMI 카테고리 (str)
        """
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "저체중"
        elif bmi < 23:
            return "정상"
        elif bmi < 25:
            return "과체중"
        elif bmi < 30:
            return "비만"
        else:
            return "고도비만"


    def get_result(self) -> dict:
        """
        BMI 계산 결과를 한 번에 반환

        :return: {
            "bmi": float,
            "category": str
        }
        """
        bmi = self.calculate_bmi()
        category = self.get_bmi_category()

        return {
            "bmi": round(bmi, 2),
            "category": category
        }