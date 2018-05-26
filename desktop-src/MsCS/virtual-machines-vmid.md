---
title: VmId
description: Provides the GUID that identifies the Virtual Machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: f410b1d1-68b1-4997-99ed-3cf1bd11c062
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- VmId Failover Cluster ,for virtual machines
- VmId Failover Cluster
topic_type:
- apiref
api_name:
- VmId
api_type:
- NA
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# VmId

Provides the **GUID** that identifies the Virtual Machine. The following table summarizes the attributes of the **VmId** property.



| Attribute            | Value                                                           |
|----------------------|-----------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string containing a **GUID**<br/> |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>              |
| Status<br/>    | Required<br/>                                             |
| Structure<br/> | [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)<br/>                  |
| Minimum<br/>   | **NULL**<br/>                                             |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/>   |
| Default<br/>   | **NULL**<br/>                                             |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master) macro creates a [**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **VmId** can be set with the following example code.


```C++
WCHAR                szVmIdData[] = L"30f163fa-f38d-45b5-b163-8f9c8071c72d";
CLUSPROP_SZ_DECLARE( VmIdValue, sizeof(szVmIdData) / sizeof(WCHAR) );

VmIdValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
VmIdValue.cbLength  = sizeof( szVmIdData );
StringCbCopy( VmIdValue.sz, VmIdValue.cbLength, szVmIdData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Private Properties](virtual-machine-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](/windows/previous-versions/ClusAPI/?branch=master)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](/windows/previous-versions/ClusAPI/nf-clusapi-clusprop_sz_declare?branch=master)
</dt> </dl>

 

 





