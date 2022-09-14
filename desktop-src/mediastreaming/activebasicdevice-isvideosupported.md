---
title: ActiveBasicDevice IsVideoSupported property (PlayToDevice.h)
description: Gets a value that indicates if the device supports video.
ms.assetid: E8D33A04-748D-42F8-878F-35D973A6B559
keywords:
- IsVideoSupported property Media Streaming API
- IsVideoSupported property Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , IsVideoSupported property
topic_type:
- apiref
api_name:
- ActiveBasicDevice.IsVideoSupported
- ActiveBasicDevice.get_IsVideoSupported
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::IsVideoSupported property

Gets a value that indicates if the device supports video.

This property is read-only.

## Syntax


```C++
HRESULT get_IsVideoSupported(
  [out] boolean *value
);
```



## Property value

A pointer to a **boolean** that indicates if the device supports video.

**true** if the device supports video; otherwise, **false**.

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

 

