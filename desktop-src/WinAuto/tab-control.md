---
title: Tab Control (MSAA UI Element Reference)
description: A tab control defines multiple pages for the same area of a window or dialog box.
ms.assetid: 664dd109-3c4a-4106-9b92-e10ec5a33463
ms.topic: article
ms.date: 05/31/2018
---

# Tab Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Tab Control** objects for purposes of MSAA UI Element Reference. How to create **Tab Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A tab control defines multiple pages for the same area of a window or dialog box. Each page consists of a set of information or a group of controls that an application displays when the user selects the corresponding tab. The Windows operating system uses tab controls to display the taskbar buttons, with the exception of the **Start** button.

The window class name for a tab control is WC\_TABCONTROL, which is defined as "SysTabControl" in Commctrl.h.

## IAccessible Methods

A tab control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:



| Method                                                                    | Comments                                                                                                  |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) | The [**accDoDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accdodefaultaction) method clicks the page tab. |
| [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)                 |                                                                                                           |
| [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)               |                                                                                                           |
| [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)               |                                                                                                           |
| [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)                   |                                                                                                           |



 

## IAccessible Properties

A tab control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|--------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accDefaultAction**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction)       | The **DefaultAction** property is "Switch".                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp)                         |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accHelpTopic**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelptopic)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | The **KeyboardShortcut** property is the tab control's access key, which is an underlined character in the control's window text. This string contains the access key character appended to the string "Alt+".                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed within the tab control.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_PAGETABLIST**](object-roles.md) ) that surrounds the control and has the same window class name as the control.                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | The **Role** property is [**ROLE\_SYSTEM\_PAGETAB**](object-roles.md).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection)               |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_SELECTABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_SELECTED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_PRESSED**](object-state-constants.md)<br/> |



 

## Notes

Tab controls incorrectly return S\_OK from the [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect) method when called with the [**SELFLAG\_TAKEFOCUS**](selflag.md) flag. Tab controls cannot take the keyboard focus.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





