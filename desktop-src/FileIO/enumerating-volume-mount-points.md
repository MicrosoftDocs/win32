---
description: Functions to use to enumerate mounted folders on a volume.
ms.assetid: 052a363f-adfd-4f66-a8b0-5d9d37eedcb0
title: Enumerating Mounted Folders
ms.topic: article
ms.date: 05/31/2018
---

# Enumerating Mounted Folders

The following functions are used to enumerate the mounted folders on a specified NTFS volume:

-   [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa)
-   [**FindNextVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findnextvolumemountpointa)
-   [**FindVolumeMountPointClose**](/windows/desktop/api/WinBase/nf-winbase-findvolumemountpointclose)

These functions operate in a manner very similar to the [**FindFirstFile**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstfilea), [**FindNextFile**](/windows/desktop/api/FileAPI/nf-fileapi-findnextfilea), and [**FindClose**](/windows/desktop/api/FileAPI/nf-fileapi-findclose) functions.

To enumerate mounted folders on a volume, first find out if the volume supports mounted folders. To do so, use the volume name returned by the [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew) and [**FindNextVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findnextvolumew) functions to call the [**GetVolumeInformation**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa) function. The names returned include a trailing backslash (\\) to be compatible with the [**GetDriveType**](/windows/desktop/api/FileAPI/nf-fileapi-getdrivetypea) function and related functions. For more information on the functions used to scan the volumes on a computer, see [Enumerating Volumes](enumerating-volumes.md). When you call the **GetVolumeInformation** function, if "NTFS" is returned in the *lpFileSystemNameBuffer* parameter, the volume is an NTFS volume. The NTFS file system supports mounted folders.

If the volume is an NTFS volume, begin a search for the mounted folders by calling [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa). If the search is successful, process the results according to your application's requirements. Then use [**FindNextVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findnextvolumemountpointa) in a loop to locate and process the mounted folders one at a time. When there are no more mounted folders to be enumerated, close the search handle by calling [**FindVolumeMountPointClose**](/windows/desktop/api/WinBase/nf-winbase-findvolumemountpointclose). Note that the search will find only the mounted folders that are on the specified volume.

You should not assume any correlation between the order of the mounted folders that are returned by these functions and the order of the mounted folders that are returned by other functions or tools.

 

 



