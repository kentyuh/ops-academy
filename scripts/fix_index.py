p = "index.html"
s = open(p, encoding="utf-8").read()
needle = '<p class="section-sub">每周精选几条可直接落地的运维小贴士。</p>'
marker = "\n\n<!-- ===== 视图：技术架构 ===== -->"
old = needle + marker
new = needle + "\n  </div>\n</section>" + marker
if s.count(needle) == 1 and old in s:
    s = s.replace(old, new, 1)
    open(p, "w", encoding="utf-8").write(s)
    print("patched")
else:
    print("skip: needle_count=%d already_ok=%s" % (s.count(needle), needle + "\n  </div>" in s))
