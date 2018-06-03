---
title: MSFT\_DiskImageToVolume class
description: Association between DiskImage and Volume.
ms.assetid: A8E35879-C5E8-4FEA-A34E-397A0D99D6B9
keywords:
- MSFT_DiskImageToVolume class Windows Storage Management API
- MSFT_DiskImageToVolume class Windows Storage Management API , described
topic_type:
- apiref
api_name:
- MSFT_DiskImageToVolume
- MSFT_DiskImageToVolume.DiskImage
- MSFT_DiskImageToVolume.Volume
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

# MSFT\_DiskImageToVolume class

Association between [**DiskImage**](msft-diskimage.md) and [**Volume**](msft-volume.md).

The following syntax is simplified from Managed Object Format (MOF) code.

## Syntax

``` syntax
[Association]
class MSFT_DiskImageToVolume
{
  MSFT_DiskImage REF DiskImage;
  MSFT_Volume    REF Volume;
};
```

## Members

The **MSFT\_DiskImageToVolume** class has these types of members:

-   [Properties](#properties)

### Properties

The **MSFT\_DiskImageToVolume** class has these properties.

<dl> <dt>

**DiskImage**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_DiskImage**](msft-diskimage.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> <dt>

**Volume**
</dt> <dd> <dl> <dt>

Data type: **[**MSFT\_Volume**](msft-volume.md)**
</dt> <dt>

Access type: Read-only
</dt> <dt>

Qualifiers: [**Key**](https://msdn.microsoft.com/library/aa393650)
</dt> </dl>

</dd> </dl>

## Requirements



|                                     |                                                                                           |
|-------------------------------------|-------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps only\]<br/>                                      |
| Namespace<br/>                | Root\\Microsoft\\Windows\\Storage<br/>                                              |
| MOF<br/>                      | <dl> <dt>Storagewmi.mof</dt> </dl> |



## See also

<dl> <dt>

[**MSFT\_DiskImage**](msft-diskimage.md)
</dt> <dt>

[**MSFT\_Volume**](msft-volume.md)
</dt> </dl>

 

 





