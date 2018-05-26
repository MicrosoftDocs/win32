---
title: Desktop Window (MSAA UI Element Reference)
description: The desktop window displays the desktop list view (which contains icons such as My Computer) and the taskbar that contains the Start button.
ms.assetid: 3668c26e-6462-4219-95d3-507811ed7f3c
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Desktop Window (MSAA UI Element Reference)

The desktop window displays the desktop list view (which contains icons such as My Computer) and the taskbar that contains the **Start** button.

This object is rarely queried by clients because the list view and the taskbar cover the entire desktop. The desktop object is retrieved when you log on, before the operating system shell displays the list view and taskbar. In some cases, the desktop is obtained when navigating from other objects.

The window class name for the desktop window is "\#32769".

## IAccessible Methods

The desktop window supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

The desktop window supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)             | The Name property is "Desktop".                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)             | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client).                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accSelection**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accselection?branch=master)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





