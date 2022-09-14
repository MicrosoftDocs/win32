---
title: How Active Accessibility Works
description: Microsoft Active Accessibility is designed to help accessibility aids, called clients, interact with standard and custom UI elements of other applications and the operating system.
ms.assetid: 29325f0a-c6ca-42b1-b85d-2671f7041034
ms.topic: article
ms.date: 05/31/2018
---

# How Active Accessibility Works

Microsoft Active Accessibility is designed to help accessibility aids, called *clients*, interact with standard and custom UI elements of other applications and the operating system. A Microsoft Active Accessibility client is any program that uses Microsoft Active Accessibility to access, identify, or manipulate the UI elements of an application. Clients include accessibility aids, automated testing tools, and some computer-based training applications.

Using Microsoft Active Accessibility, a client application can:

-   Query for information; for example, about a UI element at a particular location.
-   Receive notifications when information changes; for example, when a control becomes grayed or when a text string changes.
-   Carry out actions that affect user interface or document contents; for example, click a push button, drop down a menu, and choose a menu command.

The applications that interact with and provide information for clients are called *servers*. A server uses Microsoft Active Accessibility to provide information about its UI elements to clients. Any control, module, or application that uses Microsoft Active Accessibility to expose information about its user interface is considered a Microsoft Active Accessibility server. Servers communicate with clients by sending event notifications (such as calling [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent)) and responding to client requests for access to UI elements (such as handling [**WM\_GETOBJECT**](wm-getobject.md) messages sent from [*OLEACC*](uiauto-glossary.md)). Servers expose information through the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface.

Using Microsoft Active Accessibility, a server application can:

-   Provide information about its custom user interface objects and the contents of its client windows.
-   Send notifications when its user interface changes.

For example, to enable a user to select commands verbally from a word processor custom toolbar, a speech recognition program must have information about that toolbar. The word processor would therefore need to make that information available. Microsoft Active Accessibility provides the means for the word processor to expose information about its custom toolbar and for the speech recognition program to get that information.

### Client Applications and Active Accessibility

A Microsoft Active Accessibility client must be notified when the server UI has changed so that it can convey that information to the user. To ensure that the client is informed about UI changes, it uses a mechanism called Window Events, or WinEvents, to register to receive notifications. For more information, see [WinEvents](winevents-infrastructure.md).

To learn about and manipulate a particular UI element, clients use the Microsoft Active Accessibility Component Object Model (COM) interface, [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible).

A client can retrieve an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) object for a UI element in the following four ways:

-   Call [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow) and pass the UI element's window handle.
-   Call [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint) and pass a screen location that lies within the UI element's bounding rectangle.
-   Set a WinEvent hook, receive a notification, and call [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent) to retrieve an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface pointer for the UI element that generated the event.
-   Call an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) method such as [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate) or [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent) to move to a different **IAccessible** object.

 

 




