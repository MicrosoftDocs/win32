---
description: An application can decompress a compressed file a portion at a time by using the LZSeek and LZRead functions.
ms.assetid: 9ceec1d4-37cd-4717-a731-dfb9cddb268c
title: Reading from Compressed Files
ms.topic: article
ms.date: 05/31/2018
---

# Reading from Compressed Files

In addition to decompressing a complete file in a single operation, an application can decompress a compressed file a portion at a time by using the [**LZSeek**](/windows/desktop/api/LzExpand/nf-lzexpand-lzseek) and [**LZRead**](/windows/desktop/api/LzExpand/nf-lzexpand-lzread) functions. These functions are particularly useful when it is necessary to extract parts of large files. For example, a font manufacturer may have compressed files containing font metrics in addition to character data. To use the information in these files, an application would need to decompress the file; however, most applications would use only part of the file at any particular time. To get information about font metrics, the application would extract data from the header. To get information from the text, the application would reposition the file pointer by calling **LZSeek** and extract character data by calling **LZRead**.

 

 



