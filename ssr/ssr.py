"""Main module."""
import os

class SSR(object):
    """
    Console Interface and Processing of simple commands.
    """
    def __init__(self, args):
        """Set up and parse command line options"""
        self.args = args
        pass

    def process(self):
        """
        Main entry point.
        Process command line options, call appropriate logic.
        """
        def get_username():
            import pwd
            return pwd.getpwuid( os.getuid() )[ 0 ]        

        def get_mnt_folder():
            import platform
            ms = platform.uname()
            node = ms.node.replace(' ', '-')
            return f'reverse-{node}'

        import random
        cwd = os.getcwd()
        port = random.randint(9001,9999)
        username = get_username()
        mnt_folder = '/mnt/' + get_mnt_folder()
        scmd = f'''ssh -t {self.args._[0]} -R {port}:0:22 'sudo rm ~/.ssh/known_hosts;  sudo mkdir -p {mnt_folder}; alias ime="bash /media/cdrom/install-me.sh"; sudo umount -l {mnt_folder};sudo sshfs "{username}@0:{cwd}/" "{mnt_folder}" -p {port} -o reconnect,allow_other,ServerAliveInterval=10,ServerAliveCountMax=2; bash -l'  '''
        print(scmd)
        os.system(scmd)


def main():
    """
     Start procedure
    """
    return
    ssr = SSR()
    ssr.process()

if __name__ == '__main__':
    main()


