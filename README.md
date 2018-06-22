# median_voting
The median voting procedure is often used for financial votes. It calculates the highest value that has a majority given all votes.
Example: There is a petition for 200€. All people / groups that are allowed to vote on this have casted the following votes: 0, 150, 150, 200, 200, 200. So we have six voters and thus for a majority we need more than three votes. The highest value that has this property is 150€.

## Installation
Just install via pip:
```bash
pip install median_voting
```

## Creating a Median Vote
This library also supports so called *weighted votes*. This means that each person / group that casts a vote can have a weight > 0 (for example weighted according to a number of people the group represents). In the example above all voters had a weight of 1, i.e. all the same weight. We can think of the voting from above as a voting with groups with different weights:
* Group 1 has a weight of 1 and voted for 0€
* Group 2 has a weight of 2 and voted for 150€
* Group 3 has a weight of 3 and voted for 200€

To create this voting look at the following code:
```python
v1 = MedianVote(0)  
v2 = MedianVote(150, 2)  
v3 = MedianVote(200, 3)  

stat = MedianStatistics([v1, v2, v3])  
assert stat.median() == 150
```

A `MedianVote` object stores the information about a casted vote: The first argument is the value voted for and the second (optional) argument the weight (defaults to 1, must be > 0). The `MedianStatistics` type is used to query results. The most important method is the `median` method that just returns the result (or  `None` if no vote reached a majority, this should usually not happen because 0 should always have a majority). See the code documentation for more details.
There is also a rather experimental `details` method, again see the source code for details.

## License
**MIT License**

Copyright (c) 2018 Fabian Wenzelmann

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
