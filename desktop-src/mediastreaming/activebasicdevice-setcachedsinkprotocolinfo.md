---
title: ActiveBasicDevice SetCachedSinkProtocolInfo method (PlayToDevice.h)
description: Gets the cached sink protocol info for the device. | ActiveBasicDevice SetCachedSinkProtocolInfo method (PlayToDevice.h)
ms.assetid: C4856B97-89F9-43EC-B778-9E0CDAAF2C47
keywords:
- SetCachedSinkProtocolInfo method Media Streaming API
- SetCachedSinkProtocolInfo method Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , SetCachedSinkProtocolInfo method
topic_type:
- apiref
api_name:
- ActiveBasicDevice.SetCachedSinkProtocolInfo
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# ActiveBasicDevice::SetCachedSinkProtocolInfo method

Gets the cached sink protocol info for the device.

## Syntax


```C++
HRESULT SetCachedSinkProtocolInfo(
  [in] GUID   physicalNetworkInterface,
  [in] UINT64 bitrate
);
```



## Parameters

<dl> <dt>

*physicalNetworkInterface* \[in\]
</dt> <dd>

Specifies the physical network interface.

</dd> <dt>

*bitrate* \[in\]
</dt> <dd>

The bitrate value.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

