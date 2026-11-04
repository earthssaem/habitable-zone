"""index.html에 쓰인 글자만 담은 Jua 글꼴(woff2)을 만들어 <style> 맨 앞 @font-face에 base64로 넣는다.
사용법: pip install fonttools brotli 후 python3 tools/embed-jua.py index.html Jua-Regular.ttf <작업 폴더>
Jua-Regular.ttf 받기: curl -A "Wget/1.0" "https://fonts.googleapis.com/css2?family=Jua" 로 나온 .ttf 주소를 내려받는다."""
import base64, subprocess, sys, os, re
html, ttf, work = sys.argv[1], sys.argv[2], sys.argv[3]
s = open(html, encoding='utf-8').read()
# 이전에 넣은 글꼴 데이터는 글자 수집에서 뺀다
body = re.sub(r'/\* JUA-FONT-START \*/.*?/\* JUA-FONT-END \*/', '', s, flags=re.S)
chars = set(c for c in body if ord(c) > 126) | set(chr(i) for i in range(32, 127))
open(os.path.join(work, 'chars.txt'), 'w', encoding='utf-8').write(''.join(sorted(chars)))
out = os.path.join(work, 'jua-sub.woff2')
subprocess.run(['pyftsubset', ttf, '--text-file=' + os.path.join(work, 'chars.txt'), '--flavor=woff2', '--output-file=' + out,
                '--layout-features=*', '--no-hinting', '--desubroutinize'], check=True)
b64 = base64.b64encode(open(out, 'rb').read()).decode()
face = ("/* JUA-FONT-START */\n"
        "  /* 글꼴 Jua — Copyright 2018 The BM JUA Project Authors, SIL Open Font License 1.1 (https://openfontlicense.org).\n"
        "     외부 서버 없이 쓰려고 이 앱에 쓰인 글자만 골라(서브셋) 넣었다. 문구를 바꾸면 CLAUDE.md의 방법으로 다시 만든다. */\n"
        "  @font-face{font-family:'Jua'; font-style:normal; font-weight:400; font-display:block; src:url(data:font/woff2;base64," + b64 + ") format('woff2')}\n"
        "  /* JUA-FONT-END */")
if '/* JUA-FONT-START */' in s:
    s = re.sub(r'/\* JUA-FONT-START \*/.*?/\* JUA-FONT-END \*/', lambda m: face, s, flags=re.S)
else:
    s = s.replace('<style>\n', '<style>\n  ' + face + '\n', 1)
open(html, 'w', encoding='utf-8').write(s)
print('chars', len(chars), 'woff2', os.path.getsize(out), 'bytes')
