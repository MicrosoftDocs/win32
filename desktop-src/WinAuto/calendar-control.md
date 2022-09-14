---
title: Calendar Control (MSAA UI Element Reference)
description: Calendar controls provide a simple and intuitive way for a user to select a date from a familiar interface.
ms.assetid: cfb1e420-bb8f-4100-9c83-304d11573c0e
ms.topic: article
ms.date: 05/31/2018
---

# Calendar Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Calendar Control** objects for purposes of MSAA UI Element Reference. How to create **Calendar Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Calendar controls provide a simple and intuitive way for a user to select a date from a familiar interface.

The window class name for a month calendar control is MONTHCAL\_CLASS, which is defined as "SysMonthCal32" in Commctrl.h. Information in this topic applies to the month calendar control in version 5 of Commctrl.h.

## IAccessible Methods

Calendar controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

Calendar controls support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount) | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)             | The **Name** property is obtained from the static text control that labels the calendar control. When creating controls, server developers must ensure that a static text control immediately precedes the control that it labels within the tab order.                                                                                                                                                                                                                 |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                             |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)             | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md).                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md)[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





