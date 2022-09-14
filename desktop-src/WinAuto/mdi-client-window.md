---
title: MDI Client Window (MSAA UI Element Reference)
description: The multiple document interface (MDI) is a specification that defines the standard user interface for applications written for Windows. An MDI application enables a user to work with more than one document at a time.
ms.assetid: ede2dd19-e4c6-43e8-8f22-f807621dfa0d
ms.topic: article
ms.date: 05/31/2018
---

# MDI Client Window (MSAA UI Element Reference)

The multiple document interface (MDI) is a specification that defines the standard user interface for applications written for Windows. An MDI application enables a user to work with more than one document at a time.

An MDI application has three kinds of windows: a frame window, a client window, and a number of child windows. The frame window is like the main window of an application, and it surrounds the client window. The client window is a child of the frame window and serves as the background for the child windows. The client window also provides support for creating and manipulating the child windows in which documents are displayed.

The window class name for an MDI client window is "MDIClient".

## IAccessible Methods

An MDI client window supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

An MDI client window supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                 | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|--------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount) | The **ChildCount** property is the number of child windows in which documents are displayed.                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)           |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)             | The **Name** property is "Workspace".                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)         | The **Parent** property is the MDI frame window.                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)             | The **Role** property is [**ROLE\_SYSTEM\_CLIENT**](object-roles.md)                                                                                                                                                                                                                                                                                                                                                                                  |
| [**get\_accSelection**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accselection)   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)           | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md)<br/> |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





