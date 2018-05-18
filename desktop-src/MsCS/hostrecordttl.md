---
title: HostRecordTTL
description: Time To Live (TTL) in seconds to be set for the resource records published for the cluster name.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '7c0ecb4a-b89d-4bb8-9a8a-a77f657b6bf6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["HostRecordTTL Failover Cluster , for Network Name properties", "HostRecordTTL Failover Cluster"]
topic_type:
- apiref
api_name:
- HostRecordTTL
api_type:
- NA
---

# HostRecordTTL

Time To Live (TTL) in seconds to be set for the resource records published for the cluster name. The following table summarizes the attributes of the **HostRecordTTL** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Status    | Optional                                  |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
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



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





