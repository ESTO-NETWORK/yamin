from django.shortcuts import render
from django.views.generic import View
# sub 함수 사용 위해 re 모듈 사용
import re
from django.http import JsonResponse
import json


# Create your views here.

class IndexView(View):
    def post(self, request):
        body = json.loads(request.body)
        result = hangul_split(body)
        return JsonResponse({'translate_result': result})

    def get(self, request):
        print(hangul_split('동해물과 백두산이'))
        return render(request, 'www/index.html')


# 한글 완성자 문자열 초성, 중성, 종성으로 분리하는 함수
def hangul_split(txt):
    """
    - Hangul Jamo Unicode = 자음, 모음 영역 (0x1100 ~ 0x11FF)
    - Hangul Syllables Unicode (가~힣) = 한글 음절 영역 (0xAC00(Dec 44032) ~ 0xD7A3(Dec 55203), 총 11,172자)
    
    - 유니코드에서의 한글 형식 = 0xAC00 + 28*21*(초성 index) + 28*(중성 index) + (종성 index)
    - 초성 분리 공식 = (유니코드 값 - 0xAC00) / (28*21)
    - 중성 분리 공식 = ((유니코드 값 - 0xAC00) % (28*21)) / 28
    - 종성 분리 공식 = (유니코드 값 - 0xAC00) % 28
    """

    # 초성(19개), 중성(21개), 종성(28개) 저장 리스트
    hangul_cho = ['ㄱ', 'ㄲ', 'ㄴ', 'ㄷ', 'ㄸ', 'ㄹ', 'ㅁ', 'ㅂ', 'ㅃ', 'ㅅ', 'ㅆ', 'ㅇ', 'ㅈ', 'ㅉ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']
    hangul_jung = ['ㅏ', 'ㅐ', 'ㅑ', 'ㅒ', 'ㅓ', 'ㅔ', 'ㅕ', 'ㅖ', 'ㅗ', 'ㅘ', 'ㅙ', 'ㅚ', 'ㅛ', 'ㅜ', 'ㅝ', 'ㅞ', 'ㅟ', 'ㅠ', 'ㅡ', 'ㅢ', 'ㅣ']
    hangul_jong = [' ', 'ㄱ', 'ㄲ', 'ㄳ', 'ㄴ', 'ㄵ', 'ㄶ', 'ㄷ', 'ㄹ', 'ㄺ', 'ㄻ', 'ㄼ', 'ㄽ', 'ㄾ', 'ㄿ', 'ㅀ', 'ㅁ', 'ㅂ', 'ㅄ', 'ㅅ', 'ㅆ', 'ㅐ', 'ㅈ', 'ㅊ', 'ㅋ', 'ㅌ', 'ㅍ', 'ㅎ']

    rtxt = re.sub(r'[^가-힣]', '', txt)  # 한글 완성자만 남김 (다른 문자 요소[영어, 숫자 등] 다 소거)

    result = []  # 한글 문자열 분리한 결과를 저장할 리스트

    for i in rtxt:  # 문자별로 초성, 중성, 종성 분리 작업 loop
        temp = ord(i) - 44032  # 한글 완성자의 유니코드 포인터 값 추출
        cho = temp // (21 * 28)  # 초성 값 추출
        jung = (temp // 28) % 21  # 중성 값 추출
        jong = temp % 28  # 종성 값 추출

        # 한글 완성자의 요소 뜯어 리스트로 저장
        # (ex) result = [['ㅎ','ㅏ','ㄴ'],['ㄱ','ㅡ','ㄹ']]
        result.append([hangul_cho[cho], hangul_jung[jung], hangul_jong[jong]])

    return result
