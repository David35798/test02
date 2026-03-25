from flask import Blueprint, render_template, request
from backend.services.bmi import BMICalculator
from backend.models.db import Database

main = Blueprint("main", __name__)


@main.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@main.route('/calculate', methods=['POST'])
def calculate():
    try:
        weight = float(request.form['weight'])
        height = float(request.form['height'])

        # 유효성 검사
        if weight <= 0 or height <= 0:
            return render_template('index.html', error="체중과 신장은 양수여야 합니다.")

        # BMI 계산
        calculator = BMICalculator(weight, height)
        result = calculator.get_result()

        # DB 저장
        db = Database()
        db.save_bmi_record(weight, height, result["bmi"], result["category"])

        return render_template(
            'result.html',
            bmi=result["bmi"],
            category=result["category"],
            weight=weight,
            height=height
        )

    except ValueError:
        return render_template('index.html', error="유효한 숫자를 입력해주세요.")


@main.route('/history')
def history():
    db = Database()
    records = db.get_bmi_records(10)
    return render_template('history.html', records=records)