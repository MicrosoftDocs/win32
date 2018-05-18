---
title: CreatingDC
description: Stores the name of the domain controller that was used to obtain the VirtualServer Computer object.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '62A2EE52-A777-43A8-B922-6DA1A96198D9'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["CreatingDC Failover Cluster ,for virtual machine replication brokers", "CreatingDC Failover Cluster"]
topic_type:
- apiref
api_name:
- CreatingDC
api_type:
- NA
---

# CreatingDC

Stores the name of the domain controller that was used to obtain the **VirtualServer** Computer object. The following table summarizes the attributes of the **CreatingDC** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[Virtual Machine Replication Broker Private Properties](virtual-machine-replication-broker-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**ResourceData**](virtual-machine-replication-brokers-resourcedata.md)
</dt> </dl>

 

 





