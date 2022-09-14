---
description: All information about a file, including its size, time and date stamps, permissions, and data content, is stored either in master file table (MFT) entries, or in space outside the MFT that is described by MFT entries.
ms.assetid: e0933846-278e-4bc8-8982-c5819c252dad
title: Master File Table (Local File Systems)
ms.topic: article
ms.date: 05/31/2018
---

# Master File Table (Local File Systems)

The NTFS file system contains a file called the *master file table*, or MFT. There is at least one entry in the MFT for every file on an NTFS file system volume, including the MFT itself. All information about a file, including its size, time and date stamps, permissions, and data content, is stored either in MFT entries, or in space outside the MFT that is described by MFT entries.

As files are added to an NTFS file system volume, more entries are added to the MFT and the MFT increases in size. When files are deleted from an NTFS file system volume, their MFT entries are marked as free and may be reused. However, disk space that has been allocated for these entries is not reallocated, and the size of the MFT does not decrease.

The NTFS file system reserves space for the MFT to keep the MFT as contiguous as possible as it grows. The space reserved by the NTFS file system for the MFT in each volume is called the MFT zone. Space for file and directories are also allocated from this space, but only after all of the volume space outside of the MFT zone has been allocated.

Depending on the average file size and other variables, either the reserved MFT zone or the unreserved space on the disk may be allocated first as the disk fills to capacity. Volumes with a small number of relatively large files will allocate the unreserved space first, while volumes with a large number of relatively small files allocate the MFT zone first. In either case, fragmentation of the MFT starts to take place when one region or the other becomes fully allocated. If the unreserved space is completely allocated, space for user files and directories will be allocated from the MFT zone. If the MFT zone is completely allocated, space for new MFT entries will be allocated from the unreserved space.

The MFT itself can be defragmented. To reduce the chance of the MFT zone becoming fully allocated before the defragmentation process is complete, leave as much space at the beginning of the MFT zone as possible before defragmenting the volume. If the MFT zone becomes fully allocated before defragmentation has completed, there must be unallocated space outside of the MFT zone.

The default MFT zone is calculated and reserved by the system when it mounts the volume, and is based on volume size. You can increase the MFT zone by means of the registry entry detailed in [Microsoft Knowledge Base Article 174619](https://support.microsoft.com/kb/174619), but you cannot make the default MFT zone smaller than what is calculated. Increasing the MFT zone does not decrease the disk space that users can use for data files.

To determine the current size of the MFT, analyze the NTFS file system drive with Disk Defragmenter, then click the **View Report** button. The drive statistics will be displayed, including the current MFT size, and number of fragments. You can also obtain the size of the MFT by using the [**FSCTL\_GET\_NTFS\_VOLUME\_DATA**](/windows/win32/api/winioctl/ni-winioctl-fsctl_get_ntfs_volume_data) control code.

 

 
