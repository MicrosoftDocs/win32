---
title: AccessibleObjectFromPointReturnedNullChildId
description: AccessibleObjectFromPointReturnedNullChildId
ms.assetid: 20511B76-736B-4B43-8DC3-4306DF74CF73
ms.topic: article
ms.date: 05/31/2018
---

# AccessibleObjectFromPointReturnedNullChildId

## Text

AccessibleObjectFromPoint({0}, {1}) returned a null ChildId

## Type

Error

## Description

The ChildId of the object's [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface obtained for the given coordinates is NULL.

## Possible causes

User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.

## Related topics

<dl> <dt>

[Navigation Through Hit Testing and Screen Location](navigation-through-hit-testing-and-screen-location.md)
</dt> <dt>

[**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint)
</dt> </dl>

 

 




