---
title: MSFT\_DiskToPartition class
description: Association between Disk and Partition.
ms.assetid: 6d293eea-3c40-414d-bb05-c59a37ccb1e7
keywords:
- MSFT_DiskToPartition class Windows Storage Management API
- MSFT_DiskToPartition class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_DiskToPartition
- MSFT_DiskToPartition.Disk
- MSFT_DiskToPartition.Partition
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MSFT\_DiskToPartition class

Association between [**Disk**](msft-disk.md) and [**Partition**](msft-partition.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_DiskToPartition
{
  MSFT_Disk      REF Disk;
  MSFT_Partition REF Partition;
};
```

## Members

The **MSFT\_DiskToPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DiskToPartition** class has these properties.

<dl> <dt>

**Disk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Disk**](msft-disk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**Partition**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Partition**](msft-partition.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Disk**](msft-disk.md)
</dt> <dt>

[**MSFT\_Partition**](msft-partition.md)
</dt> </dl>

 

 





