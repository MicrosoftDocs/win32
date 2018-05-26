---
title: SetNetworkConstraint method of the MSFT\_WvrAdminTasks class
description: Creates a new replication network constraint for the partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5cf50f66-232a-4737-abae-71492c3514ef
ms.prod: windows-server-dev
ms.technology:
- storage-replica
- windows-management-instrumentation
ms.tgt_platform: multiple
keywords:
- SetNetworkConstraint method
- SetNetworkConstraint method, MSFT_WvrAdminTasks class
- MSFT_WvrAdminTasks class, SetNetworkConstraint method
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.SetNetworkConstraint
api_location:
- wvrcimprov.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SetNetworkConstraint method of the MSFT\_WvrAdminTasks class

Creates a new replication network constraint for the partnership.

## Syntax


```mof
uint32 SetNetworkConstraint(
  [in]  string                    SourceComputerName,
  [in]  string                    SourceRGName,
  [in]  string                    DestinationComputerName,
  [in]  string                    DestinationRGName,
  [in]  string                    SourceNWInterfaceIndex[],
  [in]  string                    DestinationNWInterfaceIndex[],
  [out] MSFT_WvrNetworkConstraint Output[]
);
```



## Parameters

<dl> <dt>

*SourceComputerName* \[in\]
</dt> <dd>

The source computer name.

</dd> <dt>

*SourceRGName* \[in\]
</dt> <dd>

The source RG name.

</dd> <dt>

*DestinationComputerName* \[in\]
</dt> <dd>

The destination computer name.

</dd> <dt>

*DestinationRGName* \[in\]
</dt> <dd>

The destination RG name.

</dd> <dt>

*SourceNWInterfaceIndex* \[in\]
</dt> <dd>

The source NW interface index.

</dd> <dt>

*DestinationNWInterfaceIndex* \[in\]
</dt> <dd>

The destination NW Interface index.

</dd> <dt>

*Output* \[out\]
</dt> <dd>

On success, contains a collection of [**MSFT\_WvrNetworkConstraint**](msft-wvrnetworkconstraint.md) objects.

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

 

 





