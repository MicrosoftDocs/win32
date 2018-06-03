---
title: MSFT\_StorageSubSystemToStorageEnclosure class
description: Association between StorageSubSystem and StorageEnclosure.
ms.assetid: 787A2FC9-A215-4F76-936E-709D5BC0FD30
keywords:
- MSFT_StorageSubSystemToStorageEnclosure class Windows Storage Management API
- MSFT_StorageSubSystemToStorageEnclosure class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToStorageEnclosure
- MSFT_StorageSubSystemToStorageEnclosure.StorageSubSystem
- MSFT_StorageSubSystemToStorageEnclosure.StorageEnclosure
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

# MSFT\_StorageSubSystemToStorageEnclosure class

Association between [**StorageSubSystem**](msft-storagesubsystem.md) and [**StorageEnclosure**](msft-storageenclosure.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToStorageEnclosure
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_StorageEnclosure REF StorageEnclosure;
};
```

## Members

The **MSFT\_StorageSubSystemToStorageEnclosure** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStorageEnclosure** class has these properties.

<dl> <dt>

**StorageEnclosure**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                   |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> <dt>

[**MSFT\_StorageEnclosure**](msft-storageenclosure.md)
</dt> </dl>

 

 





