---
title: VmId
description: Provides the GUID that identifies the Virtual Machine.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '2f464e74-af98-4003-8b0c-186fad57cb39'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["VmId Failover Cluster ,for virtual machine configurations", "VmId Failover Cluster"]
topic_type:
- apiref
api_name:
- VmId
api_type:
- NA
---

# VmId

Provides the **GUID** that identifies the Virtual Machine. The following table summarizes the attributes of the **VmId** property.



| Attribute            | Value                                                           |
|----------------------|-----------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string containing a **GUID**<br/> |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>              |
| Status<br/>    | Required<br/>                                             |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)<br/>                  |
| Minimum<br/>   | **NULL**<br/>                                             |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/>   |
| Default<br/>   | **NULL**<br/>                                             |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **VmId** can be set with the following example code.


```C++
WCHAR                szVmIdData[] = L"473d58fa-bda8-4fdc-a235-2b0ed19aa755";
CLUSPROP_SZ_DECLARE( VmIdValue, sizeof(szVmIdData) / sizeof(WCHAR) );

VmIdValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
VmIdValue.cbLength  = sizeof( szVmIdData );
StringCbCopy( VmIdValue.sz, VmIdValue.cbLength, szVmIdData );
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Configuration Private Properties](virtual-machine-configuration-private-properties.md)
</dt> <dt>

[**CLUSPROP\_SZ**](clusprop-sz.md)
</dt> <dt>

[**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md)
</dt> </dl>

 

 





