"""Build the two letters from one template.

  index.html          from Dhruv & Saumya, for friends
  family/index.html   from both families, for relatives
  hindi/index.html    the family letter in Hindi

Run from the repo root:  python3 src/build.py
"""
import os
import re

BASE = "https://dhruv1701.github.io/dhruv-saumya/"
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SIGNATURE = '    <p class="signature">Dhruv <span class="amp">&amp;</span> Saumya</p>'

VARIANTS = {
    "friends": {
        "out": "index.html",
        "LANG": "en",
        "BODY_CLASS": "en",
        "DATELINE": "Meerut, 21 December 2026",
        "D_DAY": "Monday",
        "D_DATE": "21 December 2026",
        "D_TIME": "5:30 pm <em>onwards</em>",
        "D_ADDR": "Hanuman Chowk, Bombay Bazar,<br>Sadar Bazaar, Meerut",
        "WAY": "Find the way",
        "OPEN_LABEL": "Open the letter",
        "FOR": "For you",
        "WHEN_WHERE": "When and where",
        "CD_MANY": "{n} evenings to go",
        "CD_ONE": "tomorrow evening",
        "CD_ZERO": "this evening",
        "TITLE": "Dhruv &amp; Saumya have something to tell you…",
        "OG_TITLE": "Dhruv &amp; Saumya have something to tell you…",
        "OG_DESC": "A letter for you. Monday, 21 December 2026 · 5:30 pm · Meerut",
        "OG_IMAGE": BASE + "card-friends.jpg",
        "GREETING": "Dear you,",
        "STORY": [
            "You have been part of this story from the very start, through all the long calls, "
            "and every time you asked what was going on with us two while we smiled and changed the subject.",
            "So it is only right that you hear this from us. On the evening of 21 December, our families "
            "are sitting down together, the mithai is ordered, and we are finally making it official.",
        ],
        "LEAD": "It&rsquo;s our",
        "SUB": "the Roka of Dhruv &amp; Saumya",
        "AFTER": [
            "We are keeping it small, only the people who have stood by us the longest. "
            "You are one of them, and it would not feel right without you there.",
        ],
        "SIGNOFF": "With all our love,",
        "SIGNATURE": SIGNATURE,
        "PS": '    <p class="ps">P.S. Come hungry.</p>',
    },
    "family": {
        "out": "family/index.html",
        "LANG": "en",
        "BODY_CLASS": "en",
        "DATELINE": "Meerut, 21 December 2026",
        "D_DAY": "Monday",
        "D_DATE": "21 December 2026",
        "D_TIME": "5:30 pm <em>onwards</em>",
        "D_ADDR": "Hanuman Chowk, Bombay Bazar,<br>Sadar Bazaar, Meerut",
        "WAY": "Find the way",
        "OPEN_LABEL": "Open the letter",
        "FOR": "For you",
        "WHEN_WHERE": "When and where",
        "CD_MANY": "{n} evenings to go",
        "CD_ONE": "tomorrow evening",
        "CD_ZERO": "this evening",
        "TITLE": "Something happy to share, from the families of Dhruv &amp; Saumya…",
        "OG_TITLE": "Something happy to share, from the families of Dhruv &amp; Saumya…",
        "OG_DESC": "A letter for you. Monday, 21 December 2026 · 5:30 pm · Meerut",
        "OG_IMAGE": BASE + "card-family.jpg",
        "GREETING": "Namaste,",
        "STORY": [
            "With the blessings of our elders and by God&rsquo;s grace, our families have some happy news, "
            "and we wanted you to hear it from us first.",
            "Dhruv and Saumya have chosen each other. On the evening of 21 December, our two families will sit "
            "together for the first time as one, bless the children, share mithai, and make it official.",
        ],
        "LEAD": "It is their",
        "SUB": "the Roka of Dhruv &amp; Saumya",
        "AFTER": [
            "It will be a small gathering of our closest family. Your presence and your blessings "
            "would mean a great deal to us, and to them.",
        ],
        "SIGNOFF": "With love and respect,",
        "SIGNATURE": '    <p class="sig-pre">the families of</p>\n' + SIGNATURE,
        "PS": "",
    },
    "hindi": {
        "out": "hindi/index.html",
        "LANG": "hi",
        "BODY_CLASS": "hi",
        "TITLE": "ध्रुव एवं सौम्या के परिवार कुछ बताना चाहते हैं…",
        "OG_TITLE": "ध्रुव एवं सौम्या के परिवार कुछ बताना चाहते हैं…",
        "OG_DESC": "आपके लिए एक पत्र। सोमवार, 21 दिसंबर 2026 · शाम 5:30 बजे · मेरठ",
        "OG_IMAGE": BASE + "card-hindi.jpg",
        "DATELINE": "मेरठ, 21 दिसंबर 2026",
        "GREETING": "सादर नमस्ते,",
        "STORY": [
            "बड़ों के आशीर्वाद और ईश्वर की कृपा से हमारे परिवारों के पास एक शुभ समाचार है, "
            "और हम चाहते थे कि आप इसे सबसे पहले हमसे ही सुनें।",
            "ध्रुव और सौम्या ने एक-दूसरे को चुन लिया है। 21 दिसंबर की शाम हमारे दोनों परिवार पहली बार "
            "एक होकर साथ बैठेंगे, बच्चों को आशीर्वाद देंगे, मुँह मीठा करेंगे और इस रिश्ते को पक्का करेंगे।",
        ],
        "LEAD": "यह है उनका",
        "SUB": "ध्रुव एवं सौम्या",
        "AFTER": [
            "यह हमारे सबसे करीबी परिवारजनों का एक छोटा-सा आयोजन होगा। आपकी उपस्थिति और आपका आशीर्वाद "
            "हमारे लिए, और उन दोनों के लिए, बहुत मायने रखेगा।",
        ],
        "SIGNOFF": "सप्रेम एवं सादर,",
        "SIGNATURE": '    <p class="sig-pre">शुभाकांक्षी</p>\n    <p class="signature">ध्रुव एवं सौम्या के परिवार</p>',
        "PS": "",
        "D_DAY": "सोमवार",
        "D_DATE": "21 दिसंबर 2026",
        "D_TIME": "शाम 5:30 बजे <em>से</em>",
        "D_ADDR": "हनुमान चौक, बॉम्बे बाज़ार,<br>सदर बाज़ार, मेरठ",
        "WAY": "रास्ता देखें",
        "OPEN_LABEL": "पत्र खोलें",
        "FOR": "आपके लिए",
        "WHEN_WHERE": "कब और कहाँ",
        "CD_MANY": "{n} दिन शेष",
        "CD_ONE": "कल शाम",
        "CD_ZERO": "आज शाम",
    },
}


