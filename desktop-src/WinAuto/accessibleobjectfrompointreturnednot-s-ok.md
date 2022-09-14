---
title: AccessibleObjectFromPointReturnedNot_S_OK
description: AccessibleObjectFromPointReturnedNot\_S\_OK
ms.assetid: F5DA071A-EBB8-454C-9BC0-BC798835B7D0
ms.topic: article
ms.date: 05/31/2018
---

# AccessibleObjectFromPointReturnedNot\_S\_OK

## Text

AccessibleObjectFromPoint({0}, {1}) returned {2} and expected S\_OK

## Type

Warning

## Description

[**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint) did not return S\_OK as expected for the given coordinates.

## Possible causes

-   User interaction during verification, such as moving focus to a non-target HWND, interfered with the verification process.
-   An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[Navigation Through Hit Testing and Screen Location](navigation-through-hit-testing-and-screen-location.md)
</dt> <dt>

[**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint)
</dt> </dl>

 

 




