#!/usr/bin/env python3
"""Find broken relative file links in Markdown documents."""
import argparse,pathlib,re,sys,unittest
from urllib.parse import urlsplit,unquote
LINK=re.compile(r"!?(?:\[[^\]]*\])\((?:<([^>]+)>|([^\s)]+))(?:\s+[^)]*)?\)")
def check_file(path):
    path=pathlib.Path(path); findings=[]
    try: lines=path.read_text(encoding="utf-8").splitlines()
    except (OSError,UnicodeError) as exc: return [(str(path),0,str(exc))]
    for number,line in enumerate(lines,1):
        for match in LINK.finditer(line):
            raw=match.group(1) or match.group(2); parts=urlsplit(raw)
            if parts.scheme or parts.netloc or not parts.path: continue
            target=(path.parent/unquote(parts.path)).resolve()
            if not target.exists(): findings.append((str(path),number,raw))
    return findings
class Tests(unittest.TestCase):
    def test_missing_only(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            root=pathlib.Path(tmp); (root/"ok.md").write_text("# ok")
            p=root/"README.md"; p.write_text("[ok](ok.md) [bad](missing.md) [web](https://example.com)")
            self.assertEqual(check_file(p),[(str(p),1,"missing.md")])
    def test_anchor(self):
        import tempfile
        with tempfile.TemporaryDirectory() as tmp:
            p=pathlib.Path(tmp)/"a.md"; p.write_text("[top](#intro)")
            self.assertEqual(check_file(p),[])
def main():
    ap=argparse.ArgumentParser(description=__doc__); ap.add_argument("files",nargs="+"); a=ap.parse_args(); issues=[]
    for pattern in a.files:
        paths=list(pathlib.Path().glob(pattern)) if any(c in pattern for c in "*?[") else [pathlib.Path(pattern)]
        for p in paths:
            if p.is_file(): issues.extend(check_file(p))
    for file,line,target in issues: print(f"{file}:{line}: missing local target: {target}")
    print(f"{len(issues)} broken link(s)"); raise SystemExit(bool(issues))
if __name__=="__main__":
    if "--self-test" in sys.argv: unittest.main(argv=[sys.argv[0]])
    else: main()
