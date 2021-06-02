---
description: The time attribute specifies the time at which a parameter assumes a new value, relative to the start of the transition or effect.
ms.assetid: bb478215-cbd5-4fea-9d88-a1f2b002f3da
title: time Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# time Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `time` attribute specifies the time at which a parameter assumes a new value, relative to the start of the transition or effect.

## Possible Values

Must be a string with the format *hh:mm:ss.ff* format, where *hh* = hours, *mm* = minutes, *ss* = seconds, and *ff* = fractions of seconds. Example: 1:04:30.512. Leading units can be omitted. For example, 3:00 (three minutes) and 45 (45 seconds) are both valid.

## Applies To

[**at**](at-element.md), [**linear**](linear-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> </dl>

 

 



