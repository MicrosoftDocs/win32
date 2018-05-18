---
title: NullParent
description: NullParent
ms.assetid: 'F9563D73-66EF-4C66-8783-B034AA7A212E'
---

# NullParent

## Text

Elements parent is NULL

## Type

Error

## Description

NULL is returned when [**get\_accParent**](iaccessible-iaccessible--get-accparent.md) is called on the element. The **get\_accParent** method should return NULL only when called on the root element of the verification target.

This issue can cause navigation problems for automated tools because traversing elements might be erratic and unpredictable.

## Possible causes

An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[**IAccessible::accNavigate**](iaccessible-iaccessible--accnavigate.md)
</dt> <dt>

[**IAccessible::get\_accParent**](iaccessible-iaccessible--get-accparent.md)
</dt> </dl>

 

 




