---
title: Address
description: Provides the address for the entire network or subnet. The following table summarizes the attributes of the Address property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'ae903187-d724-4b39-a938-dcea8481037e'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Address Failover Cluster ,for networks", "Address Failover Cluster"]
topic_type:
- apiref
api_name:
- Address
api_type:
- NA
---

# Address

Provides the address for the entire [network](networks.md) or subnet. The following table summarizes the attributes of the **Address** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The **Address** property does not specify the address of an individual [node](nodes.md).

The data is formatted as *xxx*.*xxx*.*xxx*.*xxx* where *xxx* represents a decimal number between 0 and 255.

Because the **Address** property is read-only, it cannot be changed using the [CLUSCTL\_NETWORK\_SET\_COMMON\_PROPERTIES](clusctl-network-set-common-properties.md) control code.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[CLUSCTL\_NETWORK\_SET\_COMMON\_PROPERTIES](clusctl-network-set-common-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> </dl>

 

 





