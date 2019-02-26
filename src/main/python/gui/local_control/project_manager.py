import os
from git import Repo
from git import IndexFile
from src.github_control import user_account as uc

class ProjectManager(object):

    def __init__(self, user: uc.UserAccount):
        """
        Construct a new ProjectManager instance to view projects, must be associated with 
        a UserAccount
        """
        self.curr_user = user
        return None

    def find_project_repo(self, path: str) -> Repo: 
        """
        Arguments:
            path: the absolute path of the directory to be checked.
        
        Returns Repo object if the directory given from path is a working tree directory for 
        a repository or a subdirectory of a working tree, returns None otherwise. 
        """
        norm_path = os.path.normpath(path)
        if os.path.exists(norm_path) is False:
            AssertionError("Path given to find a repository is not a valid file path.")
            return None
        else:
            # primitive implementation, assume this is the working tree directory
            return Repo(path)
        
    def view_project_repo(self, path: str):
        """
        Arguments:
            path: the absolute path of the directory to be checked, error if path is invalid.
        
        If the absolute path is an existing working tree directory or a subdirectory then
        GitUp recognizes this as a project and ensures a remote repository is associated
        with the user's account to backup the local repository. If the given path is not 
        part of an existing repository then a new repository is created and associated with
        a remote repository on the user's account. Always returns a Repo instance associated
        with the path.
        """
        norm_path = os.path.normpath(path)
        if os.path.exists(norm_path) is False:
            AssertionError("Path given to view a project is not a valid file path.")

        # check if directory is associated with an existing repository
        repo = self.find_project_repo(norm_path)

        if repo is None:
            # if the directory is not part of an existing repository then create a new one associated with
            # a remote on the user's GitHub account.
            # CREATE A NEW REPOSITORY
            repo = Repo.init(path=norm_path, bare=True)
        # ensure the repository has the GitUp remote
        if not repo.remote(name="GitUp").exists:
            self.curr_user.create_remote_repo(repo)
        # return the Repo object for this path
        return repo    

    def restore_project_repo(self, path: str, repo_name: str):
        """
        Arguments:
            path: the absolute path of the directory to restore the repository, error if path is invalid.
            repo_name: the name of the repository as shown on GitHub, error if no invalid.

        Restores the latest version of a project on a remote repository (associated with the user's GitHub
        account) in a folder using the repo_name at the given path.
        """
        NotImplementedError()
    
    def delete_project_repo(self, path: str, remove_files=False):
        """
        Arguments:
            path: the absolute path of a working tree directory of an existing local repository, error if no repo.
            remove_files: if True remove the repository files on the user's GitHub acccount.
        
        Removes the origin remote from a local repository. Deletes the repository files on the users
        GitHub account if remove_files is True.
        """
        NotImplementedError()