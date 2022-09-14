---
title: ActiveBasicDevice PhysicalNetworkInterface property (PlayToDevice.h)
description: Gets the id of the physical network interface.
ms.assetid: F426462F-CE26-4EE1-B679-A4C80B2919A5
keywords:
- PhysicalNetworkInterface property Media Streaming API
- PhysicalNetworkInterface property Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , PhysicalNetworkInterface property
topic_type:
- apiref
api_name:
- ActiveBasicDevice.PhysicalNetworkInterface
- ActiveBasicDevice.get_PhysicalNetworkInterface
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::PhysicalNetworkInterface property

Gets the id of the physical network interface.

This property is read-only.

## Syntax


```C++
HRESULT get_PhysicalNetworkInterface(
  [out] GUID *value
);
```



## Property value

A pointer to a **GUID** that specifies the id of the physical network interface.

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

 

