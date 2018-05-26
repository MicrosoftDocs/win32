---
title: IMessengerWindow interface
description: Do not use. The automation interface for a Messenger window.
ms.assetid: 738c280d-cc80-41e6-a9db-dcb6e14b74b1
keywords:
- IMessengerWindow interface Windows Messenger
- IMessengerWindow interface Windows Messenger , described
topic_type:
- apiref
api_name:
- IMessengerWindow
api_location:
- Msgsc.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: interface
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IMessengerWindow interface

\[**IMessengerWindow** is no longer available for use as of Windows Vista. See [Windows Messenger](im-messenger-entry.md) for more information.\]

Do not use. The automation interface for a Messenger window.

## Members

The **IMessengerWindow** interface inherits from the [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5) interface. **IMessengerWindow** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMessengerWindow** interface has these methods.



| Method                                     | Description                                                                                                             |
|:-------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| [**Close**](im-imessengerwindow-close.md) | Closes a Messenger window. If the window is a conversation window, terminates any sessions contained in it. <br/> |
| [**Show**](im-imessengerwindow--show.md)  | Sets the visibility status of a Messenger window.<br/>                                                            |



 

### Properties

The **IMessengerWindow** interface has these properties.



| Property                                                    | Access type          | Description                                                                                                 |
|:------------------------------------------------------------|:---------------------|:------------------------------------------------------------------------------------------------------------|
| [**Height**](im-imessengerwindow-height.md)<br/>     |                      | Sets or retrieves the height of a Messenger window.<br/>                                              |
| [**HWND**](im-imessengerwindow-hwnd.md)<br/>         | Read-only<br/> | Retrieves a window handle to a Messenger window.<br/>                                                 |
| [**IsClosed**](im-imessengerwindow-isclosed.md)<br/> | Read-only<br/> | Retrieves a Boolean value that indicates the open or closed state of the window.<br/>                 |
| [**Left**](im-imessengerwindow-left.md)<br/>         |                      | Sets or retrieves the left screen position of a Messenger window, in pixels.<br/>                     |
| [**Property**](im-imessengerwindow-property.md)<br/> |                      | Sets or retrieves the conversation window properties.<br/>                                            |
| [**Top**](im-imessengerwindow-top.md)<br/>           |                      | Sets or retrieves the vertical position of a Messenger window relative to the screen, in pixels.<br/> |
| [**Width**](im-imessengerwindow-width.md)<br/>       |                      | Sets or retrieves the horizontal dimension of a Messenger window, in pixels.<br/>                     |



 

## Remarks

A Messenger window is either the main application window or any window opened by the main application window. Different API options can apply. Most dialog boxes (for example, **Add a Contact** and **Options**) cannot be controlled through the MessengerWindow APIs. These dialog boxes are considered child windows of the main Messenger application window. They can be launched by invoking Windows Messenger APIs.

The main application window is active as long as the executable is running (even in the notification area). Use the [**Window**](im-imessenger-window.md) property, which returns a pointer to a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface. However, if the application window was previously minimized to the notification area through [**Close**](im-imessengerwindow-close.md) or user action, it may also be necessary to invoke the [**Show**](im-imessengerwindow--show.md) method on the application window.

For the conversation window, use the [**InstantMessage**](im-imessenger-instantmessage.md) method or its variants ([**StartVoice**](im-imessenger-startvoice.md), [**SendFile**](im-imessenger-sendfile.md), [**Page**](im-imessenger-page.md), [**InviteApp**](im-imessenger-inviteapp.md)), which return a pointer to a pointer to the [IDispatch](c1accca9-971c-4435-8a5e-e25404a3fb25) interface on a new or existing [**MessengerWindow**](im-messengerwindow.md) object.

To reference an existing [**MessengerWindow**](im-messengerwindow.md), use the return value of the methods used to invoke the window, such as [**InstantMessage**](im-imessenger-instantmessage.md) or its variants.

## Requirements



|                                     |                                                                                       |
|-------------------------------------|---------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows XP \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2003 \[desktop apps only\]<br/>                                  |
| End of client support<br/>    | Windows XP<br/>                                                                 |
| End of server support<br/>    | Windows Server 2003<br/>                                                        |
| Product<br/>                  | Messenger 4.0<br/>                                                              |
| Header<br/>                   | <dl> <dt>Msgrua.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>Msgrua.idl</dt> </dl> |
| DLL<br/>                      | <dl> <dt>Msgsc.dll</dt> </dl>  |



 

 





