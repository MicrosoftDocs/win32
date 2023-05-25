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
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# Seeking to a New Position in a File

\[The feature associated with this page, [Multimedia File I/O](/windows/win32/multimedia/multimedia-file-i-o), is a legacy feature. It has been superseded by [Source Reader](/windows/win32/medfound/source-reader). **Source Reader** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Source Reader** instead of **Multimedia File I/O**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

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



 

 