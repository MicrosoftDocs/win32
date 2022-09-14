---
description: The start attribute specifies the start time of an object, relative to the parent object.
ms.assetid: '971de88e-c1ee-4e07-bf8e-3153e4fd11f3'
title: start Attribute
ms.topic: article
ms.date: 05/31/2018
---

# start Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `start` attribute specifies the start time of an object, relative to the parent object.

## Possible Values

Must be a string with the format *hh:mm:ss.ff* format, where *hh* = hours, *mm* = minutes, *ss* = seconds, and *ff* = fractions of seconds. Example: 1:04:30.512. Leading units can be omitted. For example, 3:00 (three minutes) and 45 (45 seconds) are both valid.

## Applies To

[**clip**](clip-element.md), [**effect**](effect-element.md), [**transition**](transition-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineObj::SetStartStop**](iamtimelineobj-setstartstop.md)
</dt> </dl>

 

 



