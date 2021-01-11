---
description: A file pointer is a 64-bit offset value that specifies the next byte to be read or the location to receive the next byte written.
ms.assetid: 1e8bc657-affa-4a17-8435-c93de5075a1d
title: File Pointers
ms.topic: article
ms.date: 05/31/2018
---

# File Pointers

When a file is opened, Windows associates a *file pointer* with the default stream. This file pointer is a 64-bit offset value that specifies the next byte to be read or the location to receive the next byte written. Each time a file is opened, the system places the file pointer at the beginning of the file, which is offset zero. Each read and write operation advances the file pointer by the number of bytes being read and written. For example, if the file pointer is at the beginning of the file and a read operation of 5 bytes is requested, the file pointer will be located at offset 5 immediately after the read operation. As each byte is read or written, the system advances the file pointer. The file pointer can also be repositioned by calling the [**SetFilePointer**](/windows/desktop/api/FileAPI/nf-fileapi-setfilepointer) function.

When the file pointer reaches the end of a file and the application attempts to read from the file, no error occurs, but no bytes are read. Therefore, reading zero bytes without an error means the application has reached the end of the file. Writing zero bytes does nothing.

An application can truncate or extend a file by using the [**SetEndOfFile**](/windows/desktop/api/FileAPI/nf-fileapi-setendoffile) function. This function sets the end of file to the current position of the file pointer.

 

 



