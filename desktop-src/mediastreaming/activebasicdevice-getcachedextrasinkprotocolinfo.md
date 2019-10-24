---
title: ActiveBasicDevice GetCachedExtraSinkProtocolInfo method
description: Gets additional cached sink protocol info for the device.
ms.assetid: 97112921-1C1D-4FC9-8FE6-1381F3773351
keywords:
- GetCachedExtraSinkProtocolInfo method Media Streaming API
- GetCachedExtraSinkProtocolInfo method Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , GetCachedExtraSinkProtocolInfo method
topic_type:
- apiref
api_name:
- ActiveBasicDevice.GetCachedExtraSinkProtocolInfo
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::GetCachedExtraSinkProtocolInfo method

Gets additional cached sink protocol info for the device.

## Syntax


```C++
HRESULT GetCachedExtraSinkProtocolInfo(
  [out, retval] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

The extra cached sink protocol info for the device.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

[**ActiveBasicDevice**](https://msdn.microsoft.com/en-us/library/Dn385755(v=VS.85).aspx)
</dt> </dl>

 

 





