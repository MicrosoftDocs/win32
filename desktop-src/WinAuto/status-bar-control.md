---
title: Status Bar Control (MSAA UI Element Reference)
description: Status bars display status information in a horizontal window at the bottom of an application window.
ms.assetid: e910a5c6-84d5-4ade-abf5-792ff1915021
ms.topic: article
ms.date: 05/31/2018
---

# Status Bar Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Status Bar Control** objects for purposes of MSAA UI Element Reference. How to create **Status Bar Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Status bars display status information in a horizontal window at the bottom of an application window. Status bars are often divided into parts, called panes, and each pane displays different status information. Additionally, status bars can contain objects of different types, including buttons and progress bars. The window class name for a status bar control is STATUSCLASSNAME, which is defined as "msctls\_statusbar32" in Commctrl.h.

## IAccessible Methods

Status bars support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

Status bars support the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount) | The **ChildCount** property is the number of panes in the status bar.                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)             | The status bar object itself does not have a **Name** property. The **Name** property of each pane in the status bar is the same as the displayed text.                                                                                                                                                                                                                                                                                                                   |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)         | The **Parent** property of the status bar object is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md) ) that surrounds the control and has the same window class name as the control. The **Parent** property of the panes in the status bar is the status bar object.                                                                                                                                                                           |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)             | The **Role** property for the status bar object itself is [**ROLE\_SYSTEM\_STATUSBAR**](object-roles.md). The text displayed in a status bar has [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md) as its **Role** property.                                                                                                                                                                                                 |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)<br/> |



 

## Notes

Because keyboard shortcuts are not supported for status bar controls or text areas on status bars, [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) is not supported.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





