---
title: ActiveBasicDevice GetCachedSinkProtocolInfo method (PlayToDevice.h)
description: Gets the cached sink protocol info for the device. | ActiveBasicDevice GetCachedSinkProtocolInfo method (PlayToDevice.h)
ms.assetid: C6A3C4B5-1883-4E71-83D2-11E378A4FBCA
keywords:
- GetCachedSinkProtocolInfo method Media Streaming API
- GetCachedSinkProtocolInfo method Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , GetCachedSinkProtocolInfo method
topic_type:
- apiref
api_name:
- ActiveBasicDevice.GetCachedSinkProtocolInfo
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ActiveBasicDevice::GetCachedSinkProtocolInfo method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets the cached sink protocol info for the device.

## Syntax


```C++
HRESULT GetCachedSinkProtocolInfo(
  [out, retval] HSTRING *value
);
```



## Parameters

<dl> <dt>

*value* \[out, retval\]
</dt> <dd>

The cached sink protocol info for the device.

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

 

