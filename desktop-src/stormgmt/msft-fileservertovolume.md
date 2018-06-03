---
title: MSFT\_FileServerToVolume class
description: Association between MSFT\_FileServer and eligible MSFT\_Volume objects for file shares.
ms.assetid: B59D8A8D-6CDC-4D3C-AE7F-AA1F8A433364
keywords:
- MSFT_FileServerToVolume class Windows Storage Management API
- MSFT_FileServerToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_FileServerToVolume
- MSFT_FileServerToVolume.FileServer
- MSFT_FileServerToVolume.Volume
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

# MSFT\_FileServerToVolume class

Association between [**MSFT\_FileServer**](msft-fileserver.md) and eligible [**MSFT\_Volume**](msft-volume.md) objects for file shares.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_FileServerToVolume
{
  MSFT_FileServer REF FileServer;
  MSFT_Volume     REF Volume;
};
```

## Members

The **MSFT\_FileServerToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_FileServerToVolume** class has these properties.

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

[**MSFT\_FileServer**](msft-fileserver.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





