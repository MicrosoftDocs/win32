---
description: Describes two types of disk quota limits and how disk quota limits are measured.
ms.assetid: 6595d5e0-eb97-437e-abd2-3a04faefde7d
title: Disk Quota Limits
ms.topic: article
ms.date: 05/31/2018
---

# Disk Quota Limits

The disk space that each file uses is charged directly to the user who owns the file. The owner of a file is identified by the security identifier (SID) in the security information for the file. The total disk space charged to a user is the sum of the length of all data streams. In other words, property set streams and resident user data streams affect the user's quota.

Quota is not charged for re-parse points, security descriptors, or other metadata that is associated with the files. Compressing or decompressing files does not affect the disk space reported for the files. Therefore, quota settings on one volume can be compared to settings on another volume.

There are two types of disk quota limits, as shown in the following table.



| Limit                        | Description                                                                                                                                                                                                                                                                    |
|------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Warning threshold<br/> | You can configure the system to generate a system logfile entry when the disk space charged to the user exceeds this value.<br/>                                                                                                                                         |
| Hard quota<br/>        | You can configure the system to generate a system logfile entry when the disk space charged to the user exceeds this value. You can also configure the system to deny additional disk space to the user when the disk space charged to the user exceeds this value.<br/> |



 

The NTFS file system automatically creates a user quota entry when a user first writes to the volume. Entries that are created automatically are assigned the default warning threshold and hard quota limit values for the volume.

 

 




