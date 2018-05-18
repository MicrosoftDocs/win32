---
title: MSFT\_StorageNodeToVirtualDisk class
description: Association between a storage node and a virtual disk.
ms.assetid: '7A193FBD-6435-4CF3-86D3-FAEEB755C21F'
keywords: ["MSFT_StorageNodeToVirtualDisk class Windows Storage Management API", "MSFT_StorageNodeToVirtualDisk class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageNodeToVirtualDisk
- MSFT_StorageNodeToVirtualDisk.StorageNode
- MSFT_StorageNodeToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageNodeToVirtualDisk class

Association between a storage node and a virtual disk.

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageNodeToVirtualDisk
{
  MSFT_StorageNode REF StorageNode;
  MSFT_VirtualDisk REF VirtualDisk;
};
```

## Members

The **MSFT\_StorageNodeToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageNodeToVirtualDisk** class has these properties.

<dl> <dt>

**StorageNode**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageNode**](msft-storagenode.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**VirtualDisk**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_VirtualDisk**](msft-virtualdisk.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



 

 





