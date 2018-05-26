---
title: DatabaseReadWriteMode
description: Specifies the read/write mode for the cluster database.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: E001D255-4E59-44C4-A98A-083B8ACBF630
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DatabaseReadWriteMode Failover Cluster
topic_type:
- apiref
api_name:
- DatabaseReadWriteMode
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DatabaseReadWriteMode

Specifies the read/write mode for the cluster database.



| Attribute            | Value                                     |
|----------------------|-------------------------------------------|
| Data type<br/> | **DWORD**                                 |
| Access<br/>    | [Read/write](read-write-properties.md)   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum<br/>   | 0<br/>                              |
| Maximum<br/>   | 2<br/>                              |
| Default<br/>   | 0<br/>                              |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_DATABASE\_READ\_WRITE\_MODE**.

The possible values are:



| Name                                 | Value        |
|--------------------------------------|--------------|
| Everybody<br/>                 | 0<br/> |
| MajorityWriteMajorityRead<br/> | 1<br/> |
| MajorityWriteLocalRead<br/>    | 2<br/> |



 

## Requirements



|                                     |                                   |
|-------------------------------------|-----------------------------------|
| Minimum supported client<br/> | None supported<br/>         |
| Minimum supported server<br/> | Windows Server 2012 R2<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





