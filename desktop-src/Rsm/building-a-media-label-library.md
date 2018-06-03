---
Description: A media label library (MLL) is a DLL that can identify tapes written using a particular tape format.
ms.assetid: 1fe5f581-1278-465c-8265-53ec1b670b2c
title: Building a Media Label Library
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Building a Media Label Library

\[[Removable Storage Manager](removable-storage-manager.md) is no longer available as of Windows 7 and Windows Server 2008 R2.\]

A media label library (MLL) is a DLL that can identify tapes written using a particular tape format. If your application uses a standard tape format (MTF, QIC 113 or HP OmniBack II), then you do not need to develop your own MLL. If you use a different tape format then you will have to develop your own MLL, which you must install as part of your application installation.

MLLs are currently used only with tape media. Disk media, or file system capable media, are identified in a different manner. The system call [**GetVolumeInformation**](https://msdn.microsoft.com/library/windows/desktop/aa364993) is used to determine the file system type, volume serial number and volume name of disk sides. This information is used as the OMID.

For more information about building a media label library, see [Developing a Media Label Library](developing-a-media-label-library.md).

 

 



