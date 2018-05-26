---
title: ElementIsNotChildOfElementsParent
description: ElementIsNotChildOfElementsParent
ms.assetid: DFD5CC2A-B5F4-49F2-B3EF-2CD447A575E2
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ElementIsNotChildOfElementsParent

## Text

Element is not a child of it's parent

## Type

Error

## Description

When [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master) is called on the child element returned by [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master) (using either the NAVDIR\_FIRSTCHILD or NAVDIR\_LASTCHILD navigation constants), the parent element returned does not match the parent element specified in the **accNavigate** call.

This issue can cause navigation problems for automated tools because traversing elements might be erratic and unpredictable.

## Possible causes

An incorrect or invalid MSAA implementation.

## Related topics

<dl> <dt>

[**IAccessible::accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
</dt> <dt>

[**IAccessible::get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)
</dt> </dl>

 

 




