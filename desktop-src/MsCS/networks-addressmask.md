---
title: AddressMask
description: Provides the mask that distinguishes the network and host portions of an address. The following table summarizes the attributes of the AddressMask property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '0e58bbaa-3c93-495b-b283-2c0b584119d6'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["AddressMask Failover Cluster ,for networks", "AddressMask Failover Cluster"]
topic_type:
- apiref
api_name:
- AddressMask
api_type:
- NA
---

# AddressMask

Provides the mask that distinguishes the [network](networks.md) and host portions of an address. The following table summarizes the attributes of the **AddressMask** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read-only](read-only-properties.md)                            |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The data in the **AddressMask** property is formatted as *xxx*.*xxx*.*xxx*.*xxx* where *xxx* represents a decimal number between 0 and 255.

Because the **AddressMask** property is read-only, it cannot be changed using the [CLUSCTL\_NETWORK\_SET\_COMMON\_PROPERTIES](clusctl-network-set-common-properties.md) control code.

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

 

 





