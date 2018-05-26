---
title: Switch Window (MSAA UI Element Reference)
description: The switch window displays whenever a user presses ALT+TAB to switch to a different application. The switch window contains an icon for each application currently running.
ms.assetid: 77b32eb1-7722-410b-b141-ac09fc7fdffb
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Switch Window (MSAA UI Element Reference)

The switch window displays whenever a user presses ALT+TAB to switch to a different application. The switch window contains an icon for each application currently running.

The window class name for the switch window is "\#32771".

## IAccessible Methods

The switch window supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) methods:



| Method                                                                    | Comments                                                                                                                                                                                                                          |
|---------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) | The switch window object itself does not have a **DefaultAction** property. The [**accDoDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accdodefaultaction?branch=master) method for each item in the switch window activates the specified item. |
| [**accHitTest**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acchittest?branch=master)                 |                                                                                                                                                                                                                                   |
| [**accLocation**](/windows/win32/Oleacc/nf-oleacc-iaccessible-acclocation?branch=master)               |                                                                                                                                                                                                                                   |
| [**accNavigate**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accnavigate?branch=master)               |                                                                                                                                                                                                                                   |
| [**accSelect**](/windows/win32/Oleacc/nf-oleacc-iaccessible-accselect?branch=master)                   |                                                                                                                                                                                                                                   |



 

## IAccessible Properties

The switch window supports the following [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) properties:



|                                                                                |                                                                                                                                                                                                                                |
|--------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**get\_accChildCount**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accchildcount?branch=master)       | The **ChildCount** property is zero.                                                                                                                                                                                           |
| [**get\_accDefaultAction**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accdefaultaction?branch=master) | The switch window object itself does not have a **DefaultAction** property. The **DefaultAction** property for each item in the switch window is "Switch".                                                                     |
| [**get\_accFocus**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accfocus?branch=master)                 | The switch window parent object cannot receive focus; only the individual children can receive focus.                                                                                                                          |
| [**get\_accName**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accname?branch=master)                   | The switch window object itself does not have a **Name** property. The **Name** property for each application icon in the switch window is the same as the displayed application name.                                         |
| [**get\_accRole**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accrole?branch=master)                   | The switch window object itself has a **Role** property of "window \[32771\]". Also, each application icon in the switch window has the **Role** property [**ROLE\_SYSTEM\_LISTITEM**](object-roles.md#role-system-listitem). |
| [**get\_accState**](/windows/win32/Oleacc/nf-oleacc-iaccessible-get_accstate?branch=master)                 | The switch window object itself does not support the **State** property. The **State** value for the list view items is [**STATE\_SYSTEM\_FOCUSABLE**](object-state-constants.md#state-system-focusable).                     |



 

## Related topics

<dl> <dt>

[IAccessible Interface](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master)
</dt> </dl>

 

 




