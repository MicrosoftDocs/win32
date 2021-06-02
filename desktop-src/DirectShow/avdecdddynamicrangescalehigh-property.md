---
description: Specifies the high-level cut when the decoder performs dynamic range control on a Dolby AC-3 audio stream.
ms.assetid: 8771a5f9-878b-43fd-8eaa-0bfc276194aa
title: AVDecDDDynamicRangeScaleHigh property (Codecapi.h)
ms.topic: reference
ms.date: 05/31/2018
---

# AVDecDDDynamicRangeScaleHigh property

Specifies the high-level cut when the decoder performs dynamic range control on a Dolby AC-3 audio stream.

This property is read/write.

## Data type

**UINT32** (**VT\_UI4**)

## Property GUID

**CODECAPI\_AVDecDDDynamicRangeScaleHigh**

## Property value

The value of this property has the following range.



| Value | Description                                                    |
|-------|----------------------------------------------------------------|
| 0     | No dynamic range compression. Preserve the full dynamic range. |
| 100   | Apply full dynamic range compression.                          |



 

## Remarks

This property applies only when the value of the [**AVDecDDOperationalMode**](avdecddoperationalmode-property.md) property is eAVDecDDOperationalMode\_LINE.

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

 

 




