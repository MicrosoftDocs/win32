---
title: GetGroup method of the MSFT\_WvrAdminTasks class
description: Retrieves a replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 4c7479eb-a55b-485f-acd3-c431e4cd4bb5
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- GetGroup method
- GetGroup method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, GetGroup method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.GetGroup
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# GetGroup method of the MSFT\_WvrAdminTasks class

Retrieves a replication group.

## Syntax


```mof
uint32 GetGroup(
  [in]  string                   ComputerName,
  [in]  string                   Name,
  [out] MSFT_WvrReplicationGroup Output[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the destination computer.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

Returns the resulting [**MSFT\_WvrReplicationGroup**](msft-wvrreplicationgroup.md) embedded instance.

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

 

 





