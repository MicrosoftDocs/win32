---
title: AccessibleObjectFromPointReturnedNullIAccessible
description: AccessibleObjectFromPointReturnedNullIAccessible
ms.assetid: DF786659-8ADC-4EB0-A606-8B80C139691A
ms.topic: article
ms.date: 05/31/2018
---

# AccessibleObjectFromPointReturnedNullIAccessible

## Text

AccessibleObjectFromPoint({0}, {1}) returned null

## Type

Error

## Description

The address of the UI element's [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface obtained for the given coordinates is NULL.

## Possible causes

-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.
-   An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[Navigation Through Hit Testing and Screen Location](navigation-through-hit-testing-and-screen-location.md)
</dt> <dt>

[**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint)
</dt> </dl>

 

 




