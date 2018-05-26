---
title: Tab Control (MSAA UI Element Reference)
description: A tab control defines multiple pages for the same area of a window or dialog box.
ms.assetid: 664dd109-3c4a-4106-9b92-e10ec5a33463
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Tab Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Tab Control** objects for purposes of MSAA UI Element Reference. How to create **Tab Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A tab control defines multiple pages for the same area of a window or dialog box. Each page consists of a set of information or a group of controls that an application displays when the user selects the corresponding tab. The Windows operating system uses tab controls to display the taskbar buttons, with the exception of the **Start** button.

The window class name for a tab control is WC\_TABCONTROL, which is defined as "SysTabControl" in Commctrl.h.

## IAccessible Methods

A tab control supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                                                                  |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | The [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) method clicks the page tab. |
| [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                                                           |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                                                           |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                                                           |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                                                           |



 

## IAccessible Properties

A tab control supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)       | The **DefaultAction** property is "Switch".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelp**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelp?branch=master)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelpTopic**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelptopic?branch=master)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the tab control's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed within the tab control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_PAGETABLIST**](object-roles.md#role-system-pagetablist) ) that surrounds the control and has the same window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_PAGETAB**](object-roles.md#role-system-pagetab).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accSelection**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accselection?branch=master)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_SELECTABLE**](object-state-constants.md#state-system-selectable) \| [**STATE\_SYSTEM\_SELECTED**](object-state-constants.md#state-system-selected) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md#state-system-pressed)<br/> |



 

## Notes

Tab controls incorrectly return S\_OK from the [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master) method when called with the [**SELFLAG\_TAKEFOCUS**](selflag.md#selflag-takefocus) flag. Tab controls cannot take the keyboard focus.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





