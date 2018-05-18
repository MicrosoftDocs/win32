---
Description: 'Windows uses a file pointer to keep track of bytes read or written.'
ms.assetid: '21c75d96-0357-422d-b12b-74c56f64ecf1'
title: Positioning a File Pointer
---

# Positioning a File Pointer

When an application calls [**CreateFile**](createfile.md) to open a file for the first time, Windows places the [file pointer](file-pointers.md) at the beginning of the file. As bytes are read from or written to the file, Windows advances the file pointer the number of bytes read or written.

An application can position the file pointer to a specified offset by calling [**SetFilePointer**](setfilepointer.md).

The [**SetFilePointer**](setfilepointer.md) function can also be used to query the current file pointer position by specifying a move method of **FILE\_CURRENT** and a distance of zero.

 

 



