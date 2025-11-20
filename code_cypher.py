import base64
import codecs

ENCODED = (
    "KITLpdWb0V3LgojRU1EWKw0UGRVRHBiOalVRU1kWFRVVJpEIUBVSaBiVTl1TKogLi1Gd2lHWg8methXY5tEItVmcgUnY5lHdgImYtRXd6VEItogL19WajBSRY1EI2lHI1RXa2tWa1BSaql3atomdtZGI2lmcppFItogL0V3c2RHIzl3bgkmd5hWasByboVmdpJFItogOVpVWVVVSCBiVJx0TLpgCuQlWJdUTgwSSBl1SClUU"
)

def rot13(s: str) -> str:
    return codecs.encode(s, "rot_13")

def atbash(s: str) -> str:
    out = []
    for ch in s:
        if "A" <= ch <= "Z":
            out.append(chr(ord("Z") - (ord(ch) - ord("A"))))
        elif "a" <= ch <= "z":
            out.append(chr(ord("z") - (ord(ch) - ord("a"))))
        else:
            out.append(ch)
    return "".join(out)

def try_naive_base64_first(encoded: str):
    print("Attempt 1: Base64 decode directly (expected to fail)")
    try:
        print(base64.b64decode(encoded.encode()).decode())
    except Exception as e:
        print("Decoding failed as expected:", e)

def hint():
    print("\nHINT: Consider reversing the string before Base64.\n"
          "Then explore combinations of Atbash and ROT13.\n"
          "Ask your AI assistant to enumerate and test decoding pipelines step-by-step.")

if __name__ == "__main__":
    try_naive_base64_first(ENCODED)
    hint()
