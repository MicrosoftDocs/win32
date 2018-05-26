---
title: DumpPolicy
description: Dump policy.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 977A35E0-8654-4ADF-A610-272A1D010B57
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DumpPolicy Failover Cluster
topic_type:
- apiref
api_name:
- DumpPolicy
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DumpPolicy

Dump policy.



| Attribute            | Value                                                        |
|----------------------|--------------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                         |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>           |
| Structure<br/> | [**CLUSPROP\_ULARGE\_INTEGER**](/windows/previous-versions/ClusAPI/ns-clusapi-clusprop_ularge_integer?branch=master) |
| Minimum<br/>   | 0<br/>                                                 |
| Maximum<br/>   | 0<br/>                                                 |
| Default<br/>   | **( DWORD\_PTR ) &ClusterDumpPolicyDefaults**<br/>     |



 

## Remarks

The constant for this property is **CLUSREG\_DUMP\_POLICY**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





