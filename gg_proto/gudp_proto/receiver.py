from gudp_client import Client

def run():
    c = Client(1,"127.0.0.1", 8080, "127.0.0.1", 8082)
    while True:
        q = c.recv()
        print("q : {}".format(q))


if __name__ == "__main__":
    run()