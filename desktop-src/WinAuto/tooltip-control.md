---
title: ToolTip Control (MSAA UI Element Reference)
description: A tooltip control displays a small pop-up window that contains a line of text that describes the purpose of a tool, represented as a graphical object, in an application.
ms.assetid: 'd3a65d7b-b882-4a1a-bac2-6995b64cf4af'
---

# ToolTip Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **ToolTip Control** objects for purposes of MSAA UI Element Reference. How to create **ToolTip Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A tooltip control displays a small pop-up window that contains a line of text that describes the purpose of a tool, represented as a graphical object, in an application.

The window class name for a tooltip is TOOLTIPS\_CLASS, which is defined as "tooltips\_class" in Commctrl.h.

## IAccessible Methods

A tooltip control supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

A tooltip control supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md) | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)             | The **Name** property is the text contained in the tooltip control.                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                               |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)             | The **Role** property is [**ROLE\_SYSTEM\_TOOLTIP**](object-roles.md#role-system-tooltip).                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





