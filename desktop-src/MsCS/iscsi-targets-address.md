---
title: Address
description: Provides the address for the Internet Small Computer System Interface (iSCSI) target resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'F6FF377A-0840-4539-8C4D-199D1C845DEE'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Address Failover Cluster , for iSCSI Target private properties", "Address Failover Cluster"]
topic_type:
- apiref
api_name:
- Address
api_type:
- NA
---

# Address

Provides the address for the Internet Small Computer System Interface (iSCSI) target [resource](resources.md). The following table summarizes the attributes of the **Address** property.



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

[iSCSI Target Private Properties](iscsi-target-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





