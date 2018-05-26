---
title: Touch Hit Testing
description: The topics in this section provide an overview of support for Touch Hit Testing in Windows 8.
ms.assetid: bdd7630c-b2d8-4080-a149-efec018f697d
keywords:
- user interaction
- input
- pointer
- touch
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Touch Hit Testing

## Purpose

The topics in this section provide an overview of support for Touch Hit Testing in Windows 8. Touch Hit Testing enables identifying an input target based on whether the content area of a UI element falls within the contact area or includes the contact point.

For Windows 8, touch hit testing uses complex contact geometry for the entire touch area rather than a single interpolated x-y coordinate. Using the entire contact geometry greatly improves precision and accuracy when you're identifying the most likely target of touch input.

## In this section



| Topic                                                   | Description                                                                                                                                 |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [Touch Hit Testing Reference](reference.md)<br/> | The topics in this section provide the reference specifications for [Touch Hit Testing](https://msdn.microsoft.com/library/windows/desktop/hh437255).<br/> |



 

## Developer audience

The Touch Hit Testing APIs are designed for developers who are building UI frameworks that provide a consistent touch-optimized user experience across desktop applications.

## Related topics

<dl> <dt>

[User Interaction](https://msdn.microsoft.com/library/windows/desktop/ff657750)
</dt> </dl>

 

 





