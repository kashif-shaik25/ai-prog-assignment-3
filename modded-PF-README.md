
In the first version of this bot, we assumed the UGV had a perfect map of the battlefield before it ever started moving. 
This second iteration upgrades the UGV to handle "Unknown Environments." The vehicle now starts with a blank map and must learn about its surroundings as it travels.

## How it Works
Instead of calculating a single path and following it blindly, the UGV now operates on a **Sense-Plan-Act** loop:

1. **Sensing:** The UGV has a limited "sensor range" (set to 5km). It only sees obstacles that are physically close to its current position.
2. **Learning:** Every time a sensor picks up an obstacle, the UGV updates its internal memory. It "remembers" where the danger is so it doesn't make the same mistake twice.
3. **Re-planning:** If the UGV realizes its current planned path is blocked by a newly discovered obstacle, it stops immediately. It then uses the A* algorithm to calculate a brand new route from its current coordinates to the goal, using all the data it has gathered so far.

## Performance Metrics (MoE)
To judge how effective this "blind" navigation is, we track:
* **Total Distance:** How much extra ground did we cover because we didn't know the map at the start?
* **Re-plan Count:** How many times did the UGV have to "change its mind" after hitting a dead end? This is a key measure of how efficiently the vehicle reacts to surprises.
* **Success Rate:** Can the UGV actually find the goal when it's forced to explore the map manually?


## Setup
Run the script as usual:
```bash
python dynamic_ugv.py
