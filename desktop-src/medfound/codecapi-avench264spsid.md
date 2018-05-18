---
Description: 'Sets the sequence parameter set (SPS) identifier in the SPS network abstraction layer (NAL) unit of the H.264 bit stream.'
ms.assetid: '583DD539-6EE8-4DD4-A0FE-D2BBE1A4302F'
title: 'CODECAPI\_AVEncH264SPSID property'
---

# CODECAPI\_AVEncH264SPSID property

Sets the sequence parameter set (SPS) identifier in the SPS network abstraction layer (NAL) unit of the H.264 bit stream.

## Data type

**ULONG** (VT\_UI4)

## Property GUID

**CODECAPI\_AVEncH264SPSID**

## Property value

Specifies the value of **seq\_parameter\_set\_id** in the SPS NAL unit. The **seq\_parameter\_set\_id** syntax element identifies the sequence parameter set. The resulting bit stream can be concatenated with other bit streams, to produce a longer bit stream that contains multiple sequence parameter sets with different SPS identifiers.

The valid range is 0–31, as specified in the H.264/AVC specification.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8 \[desktop apps \| UWP apps\]<br/>                                     |
| Minimum supported server<br/> | Windows Server 2012 \[desktop apps \| UWP apps\]<br/>                           |
| Header<br/>                   | <dl> <dt>Codecapi.h</dt> </dl> |



## See also

<dl> <dt>

[Media Foundation Properties](media-foundation-properties.md)
</dt> <dt>

[**ICodecAPI**](dshow.icodecapi)
</dt> </dl>

 

 




