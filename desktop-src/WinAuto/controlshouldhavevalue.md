---
title: ControlShouldHaveValue
description: ControlShouldHaveValue
ms.assetid: 90C37CC5-21D2-4D26-B6D9-2C95C52127BF
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ControlShouldHaveValue

## Text

A control with role of {0} should have a value but get\_accValue is not implemented

## Type

Error

## Description

An element does not supply a value as expected based on the assigned MSAA role, implying that the element does not have the [**get\_accValue**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accvalue?branch=master) method implemented. For example, the following MSAA roles should all supply a value.

-   ROLE\_SYSTEM\_COMBOBOX
-   ROLE\_SYSTEM\_IPADDRESS
-   ROLE\_SYSTEM\_LINK
-   ROLE\_SYSTEM\_OUTLINEITEM
-   ROLE\_SYSTEM\_PROGRESSBAR
-   ROLE\_SYSTEM\_SLIDER
-   ROLE\_SYSTEM\_SPINBUTTON
-   ROLE\_SYSTEM\_SCROLLBAR
-   ROLE\_SYSTEM\_TEXT

This issue is a problem for people who rely on a screen-reader and keyboard for navigation because an element that has an intrinsic value must be able to report that value to a user.

## Possible causes

The element or its parent has an MSAA role set inappropriately.

## Related topics

<dl> <dt>

[**IAccessible::get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)
</dt> <dt>

[**Object Roles**](object-roles.md)
</dt> </dl>

 

 




