---
title: Client Guidelines
description: Client developers should use the following functionality to get information about the user interface elements
ms.assetid: '0e102e60-4d11-490e-88d5-dfadba620781'
---

# Client Guidelines

Client developers should use the following functionality to get information about the user interface elements:

-   To get an [**IAccessible**](iaccessible.md) interface to objects, call [**AccessibleObjectFromWindow**](accessibleobjectfromwindow.md), [**AccessibleObjectFromPoint**](accessibleobjectfrompoint.md), or [**AccessibleObjectFromEvent**](accessibleobjectfromevent.md).
-   To examine and manipulate accessible objects, use the [**IAccessible**](iaccessible.md) properties and methods.
-   To receive [WinEvents](winevents.md), call [**SetWinEventHook**](setwineventhook.md) to register a WinEvent callback function for those events that are relevant to the client application.

## In this section

-   [How Clients Obtain Child IDs](how-clients-obtain-child-ids.md)

 

 




