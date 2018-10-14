import threading
import queue
import time

class _WorkItem(object):
    def __init__(self, fn, args, kwargs):
        self.fn = fn
        self.args = args
        self.kwargs = kwargs

    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except Exception as e:
            print(e)
            
class ThreadPool(object):
    def __init__(self, max_workers, thread_name_prefix=''):
        self._max_workers = max_workers
        self._work_queue = queue.Queue() # work queue, which size can larger than max_workers
        self._work_queue_size = 0
        self._threads = set() # actual executing
        self._shutdown_lock = threading.Lock()
        self._thread_name_prefix = thread_name_prefix
    
    def showMeta(self):
        print("threads hold: {}, works: {}".format(len(self._threads), self._work_queue_size))

    def _consuming_worker(self):
        while True:
            w = self._work_queue.get(block=True) 
            if w is not None:
                w.run()
                self._work_queue_size -= 1
                del w            

    def submit(self, fn, *args, **kwargs):
        with self._shutdown_lock:
            w = _WorkItem(fn, args, kwargs)
            self._work_queue.put(w)
            self._work_queue_size += 1
            self._adjust_thread_count() # will create thread if no exceed max. size

    def _adjust_thread_count(self):
        num_threads = len(self._threads)
        if num_threads < self._max_workers:
            thread_name = '%s_%d' % (self._thread_name_prefix or self, num_threads)
            t = threading.Thread(
                name=thread_name,
                target=self._consuming_worker)
            print("create thread ({})".format(thread_name))
            t.daemon = True
            t.start()
            self._threads.add(t)

def working(num):
    print("     [{}] sleep 3 second...".format(num))
    time.sleep(2)
    print("     [{}] wake up! ".format(num))

def main():
    pool = ThreadPool(2)
    pool.showMeta()
    for i in range(10):
        pool.submit(working, i + 1)
        pool.showMeta()
    pool.showMeta()
    
if __name__ == "__main__":
    print("start...")
    main()
    time.sleep(30)
    print("done")
        