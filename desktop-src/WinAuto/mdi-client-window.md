---
title: MDI Client Window (MSAA UI Element Reference)
description: The multiple document interface (MDI) is a specification that defines the standard user interface for applications written for Windows. An MDI application enables a user to work with more than one document at a time.
ms.assetid: ede2dd19-e4c6-43e8-8f22-f807621dfa0d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# MDI Client Window (MSAA UI Element Reference)

The multiple document interface (MDI) is a specification that defines the standard user interface for applications written for Windows. An MDI application enables a user to work with more than one document at a time.

An MDI application has three kinds of windows: a frame window, a client window, and a number of child windows. The frame window is like the main window of an application, and it surrounds the client window. The client window is a child of the frame window and serves as the background for the child windows. The client window also provides support for creating and manipulating the child windows in which documents are displayed.

The window class name for an MDI client window is "MDIClient".

## IAccessible Methods

An MDI client window supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:

-   [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)
-   [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)
-   [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)
-   [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)

## IAccessible Properties

An MDI client window supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master) | The **ChildCount** property is the number of child windows in which documents are displayed.                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)             | The **Name** property is "Workspace".                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accParent**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accparent?branch=master)         | The **Parent** property is the MDI frame window.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)             | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client)                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accSelection**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accselection?branch=master)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 





