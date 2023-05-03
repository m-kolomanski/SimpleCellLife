Simple cell life simulation. This time Imma do it for real.<br>
Not ready for any release yet, everything is barely taped together.

<h1>Usage</h1>
To run, clone the repository and run:
```
python SimpleCellLife.py
```
In the menu you need to provide:
<ul>
<li>Map X dimension;</li>
<li>Map Y dimension;</li>
<li>Tick rate in ms;</li>
<li>Mutation rate in % (min: 0, max: 100).</li>
</ul>
Then all is left to do is to press the <b>Start simulation</b> button. You can change tick and mutation rate while the simulation is running.

<h1>Timeline</h1>
<h2>23-05-03</h2>
Reworked the whole program, added crude support for Tkinter interface.
<h2>22-04-20</h2>
Added RGB genes that denote first possible cell phenotype - its color. Genes are inherited when cells evolve and mutate in random direction. Additionally, map is now printed with a help of ANSI colors, helping to visualize the map.
<h2>22-04-19</h2>
Reworked cell splitting to be based around the tile owner, representing each "player" getting a "turn". Added simple stats to be printed out.
<h2>22-04-16</h2>
Implemented very simple owner and tile classes.
<h2>22-04-06:</h2>
Very basic simple script. Generates a matrix with 0's representing empty spaces and a single 1, representing a cell. The cell can then split and occupy neighbouring places. The cell also has a chance to mutate, represented by adding +1 to cell value.
