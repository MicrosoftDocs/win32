---
title: Calendar Control (MSAA UI Element Reference)
description: Calendar controls provide a simple and intuitive way for a user to select a date from a familiar interface.
ms.assetid: 'cfb1e420-bb8f-4100-9c83-304d11573c0e'
---

# Calendar Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Calendar Control** objects for purposes of MSAA UI Element Reference. How to create **Calendar Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Calendar controls provide a simple and intuitive way for a user to select a date from a familiar interface.

The window class name for a month calendar control is MONTHCAL\_CLASS, which is defined as "SysMonthCal32" in Commctrl.h. Information in this topic applies to the month calendar control in version 5 of Commctrl.h.

## IAccessible Methods

Calendar controls support the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

Calendar controls support the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md) | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)             | The **Name** property is obtained from the static text control that labels the calendar control. When creating controls, server developers must ensure that a static text control immediately precedes the control that it labels within the tab order.                                                                                                                                                                                                                 |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                             |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)             | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client).                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md)[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





