---
Description: 'To use operating system resources efficiently, an application should close files when they are no longer needed by using the CloseHandle function. If a file is open when an application terminates, the system closes it automatically.'
ms.assetid: '6cf9694a-00c4-4750-8822-c25a1a102fd4'
title: Closing and Deleting Files
---

# Closing and Deleting Files

To use operating system resources efficiently, an application should close files when they are no longer needed by using the [**CloseHandle**](https://msdn.microsoft.com/library/windows/desktop/ms724211) function. If a file is open when an application terminates, the system closes it automatically.

The [**DeleteFile**](deletefile.md) function can be used to delete a file on close. A file cannot be deleted until all handles to it are closed. If a file cannot be deleted, its name cannot be reused. To reuse a file name immediately, rename the existing file.

If you are deleting an open file or directory on a remote machine and it has already been opened on the remote machine without the read share permission set, do not call [**CreateFile**](createfile.md) or [**OpenFile**](openfile.md) to open the file or directory for deletion first. Doing so will result in a sharing violation.

 

 



