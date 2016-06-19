####pktestdrvpydev
#####Chapter 1
in project root folder, run
```
python -m unittest
```
do not forget to add a __init__  
######
-s startdict -t topdict
```
python -m unittest discover -s CP1\test -t .
python -m unittest CP1.test.test_stock
```
#####cp4 Using mock
######simple test without mock
```
>>> from CP4.event import Event
>>> def handle(num):
...     print("{0}".format(num))
...
>>> event=Event()
>>> event.fire(3)
>>> event.connect(handle)
>>> event.fire(3)
3
```
######Using the python mocking framework
```
assert_called_with
assert_called_once_with
assert_any_call
assert_has_calls
```