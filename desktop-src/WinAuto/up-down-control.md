---
title: Up-Down Control (MSAA UI Element Reference)
description: An up-down control, also known as a spin control, combines a pair of buttons displayed as arrows with a buddy edit control. Clicking the arrows increments or decrements the value in the edit control.
ms.assetid: '45e56c0f-4ac6-4731-b9a6-be4613bf40ae'
---

# Up-Down Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Up-Down Control** objects for purposes of MSAA UI Element Reference. How to create **Up-Down Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

An up-down control, also known as a spin control, combines a pair of buttons displayed as arrows with a buddy edit control. Clicking the arrows increments or decrements the value in the edit control.

The window class name for a up-down control is UPDOWN\_CLASS, which is defined as "msctls\_updown32" in Commctrl.h.

## IAccessible Methods

An up-down control supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

An up-down control supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md) | The **ChildCount** property is "2" (the up and down arrow buttons).                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accHelp**](iaccessible-iaccessible--get-acchelp.md)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accHelpTopic**](iaccessible-iaccessible--get-acchelptopic.md)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)             | The **Name** property for the up-down control object is obtained from the control's window text (or caption). This text is not displayed with the up-down control, so server developers must provide meaningful text in the control's resource definition statement to help users of client utilities identify the control. The **Name** property for the top arrow button in the up-down control is "More", and the **Name** property for the bottom arrow button is "Less". |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)         | The **Parent** property of the up-down control is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control. The **Parent** property of the up and down arrow buttons is the up-down control object.                                                                                                                                                    |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)             | The **Role** property for up-down control object is [**ROLE\_SYSTEM\_SPINBUTTON**](object-roles.md#role-system-spinbutton). The **Role** property for the arrow buttons is [**ROLE\_SYSTEM\_PUSHBUTTON**](object-roles.md#role-system-pushbutton).                                                                                                                                                                                                                          |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)           | The State property for up-down control object is one of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/>                                                                                                                                                                                      |
| [**get\_accValue**](iaccessible-iaccessible--get-accvalue.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

## Notes

Microsoft Active Accessibility exposes the buddy edit control as a separate object.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





