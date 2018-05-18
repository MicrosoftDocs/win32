---
title: Switch Window (MSAA UI Element Reference)
description: The switch window displays whenever a user presses ALT+TAB to switch to a different application. The switch window contains an icon for each application currently running.
ms.assetid: '77b32eb1-7722-410b-b141-ac09fc7fdffb'
---

# Switch Window (MSAA UI Element Reference)

The switch window displays whenever a user presses ALT+TAB to switch to a different application. The switch window contains an icon for each application currently running.

The window class name for the switch window is "\#32771".

## IAccessible Methods

The switch window supports the following [**IAccessible**](iaccessible.md) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) | The switch window object itself does not have a **DefaultAction** property. The [**accDoDefaultAction**](iaccessible-iaccessible--accdodefaultaction.md) method for each item in the switch window activates the specified item. |
| [**accHitTest**](iaccessible-iaccessible--acchittest.md)                 |                                                                                                                                                                                                                                   |
| [**accLocation**](iaccessible-iaccessible--acclocation.md)               |                                                                                                                                                                                                                                   |
| [**accNavigate**](iaccessible-iaccessible--accnavigate.md)               |                                                                                                                                                                                                                                   |
| [**accSelect**](iaccessible-iaccessible--accselect.md)                   |                                                                                                                                                                                                                                   |



 

## IAccessible Properties

The switch window supports the following [**IAccessible**](iaccessible.md) properties:



|                                                                                |                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](iaccessible-iaccessible--get-accchildcount.md)       | The **ChildCount** property is zero.                                                                                                                                                                                           |
| [**get\_accDefaultAction**](iaccessible-iaccessible--get-accdefaultaction.md) | The switch window object itself does not have a **DefaultAction** property. The **DefaultAction** property for each item in the switch window is "Switch".                                                                     |
| [**get\_accFocus**](iaccessible-iaccessible--get-accfocus.md)                 | The switch window parent object cannot receive focus; only the individual children can receive focus.                                                                                                                          |
| [**get\_accName**](iaccessible-iaccessible--get-accname.md)                   | The switch window object itself does not have a **Name** property. The **Name** property for each application icon in the switch window is the same as the displayed application name.                                         |
| [**get\_accRole**](iaccessible-iaccessible--get-accrole.md)                   | The switch window object itself has a **Role** property of "window \[32771\]". Also, each application icon in the switch window has the **Role** property [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md#role-system-listitem). |
| [**get\_accState**](iaccessible-iaccessible--get-accstate.md)                 | The switch window object itself does not support the **State** property. The **State** value for the list view items is [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable).                     |



 

## Related topics

<dl> <dt>

[IAccessible Interface](iaccessible.md)
</dt> </dl>

 

 




