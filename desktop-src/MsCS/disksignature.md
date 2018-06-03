---
title: DiskSignature
description: Specifies the disk signature for the Physical Disk resource formatted with a Master Boot Record (MBR) partitioning scheme.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 6c841b63-6856-4ddc-b0d9-7eefece85b8d
ms.prod: windows-server-dev
ms.technology: failover-clustering
ms.tgt_platform: multiple
keywords:
- DiskSignature Failover Cluster , for Physical Disk private properties
- DiskSignature Failover Cluster
topic_type:
- apiref
api_name:
- DiskSignature
api_type:
- NA
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# DiskSignature

Specifies the disk signature for the [Physical Disk](physical-disk.md) resource formatted with a Master Boot Record (MBR) partitioning scheme. The [**DiskIdType**](diskidtype.md) property of the [Physical Disk](physical-disk.md) resource has a value of **PARTITION\_STYLE\_MBR** (0) for MBR partitioned disks. The following table summarizes the attributes of the **DiskSignature** property.



| Attribute            | Value                                                |
|----------------------|------------------------------------------------------|
| Data type<br/> | **DWORD**<br/>                                 |
| Access<br/>    | [Read/write](read-write-properties.md)<br/>   |
| Status<br/>    | Required<br/>                                  |
| Structure<br/> | [**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)<br/> |
| Minimum<br/>   | 0<br/>                                         |
| Maximum<br/>   | 0xFFFFFFFF<br/>                                |
| Default<br/>   | 0<br/>                                         |



 

## Examples

The property value portion of a [property list](property-lists.md) entry for [**DiskRunChkDsk**](diskrunchkdsk.md) can be set with the following example code.


```C++
DWORD          DiskSignatureData = 0;
CLUSPROP_DWORD DiskSignatureValue;

DiskSignatureValue.Syntax.dw = CLUSPROP_SYNTAX_LIST_VALUE_DWORD;
DiskSignatureValue.cbLength  = sizeof(DWORD);
DiskSignatureValue.dw        = DiskSignatureData;
```



## Requirements



|                                     |                                                                           |
|-------------------------------------|---------------------------------------------------------------------------|
| Minimum supported client<br/> | None supported<br/>                                                 |
| Minimum supported server<br/> | Windows Server 2008 Datacenter, Windows Server 2008 Enterprise<br/> |



## See also

<dl> <dt>

[Physical Disk Private Properties](physical-disk-private-properties.md)
</dt> <dt>

[**CLUSPROP\_DWORD**](/previous-versions/windows/desktop/api/ClusAPI/)
</dt> <dt>

[**Signature**](physical-disks-signature.md)
</dt> <dt>

[**DiskIdGuid**](diskidguid.md)
</dt> </dl>

 

 





