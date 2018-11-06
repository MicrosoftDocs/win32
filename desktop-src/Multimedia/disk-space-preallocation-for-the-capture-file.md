---
title: Disk Space Preallocation for the Capture File
description: Disk Space Preallocation for the Capture File
ms.assetid: 7a11b769-65b9-4eaa-bc42-5d1d744bf181
keywords:
- WM_CAP_FILE_ALLOCATE message
- capFileAlloc macro
ms.topic: article
ms.date: 05/31/2018
---

# Disk Space Preallocation for the Capture File

Preallocating disk space for the capture file builds a file of a specified size on the disk before the start of a capture operation. Preallocating a capture file reduces the processing required while capture is in progress and results in fewer dropped frames. You can preallocate a capture file by using the [**WM\_CAP\_FILE\_ALLOCATE**](wm-cap-file-allocate.md) message (or the [**capFileAlloc**](/windows/desktop/api/Vfw/nf-vfw-capfilealloc) macro).

Typically, your application should preallocate enough disk space to contain the largest capture file anticipated. Preallocating disk space does not restrict the size of the captured file. The file size is automatically enlarged if the captured data exceeds the allocated space. Subsequent write operations to the capture file reuse the portions of disk space allocated for the file, preserving the size and fragmentation of the file.

You can also improve capture performance by defragmenting the capture file. To defragment the file, use a defragmentation utility such as Disk Defragmenter. If you use a defragmented capture file and later enlarge it, you should defragment the enlarged file. Enlarging a defragmented capture file can fragment the expanded portion of the file and reduce performance in the capture operation.

You might also improve performance by using an uncompressed disk for video capture. Compressing data during capture can limit capture throughput to the disk.

An application can reserve a permanent capture file to eliminate the time required to preallocate and defragment a file each time it is started. Because a capture file can require considerable disk space, and preallocating a capture file removes all data from an existing capture file, an application should let the user decide if the file is permanent or temporary.

 

 




