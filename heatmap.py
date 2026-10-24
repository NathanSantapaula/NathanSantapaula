# Gera heatmap.svg animado a partir da página pública de contribuições (sem token).
import re, urllib.request
USER = "NathanSantapaula"
html = urllib.request.urlopen(f"https://github.com/users/{USER}/contributions").read().decode()
cells = re.findall(r'id="contribution-day-component-(\d+)-(\d+)" data-level="(\d)"', html)
assert cells, "formato da página mudou"
COLORS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]
S = 13
rects = "".join(
    f'<rect x="{int(c)*S}" y="{int(r)*S}" width="11" height="11" rx="2" fill="{COLORS[int(l)]}" style="animation-delay:{int(c)*20}ms"/>'
    for r, c, l in cells)
w = (max(int(c) for _, c, _ in cells) + 1) * S
open("heatmap.svg", "w").write(
    f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{7*S}" viewBox="0 0 {w} {7*S}">'
    '<style>rect{opacity:0;animation:in .4s ease-out forwards}@keyframes in{to{opacity:1}}</style>'
    f'{rects}</svg>')
print(len(cells), "dias")
