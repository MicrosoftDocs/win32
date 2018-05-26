---
title: Pop-up Menu (MSAA UI Element Reference)
description: A pop-up menu displays a list of menu commands.
ms.assetid: 9dbfa2d7-a086-4348-8b84-7e36d33e2d27
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Pop-up Menu (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Pop-up Menu** objects for purposes of MSAA UI Element Reference. How to create **Pop-up Menu** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A pop-up menu displays a list of menu commands. Microsoft Active Accessibility creates a menu pop-up object when a menu item in a menu bar is opened. Microsoft Active Accessibility also creates menu pop-up objects for context menus, which are displayed when the user right-clicks a user interface element.

The window class name for a pop-up menu is "\#32768".

## IAccessible Methods

A pop-up menu supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

A pop-up menu supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)           | Retrieves the [**IDispatch**](idispatch-interface.md) for the specified menu item. The child IDs for the menu items are numbered sequentially from top to bottom starting with one.                                                                                                                                                                                                                                                                                      |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master) | The **ChildCount** property is the number of menu items in the menu, including menu separators.                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)             | The **Name** property for a pop-up menu is the same name as the menu. The **Name** property for a context menu is "Context".                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the pop-up menu and has the same **Name** property and window class name as the pop-up menu .                                                                                                                                                                                                                                                      |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)             | The **Role** property is [**ROLE\_SYSTEM\_MENUPOPUP**](object-roles.md#role-system-menupopup).                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Notes

-   Pop-up menu objects do not trigger [**EVENT\_OBJECT\_CREATE**](event-constants.md#event-object-create) and [**EVENT\_OBJECT\_DESTROY**](event-constants.md#event-object-destroy) events.
-   Multi-column menus do not support the [**NAVDIR\_LEFT**](navigation-constants.md#navdir-left) or [**NAVDIR\_RIGHT**](navigation-constants.md#navdir-right) flags of the [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master) method.
-   The events [**EVENT\_SYSTEM\_MENUPOPUPSTART**](event-constants.md#event-system-menupopupstart) and [**EVENT\_SYSTEM\_MENUPOPUPEND**](event-constants.md#event-system-menupopupend) are not sent consistently. This is a known issue and is being addressed.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> <dt>

[**Menu Bar**](menu-bar.md)
</dt> <dt>

[**Menu Item**](menu-item.md)
</dt> </dl>

 

 





