---
title: SmapiQueryPartnerGroupStatus method of the MSFT\_WvrAdminTasks class
description: TBD.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 880C22A4-5464-49AA-8515-BED57DDEC66A
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SmapiQueryPartnerGroupStatus method
- SmapiQueryPartnerGroupStatus method, MSFT_WvrAdminTasks interface
- MSFT_WvrAdminTasks interface, SmapiQueryPartnerGroupStatus method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SmapiQueryPartnerGroupStatus method of the MSFT\_WvrAdminTasks class

TBD

## Syntax


```mof
uint32 SmapiQueryPartnerGroupStatus(
  [in]  string   ReplicationGroupName,
  [out] uint16   PercentSynced,
  [out] datetime LastSyncTime,
  [out] uint32   ReplicationStatus
);
```



## Parameters

<dl> <dt>

*ReplicationGroupName* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*PercentSynced* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*LastSyncTime* \[out\]
</dt> <dd>

TBD

</dd> <dt>

*ReplicationStatus* \[out\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





