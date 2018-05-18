---
title: GetNetworkConstraint method of the MSFT\_WvrAdminTasks class
description: Retrieves a replication network constraint for the partnership.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'dab36119-d773-4632-9698-d207f410048e'
ms.prod: 'windows-server-dev'
ms.technology:
- 'storage-replica'
- 'windows-management-instrumentation'
ms.tgt_platform: multiple
keywords: ["GetNetworkConstraint method", "GetNetworkConstraint method, MSFT_WvrAdminTasks class", "MSFT_WvrAdminTasks class, GetNetworkConstraint method"]
topic_type:
- apiref
api_name:
- MSFT_WvrAdminTasks.GetNetworkConstraint
api_location:
- wvrcimprov.dll
api_type:
- COM
---

# GetNetworkConstraint method of the MSFT\_WvrAdminTasks class

Retrieves a replication network constraint for the partnership.

## Syntax


```mof
uint32 GetNetworkConstraint(
  [in]  string                    SourceRGName,
  [in]  string                    SourceComputerName,
  [in]  string                    DestinationRGName,
  [in]  string                    DestinationComputerName,
  [out] MSFT_WvrNetworkConstraint Output[]
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

</dd> <dt>

*Output* \[out\]
</dt> <dd>

ON success, returns a collection of [**MSFT\_WvrNetworkConstraint**](msft-wvrnetworkconstraint.md).

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                      |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                            |
| Namespace<br/>                | Root\\Microsoft\\Windows\\StorageReplica<br/>                                       |
| MOF<br/>                      | <dl> <dt>Wvrcimprov.mof</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Wvrcimprov.dll</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_WvrAdminTasks**](msft-wvradmintasks.md)
</dt> </dl>

 

 





