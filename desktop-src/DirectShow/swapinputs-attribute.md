---
description: The swapinputs attribute specifies whether to swap transition inputs. If the value is TRUE, the inputs are swapped. The default value is FALSE.
ms.assetid: 2b8d95ec-2c6c-4bd8-83e9-7f72770449b5
title: swapinputs Attribute
ms.topic: reference
ms.date: 05/31/2018
---

# swapinputs Attribute

> [!Note]  
> \[Deprecated. This API may be removed from future releases of Windows.\]

 

The `swapinputs` attribute specifies whether to swap transition inputs. If the value is **TRUE**, the inputs are swapped. The default value is **FALSE**.

## Possible Values

The following values are defined as TRUE: y, Y, t, T, 1. The following values are defined as FALSE: n, N, f, F, 0 (zero).

## Applies To

[**transition**](transition-element.md)

## Remarks

By default, a transition proceeds from the composite of all lower-priority layers to the layer on which the transition resides. If the `swapinputs` attribute is 1, this direction is reversed. For more information about the layering model used by DES, see [The Timeline Model](the-timeline-model.md).

## See also

<dl> <dt>

[XTL Attributes](xtl-attributes.md)
</dt> <dt>

[**IAMTimelineTrans::SetSwapInputs**](iamtimelinetrans-setswapinputs.md)
</dt> </dl>

 

 



