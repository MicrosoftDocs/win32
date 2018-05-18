---
title: Reading from a File
description: Reading from a File
ms.assetid: '7c728304-7d05-4e28-a9bd-83b5b1af39be'
keywords: ["AVIFileInfo function"]
---

# Reading from a File

You can retrieve information about an open file by using the [**AVIFileInfo**](avifileinfo.md) function. This function fills the [**AVIFILEINFO**](avifileinfo-struct.md) structure with such information as the maximum data rate, the number of streams in the file, whether the file uses an index, and whether the file is copyrighted.

To retrieve supplementary information in an AVI file, use the [**AVIFileReadData**](avifilereaddata.md) function. Supplementary information is applicable to the entire file and is not included in the normal file headers. For example, the name of the company or person who holds the copyrights of a file could be supplementary information. Supplementary information does not adhere to a specific format; it can be file specific. **AVIFileReadData** returns the supplementary information in an application-supplied buffer.

 

 




