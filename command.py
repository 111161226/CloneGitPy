import git

def excecute(cmd):
    if cmd[0] == "git":
        if len(cmd) >= 2: 
            repo = git.Repo.init()
            if cmd[1] == "add":
                if len(cmd) >= 3 and cmd[2] != ".":
                    for i in range(2, len(cmd)):
                        repo.index.add(cmd[i])
            elif cmd[1] == "commit":
                if cmd[2] == "-m" and len(cmd) >= 4:
                    mess = ""
                    for i in range(3, len(cmd)):
                        mess+=cmd[i]
                else:
                    mess = "done commit"
                repo.index.commit(mess)
            elif cmd[1] == "clone":
                if len(cmd) == 3:
                    git.Git().clone(cmd[2])
            elif cmd[1] == "remote":
                if len(cmd) == 5 and cmd[2] == "add":
                    repo.create_remote(cmd[3], cmd[4])
        
        print("excecute ", *cmd[0:])

    else:
        print("No such command")