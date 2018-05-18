---
title: ResourceData
description: Stores the virtual computer object's encrypted password if the RequireKerberos property for Network Names is set to 1.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '36b97940-8fdc-49f7-bcc3-d0c954b5c797'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["ResourceData Failover Cluster ,for network names", "ResourceData Failover Cluster"]
topic_type:
- apiref
api_name:
- ResourceData
api_type:
- NA
---

# ResourceData

Stores the virtual computer object's encrypted password if the [**RequireKerberos**](network-names-requirekerberos.md) property for [Network Names](network-name.md) is set to 1. The following table summarizes the attributes of the **ResourceData** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | byte array                                                       |
| Access    | [Read-only](read-only-properties.md)                            |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_BINARY**](clusprop-binary.md)                      |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 0                                                                |



 

## Remarks

Access to **ResourceData** is limited to the local administrator, system, and creator owner.

## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CreatingDC**](network-names-creatingdc.md)
</dt> <dt>

[**RequireDNS**](network-names-requiredns.md)
</dt> <dt>

[**RequireKerberos**](network-names-requirekerberos.md)
</dt> </dl>

 

 





