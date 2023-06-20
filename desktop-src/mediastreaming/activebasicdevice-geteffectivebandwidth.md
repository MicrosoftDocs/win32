---
title: ActiveBasicDevice GetEffectiveBandwidth method (PlayToDevice.h)
description: Gets the current effective bandwidth for the device.
ms.assetid: 88CE03AB-6F87-4E43-B673-2C693D351F10
keywords:
- GetEffectiveBandwidth method Media Streaming API
- GetEffectiveBandwidth method Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , GetEffectiveBandwidth method
topic_type:
- apiref
api_name:
- ActiveBasicDevice.GetEffectiveBandwidth
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ActiveBasicDevice::GetEffectiveBandwidth method

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets the current effective bandwidth for the device.

## Syntax


```C++
HRESULT GetEffectiveBandwidth(
  [in, retval] boolean transmitSpeed,
  [out]        ULONG64 *currentSpeed
);
```



## Parameters

<dl> <dt>

*transmitSpeed* \[in, retval\]
</dt> <dd>

Specifies whether the transmit speed is retrieved or the receive speed is retrieved.

**true** to retrieve the transmit speed. **false** to retrieve the receive speed.

</dd> <dt>

*currentSpeed* \[out\]
</dt> <dd>

Receives the current effective bandwidth.

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

 

