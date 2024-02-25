import multiprocessing

def test():
    print("this is my multiprocessing prog")

if __name__ == "__main__":
    m = multiprocessing.Process(target=test)
    print("this is my main prod")
    m.start()
    m.join()
    