---
Description: An application can decompress multiple files by using the LZOpenFile, LZCopy, and LZClose functions.
ms.assetid: 582d57c7-70a4-4711-bae5-4abfb7a196b1
title: Decompressing Multiple Files
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Decompressing Multiple Files

An application can decompress multiple files by performing the following tasks:

1.  Open the source files by calling the [**LZOpenFile**](/windows/win32/LzExpand/nf-lzexpand-lzopenfilea?branch=master) function.
2.  Open the destination files by calling [**LZOpenFile**](/windows/win32/LzExpand/nf-lzexpand-lzopenfilea?branch=master).
3.  Copy the source files to the destination files by calling the [**LZCopy**](/windows/win32/LzExpand/nf-lzexpand-lzcopy?branch=master) function.
4.  Close the files by calling the [**LZClose**](/windows/win32/LzExpand/nf-lzexpand-lzclose?branch=master) function.

 

 



