---
title: GroupType
description: Specifies the type of the resource group.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'BDD220A6-275C-45C6-B087-A70BB119447E'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["GroupType Failover Cluster"]
topic_type:
- apiref
api_name:
- GroupType
api_type:
- NA
---

# GroupType

Specifies the type of the resource group.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read-only](read-only-properties.md)     |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 100                                       |
| Maximum   | 9999                                      |
| Default   | 9999                                      |



 

## Remarks

The following values may be specified for this property:



| Name                   | Value | Description                                                 |
|------------------------|-------|-------------------------------------------------------------|
| **FileServer**         | 100   | A file server resource group.                               |
| **PrintServer**        | 101   | A print server resource group.                              |
| **DhcpServer**         | 102   | A Dynamic Host Configuration Protocol resource group.       |
| **Dtc**                | 103   | A Distributed Transaction Coordinator resource group.       |
| **Msmq**               | 104   | A Microsoft Message Queuing resource group.                 |
| **Wins**               | 105   | A Windows Internet Name Service resource group.             |
| **StandAloneDfs**      | 106   | A stand-alone Distributed File System resource group.       |
| **GenericApplication** | 107   | A generic application resource group.                       |
| **GenericService**     | 108   | A generic service resource group.                           |
| **GenericScript**      | 109   | A generic script resource group.                            |
| **IScsiNameService**   | 110   | An Internet Small Computer System Interface resource group. |
| **VirtualMachine**     | 111   | A virtual machine resource group.                           |
| **TsSessionBroker**    | 112   | A terminal services session broker resource group.          |
| **Unknown**            | 9999  | An unknown resource group.                                  |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Group Common Properties](group-common-properties.md)
</dt> </dl>

 

 





