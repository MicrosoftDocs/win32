---
title: ActiveBasicDevice MaxVolume property (PlayToDevice.h)
description: Gets the maximum volume supported by the device.
ms.assetid: EA0EC323-4A18-4CC1-8FA4-7BD302318863
keywords:
- MaxVolume property Media Streaming API
- MaxVolume property Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , MaxVolume property
topic_type:
- apiref
api_name:
- ActiveBasicDevice.MaxVolume
- ActiveBasicDevice.get_MaxVolume
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::MaxVolume property

Gets the maximum volume supported by the device.

This property is read-only.

## Syntax


```C++
HRESULT get_MaxVolume(
  [out] boolean *UINT32
);
```



## Property value

A pointer to a**UINT32** that specifies the maximum volume supported by the device.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>PlayToDevice.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>PlayToDevice.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Playtodevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**ActiveBasicDevice**](/previous-versions/windows/desktop/legacy/dn385755(v=vs.85))
</dt> </dl>

 

