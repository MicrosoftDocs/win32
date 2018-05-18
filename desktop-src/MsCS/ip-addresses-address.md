---
title: Address
description: Provides the address for the IP Address resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '514eb8f9-55c7-411b-b6ec-8373903f8f17'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["Address Failover Cluster ,for IP addresses", "Address Failover Cluster"]
topic_type:
- apiref
api_name:
- Address
api_type:
- NA
---

# Address

Provides the address for the [IP Address](ip-address.md) [resource](resources.md). The following table summarizes the attributes of the **Address** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](clusprop-sz.md)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The data in the **Address** property must be formatted as *xxx*.*xxx*.*xxx*.*xxx* where *xxx* represents a decimal number between 0 and 255. The value 255.255.255.255 is not valid.

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Address** can be set with the following example code.


```C++
WCHAR                szAddressData[] = L"111.244.221.254";
CLUSPROP_SZ_DECLARE( AddressValue, 
                     sizeof(szAddressData) / sizeof(WCHAR) );

AddressValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
AddressValue.cbLength  = sizeof( szAddressData );
StringCbCopy( AddressValue.sz, 
              AddressValue.cbLength, 
              szAddressData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Enterprise, Windows Server 2008 Datacenter<br/> |



## See also

<dl> <dt>

[IP Address Private Properties](ip-address-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





