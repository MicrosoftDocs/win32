---
title: Menu Item (MSAA UI Element Reference)
description: A menu item represents a particular item in a menu bar or pop-up menu.
ms.assetid: '330782d6-4293-4e65-ab49-a616d133d273'
---

# Menu Item (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Menu Item** objects for purposes of MSAA UI Element Reference. How to create **Menu Item** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A menu item represents a particular item in a menu bar or pop-up menu. For example, Microsoft Active Accessibility creates a menu item object for the **File** menu in the menu bar. Similarly, Microsoft Active Accessibility creates a menu item object for the **Open** menu item from the **File** pop-up menu.

The window class name for a menu item is "\#32768".

## IAccessible Methods

A menu item supports the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                                                                                       |
|---------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | For menu items from the menu bar, [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) either displays or closes the menu depending on the state of the menu. For menu items from a pop-up menu, **accDoDefaultAction** clicks the menu item to execute the menu command. |
| [**acchittest**](iaccessible-iaccessible--acchittest.md)                 |                                                                                                                                                                                                                                                                                                |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                                                                                                                                                                                                                                                |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                                                                                                                                                                                                                                                |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                                                                                                                                                                                                                                                |



 

## IAccessible Properties

A menu item supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       | Retrieves the [**IDispatch**](idispatch-interface.md) interface to the pop-up menu object for this item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is one for menu items that display a menu or submenu; otherwise the **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)       | The **DefaultAction** property for menu items that display a menu or submenu is either "Open" or "Close" depending on the state of the menu. The **DefaultAction** property for all other menu items is "Execute".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the menu item's access key, which is the underlined character in the text of the menu item's name. For example, the **KeyboardShortcut** property for theFile menu item is "f".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is the same as the name of the menu item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is the menu bar or pop-up menu that contains the menu item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_MENUITEM**](object-roles.md#role-system-menuitem).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is either [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) or a combination of one or more of the following values: [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md#state-system-checked) \| [**STATE\_SYSTEM\_DEFAULT**](object-state-constants.md#state-system-default) \| [**STATE\_SYSTEM\_HOTTRACKED**](object-state-constants.md#state-system-hottracked) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_HASPOPUP**](object-state-constants.md#state-system-haspopup)<br/> |



 

## Notes

-   When used on a menu item, [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) returns S\_OK but fails to perform the action if the character used in the access key is ?, !, @, or any other character that requires the SHIFT key or another modifier key. This also happens on international keyboards with an access key character that requires the ALT GR key to be pressed.
-   The [**accSelect**](iaccessible-iaccessible--accselect.md) method with [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) does not cause a menu item to open or close a pop-up menu. Clients use the [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) method to open or close a pop-up menu.
-   A menu bar item that does not display a pop-up menu returns "Application" for the **Name** property instead of the name of the menu item.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> <dt>

[**Menu Bar**](menu-bar.md)
</dt> <dt>

[**Pop-up Menu**](pop-up-menu.md)
</dt> </dl>

 

 





