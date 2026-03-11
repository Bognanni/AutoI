import subprocess


class OpenFile:
    def __init__(self, path_exe):
        self.path_exe = path_exe

    def exe_file(self):
        try:
            # Esegui il file utilizzando subprocess
            subprocess.Popen([self.path_exe])
        except subprocess.CalledProcessError as e:
            print(f"Errore durante l'esecuzione del file: {e}")
            return False
        return True

    def get_path_exe(self):
        return self.path_exe

    def set_path_exe(self, path_exe):
        self.path_exe = path_exe
