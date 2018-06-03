---
title: SetGroupAddVolumes method of the MSFT\_WvrAdminTasks class
description: Adds volumes to an existing replication group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 91661b8e-27e9-4b00-b97f-1ad24185bbfb
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetGroupAddVolumes method
- SetGroupAddVolumes method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SetGroupAddVolumes method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.SetGroupAddVolumes
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SetGroupAddVolumes method of the MSFT\_WvrAdminTasks class

Adds volumes to an existing replication group.

## Syntax


```mof
uint32 SetGroupAddVolumes(
  [in] string ComputerName,
  [in] string Name,
  [in] string AddVolumeName[]
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

*AddVolumeName* \[in\]
</dt> <dd>

The volume names to add.

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

 

 





