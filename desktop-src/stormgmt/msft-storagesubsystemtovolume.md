---
title: MSFT\_StorageSubSystemToVolume class
description: Association between an MSFT\_StorageSubSystem and MSFT\_Volume.
ms.assetid: EA89DCE7-39BE-4BEC-9C27-2C267595010D
keywords:
- MSFT_StorageSubSystemToVolume class Windows Storage Management API
- MSFT_StorageSubSystemToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToVolume
- MSFT_StorageSubSystemToVolume.StorageSubSystem
- MSFT_StorageSubSystemToVolume.Volume
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

# MSFT\_StorageSubSystemToVolume class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and [**MSFT\_Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToVolume
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_Volume           REF Volume;
};
```

## Members

The **MSFT\_StorageSubSystemToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToVolume** class has these properties.

<dl> <dt>

**StorageSubSystem**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)**
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

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





