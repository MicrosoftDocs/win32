---
title: Radio Button (MSAA UI Element Reference)
description: Radio buttons are used to select one of several options, usually within a dialog box.
ms.assetid: 'cf4568ff-1bc4-4770-bc54-a5d08ac0a60c'
---

# Radio Button (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Radio Button** objects for purposes of MSAA UI Element Reference. How to create **Radio Button** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Radio buttons are used to select one of several options, usually within a dialog box. A radio button contains a small circle with text next to it. When selected, the circle has a smaller, filled circle inside it. Selecting one button in a set deselects the previously selected button, so only one of the options in the set is selected at a time.

The window class name for a radio button is "BUTTON".

## IAccessible Methods

A radio button supports the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                                                                      |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | The [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) method clicks the radio button. |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)                 |                                                                                                               |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                                                               |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                                                               |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                                                               |



 

## IAccessible Properties

A radio button supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md)       | The **DefaultAction** property for a radio button is "Check".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The **KeyboardShortcut** property is the radio button's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the radio button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_RADIOBUTTON**](object-roles.md#role-system-radiobutton).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md#state-system-checked) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md#state-system-normal)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> <dt>

[**Check Box**](check-box.md)
</dt> <dt>

[**Group Box**](group-box.md)
</dt> <dt>

[**Push Button**](push-button.md)
</dt> </dl>

 

 





