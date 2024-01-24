---
title: RemoteDesktopClient class
description: Implements the Microsoft Windows Store App Remote Desktop Client Control - version 1.
ms.assetid: 0910883A-BD49-4908-8423-1FC280E0FE0C
ms.tgt_platform: multiple
keywords:
- RemoteDesktopClient class Remote Desktop Services
- RemoteDesktopClient class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- RemoteDesktopClient
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# RemoteDesktopClient class

Implements the Microsoft Windows Store App Remote Desktop Client Control - version 1

This class implements the following interfaces.

-   [**IRemoteDesktopClient**](/windows/win32/api/rdpappcontainerclient/nn-rdpappcontainerclient-iremotedesktopclient)
-   [**IRemoteDesktopClientEvents**](iremotedesktopclientevents.md)

**RemoteDesktopClient** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **RemoteDesktopClient** class has these methods.



| Method                                                                                      | Description                                                                                                                                                        |
|:--------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**attachEvent**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-attachevent)                                     | Attaches an event handler to an event.<br/>                                                                                                                  |
| [**Connect**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-connect)                                             | Initiates a connection by using the properties currently set on the Remote Desktop Protocol (RDP) app container client control.<br/>                         |
| [**DeleteSavedCredentials**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-deletesavedcredentials)               | Deletes saved credentials for the specified remote computer.<br/>                                                                                            |
| [**detachEvent**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-detachevent)                                     | Detaches an event handler from an event.<br/>                                                                                                                |
| [**Disconnect**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-disconnect)                                       | Disconnects the active connection.<br/>                                                                                                                      |
| [**OnAdminMessageReceived**](iremotedesktopclientevents-onadminmessagereceived.md)         | Called when the client control receives an administrative message.<br/>                                                                                      |
| [**OnAutoReconnected**](iremotedesktopclientevents-onautoreconnected.md)                   | Called when the client control has automatically reconnected to a remote session.<br/>                                                                       |
| [**OnAutoReconnecting**](iremotedesktopclientevents-onautoreconnecting.md)                 | Called when the client control attempts to automatically reestablish a connection to a remote session.<br/>                                                  |
| [**OnConnected**](iremotedesktopclientevents-onconnected.md)                               | Called when the client control has connected to a remote session.<br/>                                                                                       |
| [**OnConnecting**](iremotedesktopclientevents-onconnecting.md)                             | Called when the client control attempts to establish a connection to a remote session.<br/>                                                                  |
| [**OnDialogDismissed**](iremotedesktopclientevents-ondialogdismissed.md)                   | Called after a dialog box displayed by the client control is dismissed.<br/>                                                                                 |
| [**OnDialogDisplaying**](iremotedesktopclientevents-ondialogdisplaying.md)                 | Called before the control displays a dialog box.<br/>                                                                                                        |
| [**OnDisconnected**](iremotedesktopclientevents-ondisconnected.md)                         | Called when the client control has been disconnected from a remote session.<br/>                                                                             |
| [**OnKeyCombinationPressed**](iremotedesktopclientevents-onkeycombinationpressed.md)       | Called when special key combinations are pressed in the remote session.<br/>                                                                                 |
| [**OnLoginCompleted**](iremotedesktopclientevents-onlogincompleted.md)                     | Called when the client control has successfully logged on to a remote session.<br/>                                                                          |
| [**OnNetworkStatusChanged**](iremotedesktopclientevents-onnetworkstatuschanged.md)         | Called when the network status has changed.<br/>                                                                                                             |
| [**OnRemoteDesktopSizeChanged**](iremotedesktopclientevents-onremotedesktopsizechanged.md) | Called when the remote desktop size has changed.<br/>                                                                                                        |
| [**OnStatusChanged**](iremotedesktopclientevents-onstatuschanged.md)                       | Called when the client control has updated its status.<br/>                                                                                                  |
| [**OnTouchPointerCursorMoved**](iremotedesktopclientevents-ontouchpointercursormoved.md)   | Called when the touch pointer cursor has moved and the [**EventsEnabled**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclienttouchpointer-get_eventsenabled) property is set to true.<br/> |
| [**Reconnect**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-reconnect)                                         | Initiates an automatic reconnection of the Remote Desktop Protocol (RDP) app container client control to fit the session to the new width and height.<br/>   |
| [**UpdateSessionDisplaySettings**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-updatesessiondisplaysettings)   | Updates the width and height settings for the Remote Desktop Protocol (RDP) app container client control.<br/>                                               |



 

### Properties

The **RemoteDesktopClient** class has these properties.



| Property                                                             | Access type          | Description                                                                                                                                                            |
|:---------------------------------------------------------------------|:---------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Actions**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-get_actions)<br/>           | Read-only<br/> | Retrieves the actions object for the Remote Desktop Protocol (RDP) app container client.<br/>                                                                    |
| [**Settings**](iremotedesktopclient-settings.md)<br/>         | Read-only<br/> | Retrieves the settings object for the Remote Desktop Protocol (RDP) app container client.<br/>                                                                   |
| [**TouchPointer**](/windows/win32/api/rdpappcontainerclient/nf-rdpappcontainerclient-iremotedesktopclient-get_touchpointer)<br/> | Read-only<br/> | Contains the [**RemoteDesktopClientTouchPointer**](/windows/win32/api/rdpappcontainerclient/nn-rdpappcontainerclient-iremotedesktopclienttouchpointer) object for the Remote Desktop Protocol (RDP) app container client.<br/> |



 

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                     |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>   |
| CLSID<br/>                    | CLSID\_RemoteDesktopClient is defined as EAB16C5D-EED1-4E95-868B-0FBA1B42C092<br/> |



## See also

<dl> <dt>

[Remote Desktop ActiveX control classes](remote-desktop-activex-control-classes.md)
</dt> </dl>

 

