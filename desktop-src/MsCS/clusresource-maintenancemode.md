---
title: ClusResource MaintenanceMode property
description: The maintenance mode state of a disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'aa39b401-bf18-48c5-83bb-e192efe1ef41'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["MaintenanceMode property Failover Cluster", "MaintenanceMode property Failover Cluster , ClusResource interface", "ClusResource interface Failover Cluster , MaintenanceMode property"]
topic_type:
- apiref
api_name:
- ClusResource.MaintenanceMode
- ClusResource.get_MaintenanceMode
- ClusResource.put_MaintenanceMode
api_location:
- MsClus.dll
api_type:
- COM
---

# ClusResource::MaintenanceMode property

\[The **MaintenanceMode** property is available for use in the operating systems specified in the Requirements section. It may be altered or unavailable in subsequent versions.\]

Retrieves or sets the maintenance mode state of a disk resource.

This property is read/write.

## Syntax


```VB
.MaintenanceMode
```



## Property value

**Boolean** containing the maintenance mode state of the disk resource.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 Datacenter with SP1, Windows Server 2008 Enterprise with SP1<br/> |
| Header<br/>                   | <dl> <dt>MsClus.h</dt> </dl>         |
| IDL<br/>                      | <dl> <dt>MsClus.idl</dt> </dl>       |
| Type library<br/>             | <dl> <dt>MsClus.tlb</dt> </dl>       |
| DLL<br/>                      | <dl> <dt>MsClus.dll</dt> </dl>       |
| IID<br/>                      | IID\_ISClusResource is defined as F2E6070A-2631-11D1-89F1-00A0C90D061E<br/>           |



 

 





