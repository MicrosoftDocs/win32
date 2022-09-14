---
description: An application reads from and writes to a file by using the ReadFile, ReadFileEx, WriteFile, and WriteFileEx functions.
ms.assetid: 14ecb06c-3f80-47b8-9964-6a2c3b572300
title: Reading From and Writing to Files
ms.topic: article
ms.date: 05/31/2018
---

# Reading From and Writing to Files

An application reads from and writes to a file by using the [**ReadFile**](/windows/desktop/api/FileAPI/nf-fileapi-readfile), [**ReadFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-readfileex), [**WriteFile**](/windows/desktop/api/FileAPI/nf-fileapi-writefile), and [**WriteFileEx**](/windows/desktop/api/FileAPI/nf-fileapi-writefileex) functions. These functions require a handle to a file to be opened for reading and writing, respectively. They read and write a specified number of bytes at the location indicated by the file pointer. The data is read and written exactly as specified; the functions do not format the data.

When the file pointer reaches the end of a file and the application attempts to read from the file, no error occurs, but no bytes are read. Therefore, reading zero bytes without an error means the application has reached the end of the file. Writing zero bytes does nothing.

For more information, see the following topics.

## In this section



| Topic                                                                                                                                           | Description                                                                                                                          |
|-------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|
| [Positioning a File Pointer](positioning-a-file-pointer.md)<br/>                                                                         | Windows uses a file pointer to keep track of bytes read or written.<br/>                                                       |
| [Reading From or Writing To Files Using a Scatter-Gather Scheme](reading-from-or-writing-to-files-using-a-scatter-gather-scheme.md)<br/> | Describes a scatter-gather scheme for reading or writing noncontiguous chunks of data in one operation.<br/>                   |
| [Flushing System-Buffered I/O Data to Disk](flushing-system-buffered-i-o-data-to-disk.md)<br/>                                           | Windows stores the data in file read and write operations in system-maintained data buffers to optimize disk performance.<br/> |
| [Truncating or Extending Files](truncating-or-extending-files.md)<br/>                                                                   | An application can truncate or extend a file by calling [**SetEndOfFile**](/windows/desktop/api/FileAPI/nf-fileapi-setendoffile).<br/>                             |



 

 

 




