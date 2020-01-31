class FileHandler:

    @staticmethod
    def create_file(m, b):
        with open('data/theta_saver.lr', 'w') as lr:
            lr.write(f"theta0 : {b}\ntheta1 : {m}")
