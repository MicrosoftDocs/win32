---
title: Menu Bar (MSAA UI Element Reference)
description: A menu bar is the area of a window immediately beneath the title bar that contains menu items such as File, Edit, Window, and Help.
ms.assetid: 63b496c7-ae3b-49b5-8c22-41fc9a8f3981
ms.topic: article
ms.date: 05/31/2018
---

# Menu Bar (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Menu Bar** objects for purposes of MSAA UI Element Reference. How to create **Menu Bar** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A menu bar is the area of a window immediately beneath the title bar that contains menu items such as **File**, **Edit**, **Window**, and **Help**. Microsoft Active Accessibility also creates a menu bar object for a system menu, which is the menu in the top left corner of the title bar and contains menu items such as **Restore**, **Move**, **Size**, **Minimize**, and **Maximize**.

> [!Note]  
> Because menu bar controls do not receive focus, the [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) and [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus) methods are not supported for this control.

 

## IAccessible Methods

Menu bar controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

Menu bar controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                         |
|--------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild)                       | Retrieves the [**IDispatch**](idispatch-interface.md) for the specified menu item. The child IDs for the menu items are numbered sequentially from left to right starting with one.                                                                                                                                                                                             |
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)             | The **ChildCount** property is the number of menu items on the menu bar. The **ChildCount** property for a system menu is one.                                                                                                                                                                                                                                                   |
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)           | The **Description** property for a menu bar is "Contains commands to manipulate the current view or document". The **Description** property for a system menu is "Contains commands to manipulate the window".                                                                                                                                                                   |
| [**get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction)       |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)                       |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp)                         |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accHelpTopic**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelptopic)               |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | The **KeyboardShortcut** property for a menu bar beneath the title bar is "Alt". The **KeyboardShortcut** property for a system menu is "Alt+Space".                                                                                                                                                                                                                             |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | The **Name** property for a menu bar beneath the title bar is "Application". The **Name** property for a system menu is "System".                                                                                                                                                                                                                                                |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)                     |                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | The **Role** property is [**ROLE\_SYSTEM\_MENUBAR**](object-roles.md).                                                                                                                                                                                                                                                                                      |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)<br/> |



 

## Notes

The system triggers more than one [**EVENT\_SYSTEM\_MENUSTART**](event-constants.md) event that does not always have a corresponding [**EVENT\_SYSTEM\_MENUEND**](event-constants.md) event. Additionally, the system does not trigger the [**EVENT\_SYSTEM\_MENUPOPUPSTART**](event-constants.md) and [**EVENT\_SYSTEM\_MENUPOPUPEND**](event-constants.md) events consistently. This is a known issue and is being addressed.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> <dt>

[**Menu Item**](menu-item.md)
</dt> <dt>

[**Pop-up Menu**](pop-up-menu.md)
</dt> </dl>

 

 





