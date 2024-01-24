---
description: Functions used in volume management.
ms.assetid: dc985126-970c-49f2-877f-3759125e43b6
title: Volume Management Functions
ms.topic: article
ms.date: 05/31/2018
---

# Volume Management Functions

Functions used in volume management.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DefineDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-definedosdevicew)<br/>                                   | Defines, redefines, or deletes MS-DOS device names.<br/>                                                                                                                |
| [**DeleteVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-deletevolumemountpointw)<br/>                     | Deletes a drive letter or mounted folder.<br/>                                                                                                                          |
| [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew)<br/>                                   | Retrieves the name of a volume on a computer. <br/>                                                                                                                     |
| [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa)<br/>               | Retrieves the name of a mounted folder on the specified volume. <br/>                                                                                                   |
| [**FindNextVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findnextvolumew)<br/>                                     | Continues a volume search started by a call to the [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew) function. <br/>                                                           |
| [**FindNextVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findnextvolumemountpointa)<br/>                 | Continues a mounted folder search started by a call to the [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa) function. <br/>                               |
| [**FindVolumeClose**](/windows/desktop/api/FileAPI/nf-fileapi-findvolumeclose)<br/>                                   | Closes the specified volume search handle.<br/>                                                                                                                         |
| [**FindVolumeMountPointClose**](/windows/desktop/api/WinBase/nf-winbase-findvolumemountpointclose)<br/>               | Closes the specified mounted folder search handle.<br/>                                                                                                                 |
| [**GetDriveType**](/windows/desktop/api/FileAPI/nf-fileapi-getdrivetypea)<br/>                                         | Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.<br/>                                                                         |
| [**GetLogicalDrives**](/windows/desktop/api/FileAPI/nf-fileapi-getlogicaldrives)<br/>                                 | Retrieves a bitmask representing the currently available disk drives.<br/>                                                                                              |
| [**GetLogicalDriveStrings**](/windows/desktop/api/FileAPI/nf-fileapi-getlogicaldrivestringsw)<br/>                     | Fills a buffer with strings that specify valid drives in the system.<br/>                                                                                               |
| [**GetVolumeInformation**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa)<br/>                         | Retrieves information about the file system and volume associated with the specified root directory.<br/>                                                               |
| [**GetVolumeInformationByHandleW**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationbyhandlew)<br/>       | Retrieves information about the file system and volume associated with the specified file.<br/>                                                                         |
| [**GetVolumeNameForVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw)<br/> | Retrieves a volume **GUID** path for the volume that is associated with the specified volume mount point ( drive letter, volume **GUID** path, or mounted folder).<br/> |
| [**GetVolumePathName**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumepathnamew)<br/>                               | Retrieves the volume mount point where the specified path is mounted.<br/>                                                                                              |
| [**GetVolumePathNamesForVolumeName**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumepathnamesforvolumenamew)<br/>   | Retrieves a list of drive letters and mounted folder paths for the specified volume.<br/>                                                                               |
| [**QueryDosDevice**](/windows/desktop/api/FileAPI/nf-fileapi-querydosdevicew)<br/>                                     | Retrieves information about MS-DOS device names.<br/>                                                                                                                   |
| [**SetVolumeLabel**](/windows/desktop/api/WinBase/nf-winbase-setvolumelabela)<br/>                                     | Sets the label of a file system volume.<br/>                                                                                                                            |
| [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa)<br/>                           | Associates a volume with a drive letter or a directory on another volume.<br/>                                                                                          |



 

The following functions are used with volume mount points (drive letters, volume GUID paths, and mounted folders).

-   [**DeleteVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-deletevolumemountpointw)
-   [**FindFirstVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findfirstvolumew)
-   [**FindFirstVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findfirstvolumemountpointa)
-   [**FindNextVolume**](/windows/desktop/api/FileAPI/nf-fileapi-findnextvolumew)
-   [**FindNextVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-findnextvolumemountpointa)
-   [**FindVolumeClose**](/windows/desktop/api/FileAPI/nf-fileapi-findvolumeclose)
-   [**FindVolumeMountPointClose**](/windows/desktop/api/WinBase/nf-winbase-findvolumemountpointclose)
-   [**GetVolumeNameForVolumeMountPoint**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumenameforvolumemountpointw)
-   [**GetVolumePathName**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumepathnamew)
-   [**GetVolumePathNamesForVolumeName**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumepathnamesforvolumenamew)
-   [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa)

 

 




