from project.main.system import shell

def install():
    shell.execute("pip3 install pymysql")



if __name__ == '__main__':
    install()
