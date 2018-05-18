---
title: VmStoreRootPath
description: Provides the path that specifies the location of the virtual machine (VM) configuration and data.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c5cad1e2-7471-4f79-bbc5-38372186f418'
ms.prod: 'windows-server-dev'
ms.technology: 'failover-clustering'
ms.tgt_platform: multiple
keywords: ["VmStoreRootPath Failover Cluster ,for virtual machine configurations", "VmStoreRootPath Failover Cluster"]
topic_type:
- apiref
api_name:
- VmStoreRootPath
api_type:
- NA
---

# VmStoreRootPath

Provides the path that specifies the location of the virtual machine (VM) configuration and data. The following table summarizes the attributes of the **VmStoreRootPath** property.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | Null-terminated Unicode string<br/>                     |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>            |
| Status<br/>    | Required<br/>                                           |
| Structure<br/> | [**CLUSPROP\_SZ**](clusprop-sz.md)<br/>                |
| Minimum<br/>   | **NULL**<br/>                                           |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/> |
| Default<br/>   | **NULL**<br/>                                           |



 

## Remarks

The [**CLUSPROP\_SZ\_DECLARE**](clusprop-sz-declare.md) macro creates a [**CLUSPROP\_SZ**](clusprop-sz.md) structure with an array of the correct size.

## Examples

The property value portion of a [property list](property-lists.md) entry for **VmStoreRootPath** can be set with the following example code.


```C++
WCHAR                szVmStoreRootPathData[] = L"C:\\VM\\VM2\\Data";
CLUSPROP_SZ_DECLARE( VmStoreRootPathValue, sizeof(szVmStoreRootPathData) / sizeof(WCHAR) );

VmStoreRootPathValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_SZ;
VmStoreRootPathValue.cbLength  = sizeof( szVmStoreRootPathData );
StringCbCopy( VmStoreRootPathValue.sz, VmStoreRootPathValue.cbLength, szVmStoreRootPathData );
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

 

 





