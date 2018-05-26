---
title: MSFT\_VolumeToFileShare class
description: Association between a MSFT\_Volume and its MSFT\_FileShare objects.
ms.assetid: 50CF46C1-F67C-436C-9E71-7C7DFE18BDA1
keywords:
- MSFT_VolumeToFileShare class Windows Storage Management API
- MSFT_VolumeToFileShare class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_VolumeToFileShare
- MSFT_VolumeToFileShare.Volume
- MSFT_VolumeToFileShare.FileShare
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

# MSFT\_VolumeToFileShare class

Association between a [**MSFT\_Volume**](msft-volume.md) and its [**MSFT\_FileShare**](msft-fileshare.md) objects.

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_VolumeToFileShare
{
  MSFT_Volume    REF Volume;
  MSFT_FileShare REF FileShare;
};
```

## Members

The **MSFT\_VolumeToFileShare** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_VolumeToFileShare** class has these properties.

<dl> <dt>

**FileShare**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_FileShare**](msft-fileshareaccesscontrolentry.md)**
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

[**MSFT\_FileShare**](msft-fileshare.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





