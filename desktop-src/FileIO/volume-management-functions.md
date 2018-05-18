---
Description: 'Functions used in volume management.'
ms.assetid: 'dc985126-970c-49f2-877f-3759125e43b6'
title: Volume Management Functions
---

# Volume Management Functions

Functions used in volume management.

## In this section



| Topic                                                                                   | Description                                                                                                                                                                   |
|-----------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DefineDosDevice**](definedosdevice.md)<br/>                                   | Defines, redefines, or deletes MS-DOS device names.<br/>                                                                                                                |
| [**DeleteVolumeMountPoint**](deletevolumemountpoint.md)<br/>                     | Deletes a drive letter or mounted folder.<br/>                                                                                                                          |
| [**FindFirstVolume**](findfirstvolume.md)<br/>                                   | Retrieves the name of a volume on a computer. <br/>                                                                                                                     |
| [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md)<br/>               | Retrieves the name of a mounted folder on the specified volume. <br/>                                                                                                   |
| [**FindNextVolume**](findnextvolume.md)<br/>                                     | Continues a volume search started by a call to the [**FindFirstVolume**](findfirstvolume.md) function. <br/>                                                           |
| [**FindNextVolumeMountPoint**](findnextvolumemountpoint.md)<br/>                 | Continues a mounted folder search started by a call to the [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md) function. <br/>                               |
| [**FindVolumeClose**](findvolumeclose.md)<br/>                                   | Closes the specified volume search handle.<br/>                                                                                                                         |
| [**FindVolumeMountPointClose**](findvolumemountpointclose.md)<br/>               | Closes the specified mounted folder search handle.<br/>                                                                                                                 |
| [**GetDriveType**](getdrivetype.md)<br/>                                         | Determines whether a disk drive is a removable, fixed, CD-ROM, RAM disk, or network drive.<br/>                                                                         |
| [**GetLogicalDrives**](getlogicaldrives.md)<br/>                                 | Retrieves a bitmask representing the currently available disk drives.<br/>                                                                                              |
| [**GetLogicalDriveStrings**](getlogicaldrivestrings.md)<br/>                     | Fills a buffer with strings that specify valid drives in the system.<br/>                                                                                               |
| [**GetVolumeInformation**](getvolumeinformation.md)<br/>                         | Retrieves information about the file system and volume associated with the specified root directory.<br/>                                                               |
| [**GetVolumeInformationByHandleW**](getvolumeinformationbyhandlew.md)<br/>       | Retrieves information about the file system and volume associated with the specified file.<br/>                                                                         |
| [**GetVolumeNameForVolumeMountPoint**](getvolumenameforvolumemountpoint.md)<br/> | Retrieves a volume **GUID** path for the volume that is associated with the specified volume mount point ( drive letter, volume **GUID** path, or mounted folder).<br/> |
| [**GetVolumePathName**](getvolumepathname.md)<br/>                               | Retrieves the volume mount point where the specified path is mounted.<br/>                                                                                              |
| [**GetVolumePathNamesForVolumeName**](getvolumepathnamesforvolumename.md)<br/>   | Retrieves a list of drive letters and mounted folder paths for the specified volume.<br/>                                                                               |
| [**QueryDosDevice**](querydosdevice.md)<br/>                                     | Retrieves information about MS-DOS device names.<br/>                                                                                                                   |
| [**SetVolumeLabel**](setvolumelabel.md)<br/>                                     | Sets the label of a file system volume.<br/>                                                                                                                            |
| [**SetVolumeMountPoint**](setvolumemountpoint.md)<br/>                           | Associates a volume with a drive letter or a directory on another volume.<br/>                                                                                          |



 

The following functions are used with volume mount points (drive letters, volume GUID paths, and mounted folders).

-   [**DeleteVolumeMountPoint**](deletevolumemountpoint.md)
-   [**FindFirstVolume**](findfirstvolume.md)
-   [**FindFirstVolumeMountPoint**](findfirstvolumemountpoint.md)
-   [**FindNextVolume**](findnextvolume.md)
-   [**FindNextVolumeMountPoint**](findnextvolumemountpoint.md)
-   [**FindVolumeClose**](findvolumeclose.md)
-   [**FindVolumeMountPointClose**](findvolumemountpointclose.md)
-   [**GetVolumeNameForVolumeMountPoint**](getvolumenameforvolumemountpoint.md)
-   [**GetVolumePathName**](getvolumepathname.md)
-   [**GetVolumePathNamesForVolumeName**](getvolumepathnamesforvolumename.md)
-   [**SetVolumeMountPoint**](setvolumemountpoint.md)

 

 




