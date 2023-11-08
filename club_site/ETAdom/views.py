from django.shortcuts import render
from django.http import HttpResponse
import requests
import re

def index(request):

    url = 'https://school.cbe.go.kr/cw-h/M01030304/list?y=2023&m=11'

    response = requests.get(url)

    html_code = response.text

    pattern1 = r'\r|\t'
    result1 = re.sub(r'\r|\t|\n', '', html_code)

    pattern = r'<table class="tch-sch-tbl">(.*?)</table>'
    result2 = re.search(pattern, result1, re.DOTALL)

    if result2:
        text_inside_table = result2.group(1)  # 첫 번째 그룹을 가져옵니다.
        full_text = f'<table class="tch-sch-tbl">{text_inside_table}</table>'

    context = {"name": 1, "result": full_text}

    return render(request, 'ETAdom/calendar.html', context)


# Create your views here.


