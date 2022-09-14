---
title: Window (MSAA UI Element Reference)
description: Microsoft Active Accessibility creates a generic window object as a container for another object. Client developers do not convey the information from window objects to end users because these objects do not contain useful information.
ms.assetid: 'cc32528f-c454-4522-91b9-06f87cff8bf5'
ms.topic: article
ms.date: 05/31/2018
---

# Window (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Window** objects for purposes of MSAA UI Element Reference. How to create **Window** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Microsoft Active Accessibility creates a generic window object as a container for another object. Client developers do not convey the information from window objects to end users because these objects do not contain useful information.

If a server application creates a custom control, Microsoft Active Accessibility creates a window object that contains the custom control, but the server creates an accessible object to provide information about the contents of the control. The system generates object-level events for the window object, but the server must send events for the accessible object that provides information about the control.

## IAccessible Methods

The window object supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) methods:

-   [**accHitTest**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acchittest)
-   [**accLocation**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-acclocation)
-   [**accNavigate**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accnavigate)
-   [**accSelect**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-accselect)

## IAccessible Properties

The window object supports the following [**IAccessible**](/windows/desktop/api/oleacc/nn-oleacc-iaccessible) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchild)                       | Retrieves the [IDispatch](idispatch-interface.md) interface of the specified child.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accChildCount**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accchildcount)             | The **ChildCount** property is 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accDescription**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accdescription)           | The window object itself does not have a **Description** property. The **Description** property for the child object can be retrieved through the window object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accFocus**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accfocus)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accKeyboardShortcut**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_acckeyboardshortcut) | The window object itself does not have a **KeyboardShortcut** property. The **KeyboardShortcut** property for the child object is retrieved through the window object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accName**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accname)                         | The **Name** property of the window object is the same as the child object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accParent**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accparent)                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accRole**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accrole)                         | The **Role** property is [**ROLE\_SYSTEM\_WINDOW**](object-roles.md). The **Role** of the child object is retrieved through the window object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accState**](/windows/desktop/api/Oleacc/nf-oleacc-iaccessible-get_accstate)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_SIZEABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_MOVEABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md)<br/> |



 

## Notes

The events [**EVENT\_SYSTEM\_DRAGDROPSTART**](event-constants.md), [**EVENT\_SYSTEM\_DRAGDROPEND**](event-constants.md), [**EVENT\_OBJECT\_HIDE**](event-constants.md), and [**EVENT\_OBJECT\_PARENTCHANGE**](event-constants.md) are not sent by the window object. This is a known issue and is being addressed.

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/desktop/api/oleacc/nn-oleacc-iaccessible)
</dt> </dl>

 

 





