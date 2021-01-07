---
description: Volumes are implemented by a device driver called a volume manager.
ms.assetid: 424ddbd9-5692-45ef-95fb-7b00b09e3205
title: About Volume Management
ms.topic: article
ms.date: 05/31/2018
---

# About Volume Management

Volumes are implemented by a device driver called a volume manager. Examples include the FtDisk Manager, the Logical Disk Manager (LDM), and the VERITAS Logical Volume Manager (LVM). Volume managers provide a layer of physical abstraction, data protection (using some form of RAID), and performance.

## In this section



| Topic                                                                       | Description                                                                                                                                                                                                                                                                             |
|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [File System Recognition](file-system-recognition.md)<br/>           | The goal of file system recognition is to allow the Windows operating system to have an additional option for a valid but unrecognized file system other than "RAW".<br/>                                                                                                         |
| [Naming a Volume](naming-a-volume.md)<br/>                           | A label is a user-friendly name that is assigned to a volume, usually by an end user, to make it easier to recognize. A volume can have a label, a drive letter, both, or neither. To set the label for a volume, use the [**SetVolumeLabel**](/windows/desktop/api/WinBase/nf-winbase-setvolumelabela) function.<br/> |
| [Enumerating Volumes](enumerating-volumes.md)<br/>                   | To make a complete list of the volumes on a computer, or to manipulate each volume in turn, you can enumerate volumes.<br/>                                                                                                                                                       |
| [Obtaining Volume Information](obtaining-volume-information.md)<br/> | Before you access files and directories on a given volume, you should determine the capabilities of the file system by using the [**GetVolumeInformation**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa) function.<br/>                                                                              |
| [Change Journals](change-journals.md)<br/>                           | When any change is made to a file or directory in a volume, the USN change journal for that volume is updated with a description of the change and the name of the file or directory.<br/>                                                                                        |
| [Mounted Folders](volume-mount-points.md)<br/>                       | Using mounted folders, you can unify disparate file systems such as the NTFS file system, a 16-bit FAT file system, and an ISO-9660 file system on a CD-ROM drive into one logical file system on a single NTFS volume.<br/>                                                      |
| [Master File Table](master-file-table.md)<br/>                       | All information about a file, including its size, time and date stamps, permissions, and data content, is stored either in master file table (MFT) entries, or in space outside the MFT that is described by MFT entries.<br/>                                                    |



 

## Related topics

<dl> <dt>

[Basic Disks and Volumes Technical Reference](/previous-versions/windows/it-pro/windows-server-2003/cc784732(v=ws.10))
</dt> <dt>

[Dynamic Disks and Volumes Technical Reference](/previous-versions/windows/it-pro/windows-server-2003/cc785638(v=ws.10))
</dt> <dt>

[Volume Management Reference](volume-management-reference.md)
</dt> </dl>

 

