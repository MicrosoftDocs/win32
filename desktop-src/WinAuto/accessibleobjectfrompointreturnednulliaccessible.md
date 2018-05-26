---
title: AccessibleObjectFromPointReturnedNullIAccessible
description: AccessibleObjectFromPointReturnedNullIAccessible
ms.assetid: DF786659-8ADC-4EB0-A606-8B80C139691A
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AccessibleObjectFromPointReturnedNullIAccessible

## Text

AccessibleObjectFromPoint({0}, {1}) returned null

## Type

Error

## Description

The address of the UI element's [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface obtained for the given coordinates is NULL.

## Possible causes

-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.
-   An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[Navigation Through Hit Testing and Screen Location](navigation-through-hit-testing-and-screen-location.md)
</dt> <dt>

[**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master)
</dt> </dl>

 

 




