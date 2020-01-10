---
title: MsRdpClient9 class
description: Microsoft RDP Client Control (redistributable) - version 10.
ms.assetid: 3E7B1B45-B645-4F07-9A59-7A2D6B808645
ms.tgt_platform: multiple
keywords:
- MsRdpClient9 class Remote Desktop Services
- MsRdpClient9 class Remote Desktop Services , described
topic_type:
- apiref
api_name:
- MsRdpClient9
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# MsRdpClient9 class

Microsoft RDP Client Control (redistributable) - version 10

This class implements the following interfaces.

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
-   [**IDispatch**](https://msdn.microsoft.com/library/ms221608(v=VS.71).aspx)
-   [**IMsTscAxEvents**](imstscaxevents-interface.md)
-   [**IMsTscNonScriptable**](imstscnonscriptable-interface.md)
-   [**IMsRdpClientNonScriptable**](imsrdpclientnonscriptable-interface.md)
-   [**IMsRdpClientNonScriptable2**](imsrdpclientnonscriptable2.md)
-   [**IMsRdpClientNonScriptable3**](imsrdpclientnonscriptable3.md)
-   [**IMsRdpClientNonScriptable4**](imsrdpclientnonscriptable4.md)
-   [**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
-   [**IMsRdpPreferredRedirectionInfo**](imsrdppreferredredirectioninfo.md)

**MsRdpClient9** has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **MsRdpClient9** class has these methods.



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
| [**NotifyRedirectDeviceChange**](imsrdpclientnonscriptable-notifyredirectdevicechange.md)  | Notifies the device redirection module of the Remote Desktop ActiveX control that a device change has occurred on the system. This method passes [**WM\_DEVICECHANGE**](https://docs.microsoft.com/windows/desktop/DevIO/wm-devicechange) notifications to the control.<br/>                                                        |
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
| [**SendOnVirtualChannel**](imstscax-sendonvirtualchannel.md)                               | Sends data to the RD Session Host server over a virtual channel that was created previously by using the [**IMsTscAx::CreateVirtualChannels**](imstscax-createvirtualchannels.md) method.<br/>                                                                                         |
| [**SendRemoteAction**](imsrdpclient8-sendremoteaction.md)                                  | Causes an action to be performed in the remote session.<br/>                                                                                                                                                                                                                            |
| [**SetVirtualChannelOptions**](imsrdpclient-setvirtualchanneloptions.md)                   | Sets the virtual channel options for the client control.<br/>                                                                                                                                                                                                                           |
| [**SyncSessionDisplaySettings**](imsrdpclient9-syncsessiondisplaysettings.md)              | Synchronizes session display settings. <br/>                                                                                                                                                                                                                                            |
| [**UpdateSessionDisplaySettings**](https://msdn.microsoft.com/library/Mt703457(v=VS.85).aspx)          | Updates session display settings. <br/>                                                                                                                                                                                                                                                 |



 

### Properties

The **MsRdpClient9** class has these properties.



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
<td style="text-align: left;"><a href="imstscax-advancedsettings"><strong>AdvancedSettings</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An <a href="imstscadvancedsettings-interface"><strong>IMsTscAdvancedSettings</strong></a> interface pointer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient-advancedsettings2"><strong>AdvancedSettings2</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the <a href="imsrdpclientadvancedsettings-interface"><strong>IMsRdpClientAdvancedSettings</strong></a> interface, used to set advanced settings for the client control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient2-advancedsettings3"><strong>AdvancedSettings3</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the <a href="imsrdpclientadvancedsettings2"><strong>IMsRdpClientAdvancedSettings2</strong></a> interface, used to set advanced settings for the client control.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient3-advancedsettings4"><strong>AdvancedSettings4</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the <a href="imsrdpclientadvancedsettings3"><strong>IMsRdpClientAdvancedSettings3</strong></a> interface, used to set advanced settings for the client control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient4-advancedsettings5"><strong>AdvancedSettings5</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An <a href="imsrdpclientadvancedsettings4"><strong>IMsRdpClientAdvancedSettings4</strong></a> interface pointer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient5-advancedsettings6"><strong>AdvancedSettings6</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The interface to <a href="imsrdpclientadvancedsettings5"><strong>IMsRdpClientAdvancedSettings5</strong></a>.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient6-advancedsettings7"><strong>AdvancedSettings7</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The interface to <a href="imsrdpclientadvancedsettings6"><strong>IMsRdpClientAdvancedSettings6</strong></a>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient7-advancedsettings8"><strong>AdvancedSettings8</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the <a href="imsrdpclientadvancedsettings7"><strong>IMsRdpClientAdvancedSettings7</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient8-advancedsettings9"><strong>AdvancedSettings9</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An <a href="imsrdpclientadvancedsettings8"><strong>IMsRdpClientAdvancedSettings8</strong></a> interface that represents the settings object.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-allowcredentialsaving"><strong>AllowCredentialSaving</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the credentials dialog box displays a check box to enable the saving of credentials.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-allowpromptingforcredentials"><strong>AllowPromptingForCredentials</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control can prompt the user for credentials.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscnonscriptable-binarypassword"><strong>BinaryPassword</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscnonscriptable-binarysalt"><strong>BinarySalt</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-cipherstrength"><strong>CipherStrength</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The maximum encryption strength of the current control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscnonscriptable-cleartextpassword"><strong>ClearTextPassword</strong></a><br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">The Remote Desktop ActiveX control password, in plaintext format.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient-colordepth"><strong>ColorDepth</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Color depth of the current control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-connected"><strong>Connected</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The connection state of the current control.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient2-connectedstatustext"><strong>ConnectedStatusText</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Text that is displayed in the client area of the control while the control is in the connected state.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-connectingtext"><strong>ConnectingText</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The text that appears centered in the control while the control is connecting.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-connectionbartext"><strong>ConnectionBarText</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The text string to display for the connection bar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-desktopheight"><strong>DesktopHeight</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The current control's height, in pixels, on the initial remote desktop.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-desktopwidth"><strong>DesktopWidth</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The current control's width, in pixels, on the initial remote desktop.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-devicecollection"><strong>DeviceCollection</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The collection of PnP devices that are available for redirection.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-disableconnectionbar"><strong>DisableConnectionBar</strong></a><br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control should disable the connection bar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-disableremoteappcapscheck"><strong>DisableRemoteAppCapsCheck</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control should not check the server for RemoteApp capabilities.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-disconnectedtext"><strong>DisconnectedText</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The text that appears centered in the control before a connection is terminated.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-domain"><strong>Domain</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The domain to which the current user logs on.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-drivecollection"><strong>DriveCollection</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The collection of disk drives that is available for redirection.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-enablecredsspsupport"><strong>EnableCredSspSupport</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether CredSSP is enabled for this connection.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient-extendeddisconnectreason"><strong>ExtendedDisconnectReason</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Extended information about the client control's reason for disconnection.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient-fullscreen"><strong>FullScreen</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Indicates whether the control is in full-screen mode.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-fullscreentitle"><strong>FullScreenTitle</strong></a><br/></td>
<td style="text-align: left;">Write-only<br/></td>
<td style="text-align: left;">The window title displayed when the control is in full-screen mode.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-getremotemonitorsboundingbox"><strong>GetRemoteMonitorsBoundingBox</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Specifies the bounding rectangle of the remote monitor.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-horizontalscrollbarvisible"><strong>HorizontalScrollBarVisible</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Indicates whether the control has displayed a horizontal scroll bar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-launchedviaclientshellinterface"><strong>LaunchedViaClientShellInterface</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the user launched the client control by using the RD Web Access interface.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-markrdpsettingssecure"><strong>MarkRdpSettingsSecure</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether RDP settings are marked as secure.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient5-msrdpclientshell"><strong>MsRdpClientShell</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The client settings for the web portal launcher.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-negotiatesecuritylayer"><strong>NegotiateSecurityLayer</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the NegotiateSecurityLayer setting is supported for this connection.<br/>
<blockquote>
[!Note]<br />
When <a href="imsrdpclientnonscriptable3-enablecredsspsupport"><strong>CredSspSupport</strong></a> is enabled and present on the client, or when Secure Sockets Layer (SSL) is enabled with user authentication, NegotiateSecurityLayer is ignored.
</blockquote>
<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscnonscriptable-portablepassword"><strong>PortablePassword</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscnonscriptable-portablesalt"><strong>PortableSalt</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not supported.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-promptforcredentials"><strong>PromptForCredentials</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the prompt for credentials dialog box should be shown.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-promptforcredsonclient"><strong>PromptForCredsOnClient</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the client control displays a dialog box that prompts for credentials.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-publishercertificatechain"><strong>PublisherCertificateChain</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies the publisher certificate chain. The chain is stored in a variant of type VT_BYREF that contains a pointer to a <a href="https://docs.microsoft.com/windows/desktop/api/wincrypt/ns-wincrypt-cert_chain_context"><strong>CERT_CHAIN_CONTEXT</strong></a> structure.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-redirectdynamicdevices"><strong>RedirectDynamicDevices</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether dynamically attached PnP devices that are enumerated while in a session are available for redirection.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-redirectdynamicdrives"><strong>RedirectDynamicDrives</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether dynamically attached PnP drives that are enumerated while in a session are available for redirection.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-redirectionwarningtype"><strong>RedirectionWarningType</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Controls the presence and appearance of the redirection dialog box.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-remotemonitorcount"><strong>RemoteMonitorCount</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Specifies the number of remote monitors.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-remotemonitorlayoutmatcheslocal"><strong>RemoteMonitorLayoutMatchesLocal</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Specifies if the remote monitor layout is identical to the local monitor layout.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient5-remoteprogram"><strong>RemoteProgram</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The client RemoteApp setting.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient7-remoteprogram2"><strong>RemoteProgram2</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the <a href="itsremoteprogram2"><strong>ITSRemoteProgram2</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-securedsettings"><strong>SecuredSettings</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">A <a href="imstscsecuredsettings-interface"><strong>IMsTscSecuredSettings</strong></a> interface pointer.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient-securedsettings2"><strong>SecuredSettings2</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Pointer to the <a href="imsrdpclientsecuredsettings-interface"><strong>IMsRdpClientSecuredSettings</strong></a> interface, used to set secured settings for the client control.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient7-securedsettings3"><strong>SecuredSettings3</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the <a href="imsrdpclientsecuredsettings2"><strong>IMsRdpClientSecuredSettings2</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-securedsettingsenabled"><strong>SecuredSettingsEnabled</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Indicates whether the <a href="imstscsecuredsettings-interface"><strong>IMsTscSecuredSettings</strong></a> interface is available.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-server"><strong>Server</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The name of the server to which the current control is connected.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-showredirectionwarningdialog"><strong>ShowRedirectionWarningDialog</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the redirection security warning dialog box should be shown before starting a session.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-startconnected"><strong>StartConnected</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Indicates whether the control will establish the RD Session Host server connection immediately upon startup.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient5-transportsettings"><strong>TransportSettings</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The client RD Gateway setting.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient6-transportsettings2"><strong>TransportSettings2</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The interface to <a href="imsrdpclienttransportsettings2"><strong>IMsRdpClientTransportSettings2</strong></a>.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclient7-transportsettings3"><strong>TransportSettings3</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the <a href="imsrdpclienttransportsettings3"><strong>IMsRdpClientTransportSettings3</strong></a> interface.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclient9-transportsettings4"><strong>TransportSettings4</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">An object that supports the <a href="imsrdpclienttransportsettings4"><strong>IMsRdpClientTransportSettings4</strong></a> interface.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-trustedzonesite"><strong>TrustedZoneSite</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the website from which the user launched the connection is in the trusted sites list of the client computer.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable2-uiparentwindowhandle"><strong>UIParentWindowHandle</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The window handle to be the parent window for the control. This allows any windows displayed by the control to be properly modal with respect to any windows displayed by the parent application.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-usemultimon"><strong>UseMultimon</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the Remote Desktop ActiveX control should use multiple monitors.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdppreferredredirectioninfo-useredirectionservername"><strong>UseRedirectionServerName</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Whether to use the redirection server name.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-username"><strong>UserName</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">The user name logon credential.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imstscax-version"><strong>Version</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">The version number of the current control.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imstscax-verticalscrollbarvisible"><strong>VerticalScrollBarVisible</strong></a><br/></td>
<td style="text-align: left;">Read-only<br/></td>
<td style="text-align: left;">Indicates whether the control displays a vertical scroll bar.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-warnaboutclipboardredirection"><strong>WarnAboutClipboardRedirection</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the security warning dialog box should include a warning about clipboard redirection before starting a session.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable5-warnaboutdirectxredirection"><strong>WarnAboutDirectXRedirection</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">This property is not used.<br/></td>
</tr>
<tr class="odd">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable4-warnaboutprinterredirection"><strong>WarnAboutPrinterRedirection</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the redirection dialog box displays a message about printer redirection before starting a session.<br/></td>
</tr>
<tr class="even">
<td style="text-align: left;"><a href="imsrdpclientnonscriptable3-warnaboutsendingcredentials"><strong>WarnAboutSendingCredentials</strong></a><br/></td>
<td style="text-align: left;">Read/write<br/></td>
<td style="text-align: left;">Specifies whether the security warning should include a warning about sending credentials to the remote server before starting a session.<br/></td>
</tr>
</tbody>
</table>



 

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2012 R2<br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| CLSID<br/>                    | CLSID\_MsRdpClient9 is defined as 301B94BA-5D25-4A12-BFFE-3B6E7A616585<br/>      |



## See also

<dl> <dt>

[Remote Desktop ActiveX control classes](remote-desktop-activex-control-classes.md)
</dt> </dl>

 

 





