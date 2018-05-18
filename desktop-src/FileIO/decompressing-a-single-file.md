---
Description: 'An application can decompress a single compressed file by using the LZOpenFile, LZCopy, and LZClose functions.'
ms.assetid: 'e43df292-ed56-4023-92e8-de261e3b58a1'
title: Decompressing a Single File
---

# Decompressing a Single File

An application can decompress a single compressed file by performing the following tasks:

1.  Open the source file by calling the [**LZOpenFile**](lzopenfile.md) function.
2.  Open the destination file by calling [**LZOpenFile**](lzopenfile.md).
3.  Copy the source file to the destination file by calling the [**LZCopy**](lzcopy.md) function and passing the handles returned by [**LZOpenFile**](lzopenfile.md).
4.  Close the files by calling the [**LZClose**](lzclose.md) function.

 

 



