---
title: Up-Down Control (MSAA UI Element Reference)
description: An up-down control, also known as a spin control, combines a pair of buttons displayed as arrows with a buddy edit control. Clicking the arrows increments or decrements the value in the edit control.
ms.assetid: 45e56c0f-4ac6-4731-b9a6-be4613bf40ae
ms.topic: article
ms.date: 05/31/2018
---

# Up-Down Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Up-Down Control** objects for purposes of MSAA UI Element Reference. How to create **Up-Down Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

An up-down control, also known as a spin control, combines a pair of buttons displayed as arrows with a buddy edit control. Clicking the arrows increments or decrements the value in the edit control.

The window class name for a up-down control is UPDOWN\_CLASS, which is defined as "msctls\_updown32" in Commctrl.h.

## IAccessible Methods

An up-down control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

An up-down control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount) | The **ChildCount** property is "2" (the up and down arrow buttons).                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accHelp**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelp)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accHelpTopic**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acchelptopic)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)             | The **Name** property for the up-down control object is obtained from the control's window text (or caption). This text is not displayed with the up-down control, so server developers must provide meaningful text in the control's resource definition statement to help users of client utilities identify the control. The **Name** property for the top arrow button in the up-down control is "More", and the **Name** property for the bottom arrow button is "Less". |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)         | The **Parent** property of the up-down control is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same **Name** property and window class name as the control. The **Parent** property of the up and down arrow buttons is the up-down control object.                                                                                                                                                    |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)             | The **Role** property for up-down control object is [**ROLE\_SYSTEM\_SPINBUTTON**](object-roles.md). The **Role** property for the arrow buttons is [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md).                                                                                                                                                                                                                          |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)           | The State property for up-down control object is one of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)<br/>                                                                                                                                                                                      |
| [**get\_accValue**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accvalue)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

## Notes

Microsoft Active Accessibility exposes the buddy edit control as a separate object.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





