from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'www/index.html')

def hangul_split():
    """
    Hangul Jamo Unicode = 자음, 모음 영역 (0x1100 ~ 0x11FF)
    Hangul Syllables Unicode (가~힣) = 한글 음절 영역 (0xAC00 ~ 0xD7A3)

    - 초성 (19개)
        ㄱ, ㄲ, ㄴ, ㄷ, ㄸ, ㄹ, ㅁ, ㅂ, ㅃ, ㅅ, ㅆ, ㅇ, ㅈ, ㅉ, ㅊ, ㅋ, ㅌ, ㅍ, ㅎ
    - 중성 (21개)
        ㅏ, ㅐ, ㅑ, ㅒ, ㅓ, ㅔ, ㅕ, ㅖ, ㅗ, ㅘ, ㅙ, ㅚ, ㅛ, ㅜ, ㅝ, ㅞ, ㅟ, ㅠ, ㅡ, ㅢ, ㅣ
    - 종성 (28개)
        없음, ㄱ, ㄲ, ㄳ, ㄴ, ㄵ, ㄶ, ㄷ, ㄹ, ㄺ, ㄻ, ㄼ, ㄽ, ㄾ, ㄿ, ㅀ, ㅁ, ㅂ, ㅄ, ㅅ, ㅆ,
        ㅐ, ㅈ, ㅊ, ㅋ, ㅌ, ㅍ, ㅎ
    """



    return none