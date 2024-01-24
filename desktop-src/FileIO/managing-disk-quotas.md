---
description: Administrators can control the amount of data that each user can store on an NTFS file system volume.
ms.assetid: 42efbd5b-6455-4319-a76e-cdb666fc36b8
title: Managing Disk Quotas
ms.topic: article
ms.date: 05/31/2018
---

# Managing Disk Quotas

The NTFS file system supports *disk quotas*, which allow administrators to control the amount of data that each user can store on an NTFS file system volume. Administrators can optionally configure the system to log an event when users are near their quota, and to deny further disk space to users who exceed their quota. Administrators can also generate reports, and use the event monitor to track quota issues.

You can determine whether a file system supports disk quotas by calling the [**GetVolumeInformation**](/windows/desktop/api/FileAPI/nf-fileapi-getvolumeinformationa) function and examining the **FILE\_VOLUME\_QUOTAS** bit flag.

## In this section



| Topic                                                                                                   | Description                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [User-level Administration of Disk Quotas](user-level-administration-of-disk-quotas.md)<br/>     | How to get more free disk space after exceeding the quota allowance.<br/>                                                                  |
| [System-level Administration of Disk Quotas](system-level-administration-of-disk-quotas.md)<br/> | The system administrator can set quotas for specific users on a volume. The administrator can also set default quotas for the volume.<br/> |
| [Disk Quota Limits](disk-quota-limits.md)<br/>                                                   | Describes two types of disk quota limits and how disk quota limits are measured.<br/>                                                      |
| [Disk Quota Interfaces](disk-quota-interfaces.md)<br/>                                           | Interfaces used with disk quotas.<br/>                                                                                                     |



 

 

 




