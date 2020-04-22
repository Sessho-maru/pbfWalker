# pbfWalker
- `.pbf` is a file extension DAUM PotPlayer produces as its video bookmarks
- This tool converts `.pbf` file into an organized text file
- You can easily search the part of video where you want to see by parsing `.pbf` files with this tool
<img src="https://raw.githubusercontent.com/Sessho-maru/pbfWalker/master/example.gif" />

### Requirement
- All you nees is python
- If you haven't, Just turn on `Store bookmarks into .pbf files instead of Registry/INI(책갈피를 동영싱과 같은 폴더에 저장)` option in Playback setting menu
### How to use
Give it a directory where your sources are, and then this tool parses all the `.pbf` files</br>
After, this tool will convert its every timestamp and markername into text file</br></br>
If you want to convert many `.pbf`s like a whole bookmark of some lectures</br>
I recommend make a __*folder*__ that contains each lecture's `.pbf` files, like</br>
```
 folder
    ├──lectrue 1
    │    ├──00.introduction
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ...
    │    ├──01.blah
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ...
    │    ├──02.blahblah
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │        ...
    │    ...
    ├──lectrue 2
    │    ├──00.introduction
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ...
    │    ├──01.blah
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ...
    │    ├──02.blahblah
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │    │   ├──... .pbf
    │        ...
    │    ...

```
then pass __*folder*__ directory to this tool

### About this tool
This tool sorts all the files and folders in the given directory using the first occurrence integer as a key from its name</br>
Because, normally contents of a lecture are sorted by numbering and every `.pbf` file is names after its video file</br>
so, if any contents you are going to convert hasn't been numbered, You should give a number, like</br>
```
01. ... .pbf
02. ... .pbf
03. ... .pbf
...
or
#1. ... .pbf
#2. ... .pbf
#3. ... .pbf
...
```
</br>
This tool traverses every subfolder in DFS manner