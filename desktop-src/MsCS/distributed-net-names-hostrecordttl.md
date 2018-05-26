---
title: HostRecordTTL
description: Specifies the time to live (TTL), in seconds, to be set for the resource records published for the virtual machine replication broker.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: B1C29E92-2DF5-4093-B0F5-1532EC12503E
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- HostRecordTTL Failover Cluster , for distributed network names
- HostRecordTTL Failover Cluster
topic_type:
- apiref
api_name:
- HostRecordTTL
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# HostRecordTTL

Specifies the time to live (TTL), in seconds, to be set for the resource records published for the virtual machine replication broker. The following table summarizes the attributes of the **HostRecordTTL** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 1200                                      |



 

## Remarks

The constant for this property is **CLUSREG\_NAME\_NETNAME\_HOST\_TTL**.

## Examples

The property value portion of a [property list](property-lists.md) entry for **HostRecordTTL** can be set with the following example code.


```C++
DWORD          HostRecordTTLData = 1200;
CLUSPROP_DWORD HostRecordTTLValue;

HostRecordTTLValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
HostRecordTTLValue.cbLength  = sizeof(DWORD);
HostRecordTTLValue.dw        = HostRecordTTLData;
```



## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Distributed Network Name Private Properties](distributed-net-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> </dl>

 

 





