---
Description: Functions to use to enumerate mounted folders on a volume.
ms.assetid: 052a363f-adfd-4f66-a8b0-5d9d37eedcb0
title: Enumerating Mounted Folders
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Enumerating Mounted Folders

The following functions are used to enumerate the mounted folders on a specified NTFS volume:

-   [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master)
-   [**FindNextVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findnextvolumemountpointa?branch=master)
-   [**FindVolumeMountPointClose**](/windows/win32/WinBase/nf-winbase-findvolumemountpointclose?branch=master)

These functions operate in a manner very similar to the [**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master), [**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master), and [**FindClose**](/windows/win32/FileAPI/nf-fileapi-findclose?branch=master) functions.

To enumerate mounted folders on a volume, first find out if the volume supports mounted folders. To do so, use the volume name returned by the [**FindFirstVolume**](/windows/win32/FileAPI/nf-fileapi-findfirstvolumew?branch=master) and [**FindNextVolume**](/windows/win32/FileAPI/nf-fileapi-findnextvolumew?branch=master) functions to call the [**GetVolumeInformation**](/windows/win32/FileAPI/nf-fileapi-getvolumeinformationa?branch=master) function. The names returned include a trailing backslash (\) to be compatible with the [**GetDriveType**](/windows/win32/FileAPI/nf-fileapi-getdrivetypea?branch=master) function and related functions. For more information on the functions used to scan the volumes on a computer, see [Enumerating Volumes](enumerating-volumes.md). When you call the **GetVolumeInformation** function, if "NTFS" is returned in the *lpFileSystemNameBuffer* parameter, the volume is an NTFS volume. The NTFS file system supports mounted folders.

If the volume is an NTFS volume, begin a search for the mounted folders by calling [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master). If the search is successful, process the results according to your application's requirements. Then use [**FindNextVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findnextvolumemountpointa?branch=master) in a loop to locate and process the mounted folders one at a time. When there are no more mounted folders to be enumerated, close the search handle by calling [**FindVolumeMountPointClose**](/windows/win32/WinBase/nf-winbase-findvolumemountpointclose?branch=master). Note that the search will find only the mounted folders that are on the specified volume.

You should not assume any correlation between the order of the mounted folders that are returned by these functions and the order of the mounted folders that are returned by other functions or tools.

 

 



