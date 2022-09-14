---
title: InvalidRole
description: InvalidRole
ms.assetid: B0707B90-59D6-4F86-8CBB-1DF57FDBEE31
ms.topic: article
ms.date: 05/31/2018
---

# InvalidRole

## Text

The int returned from get\_accRole is not a valid role constant, ie ROLE\_SYSTEM\_\*

## Type

Error

## Description

An element is reporting an invalid MSAA role. For example, the [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole) method returns an integer value that does not map to a valid object role constant (such as ROLE\_SYSTEM\_LISTITEM).

This issue causes problems for people who rely on a screen-reader and keyboard for navigation because elements may be incorrectly identified to the user.

## Possible causes

The element or its parent has an MSAA role set inappropriately.

## Related topics

<dl> <dt>

[**IAccessible::get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)
</dt> <dt>

[**Object Roles**](object-roles.md)
</dt> </dl>

 

 




