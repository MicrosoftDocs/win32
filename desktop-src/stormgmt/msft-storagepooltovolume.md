---
title: MSFT\_StoragePoolToVolume class
description: Association between MSFT\_StoragePool and MSFT\_Volume. This association should only exist for concrete pools.
ms.assetid: E8A036AD-47E1-47CF-A382-E7FC4DB671CB
keywords:
- MSFT_StoragePoolToVolume class Windows Storage Management API
- MSFT_StoragePoolToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StoragePoolToVolume
- MSFT_StoragePoolToVolume.StoragePool
- MSFT_StoragePoolToVolume.Volume
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

# MSFT\_StoragePoolToVolume class

Association between [**MSFT\_StoragePool**](msft-storagepool.md) and [**MSFT\_Volume**](msft-volume.md). This association should only exist for concrete pools.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StoragePoolToVolume
{
  MSFT_StoragePool REF StoragePool;
  MSFT_Volume      REF Volume;
};
```

## Members

The **MSFT\_StoragePoolToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StoragePoolToVolume** class has these properties.

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

**Volume**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Volume**](msft-volume.md)**
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

[**MSFT\_StoragePool**](msft-storagepool.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





