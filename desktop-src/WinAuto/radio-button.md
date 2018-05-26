---
title: Radio Button (MSAA UI Element Reference)
description: Radio buttons are used to select one of several options, usually within a dialog box.
ms.assetid: cf4568ff-1bc4-4770-bc54-a5d08ac0a60c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Radio Button (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Radio Button** objects for purposes of MSAA UI Element Reference. How to create **Radio Button** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Radio buttons are used to select one of several options, usually within a dialog box. A radio button contains a small circle with text next to it. When selected, the circle has a smaller, filled circle inside it. Selecting one button in a set deselects the previously selected button, so only one of the options in the set is selected at a time.

The window class name for a radio button is "BUTTON".

## IAccessible Methods

A radio button supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                                                                      |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | The [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) method clicks the radio button. |
| [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                                                               |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                                                               |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                                                               |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                                                               |



 

## IAccessible Properties

A radio button supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchild?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master)       | The **DefaultAction** property for a radio button is "Check".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accDescription**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdescription?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accHelp**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelp?branch=master)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accHelpTopic**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acchelptopic?branch=master)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) | The **KeyboardShortcut** property is the radio button's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the radio button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_RADIOBUTTON**](object-roles.md#role-system-radiobutton).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md#state-system-checked) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> <dt>

[**Check Box**](check-box.md)
</dt> <dt>

[**Group Box**](group-box.md)
</dt> <dt>

[**Push Button**](push-button.md)
</dt> </dl>

 

 





