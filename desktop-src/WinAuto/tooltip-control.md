---
title: ToolTip Control (MSAA UI Element Reference)
description: A tooltip control displays a small pop-up window that contains a line of text that describes the purpose of a tool, represented as a graphical object, in an application.
ms.assetid: d3a65d7b-b882-4a1a-bac2-6995b64cf4af
ms.topic: article
ms.date: 05/31/2018
---

# ToolTip Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **ToolTip Control** objects for purposes of MSAA UI Element Reference. How to create **ToolTip Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A tooltip control displays a small pop-up window that contains a line of text that describes the purpose of a tool, represented as a graphical object, in an application.

The window class name for a tooltip is TOOLTIPS\_CLASS, which is defined as "tooltips\_class" in Commctrl.h.

## IAccessible Methods

A tooltip control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

A tooltip control supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount) | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)             | The **Name** property is the text contained in the tooltip control.                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                               |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)             | The **Role** property is [**ROLE\_SYSTEM\_TOOLTIP**](object-roles.md).                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





