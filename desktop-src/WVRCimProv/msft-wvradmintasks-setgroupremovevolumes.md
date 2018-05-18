---
title: SetGroupRemoveVolumes method of the MSFT\_WvrAdminTasks class
description: Removes volumes from an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '3382e345-3937-4279-a3bf-c3e770106c19'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["SetGroupRemoveVolumes method", "SetGroupRemoveVolumes method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, SetGroupRemoveVolumes method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.SetGroupRemoveVolumes
api_location:
- WvrCimProv.dll
api_type:
- COM
---

# SetGroupRemoveVolumes method of the MSFT\_WvrAdminTasks class

Removes volumes from an existing replication group.

## Syntax


```mof
uint32 SetGroupRemoveVolumes(
  [in] string ComputerName,
  [in] string Name,
  [in] string RemoveVolumeName[]
);
```



## Parameters

<dl> <dt>

*ComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the computer.

</dd> <dt>

*Name* \[in\]
</dt> <dd>

The name of the replication group.

</dd> <dt>

*RemoveVolumeName* \[in\]
</dt> <dd>

The volume names to remove.

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

 

 





