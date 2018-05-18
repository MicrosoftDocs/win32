---
title: MDI Client Window (MSAA UI Element Reference)
description: The multiple document interface (MDI) is a specification that defines the standard user interface for applications written for Windows. An MDI application enables a user to work with more than one document at a time.
ms.assetid: 'ede2dd19-e4c6-43e8-8f22-f807621dfa0d'
---

# MDI Client Window (MSAA UI Element Reference)

The multiple document interface (MDI) is a specification that defines the standard user interface for applications written for Windows. An MDI application enables a user to work with more than one document at a time.

An MDI application has three kinds of windows: a frame window, a client window, and a number of child windows. The frame window is like the main window of an application, and it surrounds the client window. The client window is a child of the frame window and serves as the background for the child windows. The client window also provides support for creating and manipulating the child windows in which documents are displayed.

The window class name for an MDI client window is "MDIClient".

## IAccessible Methods

An MDI client window supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

An MDI client window supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md) | The **ChildCount** property is the number of child windows in which documents are displayed.                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)             | The **Name** property is "Workspace".                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)         | The **Parent** property is the MDI frame window.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)             | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md#role-system-client)                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accSelection**](iaccessible-iaccessible--get-accselection.md)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





