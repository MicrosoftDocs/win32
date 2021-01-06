---
description: The mute attribute specifies the object's mute state.
ms.assetid: 9a6dccf5-ae00-4ee0-8df3-bf817fe1a164
title: mute Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# mute Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `mute` attribute specifies the object's mute state. If the value is **TRUE**, neither the object nor its children are rendered. If the value is **FALSE**, the object is rendered, and its children are rendered according to their own mute state. The default value is **FALSE**.

## Possible Values

The following values are defined as TRUE: y, Y, t, T, 1. The following values are defined as FALSE: n, N, f, F, 0 (zero).

## Applies To

[**clip**](clip-element.md), [**composite**](composite-element.md), [**effect**](effect-element.md), [**group**](group-element.md), [**timeline**](timeline-element.md), [**transition**](transition-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineObj::SetMuted**](iamtimelineobj-setmuted.md)
</dt> </dl>

 

 



