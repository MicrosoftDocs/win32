---
description: The goal of file system recognition is to allow the Windows operating system to have an additional option for a valid but unrecognized file system other than &\#0034;RAW&\#0034;.
ms.assetid: a5b1e97c-f22a-4d90-a3f4-1589ad9d1cc3
title: File System Recognition
ms.topic: article
ms.date: 05/31/2018
---

# File System Recognition

The goal of file system recognition is to allow the Windows operating system to have an additional option for a valid but unrecognized file system other than "RAW". To achieve this, beginning with Windows 7 and Windows Server 2008 R2, the system defines a fixed data structure type that can be written to the media on which an enabled technology that alters the file system format is active. This data structure, if present on logical disk sector zero, would then be recognized by the operating system and notify the user that the media contains a valid but unrecognized file system and is not a RAW volume if the drivers for the file system are not installed.

## File System Recognition Features and Use

Several recent storage technologies have altered the on-disk file system format such that the media on which these technologies are enabled become unrecognizable to earlier versions of Windows due to the file system drivers not existing when a particular earlier version of Windows was released. The previous default behavior in this scenario was as follows. When storage media is not a known file system, it is identified as RAW, and then propagated to the Windows Shell, where Autoplay prompts with the format user interface (UI). File system recognition can solve this if the authors of the new file system correctly write the proper [**data structure**](file-system-recognition-structure.md) to the disk.

File system recognition uses the following features and layers within the operating system to achieve its goals:

-   Storage media, where a fixed data structure resides as a sequence of bytes arranged internally in a predefined structure called the [**FILE\_SYSTEM\_RECOGNITION\_STRUCTURE**](file-system-recognition-structure.md) data structure. It is the responsibility of the file system developer to create this on-disk structure properly.
-   File system recognition at the application level, achieved via the use of the [**FSCTL\_QUERY\_FILE\_SYSTEM\_RECOGNITION**](/windows/win32/api/winioctl/ni-winioctl-fsctl_query_file_system_recognition) device I/O control code. For an example of how to use this control code, see [Obtaining File System Recognition Information](obtaining-file-system-recognition-information.md).
-   Checksum validation code, stored within the [**FILE\_SYSTEM\_RECOGNITION\_STRUCTURE**](file-system-recognition-structure.md) data structure. For an example of how to compute this checksum, see [Computing a File System Recognition Checksum](computing-a-file-system-recognition-checksum.md).
-   The Windows Shell UI uses the previously listed features to provide more flexible and robust Autoplay and related support for unrecognized file systems, but it can work only if the [**FILE\_SYSTEM\_RECOGNITION\_STRUCTURE**](file-system-recognition-structure.md) data structure exists in logical disk sector zero. Developers implementing new file systems should utilize this system to ensure that their file system is not mistakenly assumed to be of type "RAW".

## Related topics

<dl> <dt>

[Computing a File System Recognition Checksum](computing-a-file-system-recognition-checksum.md)
</dt> <dt>

[Obtaining File System Recognition Information](obtaining-file-system-recognition-information.md)
</dt> <dt>

[Obtaining Volume Information](obtaining-volume-information.md)
</dt> </dl>

 

 
