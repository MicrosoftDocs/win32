---
title: MulticastAddress
description: This property is not supported.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: da50f983-bf3c-4fcf-9168-f74c7a35bdb7
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- MulticastAddress Failover Cluster ,for networks
- MulticastAddress Failover Cluster
topic_type:
- apiref
api_name:
- MulticastAddress
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MulticastAddress

\[The **MulticastAddress** property is no longer available for use as of Windows Server 2012.\]

This property is not supported.

**Windows Server 2003:  **

Provides the Class D IPv4 multicast address used for heartbeat multicasting on the [network](networks.md). The following table summarizes the attributes of the **MulticastAddress** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | Varies                                                           |



 

## Remarks

Class D IPv4 addresses are in the range 224.0.0.0 to 239.255.255.255.

If the string is not a Class D IPv4 address, the current multicast configuration is deleted and the cluster attempts to obtain a new address. This means that the contents of the **MulticastAddress**, [**MulticastConfigType**](networks-multicastconfigtype.md), [**MulticastLeaseExpires**](networks-multicastleaseexpires.md), [**MulticastLeaseObtained**](networks-multicastleaseobtained.md), [**MulticastLeaseRequestId**](networks-multicastleaserequestid.md), and [**MulticastLeaseServer**](networks-multicastleaseserver.md) properties are erased. The cluster service does not report an error when this occurs.

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **MulticastAddress** can be set with the following example code:


```C++
WCHAR                szMulticastAddressData[] = L"239.255.0.0";
CLUSPROP_SZ_DECLARE( MulticastAddressValue, 
                     sizeof(szMulticastAddressData) / sizeof(WCHAR) );

MulticastAddressValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
MulticastAddressValue.cbLength  = sizeof( szMulticastAddressData );
StringCbCopy( MulticastAddressValue.sz, 
              MulticastAddressValue.cbLength, 
              szMulticastAddressData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |
| End of server support<br/>    | Windows Server 2003 Datacenter, Windows Server 2003 Enterprise<br/> |



## See also

<dl> <dt>

[**MulticastAddressRangeLower**](networks-multicastaddressrangelower.md)
</dt> <dt>

[**MulticastAddressRangeUpper**](networks-multicastaddressrangeupper.md)
</dt> <dt>

[**MulticastConfigType**](networks-multicastconfigtype.md)
</dt> <dt>

[**MulticastDisabled**](networks-multicastdisabled.md)
</dt> </dl>

 

 





