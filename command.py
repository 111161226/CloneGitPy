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
                        mess+=cmd[i]+" "
                else:
                    mess = "done commit"
                repo.index.commit(mess)
            elif cmd[1] == "clone":
                if len(cmd) == 3:
                    git.Git().clone(cmd[2])
            elif cmd[1] == "remote":
                if len(cmd) == 5 and cmd[2] == "add":
                    repo.create_remote(cmd[3], cmd[4])
            elif cmd[1] == "push":
                if 4 <= len(cmd) <= 5:
                    if len(cmd) == 5 and cmd[3] == "--delete":
                        repo.git.push('--delete', cmd[2], cmd[4])
                    else:
                        repo.git.push(cmd[2], cmd[3])
            elif cmd[1] == "branch":
                if len(cmd) == 3:
                    repo.git.branch(cmd[2])
                else:
                    repo.git.branch()
            elif cmd[1] == "log":  
                for commit in repo.iter_commits("main"):
                    print('|' * 55)
                    print(commit.hexsha)
                    print('|' * 55)
                    for diff in commit.diff():
                        print(diff)
                            
        print("excecute ", *cmd[0:])

    else:
        print("No such command")