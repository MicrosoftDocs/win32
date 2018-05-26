---
title: DiskIdType
description: Describes the partition type of the physical disk resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5a47208b-1642-42ec-8725-aa760139afa7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskIdType Failover Cluster , for Physical Disk private properties
- DiskIdType Failover Cluster
topic_type:
- apiref
api_name:
- DiskIdType
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# DiskIdType

Describes the partition type of the physical disk resource. The following table summarizes the attributes of the **DiskIdType** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Required                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 5000                                      |
| Default   | 5000                                      |



 

## Remarks

The **DiskIdType** property can be set to one of the following values.



| Value                                    | Description                                                         |
|------------------------------------------|---------------------------------------------------------------------|
| **PARTITION\_STYLE\_MBR** (0)<br/> | The disk has a Master Boot Record (MBR) partition.<br/>       |
| **PARTITION\_STYLE\_GPT** (1)<br/> | The disk has a **GUID** Partition Table (GPT) partition.<br/> |
| 5000<br/>                          | The disk has an unrecognized partitioning scheme.<br/>        |



 

**PARTITION\_STYLE\_MBR** and **PARTITION\_STYLE\_GPT** are defined in WinIoCtl.h.

## Examples

The property value portion of a [property list](property-lists.md) entry for **DiskIdType** can be set with the following example code.


```C++
DWORD          DiskIdTypeData = 0;
CLUSPROP_DWORD DiskIdTypeValue;

DiskIdTypeValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DiskIdTypeValue.cbLength  = sizeof(DWORD);
DiskIdTypeValue.dw        = DiskIdTypeData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> </dl>

 

 





