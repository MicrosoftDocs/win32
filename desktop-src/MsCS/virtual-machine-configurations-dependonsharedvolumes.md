---
title: DependsOnSharedVolumes
description: Used by the virtual machine (VM) configuration resource type to store information about the shared volumes that are used by the VM.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 1e8cfc1f-af38-48b8-91f8-291f0c0f7b74
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DependOnSharedVolumes Failover Cluster ,for virtual machine configurations
- DependsOnSharedVolumes Failover Cluster
topic_type:
- apiref
api_name:
- DependsOnSharedVolumes
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DependsOnSharedVolumes

Used by the virtual machine (VM) configuration resource type to store information about the shared volumes that are used by the VM. The following table summarizes the attributes of the **DependsOnSharedVolumes** property.



| Attribute            | Value                                                         |
|----------------------|---------------------------------------------------------------|
| Data type<br/> | MULTI-SZ<br/>                                           |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>            |
| Status<br/>    | Required<br/>                                           |
| Structure<br/> | [**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)<br/>   |
| Minimum<br/>   | **NULL**<br/>                                           |
| Maximum<br/>   | see [Maximum String Size](maximum-string-size.md)<br/> |
| Default<br/>   | **NULL**<br/>                                           |



 

## Remarks

The format of each string within the [**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz) structure is the [resource identifier](resource-identifiers.md) of the cluster shared volume, a colon ':', and the offset (in decimal) of the volume (partition) used by the VM.

## Examples

The property value portion of a [property list](property-lists.md) entry for **DependsOnSharedVolumes** can be set with the following example code.


```C++
WCHAR szDOSVData[] = L"df1d8a5d-7d3c-4de2-bcdc-9bf5f38fa3d3:135266304\0"
                     L"2936f4ed-f55d-4fa9-bec2-108469342c6a:129761280\0";

CLUSPROP_SZ_DECLARE( DOSVValue, sizeof(szDOSVData) / sizeof(WCHAR) );

DOSVValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_MULTI_SZ;

DOSVValue.cbLength  = sizeof(szDOSVData);

CopyMemory( (PVOID)DOSVValue.sz, (PVOID)szDOSVData, sizeof(szDOSVData) );
```



## Requirements



|                                     |                                                                                 |
|-------------------------------------|---------------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                       |
| Minimum supported server<br/> | Windows Server 2008 R2 Datacenter, Windows Server 2008 R2 Enterprise<br/> |



## See also

<dl> <dt>

[Virtual Machine Configuration Private Properties](virtual-machine-configuration-private-properties.md)
</dt> <dt>

[**CLUSPROP\_MULTI\_SZ**](/previous-versions/windows/desktop/api/ClusAPI/ns-clusapi-clusprop_sz)
</dt> </dl>

 

 





