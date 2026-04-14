# Files and Folders in Python

- Files have a name and a path.
- The root folder is the lowest folder. It's C:\ on Windows and / on Linux and Mac.
- In a file path, the folders and filename are separated by backslashes on Windows and forward slashes on Linux and Mac.
- Use the os.path.join() function to combine folders with the correct slash.
- The current working directory is the folder that any relative paths are relative to.
- os.getcwd() will return the current working directory.
- os.chdir() will change the current working directory.
- Absolute paths begin with the root folder, relative paths do not. Relative paths begin with current folder.
- The . folder represents "this folder", the .. folder represents "the parent folder".
- os.path.abspath() returns an absolute path form of the path passed to it.
- os.path.isabs() returns True if the path passed to it is absolute.
- os.path.relpath() returns the relative path between two paths passed to it.
- os.makedirs() can make folders.
- os.path.getsize() returns a file's size
- os.listdir() returns a list of strings of filenames
- os.path.exists() returns True if the filename passed to it exists.
- os.path.isfile() and os.path.isdir() return True if they were passed a filename or file path.


## Reading and Writing Plaintext Files

- open() will return a file object which has reading and writing-related methods.
- Pass 'r' (or nothing) to open) to open the file in read mode, 'w' for write mode, 'a' for append mode.
- Opening a nonexistant filename in write or append mode will create that file.
- Call read () or write() to read the contents of a file or write a string to a file.
- Call readlines) to return a list of strings of the file's content.
- Call close() when you are done with the file.
- The shelve module can store Python values in a binary file.
- shelve.open() returns a dictionary-like shelf value.


## Copying and Moving Files

- import the shutil library to code for the copying and moving functions.
- shutil.copy(source, destination) to copy files from one location to another location.
- shutil.copytree(source, destination) to copy complete folder and files inside it.
- shutil.move(source, destination) to move the file from the source to destination.
- shutil.move() keep the source and destination same will rename the file.

## Deleting Files
- os. unlink() will delete a file
- os.rmdir() will delete a folder (but the folder must be empty)
- shutil.rmtree() will delete a folder and all its contents
- Deleting can be dangerous, so do a dry run first.
- send2trash.send2trash() will send a file or folder to the recycling bin

## Walking a File Directory

Let say there is a folder at some location in the laptop. And there are alot of different directories files and nested directories. Then you can walk through all of them by usin below program:
```pyhon
for folderName, subfolders, filenames in os.walk('c:\\delicious'):
print ('The folder is ' + folderName)
print ('The subfolders in ' + folderName + ' are: ' + str (subfolders))
print('The filenames in ' + folderName + ' are: ' + str (filenames))
print ()


Output:
The folder is c:\delicious
The subfolders in c:\delicious are: ['foo', 'walnut']
The filenames in c:\delicious are: ['spam.txt', 'spamspamspam.txt']
The folder is c: \delicious\foo
The subfolders in c:\delicious\foo are: []
The filenames in c:\delicious\foo are: ['spam.txt']
The folder is c:\delicious\walnut
The subfolders in c: \delicious\walnut are: ['waffles']
The filenames in c:\delicious\walnut are: ['eggs.txt']
The folder is c: \delicious\walnut\waffles
The subfolders in c:\delicious\walnut\waffles are: []
The filenames in c: \delicious\walnut|waffles are: ['bacon.txt', 'ham.txt']
```

  
