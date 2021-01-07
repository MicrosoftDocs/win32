---
description: An application can decompress multiple files by using the LZOpenFile, LZCopy, and LZClose functions.
ms.assetid: 582d57c7-70a4-4711-bae5-4abfb7a196b1
title: Decompressing Multiple Files
ms.topic: article
ms.date: 05/31/2018
---

# Decompressing Multiple Files

An application can decompress multiple files by performing the following tasks:

1.  Open the source files by calling the [**LZOpenFile**](/windows/desktop/api/LzExpand/nf-lzexpand-lzopenfilea) function.
2.  Open the destination files by calling [**LZOpenFile**](/windows/desktop/api/LzExpand/nf-lzexpand-lzopenfilea).
3.  Copy the source files to the destination files by calling the [**LZCopy**](/windows/desktop/api/LzExpand/nf-lzexpand-lzcopy) function.
4.  Close the files by calling the [**LZClose**](/windows/desktop/api/LzExpand/nf-lzexpand-lzclose) function.

 

 



