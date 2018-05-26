---
title: RemoveNetworkConstraint method of the MSFT\_WvrAdminTasks class
description: Removes an existing replication network constraint for the partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 88582f85-9ca4-49b9-81bb-5a58ff629750
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- RemoveNetworkConstraint method
- RemoveNetworkConstraint method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, RemoveNetworkConstraint method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.RemoveNetworkConstraint
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# RemoveNetworkConstraint method of the MSFT\_WvrAdminTasks class

Removes an existing replication network constraint for the partnership.

## Syntax


```mof
uint32 RemoveNetworkConstraint(
  [in] string SourceRGName,
  [in] string SourceComputerName,
  [in] string DestinationRGName,
  [in] string DestinationComputerName
);
```



## Parameters

<dl> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The source RG name.

</dd> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

The source computer name.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The destination RG name.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The destination computer name.

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





