---
title: Selecting Child Objects
description: Clients call the IAccessible accSelect method to modify selection or keyboard focus among the children in an object. The SELFLAG Constants specified with the call define the operation to perform.
ms.assetid: 5e7ad1e9-b1b2-4e76-93e8-b58251930621
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Selecting Child Objects

Clients call the [**IAccessible::accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) method to modify selection or keyboard focus among the children in an object. The [SELFLAG Constants](selflag.md) specified with the call define the operation to perform.

If [**IAccessible::accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) is called with the [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) flag on a child object that has an **HWND**, the flag takes effect only if the object's parent has the focus.

## Performing Complex Selection Operations

The following describes which SELFLAG values to specify when calling [**IAccessible::accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) to perform complex selection operations.

**To simulate a click**

-   [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) \| [**SELFLAG\_TAKESELECTION**](selflag.md#selflag-takeselection)

**To select a target item by simulating CTRL + click**

-   [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) \| [**SELFLAG\_ADDSELECTION**](selflag.md#selflag-addselection)

**To cancel selection of a target item by simulating CTRL + click**

-   [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) \| [**SELFLAG\_REMOVESELECTION**](selflag.md#selflag-removeselection)

**To simulate SHIFT + click**

-   [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) \| [**SELFLAG\_EXTENDSELECTION**](selflag.md#selflag-extendselection)

**To select a range of objects and put focus on the last object**

1.  Specify [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) on the starting object to set the selection anchor.
2.  Call [**IAccessible::accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) again and specify [**SELFLAG\_EXTENDSELECTION**](selflag.md#selflag-extendselection) \| [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) on the last object.

**To deselect all objects**

1.  Specify [**SELFLAG\_TAKESELECTION**](selflag.md#selflag-takeselection) on any object. This flag deselects all selected objects except the one just selected.
2.  Call [**IAccessible::accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) again and specify [**SELFLAG\_REMOVESELECTION**](selflag.md#selflag-removeselection) on the remaining object.

 

 




