---
description: Sets the maximum real-time input rate of video frames being fed to the encoder.
ms.assetid: ACBE8799-A81C-44C3-B985-88ADFB1E51B4
title: CODECAPI_AVEncMaxFrameRate property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncMaxFrameRate property

Sets the maximum real-time input rate of video frames being fed to the encoder.

## Data type

**ULONGULONG** (VT\_UI8)

## Property GUID

**CODECAPI\_AVEncMaxFrameRate**

## Remarks

This property allows the caller to specify the maximum real-time input rate of video frames being fed to the encoder. This gives the encoder an indication of the rate that it will need to process the incoming frames. This is useful for encoders that set themselves into a particular power state configuration based on the resolution and frame-rate of the source video.

The frame rate is expressed as a ratio. The upper 32 bits of the attribute value contain the numerator and the lower 32 bits contain the denominator. For example, if the frame rate is 30 frames per second (fps), the ratio is 30/1. If the frame rate is 29.97 fps, the ratio is 30,000/1001.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2016 \[desktop apps only\]<br/>                                  |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**ICodecAPI**](/windows/desktop/api/strmif/nn-strmif-icodecapi)
</dt> </dl>

 

