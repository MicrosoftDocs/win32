---
title: AccNavigate\_ReturnedElementWithIncorrectParent
description: AccNavigate\_ReturnedElementWithIncorrectParent
ms.assetid: 44447E47-04D5-4784-B5E9-E8C62A9834CE
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# AccNavigate\_ReturnedElementWithIncorrectParent

## Text

Calling accNavigate((Live Search), 0, NAVDIR\_FIRSTCHILD) which returned (x-gadget:///gadget.html) returned the incorrect parent(\[NULL\]) and not (Live Search)

## Type

Error

## Description

When [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master) is called on the child element returned by [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master) (using either the NAVDIR\_FIRSTCHILD or NAVDIR\_LASTCHILD navigation constants), the parent element returned does not match the parent element specified in the **accNavigate** call.

![example of an invalid msaa implementation that returns an incorrect parent element.](images/accchecker-invalid-msaa-parent.png)

This issue can cause navigation problems for automated tools because traversing elements might be erratic and unpredictable.

## Possible causes

An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[**IAccessible::accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
</dt> <dt>

[**IAccessible::get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)
</dt> </dl>

 

 




