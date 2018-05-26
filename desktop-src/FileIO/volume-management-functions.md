---
Description: Functions used in volume management.
ms.assetid: dc985126-970c-49f2-877f-3759125e43b6
title: Volume Management Functions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Volume Management Functions

Functions used in volume management.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DefineDosDevice**](/windows/win32/FileAPI/nf-fileapi-definedosdevicew?branch=master)<br/>                                   | Defines, redefines, or deletes MS-DOS device names.<br/>                                                                                                                |
| [**DeleteVolumeMountPoint**](/windows/win32/FileAPI/nf-fileapi-deletevolumemountpointw?branch=master)<br/>                     | Deletes a drive letter or mounted folder.<br/>                                                                                                                          |
| [**FindFirstVolume**](/windows/win32/FileAPI/nf-fileapi-findfirstvolumew?branch=master)<br/>                                   | Retrieves the name of a volume on a computer. <br/>                                                                                                                     |
| [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master)<br/>               | Retrieves the name of a mounted folder on the specified volume. <br/>                                                                                                   |
| [**FindNextVolume**](/windows/win32/FileAPI/nf-fileapi-findnextvolumew?branch=master)<br/>                                     | Continues a volume search started by a call to the [**FindFirstVolume**](/windows/win32/FileAPI/nf-fileapi-findfirstvolumew?branch=master) function. <br/>                                                           |
| [**FindNextVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findnextvolumemountpointa?branch=master)<br/>                 | Continues a mounted folder search started by a call to the [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master) function. <br/>                               |
| [**FindVolumeClose**](/windows/win32/FileAPI/nf-fileapi-findvolumeclose?branch=master)<br/>                                   | Closes the specified volume search handle.<br/>                                                                                                                         |
| [**FindVolumeMountPointClose**](/windows/win32/WinBase/nf-winbase-findvolumemountpointclose?branch=master)<br/>               | Closes the specified mounted folder search handle.<br/>                                                                                                                 |
| [**GetDriveType**](/windows/win32/FileAPI/nf-fileapi-getdrivetypea?branch=master)<br/>                                         | Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.<br/>                                                                         |
| [**GetLogicalDrives**](/windows/win32/FileAPI/nf-fileapi-getlogicaldrives?branch=master)<br/>                                 | Retrieves a bitmask representing the currently available disk drives.<br/>                                                                                              |
| [**GetLogicalDriveStrings**](/windows/win32/FileAPI/nf-fileapi-getlogicaldrivestringsw?branch=master)<br/>                     | Fills a buffer with strings that specify valid drives in the system.<br/>                                                                                               |
| [**GetVolumeInformation**](/windows/win32/FileAPI/nf-fileapi-getvolumeinformationa?branch=master)<br/>                         | Retrieves information about the file system and volume associated with the specified root directory.<br/>                                                               |
| [**GetVolumeInformationByHandleW**](/windows/win32/FileAPI/nf-fileapi-getvolumeinformationbyhandlew?branch=master)<br/>       | Retrieves information about the file system and volume associated with the specified file.<br/>                                                                         |
| [**GetVolumeNameForVolumeMountPoint**](/windows/win32/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw?branch=master)<br/> | Retrieves a volume **GUID** path for the volume that is associated with the specified volume mount point ( drive letter, volume **GUID** path, or mounted folder).<br/> |
| [**GetVolumePathName**](/windows/win32/FileAPI/nf-fileapi-getvolumepathnamew?branch=master)<br/>                               | Retrieves the volume mount point where the specified path is mounted.<br/>                                                                                              |
| [**GetVolumePathNamesForVolumeName**](/windows/win32/FileAPI/nf-fileapi-getvolumepathnamesforvolumenamew?branch=master)<br/>   | Retrieves a list of drive letters and mounted folder paths for the specified volume.<br/>                                                                               |
| [**QueryDosDevice**](/windows/win32/FileAPI/nf-fileapi-querydosdevicew?branch=master)<br/>                                     | Retrieves information about MS-DOS device names.<br/>                                                                                                                   |
| [**SetVolumeLabel**](/windows/win32/WinBase/nf-winbase-setvolumelabela?branch=master)<br/>                                     | Sets the label of a file system volume.<br/>                                                                                                                            |
| [**SetVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-setvolumemountpointa?branch=master)<br/>                           | Associates a volume with a drive letter or a directory on another volume.<br/>                                                                                          |



 

The following functions are used with volume mount points (drive letters, volume GUID paths, and mounted folders).

-   [**DeleteVolumeMountPoint**](/windows/win32/FileAPI/nf-fileapi-deletevolumemountpointw?branch=master)
-   [**FindFirstVolume**](/windows/win32/FileAPI/nf-fileapi-findfirstvolumew?branch=master)
-   [**FindFirstVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findfirstvolumemountpointa?branch=master)
-   [**FindNextVolume**](/windows/win32/FileAPI/nf-fileapi-findnextvolumew?branch=master)
-   [**FindNextVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-findnextvolumemountpointa?branch=master)
-   [**FindVolumeClose**](/windows/win32/FileAPI/nf-fileapi-findvolumeclose?branch=master)
-   [**FindVolumeMountPointClose**](/windows/win32/WinBase/nf-winbase-findvolumemountpointclose?branch=master)
-   [**GetVolumeNameForVolumeMountPoint**](/windows/win32/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw?branch=master)
-   [**GetVolumePathName**](/windows/win32/FileAPI/nf-fileapi-getvolumepathnamew?branch=master)
-   [**GetVolumePathNamesForVolumeName**](/windows/win32/FileAPI/nf-fileapi-getvolumepathnamesforvolumenamew?branch=master)
-   [**SetVolumeMountPoint**](/windows/win32/WinBase/nf-winbase-setvolumemountpointa?branch=master)

 

 




