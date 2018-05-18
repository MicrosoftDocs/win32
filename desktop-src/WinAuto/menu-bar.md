---
title: Menu Bar (MSAA UI Element Reference)
description: A menu bar is the area of a window immediately beneath the title bar that contains menu items such as File, Edit, Window, and Help.
ms.assetid: '63b496c7-ae3b-49b5-8c22-41fc9a8f3981'
---

# Menu Bar (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Menu Bar** objects for purposes of MSAA UI Element Reference. How to create **Menu Bar** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A menu bar is the area of a window immediately beneath the title bar that contains menu items such as **File**, **Edit**, **Window**, and **Help**. Microsoft Active Accessibility also creates a menu bar object for a system menu, which is the menu in the top left corner of the title bar and contains menu items such as **Restore**, **Move**, **Size**, **Minimize**, and **Maximize**.

> [!Note]  
> Because menu bar controls do not receive focus, the [**accSelect**](iaccessible-iaccessible--accselect.md) and [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md) methods are not supported for this control.

 

## IAccessible Methods

Menu bar controls support the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

Menu bar controls support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       | Retrieves the [**IDispatch**](idispatch-interface.md) for the specified menu item. The child IDs for the menu items are numbered sequentially from left to right starting with one.                                                                                                                                                                                             |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is the number of menu items on the menu bar. The **ChildCount** property for a system menu is one.                                                                                                                                                                                                                                                   |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           | The **Description** property for a menu bar is "Contains commands to manipulate the current view or document". The **Description** property for a system menu is "Contains commands to manipulate the window".                                                                                                                                                                   |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)       |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)                         |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)               |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property for a menu bar beneath the title bar is "Alt". The **KeyboardShortcut** property for a system menu is "Alt+Space".                                                                                                                                                                                                                             |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property for a menu bar beneath the title bar is "Application". The **Name** property for a system menu is "System".                                                                                                                                                                                                                                                |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_MENUBAR**](object-roles.md#role-system-menubar).                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Notes

The system triggers more than one [**EVENT\_SYSTEM\_MENUSTART**](event-constants.md#event-system-menustart) event that does not always have a corresponding [**EVENT\_SYSTEM\_MENUEND**](event-constants.md#event-system-menuend) event. Additionally, the system does not trigger the [**EVENT\_SYSTEM\_MENUPOPUPSTART**](event-constants.md#event-system-menupopupstart) and [**EVENT\_SYSTEM\_MENUPOPUPEND**](event-constants.md#event-system-menupopupend) events consistently. This is a known issue and is being addressed.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> <dt>

[**Menu Item**](menu-item.md)
</dt> <dt>

[**Pop-up Menu**](pop-up-menu.md)
</dt> </dl>

 

 





