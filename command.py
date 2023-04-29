import git

def excecute(cmd):
    if cmd[0] == "git":
        repo = git.Repo.init()
        print("excecute ", cmd[0:])

    else:
        print("No such command")