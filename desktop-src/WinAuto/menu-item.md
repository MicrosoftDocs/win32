---
title: Menu Item (MSAA UI Element Reference)
description: A menu item represents a particular item in a menu bar or pop-up menu.
ms.assetid: 330782d6-4293-4e65-ab49-a616d133d273
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Menu Item (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Menu Item** objects for purposes of MSAA UI Element Reference. How to create **Menu Item** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A menu item represents a particular item in a menu bar or pop-up menu. For example, Microsoft Active Accessibility creates a menu item object for the **File** menu in the menu bar. Similarly, Microsoft Active Accessibility creates a menu item object for the **Open** menu item from the **File** pop-up menu.

The window class name for a menu item is "\#32768".

## IAccessible Methods

A menu item supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | For menu items from the menu bar, [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) either displays or closes the menu depending on the state of the menu. For menu items from a pop-up menu, **accDoDefaultAction** clicks the menu item to execute the menu command. |
| [**acchittest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                                                                                                                                                                                                                                                |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                                                                                                                                                                                                                                                |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                                                                                                                                                                                                                                                |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                                                                                                                                                                                                                                                |



 

## IAccessible Properties

A menu item supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)                       | Retrieves the [**IDispatch**](idispatch-interface.md) interface to the pop-up menu object for this item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is one for menu items that display a menu or submenu; otherwise the **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)       | The **DefaultAction** property for menu items that display a menu or submenu is either "Open" or "Close" depending on the state of the menu. The **DefaultAction** property for all other menu items is "Execute".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the menu item's access key, which is the underlined character in the text of the menu item's name. For example, the **KeyboardShortcut** property for theFile menu item is "f".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is the same as the name of the menu item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is the menu bar or pop-up menu that contains the menu item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_MENUITEM**](object-roles.md#role-system-menuitem).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is either [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) or a combination of one or more of the following values: [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md#state-system-checked) \| [**STATE\_SYSTEM\_DEFAULT**](object-state-constants.md#state-system-default) \| [**STATE\_SYSTEM\_HOTTRACKED**](object-state-constants.md#state-system-hottracked) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_HASPOPUP**](object-state-constants.md#state-system-haspopup)<br/> |



 

## Notes

-   When used on a menu item, [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) returns S\_OK but fails to perform the action if the character used in the access key is ?, !, @, or any other character that requires the SHIFT key or another modifier key. This also happens on international keyboards with an access key character that requires the ALT GR key to be pressed.
-   The [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master) method with [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) does not cause a menu item to open or close a pop-up menu. Clients use the [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) method to open or close a pop-up menu.
-   A menu bar item that does not display a pop-up menu returns "Application" for the **Name** property instead of the name of the menu item.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> <dt>

[**Menu Bar**](menu-bar.md)
</dt> <dt>

[**Pop-up Menu**](pop-up-menu.md)
</dt> </dl>

 

 





