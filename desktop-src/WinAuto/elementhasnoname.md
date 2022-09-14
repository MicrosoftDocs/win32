---
title: ElementHasNoName
description: ElementHasNoName
ms.assetid: 893A758F-BD34-4ABE-A99E-8CABE33966E0
ms.topic: article
ms.date: 05/31/2018
---

# ElementHasNoName

## Text

Element has no name

## Type

Error

## Description

An element does not have a name. For example, the element does not have accName implemented and an empty string is returned when the [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname) method is used to retrieve the MSAA name of the element.

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because an element might be incorrectly identified to the user.

## Possible causes

-   The element or its parent has no name or label.
-   The element is assigned an [**accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole) that suggests the element have a name.
-   The element that has focus should not receive focus. For example, a label or a disabled control.
-   An invisible control has received focus.

## Related topics

<dl> <dt>

[**IAccessible::get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)
</dt> <dt>

[Name Property](name-property.md)
</dt> </dl>

 

 




