---
title: Client Functions
description: Client Functions
ms.assetid: c6d3577c-6975-4708-a1bd-ee70992f851d
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Client Functions

This section contains information about the client functions used with Microsoft Active Accessibility.

## In this section



| Topic                                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|-----------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AccessibleChildren**](/windows/win32/Oleacc/nf-oleacc-accessiblechildren?branch=master)<br/>                       | Retrieves the child ID or [**IDispatch**](idispatch-interface.md) of each child within an accessible container object.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| [**AccessibleObjectFromEvent**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromevent?branch=master)<br/>         | Retrieves the address of the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface for the object that generated the event that is currently being processed by the client's event hook function.<br/>                                                                                                                                                                                                                                                                                                                                                                             |
| [**AccessibleObjectFromPoint**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfrompoint?branch=master)<br/>         | Retrieves the address of the [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface pointer for the object displayed at a specified point on the screen.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [**AccessibleObjectFromWindow**](/windows/win32/Oleacc/nf-oleacc-accessibleobjectfromwindow?branch=master)<br/>       | Retrieves the address of the specified interface for the object associated with the specified window.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| [**GetOleaccVersionInfo**](/windows/win32/Oleacc/nf-oleacc-getoleaccversioninfo?branch=master)<br/>                   | Retrieves the version number and build number of the Microsoft Active Accessibility file Oleacc.dll.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| [**GetProcessHandleFromHwnd**](getprocesshandlefromhwnd.md)<br/>           | Retrieves a process handle from a window handle.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [**GetRoleText**](/windows/win32/Oleacc/nf-oleacc-getroletexta?branch=master)<br/>                                     | Retrieves the localized string that describes the object's role for the specified role value.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [**GetStateText**](/windows/win32/Oleacc/nf-oleacc-getstatetexta?branch=master)<br/>                                   | Retrieves a localized string that describes an object's state for a single predefined state bit flag. Because state values are a combination of one or more bit flags, clients call this function more than once to retrieve all state strings.<br/>                                                                                                                                                                                                                                                                                                                      |
| [**SetWinEventHook**](/windows/win32/Winuser/nf-winuser-setwineventhook?branch=master)<br/>                             | Sets an event hook function for a range of events.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| [**UnhookWinEvent**](/windows/win32/Winuser/nf-winuser-unhookwinevent?branch=master)<br/>                               | Removes an event hook function created by a previous call to [**SetWinEventHook**](/windows/win32/Winuser/nf-winuser-setwineventhook?branch=master).<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [**WindowFromAccessibleObject**](/windows/win32/Oleacc/nf-oleacc-windowfromaccessibleobject?branch=master)<br/>       | Retrieves the window handle that corresponds to a particular instance of an [**IAccessible**](/windows/win32/oleacc/nn-oleacc-iaccessible?branch=master) interface.<br/>                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| [*WinEventProc Callback Function*](/windows/win32/Winuser/nc-winuser-wineventproc?branch=master)<br/> | An application-defined callback (or hook) function that the system calls in response to events generated by an accessible object. The hook function processes the event notifications as required. Clients install the hook function and request specific types of event notifications by calling [**SetWinEventHook**](/windows/win32/Winuser/nf-winuser-setwineventhook?branch=master).<br/> The [**WINEVENTPROC**](wineventproc) type defines a pointer to this callback function. [*WinEventProc*](https://msdn.microsoft.com/library/windows/desktop/dd373885) is a placeholder for the application-defined function name.<br/> |



 

## Related topics

<dl> <dt>

[Active Accessibility User Interface Services](active-accessibility-user-interface-services-collision208.md)
</dt> </dl>

 

 





