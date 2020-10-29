# pbfWalker
- DAUMPotPlayer produces the `.pbf` file for bookmarking videos
- This tool parses .pbf file then converts its body into a text file contains pairs of bookmark name, start time
- Once you marked the position where you would want to see quickly again, you can easily find that by using this tool
<img src="https://raw.githubusercontent.com/Sessho-maru/pbfWalker/master/test/01.example.gif" />

### Requirement
- All you need is python
- Turn on `Store bookmarks into .pbf files instead of Registry/INI(책갈피를 동영싱과 같은 폴더에 저장)` if you haven't (this option makes a .pbf file right under video file what .pbf marks for)
### How to use
Give this tool a folder direction where your desired video lives</br>
then this tool will parse every `.pbf` file and produce one text file</br></br>
This tool may be useful when you're wanting to reference lecture videos quickly by mapping the name of specific subject with timestamp when it is started</br>

### About this tool
Considering lecture videos has its order and usually specifies its order by numbering
So, this tool exptects all the names of video file and folder have already been numbered
