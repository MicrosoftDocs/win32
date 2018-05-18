---
title: MSFT\_StoragePoolToStorageTier class
description: Association between a storage pool and storage tiers in that pool.
ms.assetid: '39B3D9AA-56FA-49ED-8EF2-E85947F382E0'
keywords: ["MSFT_StoragePoolToStorageTier class Windows Storage Management API", "MSFT_StoragePoolToStorageTier class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StoragePoolToStorageTier
- MSFT_StoragePoolToStorageTier.StoragePool
- MSFT_StoragePoolToStorageTier.StorageTier
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StoragePoolToStorageTier class

Association between a storage pool and storage tiers in that pool.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToStorageTier
{
  MSFT_StoragePool REF StoragePool;
  MSFT_StorageTier REF StorageTier;
};
```

## Members

The **MSFT\_StoragePoolToStorageTier** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToStorageTier** class has these properties.

<dl> <dt>

**StoragePool**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StoragePool**](msft-storagepool.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

</dd> <dt>

**StorageTier**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageTier**](msft-storagetier.md)**
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



 

 





