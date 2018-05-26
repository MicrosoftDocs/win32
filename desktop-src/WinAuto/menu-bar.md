---
title: Menu Bar (MSAA UI Element Reference)
description: A menu bar is the area of a window immediately beneath the title bar that contains menu items such as File, Edit, Window, and Help.
ms.assetid: 63b496c7-ae3b-49b5-8c22-41fc9a8f3981
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Menu Bar (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Menu Bar** objects for purposes of MSAA UI Element Reference. How to create **Menu Bar** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A menu bar is the area of a window immediately beneath the title bar that contains menu items such as **File**, **Edit**, **Window**, and **Help**. Microsoft Active Accessibility also creates a menu bar object for a system menu, which is the menu in the top left corner of the title bar and contains menu items such as **Restore**, **Move**, **Size**, **Minimize**, and **Maximize**.

> [!Note]  
> Because menu bar controls do not receive focus, the [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master) and [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master) methods are not supported for this control.

 

## IAccessible Methods

Menu bar controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

Menu bar controls support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)                       | Retrieves the [**IDispatch**](idispatch-interface.md) for the specified menu item. The child IDs for the menu items are numbered sequentially from left to right starting with one.                                                                                                                                                                                             |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is the number of menu items on the menu bar. The **ChildCount** property for a system menu is one.                                                                                                                                                                                                                                                   |
| [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master)           | The **Description** property for a menu bar is "Contains commands to manipulate the current view or document". The **Description** property for a system menu is "Contains commands to manipulate the window".                                                                                                                                                                   |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)       |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accHelp**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelp?branch=master)                         |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accHelpTopic**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelptopic?branch=master)               |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property for a menu bar beneath the title bar is "Alt". The **KeyboardShortcut** property for a system menu is "Alt+Space".                                                                                                                                                                                                                             |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property for a menu bar beneath the title bar is "Application". The **Name** property for a system menu is "System".                                                                                                                                                                                                                                                |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_MENUBAR**](object-roles.md#role-system-menubar).                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Notes

The system triggers more than one [**EVENT\_SYSTEM\_MENUSTART**](event-constants.md#event-system-menustart) event that does not always have a corresponding [**EVENT\_SYSTEM\_MENUEND**](event-constants.md#event-system-menuend) event. Additionally, the system does not trigger the [**EVENT\_SYSTEM\_MENUPOPUPSTART**](event-constants.md#event-system-menupopupstart) and [**EVENT\_SYSTEM\_MENUPOPUPEND**](event-constants.md#event-system-menupopupend) events consistently. This is a known issue and is being addressed.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> <dt>

[**Menu Item**](menu-item.md)
</dt> <dt>

[**Pop-up Menu**](pop-up-menu.md)
</dt> </dl>

 

 





