---
title: ActiveBasicDevice LogicalNetworkInterface property (PlayToDevice.h)
description: Gets the id of the logical network interface.
ms.assetid: 47C2E0BE-D3E3-4A9F-9FC6-873882811506
keywords:
- LogicalNetworkInterface property Media Streaming API
- LogicalNetworkInterface property Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , LogicalNetworkInterface property
topic_type:
- apiref
api_name:
- ActiveBasicDevice.LogicalNetworkInterface
- ActiveBasicDevice.get_LogicalNetworkInterface
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::LogicalNetworkInterface property

Gets the id of the logical network interface.

This property is read-only.

## Syntax


```C++
HRESULT get_LogicalNetworkInterface(
  [out] GUID *value
);
```



## Property value

A pointer to a**GUID** that specifies the id of the logical network interface.

## Requirements



|                                     |                                                                                             |
|-------------------------------------|---------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                                |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                     |
| Header<br/>                   | <dl> <dt>PlayToDevice.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>PlayToDevice.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Playtodevice.dll</dt> </dl> |



## See also

<dl> <dt>

[**ActiveBasicDevice**](https://msdn.microsoft.com/library/Dn385755(v=VS.85).aspx)
</dt> </dl>

 

 





