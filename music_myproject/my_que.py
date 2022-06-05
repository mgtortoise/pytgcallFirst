import queue
q = queue.Queue()
def insert_data(name):
    q.put(name)

def get_data():
     while not q.empty():
         return q.get()
