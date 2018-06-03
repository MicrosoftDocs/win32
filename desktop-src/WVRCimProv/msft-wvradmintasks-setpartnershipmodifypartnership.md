---
title: SetPartnershipModifyPartnership method of the MSFT\_WvrAdminTasks class
description: Changes the RPO or log size settings to replication groups in an existing partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 478a072c-7f4a-4792-afbd-0babd72538b6
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetPartnershipModifyPartnership method
- SetPartnershipModifyPartnership method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SetPartnershipModifyPartnership method
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetPartnershipModifyPartnership method of the MSFT\_WvrAdminTasks class

Changes the RPO or log size settings to replication groups in an existing partnership.

## Syntax


```mof
uint32 SetPartnershipModifyPartnership(
  [in] string  SourceRGName,
  [in] string  SourceComputerName,
  [in] string  DestinationRGName,
  [in] string  DestinationComputerName,
  [in] uint32  ReplicationMode,
  [in] uint32  AsyncRPO,
  [in] uint64  LogSizeInBytes,
  [in] boolean Encryption
);
```



## Parameters

<dl> <dt>

*SourceRGName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ReplicationMode* \[in\]
</dt> <dd>

TBD

<dt>

<span id="Sync"></span><span id="sync"></span><span id="SYNC"></span>

**Sync** (1)


</dt> <dd></dd> <dt>

<span id="Async"></span><span id="async"></span><span id="ASYNC"></span>

**Async** (2)


</dt> <dd></dd> </dl> </dd> <dt>

*AsyncRPO* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*LogSizeInBytes* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*Encryption* \[in\]
</dt> <dd>

TBD

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





