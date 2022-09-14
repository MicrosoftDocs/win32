---
description: Specifies the size of the buffer used during encoding. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.
ms.assetid: 3315785e-306f-44d6-ac39-796025a2da3a
title: AVEncCommonBufferSize property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncCommonBufferSize property

Specifies the size of the buffer used during encoding. This property applies only to constant bit rate (CBR) and variable bit rate (VBR) encoding modes.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncCommonBufferSize**

## Property value

This property has a linear range of values. To get the supported range, call [**ICodecAPI::GetParameterRange**](/windows/desktop/api/Strmif/nf-strmif-icodecapi-getparameterrange). Parameter ranges are not supported for H.264 UVC 1.5 camera encoders.

## Remarks

For some video formats the buffer size is specified in bits and for others it is specified in bytes. See the remarks below for specific information.

For MPEG video, this property defines the video buffer verifier (VBV) buffer size. The size of the buffer is in bits.

For H.264 video and Windows Media Video, the property defines the hypothetical reference decoder (HRD) size. The size of the buffer is in bytes.

For UVC 1.5 H264 encoding cameras, the CPB value sent to the camera encoder must be 16-bit aligned. The size of the buffer is in bytes.

This property is also used with [H.264 UVC 1.5 camera encoders](/windows/desktop/medfound/camera-encoder-h264-uvc-1-5).

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

 

