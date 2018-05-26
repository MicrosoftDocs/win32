---
title: MulticastAddressRangeUpper
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 521ec324-9bb2-4c73-8c2a-f47bc6c0878c
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MulticastAddressRangeUpper Failover Cluster ,for networks
- MulticastAddressRangeUpper Failover Cluster
topic_type:
- apiref
api_name:
- MulticastAddressRangeUpper
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# MulticastAddressRangeUpper

\[The **MulticastAddressRangeUpper** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Specifies the upper bound of a range from which a multicast address should be chosen if no Multicast Address Dynamic Client Allocation Protocol (MADCAP) server can be found. The following table summarizes the attributes of the **MulticastAddressRangeUpper** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 239.255.254.255                                                  |



 

## Remarks

Class D IPv4 addresses are in the range 224.0.0.0 to 239.255.255.255.

If either the **MulticastAddressRangeUpper** or [**MulticastAddressRangeLower**](networks-multicastaddressrangelower.md) property is not a Class D IPv4 address, the value of both properties is ignored and the default value is used. The cluster service does not report an error when this occurs.

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **MulticastAddressRangeUpper** can be set with the following example code.


```C++
WCHAR                szMulticastAddressRangeUpperData[] = L"239.255.254.255";
CLUSPROP_SZ_DECLARE( MulticastAddressRangeUpperValue, 
                     sizeof(szMulticastAddressRangeUpperData) / sizeof(WCHAR) );

MulticastAddressRangeUpperValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
MulticastAddressRangeUpperValue.cbLength  = sizeof( szMulticastAddressRangeUpperData );
StringCbCopy( MulticastAddressRangeUpperValue.sz, 
              MulticastAddressRangeUpperValue.cbLength, 
              szMulticastAddressRangeUpperData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**MulticastAddress**](networks-multicastaddress.md)
</dt> <dt>

[**MulticastAddressRangeLower**](networks-multicastaddressrangelower.md)
</dt> <dt>

[**MulticastConfigType**](networks-multicastconfigtype.md)
</dt> <dt>

[**MulticastDisabled**](networks-multicastdisabled.md)
</dt> </dl>

 

 





