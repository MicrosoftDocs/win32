---
title: ElementIsOrphaned
description: ElementIsOrphaned
ms.assetid: EB603052-2B0F-418C-947E-827453440F46
ms.topic: article
ms.date: 05/31/2018
---

# ElementIsOrphaned

## Text

Element is an orphaned IAccessible in the tree

## Type

Error

## Description

The address of the object's [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface obtained for the given coordinates is a reference to an orphaned element in the element tree.

This issue is a problem for people who rely on a screen-reader and keyboard for navigation because elements will be treated as invisible and will not be announced to the user.

## Possible causes

-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.
-   An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[Navigation Through Hit Testing and Screen Location](navigation-through-hit-testing-and-screen-location.md)
</dt> <dt>

[**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint)
</dt> </dl>

 

 




