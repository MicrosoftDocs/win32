---
description: Functions to use to create, delete, and maintain files.
ms.assetid: b9cf0ddf-efda-4997-bcc3-3056026c1264
title: Creating, Deleting, and Maintaining Files
ms.topic: article
ms.date: 05/31/2018
---

# Creating, Deleting, and Maintaining Files

The following topics describe how to create, delete, and maintain files.

## In this section



| Topic                                                                   | Description                                                                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Naming Files, Paths, and Namespaces](naming-a-file.md)<br/>     | Rules, conventions, and limitations of names for files and directories, including naming conventions, short file names vs. long file names, fully qualified paths vs. relative paths, maximum path length limitation, 8.3 file names, and namespaces.<br/>            |
| [Creating and Opening Files](creating-and-opening-files.md)<br/> | Considerations for creating or opening a file by using the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function.<br/>                                                                                                                                                            |
| [Moving and Replacing Files](moving-and-replacing-files.md)<br/> | Considerations for moving and replacing files by using the CopyFileEx, CreateFile, Replacefile, and MoveFileEx functions.<br/>                                                                                                                                        |
| [Closing and Deleting Files](closing-and-deleting-files.md)<br/> | To use operating system resources efficiently, an application should close files when they are no longer needed by using the [**CloseHandle**](/windows/desktop/api/handleapi/nf-handleapi-closehandle) function. If a file is open when an application terminates, the system closes it automatically.<br/> |
| [Defragmenting Files](defragmenting-files.md)<br/>               | *Defragmentation* is the process of moving portions of files around on a disk to defragment files, that is, the process of moving file clusters on a disk to make them contiguous.<br/>                                                                               |



 

 

