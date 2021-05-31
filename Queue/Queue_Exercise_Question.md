<h4> For all exercises use Queue class.<br>
    
Question : Design a food ordering system where your python program will run two threads,

Place Order: This thread will be placing an order and inserting that into a queue. This thread places new order every 0.5 second. (hint: use time.sleep(0.5) function)<br>
    
Serve Order: This thread will server the order. All you need to do is pop the order out of the queue and print it. This thread serves an order every 2 seconds. Also start this thread 1 second after place order thread is started.

Use this video to get yourself familiar with <a href ="https://www.youtube.com/watch?v=PJ4t2U15ACo">multithreading in python</a>

Pass following list as an argument to place order thread,

orders = ['pizza','samosa','pasta','biryani','burger']<br>

This problem is a producer,consumer problem where place_order thread is producing orders whereas server_order thread is consuming the food orders. Use Queue class implemented in a video tutorial.</h4>
