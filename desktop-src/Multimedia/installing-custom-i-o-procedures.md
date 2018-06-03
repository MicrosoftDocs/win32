---
title: Installing Custom I/O Procedures
description: Installing Custom I/O Procedures
ms.assetid: 7b26a062-fa52-4de3-b8c8-b9f9167068fc
keywords:
- multimedia file I/O,custom procedures
- file I/O,custom procedures
- input and output (I/O),custom procedures
- I/O (input and output),custom procedures
- installing custom I/O procedures
- custom I/O
- mmioInstallIOProc function
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Installing Custom I/O Procedures

To install an I/O procedure associated with the .ARC filename extension, use the [**mmioInstallIOProc**](https://www.bing.com/search?q=**mmioInstallIOProc**) function as follows:


```C++
mmioInstallIOProc (mmioFOURCC('A', 'R', 'C', ' '), 
    (LPMMIOPROC)lpmmioproc, MMIO_INSTALLPROC); 
```



When you install an I/O procedure using [**mmioInstallIOProc**](https://www.bing.com/search?q=**mmioInstallIOProc**), the procedure remains installed until you remove it. The I/O procedure is used for any file you open as long as the file has the appropriate filename extension.

You can also temporarily install an I/O procedure by using the [**mmioOpen**](https://www.bing.com/search?q=**mmioOpen**) function. In this case, the I/O procedure is used only with a file opened by using **mmioOpen** and is removed when the file is closed by using the [**mmioClose**](https://www.bing.com/search?q=**mmioClose**) function. To specify an I/O procedure when you open a file by using **mmioOpen**, use the *lpmmioinfo* parameter to reference an [**MMIOINFO**](https://www.bing.com/search?q=**MMIOINFO**) structure as follows:

1.  Set the **fccIOProc** member to **NULL**.
2.  Set the **pIOProc** member to the procedure-instance address of the I/O procedure.
3.  Set all other members to zero (unless you are opening a memory file, or directly reading or writing to the file I/O buffer).

Be sure to remove any I/O procedures you have installed before you exit your application.

 

 




