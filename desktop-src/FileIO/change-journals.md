---
description: When any change is made to a file or directory in a volume, the USN change journal for that volume is updated with a description of the change and the name of the file or directory.
ms.assetid: 9a158c2b-da8e-4ca9-b3c1-2185cf41eb7d
title: Change Journals
ms.topic: article
ms.date: 05/31/2018
---

# Change Journals

An automatic backup application is one example of a program that must check for changes to the state of a volume to perform its task. The brute force method of checking for changes in directories or files is to scan the entire volume. However, this is often not an acceptable approach because of the decrease in system performance it would cause. Another method is for the application to register a directory notification (by calling the [**FindFirstChangeNotification**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstchangenotificationa) or [**ReadDirectoryChangesW**](/windows/desktop/api/WinBase/nf-winbase-readdirectorychangesw) functions) for the directories to be backed up. This is more efficient than the first method, however, it requires that an application be running at all times. Also, if a large number of directories and files must be backed up, the amount of processing and memory overhead for such an application might also cause the operating system's performance to decrease.

To avoid these disadvantages, the NTFS file system maintains an update sequence number (USN) change journal. When any change is made to a file or directory in a volume, the USN change journal for that volume is updated with a description of the change and the name of the file or directory.

Change journals are also needed to recover file system indexing for example after a computer or volume failure. The ability to recover indexing means the file system can avoid the time-consuming process of reindexing the entire volume in such cases.

The following topics discuss change journals.

## In this section



| Topic                                                                                                                             | Description                                                                                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Change Journal Records](change-journal-records.md)<br/>                                                                   | As files, directories, and other NTFS file system objects are added, deleted, and modified, the NTFS file system enters change journal records in streams, one for each volume on the computer.<br/>                                           |
| [Using the Change Journal Identifier](using-the-change-journal-identifier.md)<br/>                                         | The NTFS file system associates an unsigned 64-bit identifier with each change journal.<br/>                                                                                                                                                   |
| [Creating, Modifying, and Deleting a Change Journal](creating-modifying-and-deleting-a-change-journal.md)<br/>             | Administrators can create, delete, and re-create change journals.<br/>                                                                                                                                                                         |
| [Obtaining a Volume Handle for Change Journal Operations](obtaining-a-volume-handle-for-change-journal-operations.md)<br/> | To obtain a handle to a volume for use with update sequence number (USN) change journal operations, call the [**CreateFile**](/windows/desktop/api/FileAPI/nf-fileapi-createfilea) function with the *lpFileName* parameter set to a string of the following form: \\\\.\\*X*.<br/> |
| [Change Journal Operations](change-journal-operations.md)<br/>                                                             | Control codes and structures to use with the NTFS file system update sequence number (USN) change journal.<br/>                                                                                                                                |



 

 

 




