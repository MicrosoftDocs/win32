---
title: MSFT\_StoragePoolToVirtualDisk class
description: Association between StoragePool and VirtualDisk.
ms.assetid: 623782e9-11c8-4344-8eae-ea6058e000c8
keywords:
- MSFT_StoragePoolToVirtualDisk class Windows Storage Management API
- MSFT_StoragePoolToVirtualDisk class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePoolToVirtualDisk
- MSFT_StoragePoolToVirtualDisk.StoragePool
- MSFT_StoragePoolToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MSFT\_StoragePoolToVirtualDisk class

Association between [**StoragePool**](msft-storagepool.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToVirtualDisk
{
  MSFT_StoragePool REF StoragePool;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_StoragePoolToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToVirtualDisk** class has these properties.

<dl> <dt>

**StoragePool**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StoragePool**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**VirtualDisk**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_VirtualDisk**
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

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





