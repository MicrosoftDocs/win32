---
title: Client Object (MSAA UI Element Reference)
description: The client area is the part of a window where the application displays output, such as text or graphics. For example, a desktop publishing application displays the current page of a document in the client area.
ms.assetid: '1b3a800e-e3c1-4737-8ad0-41707eb1e985'
---

# Client Object (MSAA UI Element Reference)

The client area is the part of a window where the application displays output, such as text or graphics. For example, a desktop publishing application displays the current page of a document in the client area.

Server application developers are responsible for creating accessible objects that provide information about the contents of the application's client area.

If a client application requests information about a custom UI element within an application, and the custom UI element that does not support the [**IAccessible**](iaccessible.md) interface, Microsoft Active Accessibility creates a default accessible object with minimal information.

## IAccessible Methods

The client area supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

The client area supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | Sends the [**WM\_GETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632627) message to retrieve the window text.                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client).                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





