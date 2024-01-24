---
title: IMsRdpDeviceV2 DriveLetterBitmap property
description: Contains a bitfield that represents a map of drive letters contained within the device.
ms.assetid: 13b7c9b9-a97f-4474-b5ad-833abff384f5
ms.tgt_platform: multiple
keywords:
- DriveLetterBitmap property Remote Desktop Services
- DriveLetterBitmap property Remote Desktop Services , IMsRdpDeviceV2 interface
- IMsRdpDeviceV2 interface Remote Desktop Services , DriveLetterBitmap property
topic_type:
- apiref
api_name:
- IMsRdpDeviceV2.DriveLetterBitmap
- IMsRdpDeviceV2.get_DriveLetterBitmap
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpDeviceV2::DriveLetterBitmap property

Contains a bitfield that represents a map of drive letters contained within the device.

This property is read-only.

## Syntax


```C++
HRESULT get_DriveLetterBitmap(
  [out, retval] ULONG *pDriveLetterBitmap
);
```



## Property value

A map of drive letters contained within the device. Each bit in the value represents a drive letter. The least significant bit represents drive letter "A", the next bit represents drive letter "B", and so on.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 with SP1<br/>                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2 with SP1<br/>                                             |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpDeviceV2 is defined as 5fb94466-7661-42a8-98b7-01904c11668f<br/>      |



## See also

<dl> <dt>

[**IMsRdpDeviceV2**](imsrdpdevicev2.md)
</dt> </dl>

 

 





