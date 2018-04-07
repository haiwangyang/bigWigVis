from svgutils.compose import *
import sys
from shared_info import get_elements
gene = sys.argv[1]

width = "50cm"
height = "25cm"

offset = 60
shrink = 0.2
x = 20
y = 3
size = 5

Figure(width, height, 
        Panel(
              SVG("svg/" + gene + ".w1118.svg").scale(shrink),
              Text("w1118", x, y, size=size, weight='bold')
             ),
        Panel(
              SVG("svg/" + gene + ".dyak.svg").scale(shrink),
              Text("Dyak", x, y, size=size, weight='bold')
             ).move(offset, 0),
        Panel(
              SVG("svg/" + gene + ".dana.svg").scale(shrink),
              Text("Dana", x, y, size=size, weight='bold')
             ).move(2 * offset, 0),
        Panel(
              SVG("svg/" + gene + ".dpse.svg").scale(shrink),
              Text("Dpse", x, y, size=size, weight='bold')
             ).move(3 * offset, 0),
        Panel(
              SVG("svg/" + gene + ".dper.svg").scale(shrink),
              Text("Dper", x, y, size=size, weight='bold')
             ).move(4 * offset, 0),
        Panel(
              SVG("svg/" + gene + ".dwil.svg").scale(shrink),
              Text("Dwil", x, y, size=size, weight='bold')
             ).move(5 * offset, 0),
        Panel(
              SVG("svg/" + gene + ".dmoj.svg").scale(shrink),
              Text("Dmoj", x, y, size=size, weight='bold')
             ).move(6 * offset, 0),
        Panel(
              SVG("svg/" + gene + ".dvir.svg").scale(shrink),
              Text("Dvir", x, y, size=size, weight='bold')
             ).move(7 * offset, 0),
        Panel(
              SVG("svg/" + gene + ".dgri.svg").scale(shrink),
              Text("Dgri", x, y, size=size, weight='bold')
             ).move(8 * offset, 0)
        ).save("svg/" + gene + ".merged.svg")

