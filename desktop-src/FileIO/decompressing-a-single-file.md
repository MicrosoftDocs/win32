---
Description: An application can decompress a single compressed file by using the LZOpenFile, LZCopy, and LZClose functions.
ms.assetid: e43df292-ed56-4023-92e8-de261e3b58a1
title: Decompressing a Single File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Decompressing a Single File

An application can decompress a single compressed file by performing the following tasks:

1.  Open the source file by calling the [**LZOpenFile**](/windows/win32/LzExpand/nf-lzexpand-lzopenfilea?branch=master) function.
2.  Open the destination file by calling [**LZOpenFile**](/windows/win32/LzExpand/nf-lzexpand-lzopenfilea?branch=master).
3.  Copy the source file to the destination file by calling the [**LZCopy**](/windows/win32/LzExpand/nf-lzexpand-lzcopy?branch=master) function and passing the handles returned by [**LZOpenFile**](/windows/win32/LzExpand/nf-lzexpand-lzopenfilea?branch=master).
4.  Close the files by calling the [**LZClose**](/windows/win32/LzExpand/nf-lzexpand-lzclose?branch=master) function.

 

 



