
# Changelog
All notable changes to this project will be documented in this file.
 
The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

# [1.3.3] - 22. 6. 2024
  
Fixed warning about header height. Update of arara compilation settings.
 
### Fixed
- Fixed "Package fancyhdr Warning: \headheight..." warning.

### Changed
- Changed arara settings to properly match the new default compiler.


## [1.3.2] - 18. 6. 2024
  
Improvements of captions in the example.
 
### Changed
- All captions are now at the bottom of the object (figure, listing, table, etc.).
- The trailing spaces have been removed from the caption


## [1.3.1] - 17. 6. 2024
  
Improvements of frontmatter, table of contents entries and sectioning.
 
### Changed
- Changed order of front matter entries (acknowledgements, dedications, etc.) to match standard sectioning.
- Excluding frontmatter entries from table of contents.

### Fixed
- Fixed missing empty page after titlepage.
- Fixed numbering/toc of subsubsection.


## [1.3.0] - 17. 6. 2024
  
Dropped older compilers that do not support computer-read PDFs (e.g., the text could not be copy-pasted). Now, only XeLaTeX and LuaLaTeX can be used.
 
### Changed
- Changed the if that processes the used compiler, so it supports only XeLaTex or LuaLaTeX. Otherwise, error is raised.



## [1.2.2] - 17. 6. 2024
  
Title page is now first, the assignment is second page.
 
### Changed
- Swapped Title page and assignment page.



## [1.2.1] - 17. 6. 2024
  
Sync of layout for oneside and twoside versions. 
 
### Changed
- The introduction chapter is numbered (as it should have been).

### Fixed
- Fixed the problem that oneside and twoside versions had different layouts because of different margings.



## [1.2.0] - 17. 6. 2024
  
Started versioning.

### Added
- Version number of the project.
- This changelog file.