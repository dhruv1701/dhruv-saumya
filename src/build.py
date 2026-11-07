"""Build the two letters from one template.

  index.html          from Dhruv & Saumya, for friends
  family/index.html   from both families, for relatives

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
        "OG_IMAGE": BASE + "card-friends-sq.jpg",
        "GREETING": "Dear you,",
        "STORY": [
            "You have known about the two of us for a long time. And for just as long, you have been asking "
            "the same question: &ldquo;Official kab kar rahe ho?&rdquo; We laughed it off, changed the subject, "
            "and never once gave you a proper answer.",
            "So it is only right that you hear this from us. On the evening of 21 December, our families "
            "are sitting down together, the mithai is ordered, and we are finally making it official.",
        ],
        "AFTER": [
            "It would make us so happy to have you there with us.",
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
        "OG_IMAGE": BASE + "card-family-sq.jpg",
        "GREETING": "Namaste,",
        "STORY": [
            "With the blessings of our elders and by God&rsquo;s grace, our families have some happy news.",
            "Dhruv and Saumya have chosen each other. On the evening of 21 December, our families will sit "
            "together as one, bless the children, share mithai, and make it official.",
        ],
        "AFTER": [
            "Your presence and your blessings would mean a great deal to us, and to them.",
        ],
        "SIGNOFF": "With love and respect,",
        "SIGNATURE": '    <p class="sig-pre">the families of</p>\n' + SIGNATURE,
        "PS": "",
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
