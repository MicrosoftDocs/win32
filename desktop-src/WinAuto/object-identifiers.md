---
title: Object Identifiers (Winuser.h)
description: This topic describes the Microsoft Active Accessibility object identifiers, 32-bit values that identify categories of accessible objects within a window.
ms.assetid: dc1603f8-29e5-4acd-817a-c6957feaff6c
topic_type:
- apiref
api_name:
- OBJID_ALERT
- OBJID_CARET
- OBJID_CLIENT
- OBJID_CURSOR
- OBJID_HSCROLL
- OBJID_NATIVEOM
- OBJID_MENU
- OBJID_QUERYCLASSNAMEIDX
- OBJID_SIZEGRIP
- OBJID_SOUND
- OBJID_SYSMENU
- OBJID_TITLEBAR
- OBJID_VSCROLL
- OBJID_WINDOW
api_location:
- winuser.h
api_type:
- HeaderDef
ms.topic: reference
ms.date: 05/31/2018
---

# Object Identifiers (Winuser.h)

This topic describes the Microsoft Active Accessibility object identifiers, 32-bit values that identify *categories* of accessible objects within a window. Microsoft Active Accessibility servers and Microsoft UI Automation providers use the object identifiers to determine the object to which a [**WM\_GETOBJECT**](wm-getobject.md) message request refers.

Clients receive these values in their [*WinEventProc*](/windows/desktop/api/Winuser/nc-winuser-wineventproc) callback function and use them to identify parts of a window. Servers use these values to identify the corresponding parts of a window when calling [**NotifyWinEvent**](/windows/desktop/api/Winuser/nf-winuser-notifywinevent) or when responding to the [**WM\_GETOBJECT**](wm-getobject.md) message.

Servers can define custom object IDs to identify other categories of objects within their applications. Custom object IDs must be assigned positive values because Microsoft Active Accessibility reserves zero and all negative values for the following standard object identifiers.

The following constants are defined in winuser.h:



| Constant                                                                                                                                                                                    | Description                                                                                                                                                                                                                                                                                                                                            |
|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| <span id="OBJID_ALERT"></span><span id="objid_alert"></span><dl> <dt>**OBJID\_ALERT**</dt> </dl>                                     | An alert that is associated with a window or an application. System provided message boxes are the only UI elements that send events with this object identifier. Server applications cannot use the **AccessibleObjectFrom***X* functions with this object identifier. This is a known issue with Microsoft Active Accessibility.<br/>          |
| <span id="OBJID_CARET"></span><span id="objid_caret"></span><dl> <dt>**OBJID\_CARET**</dt> </dl>                                     | The text insertion bar (caret) in the window.<br/>                                                                                                                                                                                                                                                                                               |
| <span id="OBJID_CLIENT"></span><span id="objid_client"></span><dl> <dt>**OBJID\_CLIENT**</dt> </dl>                                  | The window's client area. In most cases, the operating system controls the frame elements and the client object contains all elements that are controlled by the application. Servers only process the [**WM\_GETOBJECT**](wm-getobject.md) messages in which the *lParam* is OBJID\_CLIENT, OBJID\_WINDOW, or a custom object identifier.<br/> |
| <span id="OBJID_CURSOR"></span><span id="objid_cursor"></span><dl> <dt>**OBJID\_CURSOR**</dt> </dl>                                  | The mouse pointer. There is only one mouse pointer in the system, and it is not a child of any window.<br/>                                                                                                                                                                                                                                      |
| <span id="OBJID_HSCROLL"></span><span id="objid_hscroll"></span><dl> <dt>**OBJID\_HSCROLL**</dt> </dl>                               | The window's horizontal scroll bar.<br/>                                                                                                                                                                                                                                                                                                         |
| <span id="OBJID_NATIVEOM"></span><span id="objid_nativeom"></span><dl> <dt>**OBJID\_NATIVEOM**</dt> </dl>                            | In response to this object identifier, third-party applications can expose their own object model. Third-party applications can return any COM interface in response to this object identifier.<br/>                                                                                                                                             |
| <span id="OBJID_MENU"></span><span id="objid_menu"></span><dl> <dt>**OBJID\_MENU**</dt> </dl>                                        | The window's menu bar.<br/>                                                                                                                                                                                                                                                                                                                      |
| <span id="OBJID_QUERYCLASSNAMEIDX"></span><span id="objid_queryclassnameidx"></span><dl> <dt>**OBJID\_QUERYCLASSNAMEIDX**</dt> </dl> | An object identifier that Oleacc.dll uses internally. For more information, see [Appendix F: Object Identifier Values for OBJID\_QUERYCLASSNAMEIDX](appendix-f--object-identifier-values-for-objid-queryclassnameidx.md).<br/>                                                                                                                  |
| <span id="OBJID_SIZEGRIP"></span><span id="objid_sizegrip"></span><dl> <dt>**OBJID\_SIZEGRIP**</dt> </dl>                            | The window's size grip: an optional frame component located at the lower-right corner of the window frame.<br/>                                                                                                                                                                                                                                  |
| <span id="OBJID_SOUND"></span><span id="objid_sound"></span><dl> <dt>**OBJID\_SOUND**</dt> </dl>                                     | A sound object. Sound objects do not have screen locations or children, but they do have name and state attributes. They are children of the application that is playing the sound.<br/>                                                                                                                                                         |
| <span id="OBJID_SYSMENU"></span><span id="objid_sysmenu"></span><dl> <dt>**OBJID\_SYSMENU**</dt> </dl>                               | The window's system menu.<br/>                                                                                                                                                                                                                                                                                                                   |
| <span id="OBJID_TITLEBAR"></span><span id="objid_titlebar"></span><dl> <dt>**OBJID\_TITLEBAR**</dt> </dl>                            | The window's title bar.<br/>                                                                                                                                                                                                                                                                                                                     |
| <span id="OBJID_VSCROLL"></span><span id="objid_vscroll"></span><dl> <dt>**OBJID\_VSCROLL**</dt> </dl>                               | The window's vertical scroll bar.<br/>                                                                                                                                                                                                                                                                                                           |
| <span id="OBJID_WINDOW"></span><span id="objid_window"></span><dl> <dt>**OBJID\_WINDOW**</dt> </dl>                                  | The window itself rather than a child object.<br/>                                                                                                                                                                                                                                                                                               |



## Requirements



| Requirement | Value |
|-------------------|----------------------------------------------------------------------------------------------------------|
| Header<br/> | <dl> <dt>Winuser.h (include Windows.h)</dt> </dl> |



 

 





