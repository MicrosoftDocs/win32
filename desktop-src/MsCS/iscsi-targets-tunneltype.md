---
title: TunnelType
description: Describes the type of tunnel used, if any, for an Internet Small Computer System Interface (iSCSI) target. The following table summarizes the attributes of the TunnelType property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: A115C8C3-A4A6-45EE-BA80-3C5EA3353994
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- TunnelType Failover Cluster , for iSCSI Target private properties
- TunnelType Failover Cluster
topic_type:
- apiref
api_name:
- TunnelType
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# TunnelType

Describes the type of tunnel used, if any, for an Internet Small Computer System Interface (iSCSI) target. The following table summarizes the attributes of the **TunnelType** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | ""                                                               |



 

The **TunnelType** property can be set to one of the following values.



| Value    | Description                                                                                  |
|----------|----------------------------------------------------------------------------------------------|
| ""       | The tunnel type is unspecified.<br/>                                                   |
| "ISATAP" | The tunnel is an Intra-Site Automatic Tunnel Addressing Protocol (ISATAP) tunnel.<br/> |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for **TunnelType** can be set with the following example code.


```C++
WCHAR                szTunnelTypeData[] = L"ISATAP";
CLUSPROP_SZ_DECLARE( TunnelTypeValue, 
                     sizeof( szTunnelTypeData ) / sizeof( WCHAR ) );

TunnelTypeValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
TunnelTypeValue.cbLength  = sizeof( szTunnelTypeData );
StringCbCopy( TunnelTypeValue.sz, 
              TunnelTypeValue.cbLength, 
              szTunnelTypeData );
```



## Requirements



|                                     |                                |
|-------------------------------------|--------------------------------|
| Minimum supported client<br/> | None supported<br/>      |
| Minimum supported server<br/> | Windows Server 2012<br/> |



## See also

<dl> <dt>

[iSCSI Target Private Properties](iscsi-target-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





