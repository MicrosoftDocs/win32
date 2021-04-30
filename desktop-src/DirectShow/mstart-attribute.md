---
description: The mstart attribute specifies the start time of a clip, relative to the original media file.
ms.assetid: ed63f448-8ca3-4733-afc0-2d743f82bebe
title: mstart Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# mstart Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `mstart` attribute specifies the start time of a clip, relative to the original media file.

## Applies To

[**clip**](clip-element.md)

## Possible Values

Must be a string with the format *hh:mm:ss.ff* format, where *hh* = hours, *mm* = minutes, *ss* = seconds, and *ff* = fractions of seconds. Example: 1:04:30.512. Leading units can be omitted. For example, 3:00 (three minutes) and 45 (45 seconds) are both valid.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineSrc::SetMediaTimes**](iamtimelinesrc-setmediatimes.md)
</dt> </dl>

 

 



