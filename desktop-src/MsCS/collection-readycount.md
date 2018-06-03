---
title: ReadyCount
description: Indicates how many groups in a set must have met the ReadySetting criteria before the set is considered to be ready.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 3A50C566-0F88-4156-AA84-A579616682EF
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- ReadyCount Failover Cluster
topic_type:
- apiref
api_name:
- ReadyCount
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# ReadyCount

Indicates how many groups in a set must have met the [**ReadySetting**](collection-readysetting.md) criteria before the set is considered to be ready.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 0xFFFFFFFF<br/>                                |



 

<dl> <dt>

<span id="0xffffffff__default_"></span><span id="0XFFFFFFFF__DEFAULT_"></span>0xffffffff (default)
</dt> <dd>

All groups in the set must be ready before the set is considered to be ready.

</dd> <dt>

<span id="0"></span>0
</dt> <dd>

A majority of groups in the set must be ready before the set is considered to be ready.

</dd> <dt>

<span id="1...N"></span><span id="1...n"></span>1...N
</dt> <dd>

At least this many groups in the set must be ready. If this value exceeds the number of groups then all groups must be ready.

</dd> </dl>

## Remarks

The constant for this property is **CLUSREG\_NAME\_GROUPSET\_READY\_COUNT**.

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2016<br/> |



## See also

<dl> <dt>

[Groupset Common Properties](collection-common-properties.md)
</dt> </dl>

 

 





