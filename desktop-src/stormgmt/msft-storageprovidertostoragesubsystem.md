---
title: MSFT\_StorageProviderToStorageSubSystem class
description: Association between StorageProvider and StorageSubSystem.
ms.assetid: '0be0f434-3d17-4075-86db-58b11ef15544'
keywords: ["MSFT_StorageProviderToStorageSubSystem class Windows Storage Management API", "MSFT_StorageProviderToStorageSubSystem class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageProviderToStorageSubSystem
- MSFT_StorageProviderToStorageSubSystem.StorageProvider
- MSFT_StorageProviderToStorageSubSystem.StorageSubSystem
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageProviderToStorageSubSystem class

Association between [**StorageProvider**](msft-storageprovider.md) and [**StorageSubSystem**](msft-storagesubsystem.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageProviderToStorageSubSystem
{
  MSFT_StorageProvider  REF StorageProvider;
  MSFT_StorageSubSystem REF StorageSubSystem;
};
```

## Members

The **MSFT\_StorageProviderToStorageSubSystem** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageProviderToStorageSubSystem** class has these properties.

<dl> <dt>

**StorageProvider**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageProvider**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The storage provider.

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **MSFT\_StorageSubSystem**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: **Key**
</dt> </dl>

The storage subsystem.

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

[**MSFT\_StorageProvider**](msft-storageprovider.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





