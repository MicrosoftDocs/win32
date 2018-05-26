---
title: Physical Disk Private Properties
description: Physical Disk resources have the following private properties.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6b581b94-edcb-4bd5-9fba-c8c9326c23a2
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- Physical Disk resource type Failover Cluster ,private properties
- properties Failover Cluster ,Physical Disk (private) properties
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# Physical Disk Private Properties

[Physical Disk](physical-disk.md) [resources](resources.md) have the following [private properties](private-properties.md).



| Property                                                                                             | Status                                                                                                                                |
|------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**ConditionalMount**](physical-disks-conditionalmount.md)<br/>                               | Not supported. See [**DiskRunChkDsk**](diskrunchkdsk.md).<br/>                                                                 |
| [**CsvEnableBlockCache**](physical-disks-csvenableblockcache.md)<br/>                         | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**CsvEnforceWriteThrough**](physical-disk-csvenforcewritethrough.md)<br/>                    | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**DiskArbInterval**](diskarbinterval.md)<br/>                                                | TBD<br/>                                                                                                                        |
| [**DiskIdGuid**](diskarbinterval.md)<br/>                                                     | You must specify either a [**DiskIdGuid**](diskarbinterval.md) or a [**DiskSignature**](disksignature.md), but not both.<br/> |
| [**DiskIdType**](diskidtype.md)<br/>                                                          | Required.<br/>                                                                                                                  |
| [**DiskInfo**](physical-disks-diskinfo.md)<br/>                                               | Not supported. See [**DiskVolumeInfo**](diskvolumeinfo.md).<br/>                                                               |
| [**DiskPath**](diskpath.md)<br/>                                                              | Optional.<br/>                                                                                                                  |
| [**DiskReload**](diskreload.md)<br/>                                                          | Optional.<br/>                                                                                                                  |
| [**DiskRunChkDsk**](diskrunchkdsk.md)<br/>                                                    | Optional.<br/>                                                                                                                  |
| [**DiskSignature**](disksignature.md)<br/>                                                    | You must specify either a [**DiskIdGuid**](diskarbinterval.md) or a [**DiskSignature**](disksignature.md), but not both.<br/> |
| [**DiskUniqueIds**](diskuniqueids.md)<br/>                                                    | Optional.<br/>                                                                                                                  |
| [**DiskVolumeInfo**](diskvolumeinfo.md)<br/>                                                  | TBD<br/>                                                                                                                        |
| [**Drive**](physical-disks-drive.md)<br/>                                                     | Not supported.<br/>                                                                                                             |
| [**MaintenanceMode**](maintenancemode.md)<br/>                                                | TBD<br/>                                                                                                                        |
| [**MaxIoLatency**](physical-disks-maxiolatency.md)<br/>                                       | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**MountVolumeInfo**](physical-disks-mountvolumeinfo.md)<br/>                                 | Not supported. See [**DiskVolumeInfo**](diskvolumeinfo.md).<br/>                                                               |
| [**PoolId**](physical-disks-poolid.md)<br/>                                                   | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**Signature**](physical-disks-signature.md)<br/>                                             | Not supported. See [**DiskSignature**](disksignature.md).<br/>                                                                 |
| [**SkipChkdsk**](physical-disks-skipchkdsk.md)<br/>                                           | Not supported. See [**DiskRunChkDsk**](diskrunchkdsk.md).<br/>                                                                 |
| [**VirtualDiskId**](physical-disks-virtualdiskid.md)<br/>                                     | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**VirtualDiskDescription**](physical-disks-virtualdiskdescription.md)<br/>                   | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**VirtualDiskHealth**](virtualdiskhealth.md)<br/>                                            | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**VirtualDiskName**](physical-disks-virtualdiskname.md)<br/>                                 | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**VirtualDiskProvisioning**](physical-disks-virtualdiskprovisioning.md)<br/>                 | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**VirtualDiskResiliencyColumns**](physical-disks-virtualdiskresiliencycolumns.md)<br/>       | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**VirtualDiskResiliencyInterleave**](physical-disks-virtualdiskresiliencyinterleave.md)<br/> | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |
| [**VirtualDiskResiliencyType**](virtualdiskresiliencytype.md)<br/>                            | TBD<br/> **Windows Server 2008 R2 and Windows Server 2008:** Not supported.<br/> <br/>                              |



 

[Cluster Administrator](cluster-administrator.md) presents these properties on the property page associated with the **Parameters** tab for Physical Disk resources.

## Related topics

<dl> <dt>

[Cluster Properties](cluster-properties.md)
</dt> </dl>

 

 





