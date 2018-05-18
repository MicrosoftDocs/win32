---
title: HostRecordTTL
description: Specifies the time to live (TTL), in seconds, to be set for the resource records published for the virtual machine replication broker.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'CB1E95D6-A906-41A2-8514-86DD8BC85032'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["HostRecordTTL Failover Cluster , for virtual machine replication brokers", "HostRecordTTL Failover Cluster"]
topic_type:
- apiref
api_name:
- HostRecordTTL
api_type:
- NA
---

# HostRecordTTL

Specifies the time to live (TTL), in seconds, to be set for the resource records published for the virtual machine replication broker. The following table summarizes the attributes of the **HostRecordTTL** property.



| Attribute | Value                                     |
|-----------|-------------------------------------------|
| Data type | **DWORD**                                 |
| Access    | [Read/write](read-write-properties.md)   |
| Structure | [**CLUSPROP\_DWORD**](clusprop-dword.md) |
| Minimum   | 0                                         |
| Maximum   | 0xFFFFFFFF                                |
| Default   | 1200                                      |



 

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
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](clusprop-dword.md)
</dt> </dl>

 

 





