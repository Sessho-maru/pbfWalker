# pbfWalker
- DAUMPotPlayer produces the `.pbf` file to bookmarking videos
- This tool parses `.pbf` file then converts its body into a text file contains pairs of bookmark name, starting time value
- Once you have marked the position where you would want to watch again quickly, you can easily find that by using this tool
<img src="https://raw.githubusercontent.com/Sessho-maru/pbfWalker/master/test/01.example.gif" />

### Requirement
- All you need is python
- Turn on `Store bookmarks into .pbf files instead of Registry/INI(책갈피를 동영상과 같은 폴더에 저장)`</br>(this option makes a `.pbf` file be populated in same folder where target video lives)
### How to use
Give this tool a folder directory where your desired videos live</br>
then this tool will parse every `.pbf` file and produce one text file</br></br>
This tool may be useful when you're wanting to reference lecture videos quickly by mapping <br/>the name of specific subject with timestamp when it starts</br>

### About this tool
Considering lecture videos has its order and usually specifies that by numbering</br>
this tool exptects all the names of video file and folder have already been numbered