def paragraphs(items):
    return "\n".join("      <p>" + t + "</p>" for t in items)


def render(template, v):
    out = template
    for key, val in v.items():
        if key == "out":
            continue
        if key in ("STORY", "AFTER"):
            val = paragraphs(val)
        out = out.replace("{{" + key + "}}", val)
    left = re.findall(r"\{\{[A-Z_]+\}\}", out)
    assert not left, left
    return out


def artifact_copy(page):
    """The Claude artifact gets its own skeleton: keep title/style/script and the body only."""
    head = page.split("<!--ARTIFACT-START-->", 1)[1].split("<!--ARTIFACT-HEAD-END-->", 1)[0]
    body = page.split("<!--ARTIFACT-BODY-START-->", 1)[1].split("<!--ARTIFACT-BODY-END-->", 1)[0]
    head = head.replace("<title>", '<title>', 1)
    return head.strip() + '\n<meta name="claude:viewport-fit-sides" content="cover">\n' + body.strip() + "\n"


def main():
    template = open(os.path.join(ROOT, "src", "template.html"), encoding="utf-8").read()
    for name, v in VARIANTS.items():
        page = render(template, v)
        path = os.path.join(ROOT, v["out"])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        clean = page.replace("<!--ARTIFACT-START-->\n", "").replace("<!--ARTIFACT-HEAD-END-->\n", "")
        clean = clean.replace("<!--ARTIFACT-BODY-START-->\n", "").replace("<!--ARTIFACT-BODY-END-->\n", "")
        open(path, "w", encoding="utf-8").write(clean)
        print("wrote", v["out"])
        if name == "friends":
            art = os.path.join(os.path.dirname(ROOT), "roka-invite.html")
            open(art, "w", encoding="utf-8").write(artifact_copy(page))
            print("wrote ../roka-invite.html")


if __name__ == "__main__":
    main()
