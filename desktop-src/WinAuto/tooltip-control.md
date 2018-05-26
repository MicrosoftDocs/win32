---
title: ToolTip Control (MSAA UI Element Reference)
description: A tooltip control displays a small pop-up window that contains a line of text that describes the purpose of a tool, represented as a graphical object, in an application.
ms.assetid: d3a65d7b-b882-4a1a-bac2-6995b64cf4af
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# ToolTip Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **ToolTip Control** objects for purposes of MSAA UI Element Reference. How to create **ToolTip Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

A tooltip control displays a small pop-up window that contains a line of text that describes the purpose of a tool, represented as a graphical object, in an application.

The window class name for a tooltip is TOOLTIPS\_CLASS, which is defined as "tooltips\_class" in Commctrl.h.

## IAccessible Methods

A tooltip control supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

A tooltip control supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master) | The **ChildCount** property is zero.                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)             | The **Name** property is the text contained in the tooltip control.                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)         | The **Parent** property is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same **Name** property and window class name as the control.                                                                                                                                                                                                                                                               |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)             | The **Role** property is [**ROLE\_SYSTEM\_TOOLTIP**](object-roles.md#role-system-tooltip).                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





