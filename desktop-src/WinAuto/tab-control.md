---
title: Tab Control (MSAA UI Element Reference)
description: A tab control defines multiple pages for the same area of a window or dialog box.
ms.assetid: '664dd109-3c4a-4106-9b92-e10ec5a33463'
---

# Tab Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Tab Control** objects for purposes of MSAA UI Element Reference. How to create **Tab Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A tab control defines multiple pages for the same area of a window or dialog box. Each page consists of a set of information or a group of controls that an application displays when the user selects the corresponding tab. The Windows operating system uses tab controls to display the taskbar buttons, with the exception of the **Start** button.

The window class name for a tab control is WC\_TABCONTROL, which is defined as "SysTabControl" in Commctrl.h.

## IAccessible Methods

A tab control supports the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                                                                  |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | The [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) method clicks the page tab. |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)                 |                                                                                                           |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                                                           |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                                                           |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                                                           |



 

## IAccessible Properties

A tab control supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)       | The **DefaultAction** property is "Switch".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the tab control's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed within the tab control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_PAGETABLIST**](object-roles.md#role-system-pagetablist) ) that surrounds the control and has the same window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_PAGETAB**](object-roles.md#role-system-pagetab).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accSelection**](iaccessible-iaccessible--get-accselection.md)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_SELECTABLE**](object-state-constants.md#state-system-selectable) \| [**STATE\_SYSTEM\_SELECTED**](object-state-constants.md#state-system-selected) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md#state-system-pressed)<br/> |



 

## Notes

Tab controls incorrectly return S\_OK from the [**accSelect**](iaccessible-iaccessible--accselect.md) method when called with the [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) flag. Tab controls cannot take the keyboard focus.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





