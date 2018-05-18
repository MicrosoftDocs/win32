---
title: Window (MSAA UI Element Reference)
description: Microsoft Active Accessibility creates a generic window object as a container for another object. Client developers do not convey the information from window objects to end users because these objects do not contain useful information.
ms.assetid: '297ac50f-2a58-477b-ba57-5d1416c191b3'
---

# Window (MSAA UI Element Reference)

> [!Note]  
> This topic describes **Window** objects for purposes of MSAA UI Element Reference. How to create **Window** objects in various UI frameworks is not described here. See the API reference documentation for the UI framework you're using.

 

Microsoft Active Accessibility creates a generic window object as a container for another object. Client developers do not convey the information from window objects to end users because these objects do not contain useful information.

If a server application creates a custom control, Microsoft Active Accessibility creates a window object that contains the custom control, but the server creates an accessible object to provide information about the contents of the control. The system generates object-level events for the window object, but the server must send events for the accessible object that provides information about the control.

## IAccessible Methods

The window object supports the following [**IAccessible**](iaccessible.md) methods:

-   [**accHitTest**](iaccessible-iaccessible--acchittest.md)
-   [**accLocation**](iaccessible-iaccessible--acclocation.md)
-   [**accNavigate**](iaccessible-iaccessible--accnavigate.md)
-   [**accSelect**](iaccessible-iaccessible--accselect.md)

## IAccessible Properties

The window object supports the following [**IAccessible**](iaccessible.md) properties:



| Property                                                                             | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChild**](iaccessible-iaccessible--get-accchild.md)                       | Retrieves the [IDispatch](idispatch-interface.md) interface of the specified child.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)             | The **ChildCount** property is 7.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| [**get\_accDescription**](iaccessible-iaccessible--get-accdescription.md)           | The window object itself does not have a **Description** property. The **Description** property for the child object can be retrieved through the window object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                       |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accKeyboardShortcut**](iaccessible-iaccessible--get-acckeyboardshortcut.md) | The window object itself does not have a **KeyboardShortcut** property. The **KeyboardShortcut** property for the child object is retrieved through the window object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                         | The **Name** property of the window object is the same as the child object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**get\_accParent**](iaccessible-iaccessible--get-accparent.md)                     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                         | The **Role** property is [**ROLE\_SYSTEM\_WINDOW**](object-roles.md#role-system-window). The **Role** of the child object is retrieved through the window object.                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                       | The **State** property is a combination of one or more of the following [values](object-state-constants.md): [**STATE\_SYSTEM\_INVISIBLE**](object-state-constants.md#state-system-invisible) \| [**STATE\_SYSTEM\_UNAVAILABLE**](object-state-constants.md#state-system-unavailable) \| [**STATE\_SYSTEM\_SIZEABLE**](object-state-constants.md#state-system-sizeable) \| [**STATE\_SYSTEM\_MOVEABLE**](object-state-constants.md#state-system-moveable) \| [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable) \| [**STATE\_SYSTEM\_FOCUSED**](object-state-constants.md#state-system-focused)<br/> |



 

## Notes

The events [**EVENT\_SYSTEM\_DRAGDROPSTART**](event-constants.md#event-system-dragdropstart), [**EVENT\_SYSTEM\_DRAGDROPEND**](event-constants.md#event-system-dragdropend), [**EVENT\_OBJECT\_HIDE**](event-constants.md#event-object-hide), and [**EVENT\_OBJECT\_PARENTCHANGE**](event-constants.md#event-object-parentchange) are not sent by the window object. This is a known issue and is being addressed.

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 





