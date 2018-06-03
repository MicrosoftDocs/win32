---
title: MulticastAddressRangeLower
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7461c202-5087-4bd3-bb5d-1fd1e2e8f75f
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MulticastAddressRangeLower Failover Cluster ,for networks
- MulticastAddressRangeLower Failover Cluster
topic_type:
- apiref
api_name:
- MulticastAddressRangeLower
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MulticastAddressRangeLower

\[The **MulticastAddressRangeLower** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Specifies the lower bound of a range from which a multicast address should be chosen if no Multicast Address Dynamic Client Allocation Protocol (MADCAP) server can be found. The following table summarizes the attributes of the **MulticastAddressRangeLower** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Optional                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | 239.255.0.0                                                      |



 

## Remarks

Class D IPv4 addresses are in the range 224.0.0.0 to 239.255.255.255.

If either the **MulticastAddressRangeLower** or [**MulticastAddressRangeUpper**](networks-multicastaddressrangeupper.md) property is not a Class D IPv4 address, the value of both properties is ignored and the default value is used. The cluster service does not report an error when this occurs.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **MulticastAddressRangeLower** can be set with the following example code.


```C++
WCHAR                szMulticastAddressRangeLowerData[] = L"239.255.0.0";
CLUSPROP_SZ_DECLARE( MulticastAddressRangeLowerValue, 
                     sizeof(szMulticastAddressRangeLowerData) / sizeof(WCHAR) );

MulticastAddressRangeLowerValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
MulticastAddressRangeLowerValue.cbLength  = sizeof(szMulticastAddressRangeLowerData);
StringCbCopy( MulticastAddressRangeLowerValue.sz, 
              MulticastAddressRangeLowerValue.cbLength, 
              szMulticastAddressRangeLowerData );
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

[**MulticastAddressRangeUpper**](networks-multicastaddressrangeupper.md)
</dt> <dt>

[**MulticastConfigType**](networks-multicastconfigtype.md)
</dt> <dt>

[**MulticastDisabled**](networks-multicastdisabled.md)
</dt> </dl>

 

 





