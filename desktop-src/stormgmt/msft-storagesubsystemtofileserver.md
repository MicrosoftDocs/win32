---
title: MSFT\_StorageSubSystemToFileServer class
description: Association between a MSFT\_StorageSubSystem and its MSFT\_FileServer.
ms.assetid: 64B3A267-4286-4D0D-A646-F001074180EE
keywords:
- MSFT_StorageSubSystemToFileServer class Windows Storage Management API
- MSFT_StorageSubSystemToFileServer class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_StorageSubSystemToFileServer
- MSFT_StorageSubSystemToFileServer.StorageSubSystem
- MSFT_StorageSubSystemToFileServer.FileServer
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

# MSFT\_StorageSubSystemToFileServer class

Association between a [**MSFT\_StorageSubSystem**](msft-storagesubsystem.md) and its [**MSFT\_FileServer**](msft-fileserver.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_StorageSubSystemToFileServer
{
  MSFT_StorageSubSystem REF StorageSubSystem;
  MSFT_FileServer       REF FileServer;
};
```

## Members

The **MSFT\_StorageSubSystemToFileServer** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_StorageSubSystemToFileServer** class has these properties.

<dl> <dt>

**FileServer**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_FileServer**](msft-fileserver.md)**
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

[**MSFT\_FileServer**](msft-fileserver.md)
</dt> <dt>

[**MSFT\_StorageSubSystem**](msft-storagesubsystem.md)
</dt> </dl>

 

 





