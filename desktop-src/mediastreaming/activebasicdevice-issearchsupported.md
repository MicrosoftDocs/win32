---
title: ActiveBasicDevice IsSearchSupported property (PlayToDevice.h)
description: Gets a value that indicates if the device supports search.
ms.assetid: 091D467A-1FF6-4635-BF89-4E62AC9C660A
keywords:
- IsSearchSupported property Media Streaming API
- IsSearchSupported property Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , IsSearchSupported property
topic_type:
- apiref
api_name:
- ActiveBasicDevice.IsSearchSupported
- ActiveBasicDevice.get_IsSearchSupported
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::IsSearchSupported property

Gets a value that indicates if the device supports search.

This property is read-only.

## Syntax


```C++
HRESULT get_IsSearchSupported(
  [out] boolean *value
);
```



## Property value

A pointer to a**boolean** that indicates if the device supports search.

**true** if the device supports search; otherwise, **false**.

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

 

