---
description: Depending upon the application, localization may require modifying or adding resources such as files or registry keys.
ms.assetid: f5af0ecd-cb57-4858-88b4-4608893004f6
title: Adding Localized Resources
ms.topic: article
ms.date: 05/31/2018
---

# Adding Localized Resources

Depending upon the application, localization may require modifying or adding resources such as files or registry keys. The localization of the sample application MNP2000 requires adding one additional file to the package, Fre.txt, and the French versions of two existing files: Help.txt and Readme.txt.

The best practice in this case is to localize the package such that the English and French versions can safely coexist on the computer. This includes never installing two different files with identical file names into the same directory. Because Help.txt and Readme.txt have identical file names in the two language versions, the French package should install these files into a different directory than the English.

The French package installs Help.txt into a new subdirectory of the RedPark folder, French. Because the addition of Fre.txt adds a resource to the original Help component, the component code for the Help component must be different in the French and English packages. See the rules for component codes in [Changing the Component Code](changing-the-component-code.md).

The French package installs Readme.txt into the directory French so that this file name cannot conflict with the English version. The file Readme.txt is installed with the Notepad component, but the component rules do not require changing the component code. In this example, the component code of Notepad should not be change because RedPark.exe, the registry values specified in the [Registry table](registry-table.md), are shared by both language versions. See [Adding Registry Information](adding-registry-information.md).

Remove the English versions of Help.txt and Readme.txt from the source files and add the new French versions of Help.txt, Readme.txt, and Fre.txt. The localized package should map the installation of files from source to target as follows.



| File        | Description                  | Path to source                   | Path to target                                         |
|-------------|------------------------------|----------------------------------|--------------------------------------------------------|
| Redpark.exe | Text editor executable file. | C:\\Sample\\Notepad\\Redpark.exe | \[ProgramFilesFolder\]\\Red\_Park\\French\\Redpark.exe |
| Readme.txt  | An informational file.       | C:\\Sample\\Notepad\\Readme.txt  | \[ProgramFilesFolder\]\\Red\_Park\\French\\Readme.txt  |
| Help.txt    | Help manual                  | C:\\Sample\\Notepad\\Help.txt    | \[ProgramFilesFolder\]\\Red\_Park\\French\\Help.txt    |
| Fre.txt     | Phone list                   | C:\\Sample\\Notepad\\Fre.txt     | \[ProgramFilesFolder\]\\Red\_Park\\French\\Fre.txt     |



 

Use the database editor Orca that is provided with the SDK, or another editor, to open the Directory table and add a record for the installation of the new directory, French.

[Directory Table](directory-table.md)



| Directory                                        | Directory\_Parent                                | DefaultDir        |
|--------------------------------------------------|--------------------------------------------------|-------------------|
| [**TARGETDIR**](targetdir.md)                   |                                                  | SourceDir         |
| [**ProgramFilesFolder**](programfilesfolder.md) | [**TARGETDIR**](targetdir.md)                   | .                 |
| ARTSDIR                                          | NOTEPADDIR                                       | Arts:Events       |
| HOLDIR                                           | MONDIR                                           | .:Holidays        |
| MENUDIR                                          | NOTEPADDIR                                       | Menu              |
| MONDIR                                           | NOTEPADDIR                                       | Gate              |
| NOTEPADDIR                                       | [**ProgramFilesFolder**](programfilesfolder.md) | Red\_Park:Notepad |
| SPORTDIR                                         | NOTEPADDIR                                       | Sports:Events     |
| FRENCHDIR                                        | NOTEPADDIR                                       | French:.          |



 

Use your table editor to change the ComponentId of the Help component in MNPFren.msi to a new GUID.

[Component Table](component-table.md)



| Component | ComponentId                            | Directory\_ | Attributes | Condition | Keypath      |
|-----------|----------------------------------------|-------------|------------|-----------|--------------|
| Baseball  | {F54ABAC0-33F2-11D3-91D7-00C04FD70856} | SPORTDIR    | 2          |           | Baseball.txt |
| Concert   | {76FA7A80-33F6-11D3-91D8-00C04FD70856} | ARTSDIR     | 2          |           | Concert.txt  |
| Dance     | {CCF834A1-33F8-11D3-91D8-00C04FD70856} | ARTSDIR     | 2          |           | Dance.txt    |
| Football  | {CCF834A0-33F8-11D3-91D8-00C04FD70856} | SPORTDIR    | 2          |           | Football.txt |
| Help      | {9ED21229-FE3C-4FE9-B01D-57E00224FD0B} | NOTEPADDIR  | 2          |           | Help.txt     |
| January   | {CF0BC690-33C9-11D3-91D6-00C04FD70856} | MONDIR      | 2          |           | January.txt  |
| NewYears  | {A42D9140-33D8-11D3-91D6-00C04FD70856} | HOLDIR      | 2          |           | NewYears.txt |
| Notepad   | {19BED232-30AB-11D3-91D3-00C04FD70856} | FRENCHDIR   | 2          |           | Redpark.exe  |



 

Use your table editor to add Fre.txt to the [File table](file-table.md) of MNPFren.msi. Enter the LANGID for French into the Language field for the localized files. All other things being equal, if the file being installed has a different language than the file on the machine, the installer favors the file with the language that matches the product being installed. Language neutral files are treated as just another language so the product being installed is favored again. For more information, see [File Versioning Rules](file-versioning-rules.md).

[File Table](file-table.md)



| File         | Component\_ | FileName     | FileSize | Version | Language | Attributes | Sequence |
|--------------|-------------|--------------|----------|---------|----------|------------|----------|
| Baseball.txt | Baseball    | Baseball.txt | 1000     |         |          | 0          | 1        |
| Concert.txt  | Concert     | Concert.txt  | 1000     |         |          | 0          | 1        |
| Dance.txt    | Dance       | Dance.txt    | 1000     |         |          | 0          | 1        |
| Football.txt | Football    | Football.txt | 1000     |         |          | 0          | 1        |
| Help.txt     | Help        | Help.txt     | 1000     |         | 1036     | 0          | 1        |
| January.txt  | January     | January.txt  | 1000     |         |          | 0          | 1        |
| NewYears.txt | NewYears    | NewYears.txt | 1000     |         |          | 0          | 1        |
| Redpark.exe  | Notepad     | Redpark.exe  | 45328    |         |          | 0          | 1        |
| Readme.txt   | Notepad     | Readme.txt   | 1000     |         | 1036     | 0          | 1        |
| Fre.txt      | Help        | Fre.txt      | 1000     |         | 1036     | 0          | 1        |



 

This completes the sample localization.

 

 



