---
description: Specifies the chroma siting for the input video. Chroma siting defines the positions of the chroma samples relative to the luma samples.
ms.assetid: e9f8fef5-73da-424d-a239-09779b81a02b
title: AVEncVideoInputChromaSubsampling property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVEncVideoInputChromaSubsampling property

Specifies the chroma siting for the input video. Chroma siting defines the positions of the chroma samples relative to the luma samples.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVEncVideoInputChromaSubsampling**

## Property value

The value of this property is a bitwise OR of flags from the [**eAVEncVideoChromaSubsampling**](/windows/desktop/api/codecapi/ne-codecapi-eavencvideochromasubsampling) enumeration.

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

 

 




