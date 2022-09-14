---
description: An application can decompress a single compressed file by using the LZOpenFile, LZCopy, and LZClose functions.
ms.assetid: e43df292-ed56-4023-92e8-de261e3b58a1
title: Decompressing a Single File
ms.topic: article
ms.date: 05/31/2018
---

# Decompressing a Single File

An application can decompress a single compressed file by performing the following tasks:

1.  Open the source file by calling the [**LZOpenFile**](/windows/desktop/api/LzExpand/nf-lzexpand-lzopenfilea) function.
2.  Open the destination file by calling [**LZOpenFile**](/windows/desktop/api/LzExpand/nf-lzexpand-lzopenfilea).
3.  Copy the source file to the destination file by calling the [**LZCopy**](/windows/desktop/api/LzExpand/nf-lzexpand-lzcopy) function and passing the handles returned by [**LZOpenFile**](/windows/desktop/api/LzExpand/nf-lzexpand-lzopenfilea).
4.  Close the files by calling the [**LZClose**](/windows/desktop/api/LzExpand/nf-lzexpand-lzclose) function.

 

 



