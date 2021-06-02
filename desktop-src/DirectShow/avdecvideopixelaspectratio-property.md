---
description: Specifies the pixel aspect ratio of the decoded video stream.
ms.assetid: 07689d15-3e46-45f7-bdd5-ae51308ddbce
title: AVDecVideoPixelAspectRatio property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecVideoPixelAspectRatio property

Specifies the pixel aspect ratio of the decoded video stream.

This property is read-only.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecVideoPixelAspectRatio**

## Remarks

The upper 16 bits of the value contain the width, and the lower 16 bits contain the height.

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

 

 




