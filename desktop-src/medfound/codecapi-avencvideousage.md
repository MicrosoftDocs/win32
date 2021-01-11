---
description: Sets the video usage for a video encoder.
ms.assetid: 2A6941A3-CCA0-467C-AC8A-DADC2CD1D405
title: CODECAPI_AVEncVideoUsage property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# CODECAPI\_AVEncVideoUsage property

Sets the video usage for a video encoder.

## Data type

**ULONG (VT\_UI4)**

## Property GUID

**CODECAPI\_AVEncVideoUsage**

## Remarks

This property is also used with [H.264 UVC 1.5 camera encoders](camera-encoder-h264-uvc-1-5.md).

[CODECAPI\_AVEncVideoTemporalLayerCount](codecapi-avencvideotemporallayercount.md), CODECAPI\_AVEncVideoUsage, and [CODECAPI\_AVEncCommonRateControlMode](/windows/desktop/DirectShow/avenccommonratecontrolmode-property) are static encoder properties. Once set, these will only take effect after a set media type is called on the camera s output pin.

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> </dl>

 

