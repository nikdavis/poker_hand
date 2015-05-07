Big questions:

How best to represent cards (suits & values)?
* suit
* nominal value (1, 2, jack, etc)
* numeric bigness (8, 9, 10, 10/jack, 10/queen)
* numeric order (8, 9, 10, 11/jack, 12/queen)

How to represent hands?
* some object
* defined rank
  * If rank is the same, some way to compare same object


e.g.

```python
class Hand(object):
```
