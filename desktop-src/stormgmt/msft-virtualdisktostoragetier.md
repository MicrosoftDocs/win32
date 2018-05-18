---
title: MSFT\_VirtualDiskToStorageTier class
description: Association between a virtual disk and a storage tier.
ms.assetid: '363F92E4-D7D1-415F-8565-E1A41B57CF48'
keywords: ["MSFT_VirtualDiskToStorageTier class Windows Storage Management API", "MSFT_VirtualDiskToStorageTier class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_VirtualDiskToStorageTier
- MSFT_VirtualDiskToStorageTier.VirtualDisk
- MSFT_VirtualDiskToStorageTier.StorageTier
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_VirtualDiskToStorageTier class

Association between a virtual disk and a storage tier.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VirtualDiskToStorageTier
{
  MSFT_VirtualDisk REF VirtualDisk;
  MSFT_StorageTier REF StorageTier;
};
```

## Members

The **MSFT\_VirtualDiskToStorageTier** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VirtualDiskToStorageTier** class has these properties.

<dl> <dt>

**StorageTier**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageTier**](msft-storagetier.md)**
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



 

 





