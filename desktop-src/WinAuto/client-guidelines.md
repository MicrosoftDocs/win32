---
title: Client Guidelines
description: Client developers should use the following functionality to get information about the user interface elements
ms.assetid: 0e102e60-4d11-490e-88d5-dfadba620781
ms.topic: article
ms.date: 05/31/2018
---

# Client Guidelines

Client developers should use the following functionality to get information about the user interface elements:

-   To get an [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) interface to objects, call [**AccessibleObjectFromWindow**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromwindow), [**AccessibleObjectFromPoint**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfrompoint), or [**AccessibleObjectFromEvent**](/windows/desktop/api/Oleacc/nf-oleacc-accessibleobjectfromevent).
-   To examine and manipulate accessible objects, use the [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties and methods.
-   To receive [WinEvents](winevents-overview.md), call [**SetWinEventHook**](/windows/desktop/api/Winuser/nf-winuser-setwineventhook) to register a WinEvent callback function for those events that are relevant to the client application.

## In this section

-   [How Clients Obtain Child IDs](how-clients-obtain-child-ids.md)

 

 




