---
title: MSFT\_StorageSubSystemToVirtualDisk class
description: Association between StorageSubSystem and VirtualDisk.
ms.assetid: '2fb7838f-e8c7-4fb4-83f1-4746a2bb3642'
keywords: ["MSFT_StorageSubSystemToVirtualDisk class Windows Storage Management API", "MSFT_StorageSubSystemToVirtualDisk class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToVirtualDisk
- MSFT_StorageSubSystemToVirtualDisk.StorageSubSystem
- MSFT_StorageSubSystemToVirtualDisk.VirtualDisk
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToVirtualDisk class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**VirtualDisk**](msft-virtualdisk.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToVirtualDisk
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_VirtualDisk      REF VirtualDisk;
};
```

## Members

The **MSFT\_StorageSubSystemToVirtualDisk** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToVirtualDisk** class has these properties.

<dl> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageSubSystem**
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
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> <dt>

[**MSFT\_VirtualDisk**](msft-virtualdisk.md)
</dt> </dl>

 

 





