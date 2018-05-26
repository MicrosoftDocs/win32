---
title: Client Object (MSAA UI Element Reference)
description: The client area is the part of a window where the application displays output, such as text or graphics. For example, a desktop publishing application displays the current page of a document in the client area.
ms.assetid: 1b3a800e-e3c1-4737-8ad0-41707eb1e985
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Object (MSAA UI Element Reference)

The client area is the part of a window where the application displays output, such as text or graphics. For example, a desktop publishing application displays the current page of a document in the client area.

Server application developers are responsible for creating accessible objects that provide information about the contents of the application's client area.

If a client application requests information about a custom UI element within an application, and the custom UI element that does not support the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface, Microsoft Active Accessibility creates a default accessible object with minimal information.

## IAccessible Methods

The client area supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

The client area supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)             |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accKeyboardShortcut**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut?branch=master) |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                         | Sends the [**WM\_GETTEXT**](https://msdn.microsoft.com/library/windows/desktop/ms632627) message to retrieve the window text.                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                         | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client).                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md):[**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





