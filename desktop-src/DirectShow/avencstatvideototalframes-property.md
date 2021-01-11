---
description: Returns the number of video frames that the encoder received.
ms.assetid: 3de49105-3c74-4a52-9cac-465b4abfcbf5
title: AVEncStatVideoTotalFrames property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncStatVideoTotalFrames property

Returns the number of video frames that the encoder received.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncStatVideoTotalFrames**

## Remarks

This property is available after the encoding is completed.

The value of this property is the total number of frames sent to the encoder, including frames that were dropped. To get the number of encoded frames, read the [**AVEncStatVideoCodedFrames**](avencstatvideocodedframes-property.md) property.

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

 

 




