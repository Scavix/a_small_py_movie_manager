# a_small_py_movie_manager
A small management tool for local movies/videos with PySimpleGUI.

<p align="center">
  <img src="https://github.com/Scavix/a_small_py_movie_manager/blob/main/Capture.PNG" />
</p>

## Features
Add, Edit, Delete, and View movies in the archive.
Save and Load movie archives in various formats including .txt, .json, .xml, .csv, .db, .xlsx, .dat.
Scan a folder for movie files and add them to the archive.

## Usage
Run the a_movie_manager.py script.
Use the menu bar to access the various features of the application.

## Dependencies
- PySimpleGUI
- os
- json

## Limitations
The application currently does not support actual parsing of movie data from .xml, .db, .xlsx, .dat files. It only reads the file names.
The 'Scan from Folder' feature only adds the file names as movie titles to the archive.

## Future Improvements
- Implement actual parsing of movie data from .xml, .db, .xlsx, .dat files.
- Enhance the 'Scan from Folder' feature to extract movie data from the file names or file metadata.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
