---
title: SharedVolumeSecurityDescriptor
description: Specifies the security descriptor for a cluster shared volume (CSV).
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 914B569D-4ECF-4290-BBFD-FA0BA09D3404
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SharedVolumeSecurityDescriptor Failover Cluster
topic_type:
- apiref
api_name:
- SharedVolumeSecurityDescriptor
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# SharedVolumeSecurityDescriptor

Specifies the security descriptor for a cluster shared volume (CSV).



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | byte array                                                       |
| Access    | [Read/write](read-write-properties.md)                          |
| Structure | [**CLUSPROP\_BINARY**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_binary)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **CsvMdsSecurityDescriptor**                                     |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_CSV\_MDS\_SD**.

This property contains a binary that describes a security descriptor.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Cluster Common Properties](cluster-common-properties.md)
</dt> </dl>

 

 





