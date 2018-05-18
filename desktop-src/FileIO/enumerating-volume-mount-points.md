---
Description: 'Functions to use to enumerate mounted folders on a volume.'
ms.assetid: '052a363f-adfd-4f66-a8b0-5d9d37eedcb0'
title: Enumerating Mounted Folders
---

# Enumerating Mounted Folders

The following functions are used to enumerate the mounted folders on a specified NTFS volume:

-   [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md)
-   [**FindNextVolumeMountPoint**](findnextvolumemountpoint.md)
-   [**FindVolumeMountPointClose**](findvolumemountpointclose.md)

These functions operate in a manner very similar to the [**FindFirstFile**](findfirstfile.md), [**FindNextFile**](findnextfile.md), and [**FindClose**](findclose.md) functions.

To enumerate mounted folders on a volume, first find out if the volume supports mounted folders. To do so, use the volume name returned by the [**FindFirstVolume**](findfirstvolume.md) and [**FindNextVolume**](findnextvolume.md) functions to call the [**GetVolumeInformation**](getvolumeinformation.md) function. The names returned include a trailing backslash (\) to be compatible with the [**GetDriveType**](getdrivetype.md) function and related functions. For more information on the functions used to scan the volumes on a computer, see [Enumerating Volumes](enumerating-volumes.md). When you call the **GetVolumeInformation** function, if "NTFS" is returned in the *lpFileSystemNameBuffer* parameter, the volume is an NTFS volume. The NTFS file system supports mounted folders.

If the volume is an NTFS volume, begin a search for the mounted folders by calling [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md). If the search is successful, process the results according to your application's requirements. Then use [**FindNextVolumeMountPoint**](findnextvolumemountpoint.md) in a loop to locate and process the mounted folders one at a time. When there are no more mounted folders to be enumerated, close the search handle by calling [**FindVolumeMountPointClose**](findvolumemountpointclose.md). Note that the search will find only the mounted folders that are on the specified volume.

You should not assume any correlation between the order of the mounted folders that are returned by these functions and the order of the mounted folders that are returned by other functions or tools.

 

 



