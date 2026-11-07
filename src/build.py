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
        "TITLE": "A letter from Dhruv &amp; Saumya",
        "OG_TITLE": "Dhruv &amp; Saumya have some news",
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
        "TITLE": "A letter from the families of Dhruv &amp; Saumya",
        "OG_TITLE": "Happy news from the families of Dhruv &amp; Saumya",
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
