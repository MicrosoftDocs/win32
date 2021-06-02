---
description: The cutpoint attribute specifies when a transition cuts from one source to the next, if the transition is rendered as a cut. The value is relative to the start of the transition.
ms.assetid: bdb0b8cd-025f-4b56-9cd4-f71c58ee809a
title: cutpoint Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# cutpoint Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `cutpoint` attribute specifies when a transition cuts from one source to the next, if the transition is rendered as a cut. The value is relative to the start of the transition.

## Possible Values

Must be a string with the format *hh:mm:ss.ff* format, where *hh* = hours, *mm* = minutes, *ss* = seconds, and *ff* = fractions of seconds. Example: 1:04:30.512. Leading units can be omitted. For example, 3:00 (three minutes) and 45 (45 seconds) are both valid.

## Applies To

[**transition**](transition-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineTrans::SetCutPoint**](iamtimelinetrans-setcutpoint.md)
</dt> </dl>

 

 



