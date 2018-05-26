---
Description: Get the allocated size or the total size for a file by using either the GetCompressedFileSize or the GetFileSize function.
ms.assetid: 1894ea01-49ff-41e3-9912-1cd75966bd3f
title: Obtaining the Size of a Sparse File
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Obtaining the Size of a Sparse File

Use the [**GetCompressedFileSize**](/windows/win32/fileapi/nf-fileapi-getcompressedfilesizea?branch=master) function to obtain the actual size allocated on disk for a sparse file. This total does not include the size of the regions which were deallocated because they were filled with zeros. Use the [**GetFileSize**](/windows/win32/FileAPI/nf-fileapi-getfilesize?branch=master) function to determine the total size of a file, including the size of the sparse regions that were deallocated.

 

 



