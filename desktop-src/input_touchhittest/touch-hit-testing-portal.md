---
title: Touch Hit Testing
description: The topics in this section provide an overview of support for Touch Hit Testing in Windows 8.
ms.assetid: bdd7630c-b2d8-4080-a149-efec018f697d
keywords:
- user interaction
- input
- pointer
- touch
ms.topic: article
ms.date: 02/07/2020
---

# Touch Hit Testing

## Purpose

The topics in this section provide an overview of support for Touch Hit Testing in Windows. Touch Hit Testing lets you identify an input target based on whether the content area of a UI element falls within the contact area or includes the contact point.

Touch hit testing uses complex contact geometry for the entire touch area rather than a single interpolated x-y coordinate. Using the entire contact geometry greatly improves precision and accuracy when you're identifying the most likely target of touch input.

## In this section

| Topic | Description |
| --- | --- |
| [Touch Hit Testing Reference](touchhittest-reference.md)<br/> | The topics in this section provide the reference specifications for [Touch Hit Testing](touch-hit-testing-portal.md).<br/> |

## Developer audience

The Touch Hit Testing APIs are designed for developers who are building UI frameworks that provide a consistent touch-optimized user experience across desktop applications.

## Related topics

[User Interaction](../user-interaction.md)
