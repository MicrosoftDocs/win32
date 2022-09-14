---
title: AccNameShouldNotContainRole
description: AccNameShouldNotContainRole
ms.assetid: 271461FF-5123-482F-B66D-A323CB3361DD
ms.topic: article
ms.date: 05/31/2018
---

# AccNameShouldNotContainRole

## Text

Element's Name ({0}) should not contain the text of the Element's Role ({1})

## Type

Warning

## Description

The name of an element incorporates its MSAA role or UIA control type. For example, this warning can occur if the [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname) method—which is used to retrieve the MSAA name of an element—returns "ROLE\_SYSTEM\_SCROLLBAR\_\*".

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because the role will be read twice, or it may be unpronounceable or non-intuitive for users.

## Possible causes

-   The element or its parent has an incorrectly assigned name or label.
-   The element or its parent has a default name that has not been revised to a friendly name. For example, button1.
-   A developer is not aware that screen readers read names.

## Related topics

<dl> <dt>

[**IAccessible::get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)
</dt> <dt>

[Name Property](name-property.md)
</dt> </dl>

 

 




