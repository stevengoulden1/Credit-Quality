# Conventions:

## Introduction:

The following is just the tenative plan (2/1/24 at approx: 9:45 AM EST):

The general naming structure should be: {Type}_{SubTyp, optional}_{Specific_Name}_{Iteration/Edition, optional}_{Capitalized_Initials}.{Datatype}, ideally saved to whatever pertinent folders.

Ex. Data_Housing_California_I_SG.csv

Arguably, the first item, data, is superfluous. However, I'd rather every file be explicit inherently per their names so no/little confusion arises in the event of a mistake. 

Similarily, I'd think it'd be worthwhile to specify the subtype, out of anticipation that we might have multiple instances where the relevant {Specific_Name} is applicable to both - such as having both income and housing data on California.

Iteration number is somewhat broad, referring to entirely different datasets, potentially of different features, of the same type (and subtype) or even if a change was made to the original data. Ie, I'm inclined to be quite conservative with any changes and list multiple editions of the same dataframe, such as adding another 1k entries to a previously existing one, and call it a different name.

Capitalized Initials should be clear, and assumed that any questions could be asked to said person about the document.

And, datatype is datatype.

## Git Reminders:

As at least BW is new to Git, I'd figure below here would be worthwhile to right any relevant Git commands, tricks, etc. to ensure we're less likely to mess anything up. Please feel free to add and comment here!

Much of what I'll be quoting is presumably from experimentation or some online source. By default, the first place I'll be referencing to learn about a command is via: https://git-scm.com/docs , the actual documentation for git related commands.

To add comments to any of the commands, I'd recommend startng a new line, indenting, and starting the comment with a # (like in Python), to make the different code used in Terminal cleaerly distint from comments.

The commands are approximately alphabetically organizd.

### Jargon



### General

git add .
    #Adds everything
git add (specific_file.type)

git comit -m "Descriptive_Message_of_Whatever_is_being_Done"

git diff
    #Shows differencs between various componennts of the diectory.

git mv {target} {destination}
    #Like with rm, must be in the index/Git system to be valid. So, a recently created item would got be affected by this.
        #The typical 'mv' would though.

git pull origin main

git push

git reset
    #Removes any added file (but not yet pushed)
git reset (specifc_file.type)

git rm
    #Only pertinent to files that were pushed/cloned with git.
    #Remove a file from the working tree & index.
    #Add -r if trying to remove a folder.
        #Chain with the proceeding.
    #Add '--cached' to remove an item from the index ie from whatever git is tracking; the item will then still exist on your compute,
        #but currently stands to not interact with Git.

git status

### Branching

Highly recommending to check documentation such as https://git-scm.com/docs/git-branch and the like. Would like to flesh out this bit later.

git branch {name}
    #Creates a copy of all pre-existing files.
    #By default does not switch to it.
    
    # ?? Files created on a branch seemingly also are made to the main [and potentially other] branch(s)??
    
    
git switch {name}
git switch main

### Github.com

### Miscellanious

One can name multiple objects the same name, given that their datatypes are the same.
    Explicitly tested for: .txt, .py, .ipynb,.csv, and for folders.
    If one tries to make a second object of the same name then nothing will happen (not even an error message).
    
Via pressing up and down arrows, one can quickly display prevously used code.
    Note that if pressing up from code that was never ran and go back down, the original code will still be there.
    

