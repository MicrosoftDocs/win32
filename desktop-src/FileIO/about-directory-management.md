---
description: A directory that contains one or more directories is the parent of the contained directory or directories, and each contained directory is a child of the parent directory. The hierarchical structure of directories is referred to as a directory tree.
ms.assetid: e8a7bf82-0f3c-4ad9-9d10-25c4d69733dc
title: About Directory Management
ms.topic: article
ms.date: 05/31/2018
---

# About Directory Management

A directory that contains one or more directories is the *parent* of the contained directory or directories, and each contained directory is a *child* of the parent directory. The hierarchical structure of directories is referred to as a *directory tree*.

The NTFS file system implements the logical link between a directory and the files it contains as a *directory entry table*. When a file is moved into a directory, an entry is created in the table for the moved file and the name of the file is placed in the entry. When a file contained in a directory is deleted, the name and entry corresponding to the deleted file is also deleted from the table. More than one entry for a single file can exist in a directory entry table. If an additional entry is created in the table for a file, that entry is referred to as a *hard link* to that file. There is no limit to the number of hard links that can be created for a single file.

Directories can also contain junctions and reparse points.

## In this section



| Topic                                                                                 | Description                                                                                            |
|---------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|
| [Creating and Deleting Directories](creating-and-deleting-directories.md)<br/> | An application can programmatically create and delete directories.<br/>                          |
| [Directory Handles](obtaining-a-handle-to-a-directory.md)<br/>                 | Whenever a process creates or opens a directory object, it receives a handle to the object.<br/> |
| [Reparse Points](reparse-points.md)<br/>                                       | Describes reparse points.<br/>                                                                   |



 

## Related topics

<dl> <dt>

[Directory Management Reference](directory-management-reference.md)
</dt> </dl>

 

 




