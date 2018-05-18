---
title: ElementIsNotChildOfElementsParent
description: ElementIsNotChildOfElementsParent
ms.assetid: 'DFD5CC2A-B5F4-49F2-B3EF-2CD447A575E2'
---

# ElementIsNotChildOfElementsParent

## Text

Element is not a child of it's parent

## Type

Error

## Description

When [**get\_accParent**](iaccessible-iaccessible--get-accparent.md) is called on the child element returned by [**accNavigate**](iaccessible-iaccessible--accnavigate.md) (using either the NAVDIR\_FIRSTCHILD or NAVDIR\_LASTCHILD navigation constants), the parent element returned does not match the parent element specified in the **accNavigate** call.

This issue can cause navigation problems for automated tools because traversing elements might be erratic and unpredictable.

## Possible causes

An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[**IAccessible::accNavigate**](iaccessible-iaccessible--accnavigate.md)
</dt> <dt>

[**IAccessible::get\_accParent**](iaccessible-iaccessible--get-accparent.md)
</dt> </dl>

 

 




