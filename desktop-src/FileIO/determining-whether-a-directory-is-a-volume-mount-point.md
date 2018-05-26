---
Description: How to determine whether a specified directory is a mounted folder.
ms.assetid: b4a2c3d7-8805-41de-b316-592e77076570
title: Determining Whether a Directory Is a Mounted Folder
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Determining Whether a Directory Is a Mounted Folder

It is useful to determine whether a directory is a mounted folder when, for example, you are using a backup or search application that is limited to one volume. Such an application can reach information on multiple volumes if you use functions such as [**SetVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-setvolumemountpointa?branch=master) to create mounted folders for the other volumes on the volume that the application is limited to. For more information, see [Creating Mounted Folders](mounting-and-dismounting-a-volume.md).

To determine if a specified directory is a mounted folder, first call the [**GetFileAttributes**](/windows/win32/FileAPI/nf-fileapi-getfileattributesa?branch=master) function and inspect the **FILE\_ATTRIBUTE\_REPARSE\_POINT** flag in the return value to see if the directory has an associated reparse point. If it does, use the [**FindFirstFile**](/windows/win32/FileAPI/nf-fileapi-findfirstfilea?branch=master) and [**FindNextFile**](/windows/win32/FileAPI/nf-fileapi-findnextfilea?branch=master) functions to obtain the reparse tag in the **dwReserved0** member of the [**WIN32\_FIND\_DATA**](/windows/win32/MinWinBase/ns-minwinbase-_win32_find_dataa?branch=master) structure. To determine if the reparse point is a mounted folder (and not some other form of reparse point), test whether the tag value equals the value **IO\_REPARSE\_TAG\_MOUNT\_POINT**. For more information, see [Reparse Points](reparse-points.md).

To obtain the target volume of a mounted folder, use the [**GetVolumeNameForVolumeMountPoint**](/windows/win32/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw?branch=master) function.

In a similar manner, you can determine if a reparse point is a symbolic link by testing whether the tag value is **IO\_REPARSE\_TAG\_SYMLINK**.

## Related topics

<dl> <dt>

[**File Attribute Constants**](file-attribute-constants.md)
</dt> </dl>

 

 



