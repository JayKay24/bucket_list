class Entry:
    """
    Class to instantiate bucketlist entries.
    """
    def __init__(self, name):
        self.name = name
        self.done = False