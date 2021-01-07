---
description: The stop attribute specifies the stop time of an object, relative to the parent object.
ms.assetid: '1bda3472-abda-4672-9b82-311163e56fe0'
title: stop Attribute
ms.topic: article
ms.date: 05/31/2018
---

# stop Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `stop` attribute specifies the stop time of an object, relative to the parent object.

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

 

 



