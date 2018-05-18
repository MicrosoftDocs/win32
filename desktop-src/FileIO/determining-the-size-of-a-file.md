---
Description: 'The GetFileSize function retrieves the size of a file.'
ms.assetid: '4d3a3925-72e8-4350-b46d-e2c25791e862'
title: Determining the Size of a File
---

# Determining the Size of a File

The [**GetFileSize**](getfilesize.md) function retrieves the size of a file.

Because the NTFS file system implementation of files allows for multiple streams within a file, any application you write that accesses files must account for the possibility that the creator of the file can include multiple streams in the file. If multiple streams are not checked for in a file, the application can underestimate the total size of the file, among other errors.

 

 



