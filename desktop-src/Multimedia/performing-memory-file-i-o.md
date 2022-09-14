---
title: Performing Memory File I/O
description: Performing Memory File I/O
ms.assetid: c0a5c8a0-978f-47d9-8ef0-ad391b9d1e63
keywords:
- multimedia file I/O,memory
- file I/O,memory
- input and output (I/O),memory
- I/O (input and output),memory
- memory I/O
- mmioOpen function
ms.topic: article
ms.date: 05/31/2018
---

# Performing Memory File I/O

The multimedia file I/O services let you treat a block of memory as a file. This can be useful if you already have a file image in memory. Memory files let you reduce the number of special-case conditions in your code because, for I/O purposes, you can treat memory files as if they were disk-based files. You can also use memory files with the clipboard.

As with I/O buffers, memory files can use memory allocated by the application or by the file I/O manager. In addition, memory files can be either expandable or nonexpandable. When the file I/O manager reaches the end of an expandable memory file, it expands the memory file by a predefined increment.

To open a memory file, use the [**mmioOpen**](/windows/win32/api/mmiscapi/nf-mmiscapi-mmioopen) function with the *szFilename* parameter set to **NULL** and the MMIO\_READWRITE flag set in the *dwOpenFlags* parameter. Set the *lpmmioinfo* parameter to point to an [**MMIOINFO**](/previous-versions//dd757322(v=vs.85)) structure that has been set up as follows:

1.  Set the **pIOProc** member to **NULL**.
2.  Set the **fccIOProc** member to FOURCC\_MEM.
3.  Set the **pchBuffer** member to point to the memory block. To request that the file I/O manager allocate the memory block, set **pchBuffer** to **NULL**.
4.  Set the **cchBuffer** member to the initial size of the memory block.
5.  Set the **adwInfo** member to the minimum expansion size of the memory block. For a nonexpandable memory file, set **adwInfo** to **NULL**.
6.  Set all other members to zero.

There are no restrictions on allocating memory for use as a nonexpandable memory file.

 

 