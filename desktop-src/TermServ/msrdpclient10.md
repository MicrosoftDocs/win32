---
title: MsRdpClient10 class
description: Microsoft RDP Client Control (redistributable) - version 11.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '9D0F2312-0D85-402D-874D-9FA477435210'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["MsRdpClient10 class Remote Desktop Services", "MsRdpClient10 class Remote Desktop Services , described"]
topic_type:
- apiref
api_name:
- MsRdpClient10
api_location:
- MsTscAx.dll
api_type:
- COM
---

# MsRdpClient10 class

Microsoft RDP Client Control (redistributable) - version 11

This class implements the following interfaces.

-   [**IMsRdpClient10**](imsrdpclient10.md)
-   [**IMsRdpClient9**](imsrdpclient9.md)
-   [**IMsRdpClient8**](imsrdpclient8.md)
-   [**IMsRdpClient7**](imsrdpclient7.md)
-   [**IMsRdpClient6**](imsrdpclient6.md)
-   [**IMsRdpClient5**](imsrdpclient5.md)
-   [**IMsRdpClient4**](imsrdpclient4.md)
-   [**IMsRdpClient3**](imsrdpclient3.md)
-   [**IMsRdpClient2**](imsrdpclient2.md)
-   [**IMsRdpClient**](imsrdpclientshell2.md)
-   [**IMsTscAx**](imstscax-interface.md)
-   [**IDispatch**](ebbff4bc-36b2-4861-9efa-ffa45e013eb5)
-   [**IMsTscAxEvents**](imstscaxevents-interface.md)
-   [**IMsTscNonScriptable**](imstscnonscriptable-interface.md)
-   [**IMsRdpClientNonScriptable**](imsrdpclientnonscriptable-interface.md)
-   [**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md)
-   [**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
-   [**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
-   [**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
-   [**IMsRdpPreferredRedirectionInfo**](imsrdppreferredredirectioninfo.md)

**MsRdpClient10** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MsRdpClient10** class has these methods.



| Method                                                                                      | Description                                                                                                                                                                                                                                                                                   |
|:--------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**attachEvent**](imsrdpclient9-attachevent.md)                                            | Attaches an event. <br/>                                                                                                                                                                                                                                                                |
| [**Connect**](imstscax-connect.md)                                                         | Initiates a connection using the properties currently set on the control.<br/>                                                                                                                                                                                                          |
| [**CreateVirtualChannels**](imstscax-createvirtualchannels.md)                             | Creates a client-side virtual channel object for each specified virtual channel name.<br/>                                                                                                                                                                                              |
| [**detachEvent**](imsrdpclient9-detachevent.md)                                            | Detaches an event. <br/>                                                                                                                                                                                                                                                                |
| [**Disconnect**](imstscax-disconnect.md)                                                   | Disconnects the active connection.<br/>                                                                                                                                                                                                                                                 |
| [**GetErrorDescription**](imsrdpclient5-geterrordescription.md)                            | Retrieves the error codes and error messages.<br/>                                                                                                                                                                                                                                      |
| [**GetStatusText**](imsrdpclient7-getstatustext.md)                                        | Retrieves the status text for the specified status code.<br/>                                                                                                                                                                                                                           |
| [**GetVirtualChannelOptions**](imsrdpclient-getvirtualchanneloptions.md)                   | Retrieves the options set for a virtual channel.<br/>                                                                                                                                                                                                                                   |
| [**NotifyRedirectDeviceChange**](imsrdpclientnonscriptable-notifyredirectdevicechange.md)  | Notifies the device redirection module of the Remote Desktop ActiveX control that a device change has occurred on the system. This method passes [**WM\_DEVICECHANGE**](https://msdn.microsoft.com/library/windows/desktop/aa363480) notifications to the control.<br/>                                                        |
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
| [**Reconnect**](imsrdpclient8-reconnect.md)                                                | Reconnects to the remote session with the new desktop width and height.<br/>                                                                                                                                                                                                            |
| [**RequestClose**](imsrdpclient-requestclose.md)                                           | Requests a graceful shutdown of the client control.<br/>                                                                                                                                                                                                                                |
| [**ResetPassword**](imstscnonscriptable-resetpassword.md)                                  | Resets all password states in the control.<br/>                                                                                                                                                                                                                                         |
| [**SendKeys**](imsrdpclientnonscriptable-sendkeys.md)                                      | Sends a series of keystrokes to the control. The keystrokes are in scan code form, which is the keyboard data from the actual physical keys.<br/>                                                                                                                                       |
| [**SendOnVirtualChannel**](imstscax-sendonvirtualchannel.md)                               | Sends data to the RD Session Host server over a virtual channel that was created previously by using the [**IMsTscAx::CreateVirtualChannels**](imstscax-createvirtualchannels.md) method.<br/>                                                                                         |
| [**SendRemoteAction**](imsrdpclient8-sendremoteaction.md)                                  | Causes an action to be performed in the remote session.<br/>                                                                                                                                                                                                                            |
| [**SetVirtualChannelOptions**](imsrdpclient-setvirtualchanneloptions.md)                   | Sets the virtual channel options for the client control.<br/>                                                                                                                                                                                                                           |
| [**SyncSessionDisplaySettings**](imsrdpclient9-syncsessiondisplaysettings.md)              | Synchronizes session display settings. <br/>                                                                                                                                                                                                                                            |
| [**UpdateSessionDisplaySettings**](imsrdpclient9-updatesessiondisplaysettings.md)          | Updates session display settings. <br/>                                                                                                                                                                                                                                                 |



 

### Properties

The **MsRdpClient10** class has these properties.



<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr class="header">
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Access type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr class="odd">
<td style="text-align: left;">[<strong>AdvancedSettings</strong>](imstscax-advancedsettings.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An [<strong>IMsTscAdvancedSettings</strong>](imstscadvancedsettings-interface.md) interface pointer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>AdvancedSettings2</strong>](imsrdpclient-advancedsettings2.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the [<strong>IMsRdpClientAdvancedSettings</strong>](imsrdpclientadvancedsettings-interface.md) interface, used to set advanced settings for the client control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>AdvancedSettings3</strong>](imsrdpclient2-advancedsettings3.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the [<strong>IMsRdpClientAdvancedSettings2</strong>](imsrdpclientadvancedsettings2.md) interface, used to set advanced settings for the client control.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>AdvancedSettings4</strong>](imsrdpclient3-advancedsettings4.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the [<strong>IMsRdpClientAdvancedSettings3</strong>](imsrdpclientadvancedsettings3.md) interface, used to set advanced settings for the client control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>AdvancedSettings5</strong>](imsrdpclient4-advancedsettings5.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An [<strong>IMsRdpClientAdvancedSettings4</strong>](imsrdpclientadvancedsettings4.md) interface pointer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>AdvancedSettings6</strong>](imsrdpclient5-advancedsettings6.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The interface to [<strong>IMsRdpClientAdvancedSettings5</strong>](imsrdpclientadvancedsettings5.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>AdvancedSettings7</strong>](imsrdpclient6-advancedsettings7.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The interface to [<strong>IMsRdpClientAdvancedSettings6</strong>](imsrdpclientadvancedsettings6.md).<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>AdvancedSettings8</strong>](imsrdpclient7-advancedsettings8.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the [<strong>IMsRdpClientAdvancedSettings7</strong>](imsrdpclientadvancedsettings7.md) interface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>AdvancedSettings9</strong>](imsrdpclient8-advancedsettings9.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An [<strong>IMsRdpClientAdvancedSettings8</strong>](imsrdpclientadvancedsettings8.md) interface that represents the settings object.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>AllowCredentialSaving</strong>](imsrdpclientnonscriptable4-allowcredentialsaving.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the credentials dialog box displays a check box to enable the saving of credentials.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>AllowPromptingForCredentials</strong>](imsrdpclientnonscriptable5-allowpromptingforcredentials.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control can prompt the user for credentials.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>BinaryPassword</strong>](imstscnonscriptable-binarypassword.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>BinarySalt</strong>](imstscnonscriptable-binarysalt.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>CipherStrength</strong>](imstscax-cipherstrength.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The maximum encryption strength of the current control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>ClearTextPassword</strong>](imstscnonscriptable-cleartextpassword.md)<br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">The Remote Desktop ActiveX control password, in plaintext format.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ColorDepth</strong>](imsrdpclient-colordepth.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Color depth of the current control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Connected</strong>](imstscax-connected.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The connection state of the current control.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ConnectedStatusText</strong>](imsrdpclient2-connectedstatustext.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Text that is displayed in the client area of the control while the control is in the connected state.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>ConnectingText</strong>](imstscax-connectingtext.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The text that appears centered in the control while the control is connecting.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ConnectionBarText</strong>](imsrdpclientnonscriptable3-connectionbartext.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The text string to display for the connection bar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>DesktopHeight</strong>](imstscax-desktopheight.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The current control's height, in pixels, on the initial remote desktop.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>DesktopWidth</strong>](imstscax-desktopwidth.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The current control's width, in pixels, on the initial remote desktop.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>DeviceCollection</strong>](imsrdpclientnonscriptable3-devicecollection.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The collection of PnP devices that are available for redirection.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>DisableConnectionBar</strong>](imsrdpclientnonscriptable5-disableconnectionbar.md)<br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control should disable the connection bar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>DisableRemoteAppCapsCheck</strong>](imsrdpclientnonscriptable5-disableremoteappcapscheck.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control should not check the server for RemoteApp capabilities.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>DisconnectedText</strong>](imstscax-disconnectedtext.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The text that appears centered in the control before a connection is terminated.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>Domain</strong>](imstscax-domain.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The domain to which the current user logs on.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>DriveCollection</strong>](imsrdpclientnonscriptable3-drivecollection.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The collection of disk drives that is available for redirection.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>EnableCredSspSupport</strong>](imsrdpclientnonscriptable3-enablecredsspsupport.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether CredSSP is enabled for this connection.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>ExtendedDisconnectReason</strong>](imsrdpclient-extendeddisconnectreason.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Extended information about the client control's reason for disconnection.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>FullScreen</strong>](imsrdpclient-fullscreen.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Indicates whether the control is in full-screen mode.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>FullScreenTitle</strong>](imstscax-fullscreentitle.md)<br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">The window title displayed when the control is in full-screen mode.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>GetRemoteMonitorsBoundingBox</strong>](imsrdpclientnonscriptable5-getremotemonitorsboundingbox.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Specifies the bounding rectangle of the remote monitor.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>HorizontalScrollBarVisible</strong>](imstscax-horizontalscrollbarvisible.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Indicates whether the control has displayed a horizontal scroll bar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>LaunchedViaClientShellInterface</strong>](imsrdpclientnonscriptable4-launchedviaclientshellinterface.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the user launched the client control by using the RD Web Access interface.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>MarkRdpSettingsSecure</strong>](imsrdpclientnonscriptable4-markrdpsettingssecure.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether RDP settings are marked as secure.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>MsRdpClientShell</strong>](imsrdpclient5-msrdpclientshell.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The client settings for the web portal launcher.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>NegotiateSecurityLayer</strong>](imsrdpclientnonscriptable3-negotiatesecuritylayer.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the NegotiateSecurityLayer setting is supported for this connection.<br/>
<blockquote>
[!Note]<br />
When [<strong>CredSspSupport</strong>](imsrdpclientnonscriptable3-enablecredsspsupport.md) is enabled and present on the client, or when Secure Sockets Layer (SSL) is enabled with user authentication, NegotiateSecurityLayer is ignored.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>PortablePassword</strong>](imstscnonscriptable-portablepassword.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>PortableSalt</strong>](imstscnonscriptable-portablesalt.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>PromptForCredentials</strong>](imsrdpclientnonscriptable3-promptforcredentials.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the prompt for credentials dialog box should be shown.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>PromptForCredsOnClient</strong>](imsrdpclientnonscriptable4-promptforcredsonclient.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the client control displays a dialog box that prompts for credentials.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>PublisherCertificateChain</strong>](imsrdpclientnonscriptable4-publishercertificatechain.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies the publisher certificate chain. The chain is stored in a variant of type VT_BYREF that contains a pointer to a [<strong>CERT_CHAIN_CONTEXT</strong>](https://msdn.microsoft.com/library/windows/desktop/aa377182) structure.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>RedirectDynamicDevices</strong>](imsrdpclientnonscriptable3-redirectdynamicdevices.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether dynamically attached PnP devices that are enumerated while in a session are available for redirection.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RedirectDynamicDrives</strong>](imsrdpclientnonscriptable3-redirectdynamicdrives.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether dynamically attached PnP drives that are enumerated while in a session are available for redirection.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>RedirectionWarningType</strong>](imsrdpclientnonscriptable4-redirectionwarningtype.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Controls the presence and appearance of the redirection dialog box.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RemoteMonitorCount</strong>](imsrdpclientnonscriptable5-remotemonitorcount.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Specifies the number of remote monitors.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>RemoteMonitorLayoutMatchesLocal</strong>](imsrdpclientnonscriptable5-remotemonitorlayoutmatcheslocal.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Specifies if the remote monitor layout is identical to the local monitor layout.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RemoteProgram</strong>](imsrdpclient5-remoteprogram.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The client RemoteApp setting.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>RemoteProgram2</strong>](imsrdpclient7-remoteprogram2.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the [<strong>ITSRemoteProgram2</strong>](itsremoteprogram2.md) interface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>RemoteProgram3</strong>](imsrdpclient10-remoteprogram3.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the [<strong>ITSRemoteProgram3</strong>](itsremoteprogram3.md) interface.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SecuredSettings</strong>](imstscax-securedsettings.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">A [<strong>IMsTscSecuredSettings</strong>](imstscsecuredsettings-interface.md) interface pointer.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SecuredSettings2</strong>](imsrdpclient-securedsettings2.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the [<strong>IMsRdpClientSecuredSettings</strong>](imsrdpclientsecuredsettings-interface.md) interface, used to set secured settings for the client control.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>SecuredSettings3</strong>](imsrdpclient7-securedsettings3.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the [<strong>IMsRdpClientSecuredSettings2</strong>](imsrdpclientsecuredsettings2.md) interface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>SecuredSettingsEnabled</strong>](imstscax-securedsettingsenabled.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Indicates whether the [<strong>IMsTscSecuredSettings</strong>](imstscsecuredsettings-interface.md) interface is available.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Server</strong>](imstscax-server.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The name of the server to which the current control is connected.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>ShowRedirectionWarningDialog</strong>](imsrdpclientnonscriptable3-showredirectionwarningdialog.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the redirection security warning dialog box should be shown before starting a session.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>StartConnected</strong>](imstscax-startconnected.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Indicates whether the control will establish the RD Session Host server connection immediately upon startup.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>TransportSettings</strong>](imsrdpclient5-transportsettings.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The client RD Gateway setting.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>TransportSettings2</strong>](imsrdpclient6-transportsettings2.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The interface to [<strong>IMsRdpClientTransportSettings2</strong>](imsrdpclienttransportsettings2.md).<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>TransportSettings3</strong>](imsrdpclient7-transportsettings3.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the [<strong>IMsRdpClientTransportSettings3</strong>](imsrdpclienttransportsettings3.md) interface.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>TransportSettings4</strong>](imsrdpclient9-transportsettings4.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the [<strong>IMsRdpClientTransportSettings4</strong>](imsrdpclienttransportsettings4.md) interface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>TrustedZoneSite</strong>](imsrdpclientnonscriptable4-trustedzonesite.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the website from which the user launched the connection is in the trusted sites list of the client computer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>UIParentWindowHandle</strong>](imsrdpclientnonscriptable2-uiparentwindowhandle.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The window handle to be the parent window for the control. This allows any windows displayed by the control to be properly modal with respect to any windows displayed by the parent application.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>UseMultimon</strong>](imsrdpclientnonscriptable5-usemultimon.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control should use multiple monitors.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>UseRedirectionServerName</strong>](imsrdppreferredredirectioninfo-useredirectionservername.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Whether to use the redirection server name.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>UserName</strong>](imstscax-username.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The user name logon credential.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>Version</strong>](imstscax-version.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The version number of the current control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>VerticalScrollBarVisible</strong>](imstscax-verticalscrollbarvisible.md)<br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Indicates whether the control displays a vertical scroll bar.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WarnAboutClipboardRedirection</strong>](imsrdpclientnonscriptable3-warnaboutclipboardredirection.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the security warning dialog box should include a warning about clipboard redirection before starting a session.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WarnAboutDirectXRedirection</strong>](imsrdpclientnonscriptable5-warnaboutdirectxredirection.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not used.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;">[<strong>WarnAboutPrinterRedirection</strong>](imsrdpclientnonscriptable4-warnaboutprinterredirection.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the redirection dialog box displays a message about printer redirection before starting a session.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;">[<strong>WarnAboutSendingCredentials</strong>](imsrdpclientnonscriptable3-warnaboutsendingcredentials.md)<br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the security warning should include a warning about sending credentials to the remote server before starting a session.<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_MsRdpClient10 is defined as C0EFA91A-EEB7-41C7-97FA-F0ED645EFB24<br/>     |



## See also

<dl> <dt>

[Remote Desktop ActiveX control classes](remote-desktop-activex-control-classes.md)
</dt> </dl>

 

 





