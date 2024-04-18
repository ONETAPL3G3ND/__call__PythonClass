class Site:
    def __init__(self):
        self.count = 0
        self.site = "Hi, this is a small website"

    def __call__(self, *args, **kwargs):
        self.count += 1

    def get(self):
        self()
        return self.site



if __name__ == "__main__":
    site = Site()
    print(site.get())
    print(site.get())
    print(site.get())
    print(site.get())
    print(site.get())
    print(site.get())
    print(site.count)

