# 2021-06-19

Was asked yesterday about this project.
* Refreshed the code base, applying software development practices I've learned in the past 5 years.
* removed unlicensed images
* added open-source free images; included citations


# 20160824

started work on a web version

# 20140629

Perhaps instead of calling the image reader in the OS, use tkinter and imagetk
http://effbot.org/imagingbook/imagetk.htm
http://stackoverflow.com/questions/17005961/displaying-images-with-tkinter
http://code.activestate.com/recipes/521918-pil-and-tkinter-to-display-images/

I cannot find how to install imagetk

# 20140620

```
import subprocess
import time
# http://stackoverflow.com/questions/13327759/how-to-display-and-close-image-in-python
p = subprocess.Popen(["open", "39__trishia_compass.png"])
time.sleep(2)
p.kill()
```

```
import subprocess
import time
filename="39__trishia_compass.png"
retcode = subprocess.call("open " + filename, shell=True)
```

```
#http://stackoverflow.com/questions/6725099/how-can-i-close-an-image-shown-to-the-user-with-the-python-imaging-library
import subprocess
import time
filename="39__trishia_compass.png"
viewer = subprocess.Popen(['/Applications/Preview.app/Contents/MacOS/Preview', filename])
time.sleep(2)
viewer.terminate()
viewer.kill()
```

# 20140620

Summary: installed Pillow to open images
Outcome: PIL (now Pillow) is for altering images; "show()" is a debugging tool with no corresponding "close()"
Action: Don't use PIL (or Pillow) for just viewing images
```
sudo easy_install pip
sudo pip install Pillow
```

```
# http://www.pythonforbeginners.com/gui/how-to-use-pillow
python
from PIL import Image
f = Image.open("39__trishia_compass.png").show()
```

```
from PIL import Image
fp = open("39__trishia_compass.png", "rb")
im = Image.open(fp) # open from file object
#im.load() # make sure PIL has read the data
fp.close()
```

```
from PIL import Image
import time
# http://stackoverflow.com/questions/3135328/how-to-close-an-image
def do_post_processing(filename):
    with open(str(filename), 'rb') as f:
        image = Image.open(f).show()
        del image

do_post_processing("39__trishia_compass.png")
time.sleep(3) # delays for 5 seconds
do_post_processing("Dharma_Mittra.jpg")
```

# 20140531

Inspired by
http://cytoscapeweb.cytoscape.org/demos

http://wiki.cytoscape.org/Cytoscape_3/UserManual

Used Cytoscape 3.1 for visualization. Cytoscape supports setting node properties to english name
1) open graph
Start New Session > From Network File > open the graphML file produced from the Python database
2) directed graph
control panel > Style > Directed
2) set node to english name:
control panel > Style > Directed > properties > Map. > Label > Column > english_name
3) alter the node color
control panel > Style > Directed > properties > Def. > Fill Color > color
4) alter node text color
control panel > Style > Directed > properties > Def. > Label Color > color



Converted graphml from yed to networkx in Python database


Used Yed for graph creation
