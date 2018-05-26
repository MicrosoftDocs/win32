---
title: Client Guidelines
description: Client developers should use the following functionality to get information about the user interface elements
ms.assetid: 0e102e60-4d11-490e-88d5-dfadba620781
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Guidelines

Client developers should use the following functionality to get information about the user interface elements:

-   To get an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface to objects, call [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master), [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master), or [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master).
-   To examine and manipulate accessible objects, use the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties and methods.
-   To receive [WinEvents](winevents.md), call [**SetWinEventHook**](/windows/win32/Winuser/nf-winuser-setwineventhook?branch=master) to register a WinEvent callback function for those events that are relevant to the client application.

## In this section

-   [How Clients Obtain Child IDs](how-clients-obtain-child-ids.md)

 

 




