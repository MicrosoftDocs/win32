---
description: Before you access files and directories on a given volume, you should determine the capabilities of the file system by using the GetVolumeInformation function.
ms.assetid: 008e0cc4-bc12-47e8-a8b7-d4fa9395fceb
title: Obtaining Volume Information
ms.topic: article
ms.date: 05/31/2018
---

# Obtaining Volume Information

The [**GetVolumeInformation**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa) function retrieves information about the file system on a given volume. This information includes the volume name, volume serial number, file system name, file system flags, maximum length of a file name, and so on. Before you access files and directories on a given volume, you should determine the capabilities of the file system by using the [**GetVolumeInformation**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa) function. This function returns values that you can use to adapt your application to work effectively with the file system.

In general, you should avoid using static buffers for file names and paths. Instead, use the values returned by [**GetVolumeInformation**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa) to allocate buffers as you need them. If you must use static buffers, reserve 256 characters for file names and 260 characters for paths.

The [**GetSystemDirectory**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getsystemdirectorya) and [**GetWindowsDirectory**](/windows/desktop/api/sysinfoapi/nf-sysinfoapi-getwindowsdirectorya) functions retrieve the paths to the system directory and the Windows directory, respectively.

The [**GetDiskFreeSpace**](/windows/desktop/api/FileAPI/nf-fileapi-getdiskfreespacea) function retrieves organizational information about a volume, including the number of bytes per sector, the number of sectors per cluster, the number of free clusters, and the total number of clusters. However, **GetDiskFreeSpace** cannot report volume sizes that are greater than 2 GB. To ensure that your application works with large capacity hard drives, use the [**GetDiskFreeSpaceEx**](/windows/desktop/api/FileAPI/nf-fileapi-getdiskfreespaceexa) function.

The [**GetDriveType**](/windows/desktop/api/FileAPI/nf-fileapi-getdrivetypea) function indicates whether the volume referenced by the specified drive letter is a removable, fixed, CD-ROM, RAM, or network drive.

The [**GetLogicalDrives**](/windows/desktop/api/FileAPI/nf-fileapi-getlogicaldrives) function identifies the volumes present. The [**GetLogicalDriveStrings**](/windows/desktop/api/FileAPI/nf-fileapi-getlogicaldrivestringsw) function retrieves a null-terminated string for each volume present. Use these strings whenever a root directory is required.

## Related topics

<dl> <dt>

[File System Recognition](file-system-recognition.md)
</dt> </dl>

 

 
