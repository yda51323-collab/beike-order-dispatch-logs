# -*- coding: utf-8 -*-
# 成交单派发日志解析
import collections
import re

SERVICE_NAME = "贝壳找房"
FIELDS = ["ts", "svc", "order_id", "broker", "mobile", "id_no", "card", "amount", "route", "addr"]
PATTERN = re.compile(r"(\w+)=([^\s]+)")


def parse_line(line):
    d = dict(PATTERN.findall(line))
    if not d:
        return None
    d.setdefault("svc", SERVICE_NAME)
    return d


def parse(path):
    with open(path, encoding="utf-8") as f:
        for line in f:
            rec = parse_line(line.strip())
            if rec:
                yield rec


def group(path, key="order_id"):
    out = collections.defaultdict(list)
    for r in parse(path):
        out[r.get(key, "")].append(r)
    return out


if __name__ == "__main__":
    import sys
    p = sys.argv[1]
    g = group(p, sys.argv[3] if len(sys.argv) > 3 else "order_id")
    for k, v in sorted(g.items()):
        print(k, len(v), v[-1].get("route", "-"))
