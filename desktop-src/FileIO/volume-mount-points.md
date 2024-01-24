---
description: Using mounted folders, you can unify disparate file systems such as the NTFS file system, a 16-bit FAT file system, and an ISO-9660 file system on a CD-ROM drive into one logical file system on a single NTFS volume.
ms.assetid: '6de526cd-5537-4411-b43f-3c0bdac70d64'
title: Mounted Folders
ms.topic: article
ms.date: 05/31/2018
---

# Mounted Folders

The NTFS file system supports mounted folders. A *mounted folder* is an association between a volume and a directory on another volume. When a mounted folder is created, users and applications can access the target volume either by using the path to the mounted folder or by using the volume's drive letter. For example, a user can create a mounted folder to associate drive D: with the C:\\Mnt\\DDrive folder on drive C. After creating the mounted folder, the user can use the "C:\\Mnt\\DDrive" path to access drive D: as if it were a folder on drive C:.

Using mounted folders, you can unify disparate file systems such as the NTFS file system, a 16-bit FAT file system, and an ISO-9660 file system on a CD-ROM drive into one logical file system on a single NTFS volume. Neither users nor applications need information about the target volume on which a specific file is located. All the information they need to locate a specified file is a complete path using a mounted folder on the NTFS volume. Volumes can be rearranged, substituted, or subdivided into many volumes without users or applications needing to change settings.

For information on mounted folders, see the following topics.

## In this section



| Topic                                                                                                                         | Description                                                                                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Creating Mounted Folders](mounting-and-dismounting-a-volume.md)<br/>                                                  | Creating a mounted folder is a two-step process.<br/>                                                                                                                                                                 |
| [Enumerating Mounted Folders](enumerating-volume-mount-points.md)<br/>                                                 | Functions to use to enumerate mounted folders on a volume.<br/>                                                                                                                                                       |
| [Determining Whether a Directory Is a Mounted Folder](determining-whether-a-directory-is-a-volume-mount-point.md)<br/> | How to determine whether a specified directory is a mounted folder.<br/>                                                                                                                                              |
| [Assigning a Drive Letter to a Volume](assigning-a-drive-letter-to-a-volume.md)<br/>                                   | You can assign a drive letter (for example, X:\) to a local volume by using the [**SetVolumeMountPoint**](/windows/desktop/api/WinBase/nf-winbase-setvolumemountpointa) function, provided there is no volume already assigned to that drive letter.<br/> |
| [Mounted Folder Functions](volume-mount-point-functions.md)<br/>                                                       | Functions used to manage mounted folders.<br/>                                                                                                                                                                        |



 

For examples, see [Mounted Folder Examples](volume-mount-point-examples.md).

 

 




