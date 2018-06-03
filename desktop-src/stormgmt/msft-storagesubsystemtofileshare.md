---
title: MSFT\_StorageSubSystemToFileShare class
description: Association between an MSFT\_StorageSubSystem and its MSFT\_FileShare objects.
ms.assetid: 4BED3526-1DAA-4A20-97B5-BBC558FD10CF
keywords:
- MSFT_StorageSubSystemToFileShare class Windows Storage Management API
- MSFT_StorageSubSystemToFileShare class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToFileShare
- MSFT_StorageSubSystemToFileShare.StorageSubSystem
- MSFT_StorageSubSystemToFileShare.FileShare
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

# MSFT\_StorageSubSystemToFileShare class

Association between an [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and its [**MSFT\_FileShare**](msft-fileshare.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToFileShare
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_FileShare        REF FileShare;
};
```

## Members

The **MSFT\_StorageSubSystemToFileShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToFileShare** class has these properties.

<dl> <dt>

**FileShare**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_FileShare**](msft-fileshare.md)**
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
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                               |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_FileShare**](msft-fileshare.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





