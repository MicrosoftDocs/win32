---
title: MSFT\_StorageSubSystemToPartition class
description: Association between MSFT\_StorageSubSystem and MSFT\_Partition.
ms.assetid: 57565912-703D-4213-A53A-3A9A5D5EF46F
keywords:
- MSFT_StorageSubSystemToPartition class Windows Storage Management API
- MSFT_StorageSubSystemToPartition class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToPartition
- MSFT_StorageSubSystemToPartition.StorageSubSystem
- MSFT_StorageSubSystemToPartition.Partition
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

# MSFT\_StorageSubSystemToPartition class

Association between [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_Partition**](msft-partition.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToPartition
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_Partition        REF Partition;
};
```

## Members

The **MSFT\_StorageSubSystemToPartition** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToPartition** class has these properties.

<dl> <dt>

**Partition**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Partition**](msft-partition.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_Partition**](msft-partition.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





