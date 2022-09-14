---
description: The framerate attribute specifies a framerate, in frames per second.
ms.assetid: 541a86e3-7736-4de4-b509-f8d61ef9bc58
title: framerate Attribute (DirectShow)
ms.topic: reference
ms.date: 05/31/2018
---

# framerate Attribute (DirectShow)

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `framerate` attribute specifies a framerate, in frames per second.

## Possible Values

Floating-point value. The value must include the leading zero before the decimal place. For example, 0.3, not .3. Do not use more than seven decimal digits.

## Applies To

[**clip**](clip-element.md), [**group**](group-element.md), [**timeline**](timeline-element.md)

## Remarks

For the **clip** element, this attribute specifies the default frame rate of the source. Specify the attribute for still images andDIB sequences. For a still image, set the value to zero. For a DIB sequence, use a nonzero value. The default value is zero.

For the **group** element, this attribute specifies the output frame rate for the group.

For the **timeline** element, this attribute specifies the default frame rate for all groups.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineSrc::SetDefaultFPS**](iamtimelinesrc-setdefaultfps.md)
</dt> <dt>

[**IAMTimelineGroup::SetOutputFPS**](iamtimelinegroup-setoutputfps.md)
</dt> <dt>

[**IAMTimeline::SetDefaultFPS**](iamtimeline-setdefaultfps.md)
</dt> </dl>

 

 



