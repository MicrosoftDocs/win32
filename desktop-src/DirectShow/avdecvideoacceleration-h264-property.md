---
description: Enables or disables hardware acceleration for H.264 video decoding.
ms.assetid: 3912136d-0fc1-49b0-bc79-0785d63041e6
title: AVDecVideoAcceleration_H264 property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoAcceleration\_H264 property

Enables or disables hardware acceleration for H.264 video decoding.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecVideoAcceleration\_H264**

## Remarks

If the value is zero, the decoder does not use DirectX Video Acceleration (DXVA) for H.264 video decoding. For DirectShow filters, set this property before the decoder's output pin is connected.

> [!NOTE]
> When using Media Foundation (or the **IMFTransform** interface), this property has no effect. See [Supporting Direct3D 11 video decoding in Media Foundation](/windows/win32/medfound/supporting-direct3d-11-video-decoding-in-media-foundation) for how to use hardware acceleration with Media Foundation components.

## Requirements

| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps \| UWP apps\]<br/>                     |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Codec API Properties](codec-api-properties.md)
</dt> <dt>

[**ICodecAPI Interface**](/windows/desktop/api/Strmif/nn-strmif-icodecapi)
</dt> </dl>

 

 




