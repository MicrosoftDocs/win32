---
title: GetPartnershipFromGroup method of the MSFT\_WvrAdminTasks class
description: Retrieves a replication partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '4a82cd31-9a81-4c10-b122-247de9c36e6f'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetPartnershipFromGroup method", "GetPartnershipFromGroup method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, GetPartnershipFromGroup method"]
---

# GetPartnershipFromGroup method of the MSFT\_WvrAdminTasks class

Retrieves a replication partnership.

## Syntax


```mof
uint32 GetPartnershipFromGroup(
  [in]  string                         Name,
  [in]  string                         ComputerName,
  [out] MSFT_WvrReplicationPartnership Output[]
);
```



## Parameters

<dl> <dt>

*Name* \[in\]
</dt> <dd>

TBD

</dd> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the resulting [**MSFT\_WvrReplicationPartnership**](msft-wvrreplicationpartnership.md) embedded instance.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>WVRCimProv.Mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>WvrCimProv.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





