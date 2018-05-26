---
Description: The stop attribute specifies the stop time of an object, relative to the parent object.
ms.assetid: 01559d29-9c7b-4842-a1f7-16552adbda43
title: stop Attribute
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
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

 

 



