---
title: IMsRdpDriveV2 DriveLetterIndex property
description: Contains the index of the letter for the drive.
ms.assetid: 9091d1c4-b97e-4e4c-9563-5a0b881ec250
ms.tgt_platform: multiple
keywords:
- DriveLetterIndex property Remote Desktop Services
- DriveLetterIndex property Remote Desktop Services , IMsRdpDriveV2 interface
- IMsRdpDriveV2 interface Remote Desktop Services , DriveLetterIndex property
topic_type:
- apiref
api_name:
- IMsRdpDriveV2.DriveLetterIndex
- IMsRdpDriveV2.get_DriveLetterIndex
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDriveV2::DriveLetterIndex property

Contains the index of the letter for the drive.

This property is read-only.

## Syntax


```C++
HRESULT get_DriveLetterIndex(
  [out, retval] ULONG *pDriveLetterIndex
);
```



## Property value

The index of the letter for the drive. 0 = "A", 1 = "B", and so on.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 with SP1<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpDriveV2**](imsrdpdrivev2.md)
</dt> </dl>

 

 





