---
description: The mstop attribute specifies the stop time of a clip, relative to the original media file.
ms.assetid: 01559d29-9c7b-4842-a1f7-16552adbda43
title: mstop Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# mstop Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `mstop` attribute specifies the stop time of a clip, relative to the original media file.

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

 

 



