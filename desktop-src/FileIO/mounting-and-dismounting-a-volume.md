---
description: Creating a mounted folder is a two-step process.
ms.assetid: 02ecdf93-1133-48af-a6c9-52142256673f
title: Creating Mounted Folders
ms.topic: article
ms.date: 05/31/2018
---

# Creating Mounted Folders

Creating a mounted folder is a two-step process. First, call [**GetVolumeNameForVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw) with the mount point (drive letter, volume GUID path, or mounted folder) of the volume to be assigned to the mounted folder. Then use the [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) function to associate the returned volume GUID path with the desired directory on another volume. For example code, see [Creating a Mounted Folder](mounting-a-volume-at-a-mount-point.md).

Your application can designate any empty directory on a volume other than the root as a mounted folder. When you call the [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) function, that directory becomes the mounted folder. You can assign the same volume to multiple mounted folders.

After the mounted folder has been established, it is maintained through computer restarts automatically.

If a volume fails, any volumes that have been assigned to mounted folders on that volume can no longer be accessed through those mounted folders. For example, suppose you have two volumes, C: and D:, and that D: is associated with the mounted folder C:\\MountD\\. If volume C: fails, volume D: can no longer be accessed through the path C:\\MountD\\.

Only NTFS file system volumes can have mounted folders, but the target volumes for the mounted folders can be non-NTFS volumes.

Mounted folders are implemented by using reparse points and are subject to their restrictions. For more information, see [Reparse Points](reparse-points.md). It is not necessary to manipulate reparse points to use mounted folders; functions such as [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) handle all the reparse point details for you.

Because mounted folders are directories, you can rename, remove, move, and otherwise manipulate them, as you would other directories.

(Note: The TechNet documentation uses the term *mounted drives* to refer to *mounted folders*.)

 

 



