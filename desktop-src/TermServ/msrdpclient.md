---
title: MsRdpClient class
description: Microsoft RDP Client Control (redistributable) - version 2.
ms.assetid: 58A779AF-4946-4D3B-B640-5675092A641D
ms.tgt_platform: multiple
keywords:
- MsRdpClient class Remote Desktop Services
- MsRdpClient class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- MsRdpClient
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MsRdpClient class

Microsoft RDP Client Control (redistributable) - version 2

This class implements the following interfaces.

-   [**IMsRdpClient**](imsrdpclientshell2.md)
-   [**IMsTscAx**](imstscax-interface.md)
-   [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
-   [**IMsTscAxEvents**](imstscaxevents-interface.md)
-   [**IMsTscNonScriptable**](imstscnonscriptable-interface.md)
-   [**IMsRdpClientNonScriptable**](imsrdpclientnonscriptable-interface.md)

**MsRdpClient** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MsRdpClient** class has these methods.



| Method                                                                                      | Description                                                                                                                                                                                                                                                                                   |
|:--------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Connect**](imstscax-connect.md)                                                         | Initiates a connection using the properties currently set on the control.<br/>                                                                                                                                                                                                          |
| [**CreateVirtualChannels**](imstscax-createvirtualchannels.md)                             | Creates a client-side virtual channel object for each specified virtual channel name.<br/>                                                                                                                                                                                              |
| [**Disconnect**](imstscax-disconnect.md)                                                   | Disconnects the active connection.<br/>                                                                                                                                                                                                                                                 |
| [**GetVirtualChannelOptions**](imsrdpclient-getvirtualchanneloptions.md)                   | Retrieves the options set for a virtual channel.<br/>                                                                                                                                                                                                                                   |
| [**NotifyRedirectDeviceChange**](imsrdpclientnonscriptable-notifyredirectdevicechange.md)  | Notifies the device redirection module of the Remote Desktop ActiveX control that a device change has occurred on the system. This method passes [**WM\_DEVICECHANGE**](/windows/desktop/DevIO/wm-devicechange) notifications to the control.<br/>                                                        |
| [**OnAuthenticationWarningDismissed**](imstscaxevents-onauthenticationwarningdismissed.md) | Called after an ActiveX control displays an authentication dialog box (for example, the certificate error dialog box).<br/>                                                                                                                                                             |
| [**OnAuthenticationWarningDisplayed**](imstscaxevents-onauthenticationwarningdisplayed.md) | Called before an ActiveX control displays an authentication dialog box (for example, the certificate error dialog box).<br/>                                                                                                                                                            |
| [**OnAutoReconnected**](imstscaxevents-onautoreconnected.md)                               | Called when the client control has automatically reconnected to a remote session.<br/>                                                                                                                                                                                                  |
| [**OnAutoReconnecting**](-imstscaxevents--onautoreconnecting.md)                           | Called when a client is in the process of automatically reconnecting a session with a RD Session Host server.<br/>                                                                                                                                                                      |
| [**OnAutoReconnecting2**](imstscaxevents-onautoreconnecting2.md)                           | Called when a client is in the process of automatically reconnecting a session with a RD Session Host server.<br/>                                                                                                                                                                      |
| [**OnChannelReceivedData**](imstscaxevents-onchannelreceiveddata.md)                       | Called when the client receives data on a scriptable virtual channel.<br/>                                                                                                                                                                                                              |
| [**OnConfirmClose**](imstscaxevents-onconfirmclose.md)                                     | Called when the client calls the [**IMsRdpClient::RequestClose**](imsrdpclient-requestclose.md) method.<br/>                                                                                                                                                                           |
| [**OnConnected**](imstscaxevents-onconnected.md)                                           | Called when the client control is in the process of establishing a connection with a RD Session Host server.<br/>                                                                                                                                                                       |
| [**OnConnecting**](imstscaxevents-onconnecting.md)                                         | Called when the client control begins connecting to a server in response to a call to [**IMsTscAx::Connect**](imstscax-connect.md).<br/>                                                                                                                                               |
| [**OnConnectionBarPullDown**](imstscaxevents-onconnectionbarpulldown.md)                   | Called when the user has dragged down on the connection bar.<br/>                                                                                                                                                                                                                       |
| [**OnDevicesButtonPressed**](imstscaxevents-ondevicesbuttonpressed.md)                     | Called when the devices button in the connection bar has been pressed.<br/>                                                                                                                                                                                                             |
| [**OnDisconnected**](imstscaxevents-ondisconnected.md)                                     | Called when the client control has been disconnected from the RD Session Host server.<br/>                                                                                                                                                                                              |
| [**OnEnterFullScreenMode**](imstscaxevents-onenterfullscreenmode.md)                       | Called when the client enters full-screen mode. For example, this event is called when the user presses the full-screen mode [shortcut key](terminal-services-shortcut-keys.md) combination (CTRL+ALT+BREAK).<br/>                                                                     |
| [**OnFatalError**](imstscaxevents-onfatalerror.md)                                         | Called when the client control encounters a fatal error.<br/>                                                                                                                                                                                                                           |
| [**OnFocusReleased**](imstscaxevents-onfocusreleased.md)                                   | Called when the release focus key combination is pressed. For example, this event is called when the user presses the CTRL+ALT+LEFT ARROW or the CTRL+ALT+RIGHT ARROW key combination.<br/>                                                                                             |
| [**OnIdleTimeoutNotification**](imstscaxevents-onidletimeoutnotification.md)               | Called when there has been no mouse or keyboard input by the user during the period of time set by the [**IMsRdpClientAdvancedSettings::put\_MinutesToIdleTimeout**](imsrdpclientadvancedsettings-minutestoidletimeout.md) method.<br/>                                                |
| [**OnLeaveFullScreenMode**](imstscaxevents-onleavefullscreenmode.md)                       | Called when the client leaves full-screen mode. For example, this event is called when the user presses the full-screen mode [shortcut key](terminal-services-shortcut-keys.md) combination (CTRL+ALT+BREAK).<br/>                                                                     |
| [**OnLoginComplete**](imstscaxevents-onlogincomplete.md)                                   | Called when the client control has successfully logged on to a RD Session Host server, following the display of the Windows Logon dialog box.<br/>                                                                                                                                      |
| [**OnLogonError**](imstscaxevents-onlogonerror.md)                                         | Called when a logon error or other logon event occurs.<br/>                                                                                                                                                                                                                             |
| [**OnMouseInputModeChanged**](imstscaxevents-onmouseinputmodechanged.md)                   | Called when the mouse input mode has changed.<br/>                                                                                                                                                                                                                                      |
| [**OnNetworkStatusChanged**](imstscaxevents-onnetworkstatuschanged.md)                     | Called when the network status has changed.<br/>                                                                                                                                                                                                                                        |
| [**OnReceivedTSPublicKey**](imstscaxevents-onreceivedtspublickey.md)                       | Called during the connection sequence when the client retrieves the public key from the server. This event is only called if the **NotifyTSPublicKey** property is **VARIANT\_TRUE**.<br/>                                                                                              |
| [**OnRemoteDesktopSizeChange**](imstscaxevents-onremotedesktopsizechange.md)               | Called to indicate that the size of the client control on the remote desktop has changed in response to a client control operation.<br/>                                                                                                                                                |
| [**OnRemoteProgramDisplayed**](imstscaxevents-onremoteprogramdisplayed.md)                 | Called when a RemoteApp program is displayed.<br/>                                                                                                                                                                                                                                      |
| [**OnRemoteProgramResult**](imstscaxevents-onremoteprogramresult.md)                       | Called when a RemoteApp program returns a result to the client control.<br/>                                                                                                                                                                                                            |
| [**OnRemoteWindowDisplayed**](imstscaxevents-onremotewindowdisplayed.md)                   | Called when a RemoteApp window is displayed.<br/>                                                                                                                                                                                                                                       |
| [**OnRequestContainerMinimize**](imstscaxevents-onrequestcontainerminimize.md)             | Called when the user presses the **Minimize** button on the connection bar in full-screen mode. The firing of this event is a request that the container application minimize itself.<br/>                                                                                              |
| [**OnRequestGoFullScreen**](imstscaxevents-onrequestgofullscreen.md)                       | Called when the client requests to switch to full-screen mode and the [**IMsTscAdvancedSettings::put\_ContainerHandledFullScreen**](imstscadvancedsettings-containerhandledfullscreen.md) method is called to set the **ContainerHandledFullScreen** property to a nonzero value.<br/> |
| [**OnRequestLeaveFullScreen**](imstscaxevents-onrequestleavefullscreen.md)                 | Called when the client requests to leave full-screen mode and the [**IMsTscAdvancedSettings::put\_ContainerHandledFullScreen**](imstscadvancedsettings-containerhandledfullscreen.md) property has been set to a nonzero value.<br/>                                                   |
| [**OnServiceMessageReceived**](imstscaxevents-onservicemessagereceived.md)                 | Called when the client receives a system message.<br/>                                                                                                                                                                                                                                  |
| [**OnUserNameAcquired**](imstscaxevents-onusernameacquired.md)                             | Called when the user name has been acquired by the control.<br/>                                                                                                                                                                                                                        |
| [**OnWarning**](imstscaxevents-onwarning.md)                                               | Called when the client control encounters an error condition that is not fatal.<br/>                                                                                                                                                                                                    |
| [**RequestClose**](imsrdpclient-requestclose.md)                                           | Requests a graceful shutdown of the client control.<br/>                                                                                                                                                                                                                                |
| [**ResetPassword**](imstscnonscriptable-resetpassword.md)                                  | Resets all password states in the control.<br/>                                                                                                                                                                                                                                         |
| [**SendKeys**](imsrdpclientnonscriptable-sendkeys.md)                                      | Sends a series of keystrokes to the control. The keystrokes are in scan code form, which is the keyboard data from the actual physical keys.<br/>                                                                                                                                       |
| [**SendOnVirtualChannel**](imstscax-sendonvirtualchannel.md)                               | Sends data to the RD Session Host server over a virtual channel that was created previously by using the [**IMsTscAx::CreateVirtualChannels**](imstscax-createvirtualchannels.md) method.<br/>                                                                                         |
| [**SetVirtualChannelOptions**](imsrdpclient-setvirtualchanneloptions.md)                   | Sets the virtual channel options for the client control.<br/>                                                                                                                                                                                                                           |



 

