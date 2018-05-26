---
title: SubnetMask
description: Describes the subnet mask to be applied for routing for the IP address.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 413d0d3c-1bb9-4570-ac18-23644f5e7804
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- SubnetMask Failover Cluster ,for IP addresses
- SubnetMask Failover Cluster
topic_type:
- apiref
api_name:
- SubnetMask
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# SubnetMask

Describes the subnet mask to be applied for routing for the [IP address](ip-address.md). The following table summarizes the attributes of the **SubnetMask** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The data in the **SubnetMask** property must be formatted as *xxx*.*xxx*.*xxx*.*xxx* where *xxx* represents a decimal number between 0 and 255. The value 255.255.255.255 is not valid.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **SubnetMask** can be set with the following example code.


```C++
WCHAR                szSubnetMaskData[] = L"255.255.0.0";
CLUSPROP_SZ_DECLARE( SubnetMaskValue, 
                     sizeof( szSubnetMaskData ) / sizeof( WCHAR ) );

SubnetMaskValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
SubnetMaskValue.cbLength  = sizeof( szSubnetMaskData );
StringCbCopy( SubnetMaskValue.sz, 
              SubnetMaskValue.cbLength, 
              szSubnetMaskData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[IP Address Private Properties](ip-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





