---
title: ActiveBasicDevice IsImageSupported property (PlayToDevice.h)
description: Gets a value that indicates if the device supports images.
ms.assetid: FC53B87C-D739-4AD4-9DD3-415AC8692224
keywords:
- IsImageSupported property Media Streaming API
- IsImageSupported property Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , IsImageSupported property
topic_type:
- apiref
api_name:
- ActiveBasicDevice.IsImageSupported
- ActiveBasicDevice.get_IsImageSupported
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::IsImageSupported property

Gets a value that indicates if the device supports images.

This property is read-only.

## Syntax


```C++
HRESULT get_IsImageSupported(
  [out] boolean *value
);
```



## Property value

A pointer to a **boolean** that indicates if the device supports images.

**true** if the device supports images; otherwise, **false**.

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

 

