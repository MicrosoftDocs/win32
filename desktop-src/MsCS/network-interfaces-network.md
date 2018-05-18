---
title: Network
description: Provides the name of the network to which the network interface is connected. The following table summarizes the attributes of the Network property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'f6e097b1-bb1c-475c-9653-c800fe2c8246'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Network Failover Cluster ,for network interfaces", "Network Failover Cluster"]
topic_type:
- apiref
api_name:
- Network
api_type:
- NA
---

# Network

Provides the name of the [network](networks.md) to which the [network interface](network-interfaces.md) is connected. The following table summarizes the attributes of the **Network** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

Because the **Network** property is read-only, it cannot be changed using the [CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md) control code.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_NETINTERFACE\_SET\_COMMON\_PROPERTIES](clusctl-netinterface-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> </dl>

 

 





