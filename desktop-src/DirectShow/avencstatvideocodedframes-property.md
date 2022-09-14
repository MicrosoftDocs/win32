---
description: Returns the number of video frames that were encoded.
ms.assetid: ade9fe69-b3dd-44aa-856b-75d4a7e4c680
title: AVEncStatVideoCodedFrames property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncStatVideoCodedFrames property

Returns the number of video frames that were encoded.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncStatVideoCodedFrames**

## Remarks

This property is available after the encoding is completed.

The value of this property is equal to the [**AVEncStatVideoTotalFrames**](avencstatvideototalframes-property.md) property minus the number of dropped frames. The encoder might drop frames to stay within the specified bit rate constraints. It might also drop frames at the end of the stream (see [**AVEncCommonStreamEndHandling**](avenccommonstreamendhandling-property.md) property).

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

 

 




