from funcofgitapi import *
import time


def take_variant(lab, taskid):
    if lab == 2:
        if taskid < 17:
            return taskid + 4
        elif taskid > 16:
            return taskid - 16
    elif lab == 3:
        if taskid < 21:
            return taskid
        else:
            return taskid % 20
    else: return taskid

class GitHub:
    @classmethod
    def check_commit(repo, lab, nick, num_in_list):
        REPO_OWNER = "suai-os-2024"
        repo = f"{REPO_OWNER}/os-task{lab}-{nick}"
        commits = get_commits(repo)
        sha = 0
        for commit in reversed(commits):
            sha = commit['sha']
            commit_date = commit['commit']['committer']['date']
            runs = get_workflow_runs(repo, sha)
            
            if runs['total_count'] > 0:
                all_tests_passed = True
                for run in runs['workflow_runs']:
                    if run['conclusion'] != 'success':
                        all_tests_passed = False
                        break
                
                if all_tests_passed:
                    print(f"Первый коммит, прошедший все тесты: {sha}, дата коммита: {commit_date}")
                    break
                
        workflow_runs = get_workflow_runs_by_sha(repo, sha)
        if workflow_runs:
            taskid = check_all_tests_passed(repo, workflow_runs)
            print("TASKDID is ", taskid)
        if taskid == 0:
            return -3 # file with taskid not detected
        var = take_variant(lab, taskid)
        if lab == 2 or lab == 3:
            if num_in_list != take_variant(lab, num_in_list):
                return -2 # flag of wrong taskid
        else:
            if num_in_list != taskid:
                return -2
            
        flag_of_changes = check_changes(repo, sha, lab)
        if flag_of_changes == 0:
            return -4 # detected changes in file
        
        
        