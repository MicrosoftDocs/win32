---
title: ARIA Range Control Attributes Incompatible
description: ARIA Range Control Attributes Incompatible
ms.assetid: 265AE578-D841-4931-9F4A-97BB86ECEC88
keywords:
- AriaRangeControlAttributesIncompatibleId
ms.topic: article
ms.date: 05/31/2018
---

# ARIA Range Control Attributes Incompatible

## Text

Element has **progressbar** or **slider** role but exposed **aria-valuenow** value is outside of **aria-valuemin** **aria-valuemax** range.

## Type

Error

## Description

This error applies to elements that have a [**role**](https://developer.mozilla.org/docs/Web/HTML/Reference) (implicit or explicit) equal to **progressbar**, **slider**, or **spinbutton**.

This error indicates that the exposed [**aria-valuenow**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) value is not in the range defined by the [**aria-valuemin**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) and [**aria-valuemax**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) attributes.

To fix this error, check your implementation to ensure that the [**aria-valuemin**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) and [**aria-valuemax**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) attributes are correctly set, and that the [**aria-valuenow**](https://developer.mozilla.org/docs/Web/Accessibility/ARIA) attribute value is properly maintained.

## Related topics

<dl> <dt>

[ARIA Range Control Attributes Missing](aria-range-control-attributes-missing.md)
</dt> </dl>

 

 




