---
Description: 'Get the allocated size or the total size for a file by using either the GetCompressedFileSize or the GetFileSize function.'
ms.assetid: '1894ea01-49ff-41e3-9912-1cd75966bd3f'
title: Obtaining the Size of a Sparse File
---

# Obtaining the Size of a Sparse File

Use the [**GetCompressedFileSize**](getcompressedfilesize.md) function to obtain the actual size allocated on disk for a sparse file. This total does not include the size of the regions which were deallocated because they were filled with zeros. Use the [**GetFileSize**](getfilesize.md) function to determine the total size of a file, including the size of the sparse regions that were deallocated.

 

 



