---
title: Server Functions
description: Server Functions
ms.assetid: 3cfa42c4-3d8b-44a1-9b8e-19248da12334
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Server Functions

This section contains information about the server functions used with Microsoft Active Accessibility.

## In this section



| Topic                                                                     | Description                                                                                                                                                                                                                                                                                                                                                   |
|---------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AccNotifyTouchInteraction**](/windows/win32/Oleacc/nf-oleacc-accnotifytouchinteraction?branch=master)<br/> | Allows an assistive technology (AT) application to notify the system that it is interacting with UI through a Windows Automation API (such as Microsoft UI Automation) as a result of a touch gesture from the user. This allows the assistive technology to notify the target application and the system that the user is interacting with touch.<br/> |
| [**AccSetRunningUtilityState**](/windows/win32/Oleacc/nf-oleacc-accsetrunningutilitystate?branch=master)<br/> | Sets system values that indicate whether an assistive technology (AT) application's current state affects functionality that is typically provided by the system. <br/>                                                                                                                                                                                 |
| [**CreateStdAccessibleObject**](/windows/win32/Oleacc/nf-oleacc-createstdaccessibleobject?branch=master)<br/> | Creates an accessible object with the methods and properties of the specified type of system-provided user interface element.<br/>                                                                                                                                                                                                                      |
| [**CreateStdAccessibleProxy**](/windows/win32/Oleacc/nf-oleacc-createstdaccessibleproxya?branch=master)<br/>   | Creates an accessible object that has the properties and methods of the specified class of system-provided user interface element.<br/>                                                                                                                                                                                                                 |
| [**LresultFromObject**](/windows/win32/Oleacc/nf-oleacc-lresultfromobject?branch=master)<br/>                 | Returns a reference, similar to a handle, to the specified object. Servers return this reference when handling [**WM\_GETOBJECT**](wm-getobject.md).<br/>                                                                                                                                                                                              |
| [**ObjectFromLresult**](/windows/win32/Oleacc/nf-oleacc-objectfromlresult?branch=master)<br/>                 | Retrieves a requested interface pointer for an accessible object based on a previously generated object reference.<br/> This function is designed for internal use by Microsoft Active Accessibility and is documented for informational purposes only. Neither clients nor servers should call this function.<br/>                               |
| [**IsWinEventHookInstalled**](/windows/win32/Winuser/nf-winuser-iswineventhookinstalled?branch=master)<br/>     | Determines whether there is an installed WinEvent hook that might be notified of a specified event.<br/>                                                                                                                                                                                                                                                |
| [**NotifyWinEvent**](/windows/win32/Winuser/nf-winuser-notifywinevent?branch=master)<br/>                       | Signals the system that a predefined event occurred. If any client applications have registered a hook function for the event, the system calls the client's hook function.<br/>                                                                                                                                                                        |



 

## Related topics

<dl> <dt>

[Active Accessibility User Interface Services](active-accessibility-user-interface-services-collision208.md)
</dt> </dl>

 

 





