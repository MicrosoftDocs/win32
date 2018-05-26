---
title: NullParent
description: NullParent
ms.assetid: F9563D73-66EF-4C66-8783-B034AA7A212E
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# NullParent

## Text

Elements parent is NULL

## Type

Error

## Description

NULL is returned when [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master) is called on the element. The **get\_accParent** method should return NULL only when called on the root element of the verification target.

This issue can cause navigation problems for automated tools because traversing elements might be erratic and unpredictable.

## Possible causes

An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[**IAccessible::accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
</dt> <dt>

[**IAccessible::get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)
</dt> </dl>

 

 




