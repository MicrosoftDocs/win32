---
title: Server Guidelines
description: For Microsoft Active Accessibility to work as designed, servers must provide accessibility information to clients.
ms.assetid: 88be4bae-fdeb-467c-b5b1-19f2adc0575d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Server Guidelines

For Microsoft Active Accessibility to work as designed, servers must provide accessibility information to clients.

To implement [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master), server developers must follow this basic process.

1.  Create accessible objects by implementing the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties and methods for your custom user interface elements and for your application's client. Be sure to provide a dual interface that supports both **IAccessible** and [**IDispatch**](idispatch-interface.md) so that clients written in Microsoft Visual Basic and various scripting languages can get information about the objects.
2.  Call [**NotifyWinEvent**](/windows/win32/Winuser/nf-winuser-notifywinevent?branch=master) to notify clients of changes to your custom user interface elements.
3.  Handle [**WM\_GETOBJECT**](wm-getobject.md) to provide access to your accessible objects.

For suggestions and guidelines for designing accessible objects, see [Developer's Guide for Active Accessibility Servers](developer-s-guide-for-active-accessibility-servers.md).

## In this section

-   [How Servers Implement Child IDs](how-servers-implement-child-ids.md)

 

 




