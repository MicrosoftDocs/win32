---
title: MSFT\_StorageSubSystemToStorageFaultDomain class
description: Association between MSFT\_StorageSubSystem and MSFT\_StorageFaultDomain.
ms.assetid: '6A53CF61-FFD7-4657-8B88-BD97BC80C075'
keywords: ["MSFT_StorageSubSystemToStorageFaultDomain class Windows Storage Management API", "MSFT_StorageSubSystemToStorageFaultDomain class Windows Storage Management API , described"]
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToStorageFaultDomain
- MSFT_StorageSubSystemToStorageFaultDomain.StorageSubSystem
- MSFT_StorageSubSystemToStorageFaultDomain.StorageFaultDomain
api_location:
- Root\Microsoft\Windows\Storage
api_type:
- Schema
---

# MSFT\_StorageSubSystemToStorageFaultDomain class

Association between [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md).

The following syntax is simplified from MOF code and includes all inherited properties.

## Syntax

``` syntax
class MSFT_StorageSubSystemToStorageFaultDomain
{
  MSFT_StorageSubSystem   REF StorageSubSystem;
  MSFT_StorageFaultDomain REF StorageFaultDomain;
};
```

## Members

The **MSFT\_StorageSubSystemToStorageFaultDomain** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToStorageFaultDomain** class has these properties.

<dl> <dt>

**StorageFaultDomain**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)**
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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_StorageFaultDomain**](msft-storagefaultdomain.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





