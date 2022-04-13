import re

import panflute


def action(elem: panflute.Element, doc: panflute.Doc) -> None:
    if isinstance(elem, panflute.Image) or isinstance(elem, panflute.Link):
        elem.url = re.sub(r"^\s*\.\./", "/", elem.url)


def main(doc: panflute.Doc = None):
    return panflute.run_filters([action], doc=doc)


if __name__ == "__main__":
    main()
