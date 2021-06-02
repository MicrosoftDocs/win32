---
description: The lock attribute specifies whether an object should be edited. If the value is TRUE, the application should treat the object as locked, and disallow changes to that object or its children. The default value is FALSE.
ms.assetid: 1aa92665-ab3b-4f04-9e6b-905942c197ef
title: lock Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# lock Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `lock` attribute specifies whether an object should be edited. If the value is **TRUE**, the application should treat the object as locked, and disallow changes to that object or its children. The default value is **FALSE**.

## Possible Values

Possible Values The following values are defined as TRUE: y, Y, t, T, 1. The following values are defined as FALSE: n, N, f, F, 0 (zero).

## Applies To

[**clip**](clip-element.md), [**composite**](composite-element.md), [**effect**](effect-element.md), [**group**](group-element.md), [**timeline**](timeline-element.md), [**transition**](transition-element.md)

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineObj::SetLocked**](iamtimelineobj-setlocked.md)
</dt> </dl>

 

 



