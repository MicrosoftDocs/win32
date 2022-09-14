---
title: Group Box (MSAA UI Element Reference)
description: A group box is a rectangle that surrounds a set of controls, such as check boxes or radio buttons, and contains an application-defined text (label).
ms.assetid: c6cd81a1-76c0-41c5-bb7f-4796ea7e3114
ms.topic: article
ms.date: 05/31/2018
---

# Group Box (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Group Box** objects for purposes of MSAA UI Element Reference. How to create **Group Box** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A group box is a rectangle that surrounds a set of controls, such as check boxes or radio buttons, and contains an application-defined text (label).

The sole purpose of a group box is to organize controls related by a common purpose, indicated by the label.

The window class name for a group box is "BUTTON".

## IAccessible Methods

A group box supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)

## IAccessible Properties

A group box supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)             | The **ChildCount** property is always zero.                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | Group boxes do not have keyboard shortcuts. However, if the window text for the group box contains an ampersand (&) character, Microsoft Active Accessibility returns a non-Null string as the **KeyboardShortcut** property.                                                                                                                                                                                                                                            |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | The **Name** property is obtained from the control's window text (or caption), which is displayed with the group box.                                                                                                                                                                                                                                                                                                                                                    |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)                     | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                              |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | The **Role** property is [**ROLE\_SYSTEM\_GROUPING**](object-roles.md).                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





