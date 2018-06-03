---
title: DnsName
description: The full DNS label associated with the Netname resource.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 7c8cec95-c9c5-4f71-9fcf-ab266034872e
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DnsName Failover Cluster , for Network Name properties
- DnsName Failover Cluster
topic_type:
- apiref
api_name:
- DnsName
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DnsName

The full DNS label associated with the Netname resource. The following table summarizes the attributes of the **DnsName** property.



| Attribute | Value                                                            |
|-----------|------------------------------------------------------------------|
| Data type | Null-terminated Unicode string                                   |
| Access    | [Read/write](read-write-properties.md)                          |
| Status    | Required                                                         |
| Structure | [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)                              |
| Maximum   | None (but see [Maximum Property Size](maximum-string-size.md).) |
| Default   | **NULL**                                                         |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare) macro creates a [**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **Name** can be set with the following example code.


```C++
WCHAR szDnsNameData[]  = L"myDNS";
CLUSPROP_SZ_DECLARE(     DnsNameValue, sizeof( szDnsNameData ) / sizeof( WCHAR ) );

DnsNameValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
DnsNameValue.cbLength  = sizeof( szDnsNameData );
StringCbCopy(            DnsNameValue.sz, 
                         DnsNameValue.cbLength, 
                         szDnsNameData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Cluster Name Private Properties](network-name-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/previous-versions/windows/desktop/api/ClusAPI/nf-clusapi-clusprop_sz_declare)
</dt> </dl>

 

 





