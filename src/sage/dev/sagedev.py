- David Roe, Frej Drejhammar, Julian Rueth, Martin Raum, Nicolas M. Thiery,
  R. Andrew Ohana, Robert Bradshaw, Timo Kluck: initial version
#                          Volker Braun <vbraun.name@gmail.com>
import os
import urllib, urlparse
import re

from patch import MercurialPatchMixin

from sage.env import TRAC_SERVER_URI
# http://stackoverflow.com/questions/12093748/how-do-i-check-for-valid-git-branch-names
GIT_BRANCH_REGEX = re.compile(
    r'^(?!.*/\.)(?!.*\.\.)(?!/)(?!.*//)(?!.*@\{)(?!.*\\)'
    r'[^\040\177 ~^:?*[]+(?<!\.lock)(?<!/)(?<!\.)$')
#
# The first line should contain a short summary of your changes, the
# following lines should contain a more detailed description. Lines
# starting with '#' are ignored.
class SageDev(MercurialPatchMixin):
    - ``config`` -- a :class:`~sage.dev.config.Config` or ``None``
      (default: ``None``), the configuration of this object; the
      defaults uses the configuration stored in ``DOT_SAGE/devrc``.
    - ``UI`` -- a :class:`~sage.dev.user_interface.UserInterface` or ``None`` (default:
                self._UI.show('The developer scripts used to store some of their data in "{0}".'
                              ' This file has now moved to "{1}". I moved "{0}" to "{1}". This might'
                              ' cause trouble if this is a fresh clone of the repository in which'
                              ' you never used the developer scripts before. In that case you'
                              ' should manually delete "{1}" now.', old_file, new_file)
        move_legacy_saving_dict('ticketfile', self.config['sagedev'].get(
            'ticketfile', os.path.join(DOT_SAGE, 'branch_to_ticket')), ticket_file)
        move_legacy_saving_dict('branchfile', self.config['sagedev'].get(
            'branchfile', os.path.join(DOT_SAGE, 'ticket_to_branch')), branch_file)
        move_legacy_saving_dict('dependenciesfile', self.config['sagedev'].get(
            'dependenciesfile', os.path.join(DOT_SAGE, 'dependencies')), dependencies_file)
        move_legacy_saving_dict('remotebranchesfile', self.config['sagedev'].get(
            'remotebranchesfile', os.path.join(DOT_SAGE, 'remote_branches')), remote_branches_file)
            from sage.dev.misc import tmp_dir
            self._tmp_dir = tmp_dir()
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)

            Created ticket #2 at https://trac.sagemath.org/2.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=2" to create a new local branch)
            self._UI.debug("Ticket creation aborted.")
        ticket_url = urlparse.urljoin(self.trac._config.get('server', TRAC_SERVER_URI), str(ticket))
        self._UI.show("Created ticket #{0} at {1}.".format(ticket, ticket_url))
        self._UI.info(['',
                       '(use "{0}" to create a new local branch)'
                       .format(self._format_command("checkout", ticket=ticket))])
        Checking out a branch::
            On local branch "branch1" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
        ticket = self._current_ticket()
        branch = self.git.current_branch()
        if ticket:
            self._UI.show(['On ticket #{0} with associated local branch "{1}".'], ticket, branch)
        else:
            self._UI.show(['On local branch "{0}" without associated ticket.'], branch)
        self._UI.info(['',
                       'Use "{0}" to include another ticket/branch.',
                       'Use "{1}" to save changes into a new commit.'],
                      self._format_command("merge"),
                      self._format_command("commit"))


            Ticket name "1" is not valid or ticket does not exist on trac.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/bob/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Ticket #1 refers to the non-existant local branch "ticket/1". If you have not
            manually interacted with git, then this is a bug in sagedev. Removing the
            association from ticket #1 to branch "ticket/1".
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #2 at https://trac.sagemath.org/2.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=2" to create a new local branch)
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            This happened while executing "git -c user.email=doc@test.test -c
            user.name=alice checkout ticket/1".
            sage: open("tracked", "w").close()
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Keep/stash] d
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #2 at https://trac.sagemath.org/2.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=2" to create a new local branch)
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #3 at https://trac.sagemath.org/3.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=3" to create a new local branch)
            On ticket #3 with associated local branch "ticket/3".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #4 at https://trac.sagemath.org/4.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=4" to create a new local branch)
            On ticket #4 with associated local branch "ticket/4".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #5 at https://trac.sagemath.org/5.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=5" to create a new local branch)
            Ticket name "1000" is not valid or ticket does not exist on trac.
            Created ticket #6 at https://trac.sagemath.org/6.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=6" to create a new local branch)
            Branch field is not set for ticket #5 on trac.
            Created ticket #7 at https://trac.sagemath.org/7.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=7" to create a new local branch)
            On ticket #7 with associated local branch "ticket/7".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #8 at https://trac.sagemath.org/8.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=8" to create a new local branch)
            sage: UI.append("cancel")
            Repository is in an unclean state (merge). Resetting the state will discard any
            uncommited changes.
            Reset repository? [reset/Cancel] cancel
            Aborting checkout of branch "ticket/8".
            <BLANKLINE>
            #  (use "sage --dev commit" to save changes in a new commit)
            Created ticket #9 at https://trac.sagemath.org/9.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=9" to create a new local branch)

        The new branch is based on master which is not the same commit
        as the current branch ``ticket/7``, so it is not a valid
        option to ``'keep'`` changes::

            sage: UI.append("cancel")
            sage: dev.checkout(ticket=9)
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] cancel
            Aborting checkout of branch "ticket/9".
            <BLANKLINE>
            #  (use "sage --dev commit" to save changes in a new commit)

        Finally, in this case we can keep changes because the base is
        the same commit as the current branch::
            Created ticket #10 at https://trac.sagemath.org/10.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=10" to create a new local branch)
            sage: dev.checkout(ticket=10, base='ticket/7')
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Keep/stash] keep
            On ticket #10 with associated local branch "ticket/10".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            self._UI.debug('The branch for ticket #{0} is now "{1}".', ticket, branch)
            self._UI.debug('Now checking out branch "{0}".', branch)
                self._UI.debug('Checking out branch "{0}".', branch)
            raise SageDevValueError('currently on no ticket, "base" must not be None')
                    self._UI.debug('The branch field on ticket #{0} is not set. Creating a new branch'
                                   ' "{1}" off the master branch "{2}".', ticket, branch, MASTER_BRANCH)
                        self._UI.error('The branch field on ticket #{0} is set to the non-existent "{1}".'
                                       ' Please set the field on trac to a field value.',
                                       ticket, remote_branch)
                        self._UI.info(['', '(use "{0}" to edit the ticket description)'],
                                       self._format_command("edit-ticket", ticket=ticket))

                    self.git.super_silent.fetch(self.git._repository_anonymous, remote_branch)
                    self.git.super_silent.branch(branch, 'FETCH_HEAD')
                    self._UI.show('About to create a new branch for #{0} based on "{1}". However, the trac'
                                  ' ticket for #{0} already refers to the branch "{2}". The new branch will'
                                  ' not contain any work that has already been done on "{2}".',
                                  ticket, base, remote_branch)
                    if not self._UI.confirm('Create fresh branch?', default=False):
                        self._UI.info(['', 'Use "{1}" to work on a local copy of the existing remote branch "{0}".'],
                                      remote_branch, command)
                self._UI.debug('Creating a new branch for #{0} based on "{1}".', ticket, base)
                self._UI.debug('Deleting local branch "{0}".', branch)
            self._UI.debug("Locally recording dependency on {0} for #{1}.",
                           ", ".join(["#"+str(dep) for dep in dependencies]), ticket)
        self._set_remote_branch_for_branch(branch, self._remote_branch_for_ticket(ticket))
        self._UI.debug('Checking out to newly created branch "{0}".'.format(branch))
    def checkout_branch(self, branch, helpful=True):
        - ``branch`` -- a string, the name of a local branch
        Checking out a branch::
            On local branch "branch1" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Branch "branch3" does not exist locally.
            <BLANKLINE>
            #  (use "sage --dev tickets" to list local branches)
            sage: open("untracked", "w").close()
            On local branch "branch2" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            sage: open("tracked", "w").close()
            sage: UI.append("cancel")
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] cancel
            Aborting checkout of branch "branch1".
            <BLANKLINE>
            #  (use "sage --dev commit" to save changes in a new commit)
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] s
            Your changes have been moved to the git stash stack. To re-apply your changes
            later use "git stash apply".
            On local branch "branch1" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.

        And retrieve the stashed changes later::
            On local branch "branch2" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            sage: dev.git.echo.stash('apply')
            # On branch branch2
            # Changes not staged for commit:
            #   (use "git add <file>..." to update what will be committed)
            #   (use "git checkout -- <file>..." to discard changes in working directory)
            #
            #   modified:   tracked
            #
            # Untracked files:
            #   (use "git add <file>..." to include in what will be committed)
            #
            #   untracked
            no changes added to commit (use "git add" and/or "git commit -a")
            sage: UI.append("discard")
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] discard
            On local branch "branch1" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            sage: UI.append('r')
            Repository is in an unclean state (merge). Resetting the state will discard any
            uncommited changes.
            Reset repository? [reset/Cancel] r
            On local branch "merge_branch" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            On local branch "branch1" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] discard
            On local branch "branch1" without associated ticket.
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            This happened while executing "git -c user.email=doc@test.test -c
            user.name=doctest checkout branch2".
            error: The following untracked working tree files would be overwritten
            by checkout:
            self.reset_to_clean_state(helpful=False)
            if helpful:
                self._UI.show('Aborting checkout of branch "{0}".', branch)
                self._UI.info(['', '(use "{0}" to save changes in a new commit)'],
                              self._format_command("commit"))
            self.clean(error_unless_clean=(current_commit != target_commit))
            if helpful:
                self._UI.show('Aborting checkout of branch "{0}".', branch)
                self._UI.info(['', '(use "{0}" to save changes in a new commit)'],
                              self._format_command("commit"))
            # this leaves locally modified files intact (we only allow this to happen
            # if current_commit == target_commit
    def pull(self, ticket_or_remote_branch=None):
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Branch field is not set for ticket #1 on trac.
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/alice/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            Merging the remote branch "u/alice/ticket/1" into the local branch "ticket/1".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            The branch "u/bob/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            The branch field of ticket #1 needs to be updated from its current value
            "u/alice/ticket/1" to "u/bob/ticket/1"
            Change the "Branch:" field? [Yes/no] y
            Merging the remote branch "u/bob/ticket/1" into the local branch "ticket/1".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            Local commits that are not on the remote branch "u/bob/ticket/1":
            <BLANKLINE>
                ...: bob: added alices_file
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            Merging the remote branch "u/bob/ticket/1" into the local branch "ticket/1".
            Automatic merge failed, there are conflicting commits.
            <BLANKLINE>
            <BLANKLINE>
            Please edit the affected files to resolve the conflicts. When you are finished,
            your resolution will be commited.
            Finished? [ok/Abort] abort
            Merging the remote branch "u/bob/ticket/1" into the local branch "ticket/1".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            Local commits that are not on the remote branch "u/bob/ticket/1":
            <BLANKLINE>
                ...: bob: added bobs_other_file
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            Merging the remote branch "u/bob/ticket/1" into the local branch "ticket/1".
            Automatic merge failed, there are conflicting commits.
            <BLANKLINE>
                    bobs_other_file
            <BLANKLINE>
            Please edit the affected files to resolve the conflicts. When you are finished,
            your resolution will be commited.
            Finished? [ok/Abort] abort
        self.merge(remote_branch, pull=True)
            - :meth:`push` -- Push changes to the remote server.  This
              is the next step once you've committed some changes.
            - :meth:`diff` -- Show changes that will be committed.
            sage: dev.git.super_silent.checkout('-b', 'branch1')
            sage: dev._UI.extend(["y", "added tracked", "y", "y"])
            <BLANKLINE>
                tracked
            <BLANKLINE>
            Start tracking any of these files? [yes/No] y
            Start tracking "tracked"? [yes/No] y
            Commit your changes to branch "branch1"? [Yes/no] y
            <BLANKLINE>
            #  Use "sage --dev push" to push your commits to the trac server once you are done.
            sage: with open("tracked", "w") as F: F.write("foo")
            sage: dev._UI.append('y')
            sage: dev.commit(message='modified tracked')
            Commit your changes to branch "branch1"? [Yes/no] y
            <BLANKLINE>
            #  Use "sage --dev push" to push your commits to the trac server once you are done.
            self._UI.info(['',
                           '(use "{0}" to checkout a branch)'
                           .format(self._format_command("checkout"))])
            self._UI.debug('Committing pending changes to branch "{0}".'.format(branch))
                    self._UI.show(['The following files in your working directory are not tracked by git:', ''] +
                                  ['    ' + f for f in untracked_files ] +
                                  [''])
                    if self._UI.confirm('Start tracking any of these files?', default=False):
                            if self._UI.confirm('Start tracking "{0}"?'.format(file), default=False):
                    from sage.dev.misc import tmp_filename
                    commit_message = tmp_filename()
                    with open(commit_message, 'w') as f:
                        f.write(COMMIT_GUIDE)
                    self._UI.edit(commit_message)
                    message = "\n".join([line for line in open(commit_message).read().splitlines()
                                         if not line.startswith("#")]).strip()
                if not self._UI.confirm('Commit your changes to branch "{0}"?'.format(branch), default=True):
                    self._UI.info(['', 'Run "{0}" first if you want to commit to a different branch or ticket.'],
                                  self._format_command("checkout"))
                    raise OperationCancelledError("user does not want to create a commit")
                self._UI.debug("A commit has been created.")
                self._UI.info(['', 'Use "{0}" to push your commits to the trac server once you are done.'],
                              self._format_command("push"))
                self._UI.debug("Not creating a commit.")
            - :meth:`push` -- To push changes after setting the remote
              branch
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
                self._UI.error('You must specify "branch" in detached HEAD state.')
                self._UI.info(['', 'Use "{0}" to checkout a branch'],
                              self._format_command('checkout'))
                self._UI.error('no local branch for ticket #{0} found. Cannot set remote branch'
                               ' for that ticket.', ticket)
            self._UI.warning('The remote branch "{0}" is not in your user scope. You probably'
                             ' do not have permission to push to that branch.', remote_branch)
            self._UI.info(['', 'You can always use "u/{1}/{0}" as the remote branch name.'],
                          remote_branch, self.trac._username)
            - :meth:`commit` -- Save changes to the local repository.
            - :meth:`pull` -- Update a ticket with changes from the remote
              repository.
            Ticket name "1" is not valid or ticket does not exist on trac.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/alice/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/bob/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            The branch field of ticket #1 needs to be updated from its current value
            "u/alice/ticket/1" to "u/bob/ticket/1"
            Change the "Branch:" field? [Yes/no] y
            Merging the remote branch "u/bob/ticket/1" into the local branch "ticket/1".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            Local commits that are not on the remote branch "u/alice/ticket/1":
            <BLANKLINE>
                ...: alice: modified tracked
                ...: bob: modified tracked
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            The branch field of ticket #1 needs to be updated from its current value
            "u/bob/ticket/1" to "u/alice/ticket/1"
            Change the "Branch:" field? [Yes/no] y
            Local commits that are not on the remote branch "u/bob/ticket/1":
            <BLANKLINE>
                ....: bob: added tracked2
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            Not setting the branch field for ticket #1 to "u/bob/ticket/1" because
            "u/bob/ticket/1" and the current value of the branch field "u/alice/ticket/1"
            have diverged.
            <BLANKLINE>
            #  Use "sage --dev push --force --ticket=1 --remote-branch=u/bob/ticket/1" to overwrite the branch field.
            <BLANKLINE>
            #  Use "sage --dev pull --ticket=1" to merge the changes introduced by the remote "u/alice/ticket/1" into your local branch.
            Merging the remote branch "u/alice/ticket/1" into the local branch "ticket/1".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            Local commits that are not on the remote branch "u/bob/ticket/1":
            <BLANKLINE>
                ...: Merge branch 'u/alice/ticket/1' of ... into ticket/1
                ...: alice: modified tracked
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            The branch field of ticket #1 needs to be updated from its current value
            "u/alice/ticket/1" to "u/bob/ticket/1"
            Change the "Branch:" field? [Yes/no] y
            Ticket name "2" is not valid or ticket does not exist on trac.
            Created ticket #2 at https://trac.sagemath.org/2.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=2" to create a new local branch)
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            About to push the branch "ticket/1" to "u/bob/ticket/2" for ticket #2. However,
            your local branch for ticket #2 seems to be "ticket/2".
             Do you really want to proceed? [yes/No] y
            <BLANKLINE>
            #  Use "sage --dev checkout --ticket=2 --branch=ticket/1" to permanently set "ticket/1" as the branch associated to ticket #2.
            The branch "u/bob/ticket/2" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            The branch "u/bob/branch1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            The branch field of ticket #1 needs to be updated from its current value
            "u/bob/ticket/1" to "u/bob/branch1"
            Change the "Branch:" field? [Yes/no] y
            Merging the remote branch "u/bob/ticket/2" into the local branch "ticket/1".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            <BLANKLINE>
            sage: with open("another_file", "w") as f: f.write("bob after merge(2)")
            sage: bob._UI.append('n')
            The branch field of ticket #1 needs to be updated from its current value
            "u/bob/branch1" to "u/bob/ticket/1"
            Change the "Branch:" field? [Yes/no] n
            sage: bob._UI.extend(['y', 'y', 'y'])
            sage: bob.commit(message="Bob's merge")  # oops
            The following files in your working directory are not tracked by git:
            <BLANKLINE>
                another_file
            <BLANKLINE>
            Start tracking any of these files? [yes/No] y
            Start tracking "another_file"? [yes/No] y
            Commit your changes to branch "ticket/1"? [Yes/no] y
            <BLANKLINE>
            #  Use "sage --dev push" to push your commits to the trac server once you are done.
            sage: bob._UI.extend(['y', 'y'])
            Local commits that are not on the remote branch "u/bob/ticket/1":
            <BLANKLINE>
                ...: Bob's merge
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            The branch field of ticket #1 needs to be updated from its current value
            "u/bob/branch1" to "u/bob/ticket/1"
            Change the "Branch:" field? [Yes/no] y
            Uploading your dependencies for ticket #1: "" => "#2"
            sage: bob._sagedev._set_dependencies_for_ticket(1,())
            sage: with open("another_file", "w") as f: f.write("bob after push")
            sage: bob._UI.extend(['y', 'y', 'y'])
            sage: bob.commit(message='another commit')
            Commit your changes to branch "ticket/1"? [Yes/no] y
            <BLANKLINE>
            #  Use "sage --dev push" to push your commits to the trac server once you are done.
            sage: bob._UI.extend(['y', "keep", 'y'])
            Local commits that are not on the remote branch "u/bob/ticket/1":
            <BLANKLINE>
                ...: another commit
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            Trac ticket #1 depends on #2 while your local branch depends on no tickets.
            Updating dependencies is recommended but optional.
            Action for dependencies? [upload/download/keep] keep
            sage: with open("another_file", "w") as f: f.write("bob after 2nd push")
            sage: bob._UI.append('y')
            sage: bob.commit(message='final commit')
            Commit your changes to branch "ticket/1"? [Yes/no] y
            <BLANKLINE>
            #  Use "sage --dev push" to push your commits to the trac server once you are done.
            sage: bob._UI.extend(['y', 'download', 'y'])
            sage: bob.push()
            Local commits that are not on the remote branch "u/bob/ticket/1":
            <BLANKLINE>
                ...: final commit
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            Trac ticket #1 depends on #2 while your local branch depends on no tickets.
            Updating dependencies is recommended but optional.
            Action for dependencies? [upload/download/keep] download
                    raise SageDevValueError("remote_branch must be specified since #{0}"
                                            " has no remote branch set.".format(ticket))
                    raise SageDevValueError("remote_branch must be specified since the"
                                            " current branch has no remote branch set.")
        user_confirmation = False
                self._UI.show('About to push the branch "{0}" to "{1}" for ticket #{2}.'
                              ' However, your local branch for ticket #{2} seems to be "{3}".',
                              branch, remote_branch, ticket, self._local_branch_for_ticket(ticket))
                user_confirmation = self._UI.confirm(' Do you really want to proceed?', default=False)
                if user_confirmation:
                    self._UI.info(['',
                                   'Use "{2}" to permanently set "{1}" as the branch'
                                   ' associated to ticket #{0}.'],
                                  ticket, branch, self._format_command("checkout",ticket=ticket,branch=branch))
                self._UI.show('About to push the local branch "{0}" to remote branch "{1}" for'
                              ' ticket #{2}. However, that branch is already associated to ticket #{3}.',
                              branch, remote_branch, ticket, self._ticket_for_local_branch(branch))
                user_confirmation = self._UI.confirm(' Do you really want to proceed?', default=False)
                if user_confirmation:
                    self._UI.info(['', 'Use "{2}" to permanently set the branch associated to'
                                   ' ticket #{0} to "{1}". To create a new branch from "{1}" for'
                                   ' #{0}, use "{3}" and "{4}".'],
                                  ticket, branch,
                                  self._format_command("checkout",ticket=ticket,branch=branch),
                                  self._format_command("checkout",ticket=ticket),
                                  self._format_command("merge", branch=branch))

        self._UI.debug('Pushing your changes in "{0}" to "{1}".'.format(branch, remote_branch))
                self._UI.show('The branch "{0}" does not exist on the remote server.', remote_branch)
                if not self._UI.confirm('Create new remote branch?', default=True):
                    self._UI.error('Not pushing your changes because they would discard some of'
                                   ' the commits on the remote branch "{0}".', remote_branch)
                    self._UI.info(['', 'Use "{0}" if you really want to overwrite the remote branch.'],
                                  self._format_command("push", ticket=ticket,
                                                       remote_branch=remote_branch, force=True))
            if remote_branch_exists and not force and \
               self.git.commit_for_branch(branch) == self.git.commit_for_ref('FETCH_HEAD'):
                self._UI.debug('Remote branch "{0}" is idential to your local branch "{1}',
                              remote_branch, branch)
                self._UI.debug(['', '(use "{0}" to commit changes before pushing)'],
                               self._format_command("commit"))
                            self._UI.show(['Local commits that are not on the remote branch "{0}":', ''] +
                                          ['    ' + c for c in commits.splitlines()] +
                                          [''], remote_branch)
                            if not self._UI.confirm('Push to remote branch?', default=True):
                    self.git.super_silent.push(self.git._repository,
                                               "{0}:{1}".format(branch, remote_branch),
                                               force=force)
                self._UI.debug('Changes in "{0}" have been pushed to "{1}".'.format(branch, remote_branch))
            self._UI.debug("Did not push any changes.")
                self._UI.debug('Not setting the branch field for ticket #{0} because it already'
                               ' points to your branch "{1}".'.format(ticket, remote_branch))
                self._UI.debug('Setting the branch field of ticket #{0} to "{1}".'.format(ticket, remote_branch))
                        self._UI.error('Not setting the branch field for ticket #{0} to "{1}" because'
                                       ' "{1}" and the current value of the branch field "{2}" have diverged.'
                                       .format(ticket, remote_branch, current_remote_branch))
                        self._UI.info(['', 'Use "{0}" to overwrite the branch field.', '',
                                       'Use "{1}" to merge the changes introduced by'
                                       ' the remote "{2}" into your local branch.'],
                                      self._format_command("push", ticket=ticket,
                                                           remote_branch=remote_branch, force=True),
                                      self._format_command("pull", ticket=ticket),
                                      current_remote_branch)
                    self._UI.show('The branch field of ticket #{0} needs to be'
                                  ' updated from its current value "{1}" to "{2}"'
                                  ,ticket, current_remote_branch, remote_branch)
                    if not self._UI.confirm('Change the "Branch:" field?', default=True):
                    self._UI.show('Trac ticket #{0} depends on {1} while your local branch depends'
                                  ' on {2}. Updating dependencies is recommended but optional.',
                                  ticket, old_dependencies, new_dependencies or "no tickets"),
                    sel = self._UI.select('Action for dependencies?', options=("upload", "download", "keep"))
                        self._UI.debug("Setting dependencies for #{0} to {1}.", ticket, old_dependencies)
                self._UI.debug("Not uploading your dependencies for ticket #{0} because the"
                               " dependencies on trac are already up-to-date.", ticket)
                self._UI.show('Uploading your dependencies for ticket #{0}: "{1}" => "{2}"',
                              ticket, old_dependencies, new_dependencies)
    def reset_to_clean_state(self, error_unless_clean=True, helpful=True):
        - ``error_unless_clean`` -- a boolean (default: ``True``),
          whether to raise an
          :class:`user_interface_error.OperationCancelledError` if the
            sage: UI.append("cancel")
            Repository is in an unclean state (merge). Resetting the state will discard any
            uncommited changes.
            Reset repository? [reset/Cancel] cancel
            <BLANKLINE>
            #  (use "sage --dev commit" to save changes in a new commit)
            sage: UI.append("reset")
            Repository is in an unclean state (merge). Resetting the state will discard any
            uncommited changes.
            Reset repository? [reset/Cancel] reset
        self._UI.show('Repository is in an unclean state ({0}).'
                      ' Resetting the state will discard any uncommited changes.',
                      ', '.join(states))
        sel = self._UI.select('Reset repository?',
                              options=('reset', 'cancel'), default=1)
        if sel == 'cancel':
            if not error_unless_clean:
            if helpful:
                self._UI.info(['', '(use "{0}" to save changes in a new commit)'],
                              self._format_command("commit"))
        elif sel == 'reset':
            self.git.reset_to_clean_state()
        else:
            assert False
    def clean(self, error_unless_clean=True):
        Restore the working directory to the most recent commit.
        - ``error_unless_clean`` -- a boolean (default: ``True``),
          whether to raise an
          :class:`user_interface_error.OperationCancelledError` if the
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] discard
            sage: UI.append("cancel")
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] cancel
            <BLANKLINE>
                 tracked
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] stash
            Your changes have been moved to the git stash stack. To re-apply your changes
            later use "git stash apply".
            self.reset_to_clean_state(error_unless_clean)
        files = [line[2:] for line in self.git.status(porcelain=True).splitlines()
                 if not line.startswith('?')]

        self._UI.show(
            ['The following files in your working directory contain uncommitted changes:'] +
            [''] +
            ['    ' + f for f in files ] +
            [''])
        cancel = 'cancel' if error_unless_clean else 'keep'
        sel = self._UI.select('Discard changes?',
                              options=('discard', cancel, 'stash'), default=1)
            self.git.clean_wrapper()
        elif sel == cancel:
            if error_unless_clean:
            self.git.super_silent.stash()
            self._UI.show('Your changes have been moved to the git stash stack. '
                          'To re-apply your changes later use "git stash apply".')
            assert False
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
        r"""
        - ``ticket`` -- an integer or string identifying a ticket or
          ``None`` (default: ``None``), the number of the ticket to
          edit.  If ``None``, edit the :meth:`_current_ticket`.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/doctest/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
        self._UI.debug("Ticket #%s marked as needing review"%ticket)
        r"""
        - ``ticket`` -- an integer or string identifying a ticket or
          ``None`` (default: ``None``), the number of the ticket to
          edit.  If ``None``, edit the :meth:`_current_ticket`.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/alice/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
        self._UI.debug("Ticket #%s marked as needing work"%ticket)
        r"""
        - ``ticket`` -- an integer or string identifying a ticket or
          ``None`` (default: ``None``), the number of the ticket to
          edit.  If ``None``, edit the :meth:`_current_ticket`.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/alice/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
        self._UI.debug("Ticket #%s marked as needing info"%ticket)
        r"""
        - ``ticket`` -- an integer or string identifying a ticket or
          ``None`` (default: ``None``), the number of the ticket to
          edit.  If ``None``, edit the :meth:`_current_ticket`.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/alice/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
        self._UI.debug("Ticket #%s reviewed!"%ticket)
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            ticket must be specified if not currently on a ticket.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Your branch "ticket/1" has 0 commits.
            The branch "u/doctest/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            Your branch "ticket/1" has 0 commits.
            The trac ticket points to the branch "u/doctest/ticket/1" which has 0 commits. It does not differ from "ticket/1".
            Your branch "ticket/1" has 1 commits.
            The trac ticket points to the branch "u/doctest/ticket/1" which has 0 commits. "ticket/1" is ahead of "u/doctest/ticket/1" by 1 commits:
            Local commits that are not on the remote branch "u/doctest/ticket/1":
            <BLANKLINE>
                ...: added tracked
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            Your branch "ticket/1" has 1 commits.
            The trac ticket points to the branch "u/doctest/ticket/1" which has 1 commits. It does not differ from "ticket/1".
            Your branch "ticket/1" has 0 commits.
            The trac ticket points to the branch "u/doctest/ticket/1" which has 1 commits. "u/doctest/ticket/1" is ahead of "ticket/1" by 1 commits:
            The branch "u/doctest/branch1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            Your branch "ticket/1" has 2 commits.
            The trac ticket points to the branch "u/doctest/branch1" which has 3 commits. "u/doctest/branch1" is ahead of "ticket/1" by 1 commits:
            Your remote branch "u/doctest/ticket/1" has 1 commits. The branches "u/doctest/ticket/1" and "ticket/1" have diverged.
            "u/doctest/ticket/1" is ahead of "ticket/1" by 1 commits:
            "ticket/1" is ahead of "u/doctest/ticket/1" by 2 commits:
        commits = lambda a, b: list(reversed(
            self.git.log("{0}..{1}".format(a,b), "--pretty=%an <%ae>: %s").splitlines()))
                return 'It does not differ from "{0}".'.format(b)
                return '"{0}" is ahead of "{1}" by {2} commits:\n{3}'.format(a,b,len(b_to_a), "\n".join(b_to_a))
                return '"{0}" is ahead of "{1}" by {2} commits:\n{3}'.format(b,a,len(a_to_b),"\n".join(a_to_b))
                return ('The branches "{0}" and "{1}" have diverged.\n"{0}" is ahead of'
                        ' "{1}" by {2} commits:\n{3}\n"{1}" is ahead of "{0}" by {4}'
                        ' commits:\n{5}'.format(a, b, len(b_to_a), "\n".join(b_to_a),
                                                len(a_to_b), "\n".join(a_to_b)))
            local_summary = 'Your branch "{0}" has {1} commits.'.format(branch, len(master_to_branch))
                ticket_summary = 'The trac ticket points to the branch "{0}" which does not exist.'
                ticket_summary = 'The trac ticket points to the' \
                    ' branch "{0}" which has {1} commits.'.format(ticket_branch, len(master_to_ticket))
                        ticket_summary += ' The branch can not be compared to your local' \
                            ' branch "{0}" because the branches are based on different versions' \
                            ' of sage (i.e. the "master" branch).'
            remote_summary = 'Your remote branch "{0}" has {1} commits.'.format(
                remote_branch, len(master_to_remote))
                    remote_summary += ' The branch can not be compared to your local' \
                        ' branch "{0}" because the branches are based on different version' \
                        ' of sage (i.e. the "master" branch).'
    def prune_tickets(self):
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            sage: dev.tickets()
            sage: dev.prune_tickets()
            sage: dev.tickets()
            sage: dev.prune_tickets()
            Cannot delete "ticket/1": is the current branch.
            <BLANKLINE>
            #  (use "sage --dev vanilla" to switch to the master branch)
            sage: dev.prune_tickets()
            Moved your branch "ticket/1" to "trash/ticket/1".
            sage: dev.tickets()
            sage: dev.prune_tickets()
                    self.abandon(ticket, helpful=False)
    def abandon(self, ticket_or_branch=None, helpful=True):
        - ``helpful`` -- boolean (default: ``True``). Whether to print
          informational messages to guide new users.

            - :meth:`prune_tickets` -- abandon tickets that have
              been closed.
            - :meth:`tickets` -- list local non-abandoned tickets.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/doctest/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            Cannot delete "ticket/1": is the current branch.
            <BLANKLINE>
            #  (use "sage --dev vanilla" to switch to the master branch)
            Moved your branch "ticket/1" to "trash/ticket/1".
            <BLANKLINE>
            #  Use "sage --dev checkout --ticket=1 --base=master" to restart working on #1 with a clean copy of the master branch.
            About to create a new branch for #1 based on "master". However, the trac ticket
            for #1 already refers to the branch "u/doctest/ticket/1". The new branch will
            not contain any work that has already been done on "u/doctest/ticket/1".
            Create fresh branch? [yes/No] y
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
                raise SageDevValueError("Cannot abandon #{0}: no local branch for this ticket.", ticket)
                self._UI.error("Cannot delete the master branch.")
                    self._UI.error('Cannot delete "{0}": is the current branch.', branch)
                    self._UI.info(['', '(use "{0}" to switch to the master branch)'],
                                  self._format_command("vanilla"))
            self._UI.show('Moved your branch "{0}" to "{1}".', branch, new_branch)
            if helpful:
                self._UI.info(['',
                               'Use "{0}" to restart working on #{1} with a clean copy of the master branch.'],
                               self._format_command("checkout", ticket=ticket, base=MASTER_BRANCH), ticket)
        This method is not wrapped in the commandline dev scripts. It
        does nothing that cannot be done with ``checkout`` and
        ``merge``, it just steepens the learning curve by introducing
        yet another command. Unless a clear use case emerges, it
        should be removed.

            - :meth:`merge` -- merge into the current branch rather
              than creating a new one
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/doctest/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            sage: dev._sagedev.gather("gather_branch", "#1", "ticket/1", "u/doctest/ticket/1")
        self._UI.debug('Creating a new branch "{0}".'.format(branch))
                self._UI.debug('Merging {2} branch "{0}" into "{1}".'
                              .format(branch_name, branch, local_remote))
            self.git.clean_wrapper()
            self._UI.debug('Deleted branch "{0}".'.format(branch))
        Incorporate commits from other tickets/branches into the
        current branch.

        Optionally, you can add the merged ticket to the trac
        "Dependency:" field. Note that the merged commits become part
        of the current branch, regardless of whether they are noted on
        trac. Adding a dependency implies the following:

        - the other ticket must be positively reviewed and merged
          before this ticket may be merged into the official release
          of sage.  The commits included from a dependency don't need
          to be reviewed in this ticket, whereas commits reviewed in
          this ticket from a non-dependency may make reviewing the
          other ticket easier.

        - you can more easily merge in future changes to dependencies.
          So if you need a feature from another ticket it may be
          appropriate to create a dependency to that you may more
          easily benefit from others' work on that ticket.

        - if you depend on another ticket then you need to worry about
          the progress on that ticket.  If that ticket is still being
          actively developed then you may need to make further merges
          in the future if conflicts arise.

            - :meth:`show_dependencies` -- see the current
              dependencies.
            - :meth:`GitInterface.merge` -- git's merge command has
              more options and can merge multiple branches at once.
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            Created ticket #2 at https://trac.sagemath.org/2.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=2" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Cannot merge remote branch for #1 because no branch has been set on the trac
            ticket.
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/alice/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Merging the local branch "ticket/1" into the local branch "ticket/2".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            <BLANKLINE>
            Merging the remote branch "u/alice/ticket/1" into the local branch "ticket/2".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            Merging the local branch "ticket/1" into the local branch "ticket/2".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            Merging the local branch "ticket/1" into the local branch "ticket/2".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            Branch "ticket/1" does not exist on the remote system.
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/bob/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            The branch field of ticket #1 needs to be updated from its current value
            "u/alice/ticket/1" to "u/bob/ticket/1"
            Change the "Branch:" field? [Yes/no] y
            Merging the remote branch "u/bob/ticket/1" into the local branch "ticket/2".
            Automatic merge failed, there are conflicting commits.
            <BLANKLINE>
            <BLANKLINE>
            Please edit the affected files to resolve the conflicts. When you are finished,
            your resolution will be commited.
            Finished? [ok/Abort] abort
            sage: alice._UI.append("ok")
            Merging the remote branch "u/bob/ticket/1" into the local branch "ticket/2".
            Automatic merge failed, there are conflicting commits.
            <BLANKLINE>
            <BLANKLINE>
            Please edit the affected files to resolve the conflicts. When you are finished,
            your resolution will be commited.
            Finished? [ok/Abort] ok
            Created a commit from your conflict resolution.
            cannot merge a ticket into itself

        We also cannot merge if the working directory has uncommited changes::
            sage: alice._UI.append("cancel")
            sage: with open("alice2","w") as f: f.write("uncommited change")
            sage: alice.merge(1)
            The following files in your working directory contain uncommitted changes:
            <BLANKLINE>
                 alice2
            <BLANKLINE>
            Discard changes? [discard/Cancel/stash] cancel
            Cannot merge because working directory is not in a clean state.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your changes)
            self._UI.info(['', '(use "{0}" to commit your changes)'],
                          self._format_command('commit'))
            self._UI.error('Not on any branch.')
            self._UI.info(['', '(use "{0}" to checkout a branch)'],
                           self._format_command("checkout"))
                raise SageDevValueError('"pull" must not be "False" when merging dependencies.')
                raise SageDevValueError('"create_dependency" must not be set when merging dependencies.')
                self._UI.debug("Merging dependency #{0}.".format(dependency))
                    self._UI.error("Cannot merge remote branch for #{0} because no branch has"
                                   " been set on the trac ticket.", ticket)
        elif pull == False or (pull is None and not
                               self._is_remote_branch_name(ticket_or_branch, exists=True)):
                    raise SageDevValueError('"create_dependency" must not be "True" if'
                                            ' "ticket_or_branch" is a local branch which'
                                            ' is not associated to a ticket.')
                raise SageDevValueError('"create_dependency" must not be "True" if'
                                        ' "ticket_or_branch" is a local branch.')
                self._UI.error('Can not merge remote branch "{0}". It does not exist.',
                               remote_branch)
            self._UI.show('Merging the remote branch "{0}" into the local branch "{1}".',
                          remote_branch, current_branch)
            self._UI.show('Merging the local branch "{0}" into the local branch "{1}".',
                          branch, current_branch)
            self._UI.show('Automatic merge successful.')
            self._UI.info(['', '(use "{0}" to commit your merge)'],
                          self._format_command('commit'))
                self._UI.show('Automatic merge failed, there are conflicting commits.')
                excluded = ['Aborting',
                    "Automatic merge failed; fix conflicts and then commit the result."]
                lines = [line for line in lines if line not in excluded]
                self._UI.show([''] + lines + [''])
                self._UI.show('Please edit the affected files to resolve the conflicts.'
                              ' When you are finished, your resolution will be commited.')
                sel = self._UI.select("Finished?", ['ok', 'abort'], default=1)
                if sel == 'ok':
                    self._UI.show("Created a commit from your conflict resolution.")
                elif sel == 'abort':
                else:
                    assert False
                self.git.clean_wrapper()
                self._UI.debug("Not recording dependency on #{0} because #{1} already depends on #{0}.",
                               ticket, current_ticket)
                self._UI.show(['', "Added dependency on #{0} to #{1}."], ticket, current_ticket)
    def tickets(self, include_abandoned=False, cached=True):
            - :meth:`abandon_ticket` -- hide tickets from this method.
            - :meth:`remote_status` -- also show status compared to
              the trac server.
            - :meth:`current_ticket` -- get the current ticket.
            sage: dev.tickets()
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Created ticket #2 at https://trac.sagemath.org/2.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=2" to create a new local branch)
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            sage: dev.tickets()
            ticket_str = "#"+str(ticket) if ticket else ""
            ret.append(("{0:>7}: {1} {2}".format(ticket_str, branch, ticket_summary), extra))
            - :meth:`checkout` -- checkout another branch, ready to
              develop on it.
            - :meth:`pull` -- pull a branch from the server and merge
              it.
                self._UI.error('"{0}" does not exist locally or on the remote server.'.format(release))
            - :meth:`commit` -- record changes into the repository.
            - :meth:`tickets` -- list local tickets (you may
              want to commit your changes to a branch other than the
              current one).
            Created ticket #1 at https://trac.sagemath.org/1.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=1" to create a new local branch)
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/doctest/ticket/1" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            Created ticket #2 at https://trac.sagemath.org/2.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=2" to create a new local branch)
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/doctest/ticket/2" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            Created ticket #3 at https://trac.sagemath.org/3.
            <BLANKLINE>
            #  (use "sage --dev checkout --ticket=3" to create a new local branch)
            On ticket #3 with associated local branch "ticket/3".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            The branch "u/doctest/ticket/3" does not exist on the remote server.
            Create new remote branch? [Yes/no] y
            Merging the remote branch "u/doctest/ticket/1" into the local branch "ticket/3".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            <BLANKLINE>
            Merging the remote branch "u/doctest/ticket/2" into the local branch "ticket/3".
            Automatic merge successful.
            <BLANKLINE>
            #  (use "sage --dev commit" to commit your merge)
            <BLANKLINE>
            On ticket #1 with associated local branch "ticket/1".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            On ticket #2 with associated local branch "ticket/2".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Local commits that are not on the remote branch "u/doctest/ticket/2":
            <BLANKLINE>
                ...: added ticket2
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            On ticket #3 with associated local branch "ticket/3".
            <BLANKLINE>
            #  Use "sage --dev merge" to include another ticket/branch.
            #  Use "sage --dev commit" to save changes into a new commit.
            Local commits that are not on the remote branch "u/doctest/ticket/3":
            <BLANKLINE>
                ...: added ticket3
            <BLANKLINE>
            Push to remote branch? [Yes/no] y
            Uploading your dependencies for ticket #3: "" => "#1, #2"