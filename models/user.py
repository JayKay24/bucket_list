class User:
    """
    Class to instantiate User objects.
    """
    def __init__(self, fname, lname, password):
        self.first_name = fname
        self.last_name = lname
        self.full_name = ' '.join([self.first_name, self.last_name])
        self.password = password
        
        