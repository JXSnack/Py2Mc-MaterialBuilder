# Py2Mc Material Builder
This is the Py2Mc material builder to add new materials to Py2Mc when a new minecraft version releases.

## Manual
Open the latest [javadocs for material](https://hub.spigotmc.org/javadocs/bukkit/org/bukkit/Material.html) and open inspect element.
In inspect element paste the code in `copy_paste.js` and run it. Now you should see that the `Description` is "replace with nothing". 
Copy and paste all materials with their `Description` into the `materials.txt`. In there replace all `replace with nothing` with nothing.
Run the `main.py` and you should see your generated code in the `output.py`.