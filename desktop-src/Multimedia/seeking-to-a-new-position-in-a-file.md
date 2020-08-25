---
title: Seeking to a New Position in a File
description: Seeking to a New Position in a File
ms.assetid: 276c3e43-bf9f-4a0a-b33a-7eaa701e92a6
keywords:
- multimedia file I/O,moving to beginning of files
- file I/O,moving to beginning of files
- input and output (I/O),moving to beginning of files
- I/O (input and output),moving to beginning of files
- moving to beginning of I/O files
- multimedia file I/O,seeking new position in files
- file I/O,seeking new position in files
- input and output (I/O),seeking new position in files
- I/O (input and output),seeking new position in files
- seeking new position in I/O files
ms.topic: article
ms.date: 05/31/2018
---

# Seeking to a New Position in a File

The following example moves to the beginning of an open file using the [**mmioSeek**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioseek) function.


```C++
mmioSeek(hFile, 0L, SEEK_SET); 
```



The following example moves to the end of an open file.


```C++
mmioSeek(hFile, 0L, SEEK_END); 
```



The following example moves to a position 10 bytes from the end of an open file.


```C++
mmioSeek(hFile, -10L, SEEK_END); 

```



 

 