---
title: Status Bar Control (MSAA UI Element Reference)
description: Status bars display status information in a horizontal window at the bottom of an application window.
ms.assetid: e910a5c6-84d5-4ade-abf5-792ff1915021
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Status Bar Control (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Status Bar Control** objects for purposes of MSAA UI Element Reference. How to create **Status Bar Control** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Status bars display status information in a horizontal window at the bottom of an application window. Status bars are often divided into parts, called panes, and each pane displays different status information. Additionally, status bars can contain objects of different types, including buttons and progress bars. The window class name for a status bar control is STATUSCLASSNAME, which is defined as "msctls\_statusbar32" in Commctrl.h.

## IAccessible Methods

Status bars support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

Status bars support the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master) | The **ChildCount** property is the number of panes in the status bar.                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)             | The status bar object itself does not have a **Name** property. The **Name** property of each pane in the status bar is the same as the displayed text.                                                                                                                                                                                                                                                                                                                   |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)         | The **Parent** property of the status bar object is a window ( [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window) ) that surrounds the control and has the same window class name as the control. The **Parent** property of the panes in the status bar is the status bar object.                                                                                                                                                                           |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)             | The **Role** property for the status bar object itself is [**ROLE\_SYSTEM\_STATUSBAR**](object-roles.md#role-system-statusbar). The text displayed in a status bar has [**ROLE\_SYSTEM\_STATICTEXT**](object-roles.md#role-system-statictext) as its **Role** property.                                                                                                                                                                                                 |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Notes

Because keyboard shortcuts are not supported for status bar controls or text areas on status bars, [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) is not supported.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





