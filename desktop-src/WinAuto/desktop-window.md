---
title: Desktop Window (MSAA UI Element Reference)
description: The desktop window displays the desktop list view (which contains icons such as My Computer) and the taskbar that contains the Start button.
ms.assetid: '3668c26e-6462-4219-95d3-507811ed7f3c'
---

# Desktop Window (MSAA UI Element Reference)

The desktop window displays the desktop list view (which contains icons such as My Computer) and the taskbar that contains the **Start** button.

This object is rarely queried by clients because the list view and the taskbar cover the entire desktop. The desktop object is retrieved when you log on, before the operating system shell displays the list view and taskbar. In some cases, the desktop is obtained when navigating from other objects.

The window class name for the desktop window is "\#32769".

## IAccessible Methods

The desktop window supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

The desktop window supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)             | The Name property is "Desktop".                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)             | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client).                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accSelection**](iaccessible-iaccessible--get-accselection.md)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