### Properties

The **MsRdpClient** class has these properties.



| Property                                                                             | Access type           | Description                                                                                                                                                               |
|:-------------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdvancedSettings**](imstscax-advancedsettings.md)<br/>                     | Read-only<br/>  | An [**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md) interface pointer.<br/>                                                                       |
| [**AdvancedSettings2**](imsrdpclient-advancedsettings2.md)<br/>               | Read-only<br/>  | Pointer to the [**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md) interface, used to set advanced settings for the client control.<br/> |
| [**BinaryPassword**](imstscnonscriptable-binarypassword.md)<br/>              | Read/write<br/> | This property is not supported.<br/>                                                                                                                                |
| [**BinarySalt**](imstscnonscriptable-binarysalt.md)<br/>                      | Read/write<br/> | This property is not supported.<br/>                                                                                                                                |
| [**CipherStrength**](imstscax-cipherstrength.md)<br/>                         | Read-only<br/>  | The maximum encryption strength of the current control.<br/>                                                                                                        |
| [**ClearTextPassword**](imstscnonscriptable-cleartextpassword.md)<br/>        | Write-only<br/> | The Remote Desktop ActiveX control password, in plaintext format.<br/>                                                                                              |
| [**ColorDepth**](imsrdpclient-colordepth.md)<br/>                             | Read/write<br/> | Color depth of the current control.<br/>                                                                                                                            |
| [**Connected**](imstscax-connected.md)<br/>                                   | Read-only<br/>  | The connection state of the current control.<br/>                                                                                                                   |
| [**ConnectingText**](imstscax-connectingtext.md)<br/>                         | Read/write<br/> | The text that appears centered in the control while the control is connecting.<br/>                                                                                 |
| [**DesktopHeight**](imstscax-desktopheight.md)<br/>                           | Read/write<br/> | The current control's height, in pixels, on the initial remote desktop.<br/>                                                                                        |
| [**DesktopWidth**](imstscax-desktopwidth.md)<br/>                             | Read/write<br/> | The current control's width, in pixels, on the initial remote desktop.<br/>                                                                                         |
| [**DisconnectedText**](imstscax-disconnectedtext.md)<br/>                     | Read/write<br/> | The text that appears centered in the control before a connection is terminated.<br/>                                                                               |
| [**Domain**](imstscax-domain.md)<br/>                                         | Read/write<br/> | The domain to which the current user logs on.<br/>                                                                                                                  |
| [**ExtendedDisconnectReason**](imsrdpclient-extendeddisconnectreason.md)<br/> | Read-only<br/>  | Extended information about the client control's reason for disconnection.<br/>                                                                                      |
| [**FullScreen**](imsrdpclient-fullscreen.md)<br/>                             | Read/write<br/> | Indicates whether the control is in full-screen mode.<br/>                                                                                                          |
| [**FullScreenTitle**](imstscax-fullscreentitle.md)<br/>                       | Write-only<br/> | The window title displayed when the control is in full-screen mode.<br/>                                                                                            |
| [**HorizontalScrollBarVisible**](imstscax-horizontalscrollbarvisible.md)<br/> | Read-only<br/>  | Indicates whether the control has displayed a horizontal scroll bar.<br/>                                                                                           |
| [**PortablePassword**](imstscnonscriptable-portablepassword.md)<br/>          | Read/write<br/> | This property is not supported.<br/>                                                                                                                                |
| [**PortableSalt**](imstscnonscriptable-portablesalt.md)<br/>                  | Read/write<br/> | This property is not supported.<br/>                                                                                                                                |
| [**SecuredSettings**](imstscax-securedsettings.md)<br/>                       | Read-only<br/>  | A [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface pointer.<br/>                                                                          |
| [**SecuredSettings2**](imsrdpclient-securedsettings2.md)<br/>                 | Read-only<br/>  | Pointer to the [**IMsRdpClientSecuredSettings**](imsrdpclientsecuredsettings-interface.md) interface, used to set secured settings for the client control.<br/>    |
| [**SecuredSettingsEnabled**](imstscax-securedsettingsenabled.md)<br/>         | Read-only<br/>  | Indicates whether the [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface is available.<br/>                                                 |
| [**Server**](imstscax-server.md)<br/>                                         | Read/write<br/> | The name of the server to which the current control is connected.<br/>                                                                                              |
| [**StartConnected**](imstscax-startconnected.md)<br/>                         | Read/write<br/> | Indicates whether the control will establish the RD Session Host server connection immediately upon startup.<br/>                                                   |
| [**UserName**](imstscax-username.md)<br/>                                     | Read/write<br/> | The user name logon credential.<br/>                                                                                                                                |
| [**Version**](imstscax-version.md)<br/>                                       | Read-only<br/>  | The version number of the current control.<br/>                                                                                                                     |
| [**VerticalScrollBarVisible**](imstscax-verticalscrollbarvisible.md)<br/>     | Read-only<br/>  | Indicates whether the control displays a vertical scroll bar.<br/>                                                                                                  |



 

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_MsRdpClient is defined as 791fa017-2de3-492e-acc5-53c67a2b94d0<br/>       |



## See also

<dl> <dt>

[Remote Desktop ActiveX control classes](remote-desktop-activex-control-classes.md)
</dt> </dl>

 

