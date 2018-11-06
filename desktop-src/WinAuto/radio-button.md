---
title: Radio Button (MSAA UI Element Reference)
description: Radio buttons are used to select one of several options, usually within a dialog box.
ms.assetid: cf4568ff-1bc4-4770-bc54-a5d08ac0a60c
ms.topic: article
ms.date: 05/31/2018
---

# Radio Button (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Radio Button** objects for purposes of MSAA UI Element Reference. How to create **Radio Button** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Radio buttons are used to select one of several options, usually within a dialog box. A radio button contains a small circle with text next to it. When selected, the circle has a smaller, filled circle inside it. Selecting one button in a set deselects the previously selected button, so only one of the options in the set is selected at a time.

The window class name for a radio button is "BUTTON".

## IAccessible Methods

A radio button supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:



| Method                                                                    | Comments                                                                                                      |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) | The [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) method clicks the radio button. |
| [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)                 |                                                                                                               |
| [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)               |                                                                                                               |
| [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)               |                                                                                                               |
| [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)                   |                                                                                                               |



 

## IAccessible Properties

A radio button supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)             | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction)       | The **DefaultAction** property for a radio button is "Check".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accHelpTopic**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelptopic)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | The **KeyboardShortcut** property is the radio button's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the radio button.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | The **Role** property is [**ROLE\_SYSTEM\_RADIOBUTTON**](object-roles.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_CHECKED**](object-state-constants.md) \| [**STATE\_SYSTEM\_NORMAL**](object-state-constants.md)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> <dt>

[**Check Box**](check-box.md)
</dt> <dt>

[**Group Box**](group-box.md)
</dt> <dt>

[**Push Button**](push-button.md)
</dt> </dl>

 

 





