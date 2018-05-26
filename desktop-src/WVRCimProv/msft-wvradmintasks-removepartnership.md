---
title: RemovePartnership method of the MSFT\_WvrAdminTasks class
description: Removes an existing replication partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: fd16993f-4dc9-44da-95f7-ea75a7154877
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemovePartnership method
- RemovePartnership method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, RemovePartnership method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.RemovePartnership
api_location:
- WvrCimProv.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemovePartnership method of the MSFT\_WvrAdminTasks class

Removes an existing replication partnership.

## Syntax


```mof
uint32 RemovePartnership(
  [in] string  SourceComputerName,
  [in] string  SourceRGName,
  [in] string  DestinationComputerName,
  [in] string  DestinationRGName,
  [in] boolean IgnoreRemovalFailure
);
```



## Parameters

<dl> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the source computer.

</dd> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The name of the source replication group.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The FQDN or NetBIOS name of the destination computer.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The name of the destination replication group.

</dd> <dt>

*IgnoreRemovalFailure* \[in\]
</dt> <dd>

**true** to ignore a removal failure; otherwise, **false**.

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

 

 





