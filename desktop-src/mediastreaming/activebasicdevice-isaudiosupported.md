---
title: ActiveBasicDevice IsAudioSupported property (PlayToDevice.h)
description: Gets a value that indicates if the device supports audio.
ms.assetid: 22ABB97B-58E7-4C21-B359-C10DFC9C7194
keywords:
- IsAudioSupported property Media Streaming API
- IsAudioSupported property Media Streaming API , ActiveBasicDevice interface
- ActiveBasicDevice interface Media Streaming API , IsAudioSupported property
topic_type:
- apiref
api_name:
- ActiveBasicDevice.IsAudioSupported
- ActiveBasicDevice.get_IsAudioSupported
api_location:
- playtodevice.dll
api_type:
- COM
ms.topic: reference
ms.date: 4/26/2023
ms.custom: UpdateFrequency5
---

# ActiveBasicDevice::IsAudioSupported property

\[The feature associated with this page, [Windows Media Streaming API](/windows/win32/mediastreaming/media-streaming-api-portal), is a legacy feature. It has been superseded by [Media Casting](/windows/uwp/audio-video-camera/media-casting). **Media Casting** has been optimized for Windows 10 and Windows 11. Microsoft strongly recommends that new code use **Media Casting** instead of **Windows Media Streaming API**, when possible. Microsoft suggests that existing code that uses the legacy APIs be rewritten to use the new APIs if possible.\]

Gets a value that indicates if the device supports audio.

This property is read-only.

## Syntax


```C++
HRESULT get_IsAudioSupported(
  [out] boolean *value
);
```



## Property value

A pointer to a **boolean** that indicates if the device supports audio.

**true** if the device supports audio; otherwise, **false**.

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

 

