---
title: Selection and Focus Properties and Methods
description: Like many elements in applications running on Microsoft Windows operating systems, accessible objects select and receive keyboard focus. These attributes enable users to interact with application elements, change values, and otherwise manipulate them.
ms.assetid: 8170fe19-f157-4d7d-8eec-d384e51f1560
ms.topic: reference
ms.date: 05/31/2018
---

# Selection and Focus Properties and Methods

Like many elements in applications running on Microsoft Windows operating systems, accessible objects *select* and receive keyboard *focus*. These attributes enable users to interact with application elements, change values, and otherwise manipulate them.

There are some key differences between object selection and object focus:

-   A focused object is the one object in the entire operating system that receives keyboard input. The object with the keyboard focus is either the active window or a child object of the active window.
-   A selected object is marked to participate in some type of group operation.

For example, a user can select several items in a list-view control, but the focus is given only to one object in the system at a time. Note that focused items are from a selection of items.

Clients determine whether a particular accessible object or child element has the focus by calling [**IAccessible::get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus). Clients determine whether an object is selected, or which children within an accessible object are selected, by calling [**IAccessible::get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection). For objects such as list-view controls in which more than one child is selected, the parent object must support the [IEnumVARIANT](/windows/win32/api/oaidl/nn-oaidl-ienumvariant) interface, which allows clients to enumerate the selected children.

## Events Triggered in Menus

Microsoft Active Accessibility exposes standard menus created with the Microsoft Win32 menu APIs and resource files. To be consistent with standard menus, servers with custom menus trigger [**EVENT\_OBJECT\_FOCUS**](event-constants.md), not [**EVENT\_OBJECT\_SELECTION**](event-constants.md), when a user highlights a menu item.

> [!Note]  
> Microsoft Active Accessibility does not support the selection of the text contained in edit and rich edit controls because the text is exposed as a single string in the [**Value**](value-property.md) property for these controls.

 

## In this section

-   [Selecting Child Objects](selecting-child-objects.md)

 

 