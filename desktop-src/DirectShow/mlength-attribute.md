---
description: The mlength attribute specifies the duration of a source file. This value must be the actual duration, or rendering errors may occur.
ms.assetid: f33ce85c-df61-4248-8dea-677162fa1a07
title: mlength Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# mlength Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `mlength` attribute specifies the duration of a source file. This value must be the actual duration, or rendering errors may occur.

## Applies To

[**clip**](clip-element.md)

## Possible Values

Must be a string with the format *hh:mm:ss.ff* format, where *hh* = hours, *mm* = minutes, *ss* = seconds, and *ff* = fractions of seconds. Example: 1:04:30.512. Leading units can be omitted. For example, 3:00 (three minutes) and 45 (45 seconds) are both valid.

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineSrc::SetMediaLength**](iamtimelinesrc-setmedialength.md)
</dt> </dl>

 

 



