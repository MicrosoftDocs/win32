---
title: IMsRdpExtendedSettings Property property
description: Contains a named property.
ms.assetid: 3acaeff9-1617-46c3-80c3-b87496b83670
ms.tgt_platform: multiple
keywords:
- Property property Remote Desktop Services
- Property property Remote Desktop Services , IMsRdpExtendedSettings interface
- IMsRdpExtendedSettings interface Remote Desktop Services , Property property
topic_type:
- apiref
api_name:
- IMsRdpExtendedSettings.Property
- IMsRdpExtendedSettings.get_Property
- IMsRdpExtendedSettings.put_Property
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpExtendedSettings::Property property

Contains a named property.

This property is read/write.

## Syntax


```C++
HRESULT put_Property(
  [in]          BSTR    bstrPropertyName,
  [in]          VARIANT *pValue
);

HRESULT get_Property(
  [in]          BSTR    bstrPropertyName,
  [out, retval] VARIANT *pValue
);
```



## Property value

The named property value.

| Property name | Data type | Access | Can be changed after connection started | Description |
|----------|-----------|--------|-----------------------------------------|-------------|
| ConnectToChildSession | **VT\_BOOL** | Read/Write | Yes | Setting this property to **True** causes the client control to connect to the child session on the local machine instead of a remote server. If this property is set to **true**, you cannot connect to a remote server because all connections are redirected to localhost. For more information about child sessions, see [Child Sessions](child-sessions.md). |
| DisableCredentialsDelegation | **VT\_BOOL** | Read/Write | No | If **True**, credentials are not sent to the remote server. |
| EnableFrameBufferRedirection | **VT\_BOOL** | Read/Write | No | If **True**, frame buffer redirection is attempted. For a loopback connection (the same computer is both client and server) frame buffer redirection allows the memory for the frame buffer to be shared between the sessions. |
| EnableHardwareMode | **VT\_BOOL**  | Write Only | No | If **True**, hardware assist with graphics decoding is attempted. |
| IgnoreCursors | **VT\_BOOL** | Write Only | No | If **True**, cursors sent by the remote server are ignored. |
| ManualClipboardSyncEnabled | **VT\_BOOL** | Read/Write | Yes | Setting this property to **True** means that the local and remote clipboards will not be automatically kept in sync. Instead the [**IMsRdpClipboard**](imsrdpclipboard.md) interface must be used to sync clipboard formats from the local clipboard to the remote clipboard and the remote clipboard to the local clipboard. |
| ZoomLevel | ***VT\_UI4** | Read/Write | Yes | Implements the Zoom feature by using the RDP ActiveX control. The Zoom feature is available from the **System** menu of RDP. The **ZoomLevel** property has no effect in RemoteApp mode and full-screen mode. [**IMsRdpClientAdvancedSettings::SmartSizing**](imsrdpclientadvancedsettings-smartsizing.md) and **ZoomLevel** are mutually exclusive. |
| DisableSeamlessLanguageBar  |VT_BOOL  |R/W  |No  |If **True**, this causes RemoteApp connections to revert to the legacy language bar from before Windows 8, instead of automatically synchronizing the local language to the remote session.  |
| RedirectTextProcessing  |VT_BOOL  |W  |No  |Starting in Windows 11 23H2, enables/disables the redirection of text processing which provides a like-local experience for text input scenarios, e.g., IME, emoticons.  |
| HvSocketServiceId  |VT_BSTR  |W  |No  |Specifies the ServiceId field of the [Hyper-V socket](/virtualization/hyper-v-on-windows/user-guide/make-integration-service#bind-to-a-hyper-v-socket)'s address where the RDP traffic is to be sent.  |
| DeviceScaleFactor  |VT_UI4  |R/W  |No  |Specifies the [device scale factor](/openspecs/windows_protocols/ms-rdpbcgr/ab35aee7-1cf7-42dc-ac74-d0d7f4ca64f7#gt_657d0053-ac5f-44e2-ab78-7ba35317e57a) used in the remote session. <br>Valid values: 100, 140, 180  |
| EnableLocationRedirection  |VT_BOOL  |R/W  |No  |Enables/disables the redirection of the location of the local machine to the remote session.  |
| AudioCaptureDevice  |VT_BSTR  |R/W  |No  |Specifies the device ID of the audio capture device to redirect from the client to the remote session.<br>Applications can use the [DRV_QUERYFUNCTIONINSTANCEID](/windows/win32/coreaudio/endpoint-id-strings) message to determine the device ID of the audio capture device to redirect.<br>Alternatively, this can be set to "default" to use the default device or ""none"" to disable audio capture. By default, this is set to "default". |
| RailMode  |VT_BOOL  |R  |No  |Reports whether this is a RemoteApp connection. [ITSRemoteProgram::RemoteProgramMode](/windows/win32/termserv/itsremoteprogram-remoteprogrammode) writes to this property.  |
| EnableRdsAadAuth  |VT_BOOL  |W  |No  |If **True**, [RDS AAD Auth Security](/openspecs/windows_protocols/ms-rdpbcgr/dc43f040-d75d-49a9-90c6-0c9999281136) is used.  |
| RDGIsKDCProxy  |VT_BOOL  |W  |No  |If **True**, tells the client to use RD Gateway (if specified) as a [KDC Proxy server](/openspecs/windows_protocols/MS-KKDCP/5bcebb8d-b747-4ee5-9453-428aec1c5c38).  |
| UseURCP  |VT_BOOL  |R/W  |No  |If **True**, this property enables the Universal Rate Control Protocol for UDP-based Remote Desktop connections. Currently, it is disabled by default. Enabling it if UDP is in use is recommended.  |
| DesktopScaleFactor  |VT_UI4  |R/W  |No  |Specifies the [device scale factor](/openspecs/windows_protocols/ms-rdpbcgr/ab35aee7-1cf7-42dc-ac74-d0d7f4ca64f7#gt_657d0053-ac5f-44e2-ab78-7ba35317e57a) used in the remote session. The value should be between 100 and 500 (percent).  |
| RedirectedAuthentication  |VT_BOOL  |W  |No  |If **True**, [Remote Credential Guard](/windows/security/identity-protection/remote-credential-guard?tabs=intune) is enabled.  |
| RestrictedLogon  |VT_BOOL  |W  |No  |If **True**, [Restricted Admin mode](https://social.technet.microsoft.com/wiki/contents/articles/32905.remote-desktop-services-enable-restricted-admin-mode.aspx) is enabled.  |
| AudioPlaybackDevice  |VT_BSTR  |R/W  |No  |Specifies the device ID of the audio playback device on the local machine.<br>Applications can use the [DRV_QUERYFUNCTIONINSTANCEID](/windows/win32/coreaudio/endpoint-id-strings) message to determine the device ID of the audio playback device to redirect.<br>"Alternatively, this can be set to ""default"" to use the default device or ""none"" to disable audio playback. By default, this is set to ""default"". "|
| SelectedMonitors  |VT_BSTR  |R/W  |No  |A comma-delimited or semi-column-delimited list of monitor ID to identify the selected monitors where to display the remote session. The first ID in the list will be treated as the primary monitor in the remote session.  |
| WslgModeEnabled  |VT_BOOL  |W  |No  |If **True**, the session is a WSLg session.<br>The following properties are expected to be provided:<br><ul><li>WslgSharedMemoryPath</li><li>HvSocketEnabled</li><li>HvSocketServiceId</li></ul><br>Please refer to WSLg's documentation [https://github.com/microsoft/wslg](https://github.com/microsoft/wslg). |
| ShowSessionDiagnostics  |VT_BOOL  |W  |Yes  |Writing **True** to this property immediately shows a dialog with detailed information about the remote session. <br>This property is meant to be a debugging mechanism. It is subject to change and removal. |
| PrintingProgressMode  |VT_UI4  |R/W  |No  |Possible values: <ul><li>0: the progress dialog shown when printing is disabled</li><li>1: the progress dialog shown when printing contains basic information</li><li>2: the progress dialog shown when printing contains detailed information</li></ul>|
| CorrelationId  |VT_BOOL  |W  |No  |Overrides the value returned by [IMsRdpClientNonScriptable8::CorrelationId.](/windows/win32/termserv/imsrdpclientnonscriptable8-correlationid)  |
| RequestUseNewOutputPresenter  |VT_BOOL  |W  |No  |If **True**, the remote session is presented using DirectX only without fallback to GDI. This property does not apply to remote app sessions.<br>Note: this property is subject to removal in future versions of Windows as the DirectX-only mode might become the only available option. This is currently a preview feature that should not be enabled in production code. |
| GatewayCertificateLogonAuthority  |VT_BSTR  |W  |No  |This property is not supported anymore. It is subject to removal in future versions of Windows. Do not use this property.  |
| EnableRemoteEdgeBar  |VT_BOOL  |R/W  |No  |If **True** and the **ServerSupportsEdgeActions** property is **True**, additional commands are shown in the connection toolbar of the remote session.  |
| TSGTransportIsUsed  |VT_BOOL  |R  |N/A  |If **True**, a Remote Desktop gateway is in use for the associated remote session.  |
| DiagnosticsInfo  |VT_BSTR  |W  |No  |A hexadecimal string representing the **rdpCorrelationInfo.correlationId** field of the [Client X.224 Connection Request PDU](/openspecs/windows_protocols/ms-rdpbcgr/18a27ef9-6f9a-4501-b000-94b1fe3c2c10).  |
| EndpointFedAuth  |VT_BSTR  |W  |No  |The token used for claim-based federated [RDSTLS authentication](/openspecs/windows_protocols/ms-rdpbcgr/2aa353a2-2e46-4bb7-84ef-9354eb07a25f).  |
| AllowAxToContainerEvents  |VT_BOOL  |W  |No  |This property was added in Windows 11 22H2. <ul><li>If **False** (default behavior starting in Windows 11 22H2), CTRL+ALT+ARROW key combinations are sent to the remote session.</li><li>If **True** (default behavior before Windows 11 22H2), CTRL+ALT+ARROW key combinations raises a [IMsTscAxEvents::OnFocusReleased](/windows/win32/termserv/imstscaxevents-onfocusreleased) event to the application.</li></ul> |
| ServerSupportsEdgeActions  |VT_BOOL  |R  |N/A  |Read-only property to determine whether the remote session has the **RNS_UD_SC_EDGE_ACTIONS_SUPPORTED_V1** capability [https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/379a020e-9925-4b4f-98f3-7d634e10b411](/openspecs/windows_protocols/ms-rdpbcgr/379a020e-9925-4b4f-98f3-7d634e10b411).  |
| AppContainerID  |VT_BSTR  |W  |No  |The AppContainer ID passed to [IWorkspaceScriptable3::StartWorkspaceEx2](/windows/win32/api/workspaceruntime/nf-workspaceruntime-iworkspacescriptable3-startworkspaceex2) when [IMsRdpClientNonScriptable8::StartWorkspaceExtension](/windows/win32/termserv/imsrdpclientnonscriptable8-startworkspaceextension) is invoked.<br>Note: The RemoteApp and Desktop Connections control panel is no longer in active development. It may be altered or unavailable in future versions of Windows. The use of this API is discouraged. |
| IgnoreServerGeneratedMouseMoves  |VT_BOOL  |R/W  |No  |If **True**, mouse move generated programmatically in the remote session are ignored. More precisely, the Pointer Position Update PDU are not applied. See [https://learn.microsoft.com/openspecs/windows_protocols/ms-rdpbcgr/3058381e-c856-4b26-a93c-d8f5514f8c3c](/openspecs/windows_protocols/ms-rdpbcgr/3058381e-c856-4b26-a93c-d8f5514f8c3c).  |
| RDmiDiagnosticsUrl  |VT_BSTR  |W  |No  |This property is not supported anymore. It is subject to removal in future versions of Windows. Do not use this property.  |
| EnableVailMonitorConfig  |VT_BOOL  |R/W  |No  |If **True**, extended monitor info (e.g. EDIDs) are sent to the remote session when synchronizing display configurations.  |
| Workspace Id  |VT_BSTR  |W  |No  |The unique identifier of the connection in **RemoteApp and Desktop Connections** that the remote session belongs to.  |
| ShowConnectionInformation  |VT_BOOL  |W  |Yes  |Writing **True** to this property shows the Connection Information dialog.  |
| WslgSharedMemoryPath  |VT_BSTR  |W  |No  |The path to memory session object to share graphics buffer with WSLg virtual machine.  |
| HiDefRemoteAppContainerGUID  |VT_BSTR  |W  |No  |The GUID associated with the running VM that hosts the remote application. Writing this property results in improved performance for remote applications running in a local VM due to memory sharing.  |
| KDCProxyName  |VT_BSTR  |W  |No  |"Specifies fully qualified domain name of a Key Distribution Center (KDC) Proxy server. KDC Proxy allows RDP client to use Kerberos authentication protocol when it cannot access a KDC directly.  Example of the property value: ""kdc.contoso.com"". For more info see: [Configure a Kerberos Key Distribution Center proxy](/azure/virtual-desktop/key-distribution-center-proxy), [https://learn.microsoft.com/openspecs/windows_protocols/MS-KKDCP/5bcebb8d-b747-4ee5-9453-428aec1c5c38](/openspecs/windows_protocols/MS-KKDCP/5bcebb8d-b747-4ee5-9453-428aec1c5c38) |
| DisableTouchRemoting  |VT_BOOL  |R/W  |No  |If **True**, gestures on multi-touch screens will not be sent to the remote server. By default, this is set to **False**.  |
| HvSocketEnabled  |VT_BOOL  |W  |No  |If **True**, the remote server’s name, if it is a GUID, is interpreted as the VmId field of the Hyper-V socket's address where the RDP traffic is to be sent. By default, this is set to **False**.<br>For more information about Hyper-V socket's addresses, refer to [Bind to a Hyper-V socket](/virtualization/hyper-v-on-windows/user-guide/make-integration-service#bind-to-a-hyper-v-socket).  |
| MultipenRemotingSupported  |VT_BOOL  |W  |No  |If **True**, the simultaneous injection of input from up to four pen devices is supported in the remote session. By default, this is set to **False**.  |
| ShowGatewayInformation  |VT_BOOL  |W  |Yes  |Writing **True** to this property shows a dialog showing information about the Remote Desktop gateway.<br>Windows 11 22H2 and above: this property is no longer supported and was replaced by the **ShowConnectionInformation** property. |
| RedirectUsbDrive  |VT_UI4   |R/W  |Yes  |When not set or set to 0, to 0 or not set, the USB thumb drive redirects as drive direction. When set to 1, all USB thumb drives are redirected as USB devices automatically. When set to 2, USB thumb drives are listed as USB devices, users can choose to redirect them through USB redirection from the UI (device dialog in the connection bar) or RDP file entry "UsbDevicesToRedirect". |

 
## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8<br/>                                                                                                                                                                                                                                                                                           |
| Minimum supported server<br/> | Windows Server 2012<br/>                                                                                                                                                                                                                                                                                 |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                                                         |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                                                                                                                                         |
| CLSID<br/>                    | CLSID\_MsRdpClient7NotSafeForScripting is defined as 54d38bf7-b1ef-4479-9674-1bd6ea465258<br/> CLSID\_MsRdpClient8NotSafeForScripting is defined as A3BC03A0-041D-42E3-AD22-882B7865C9C5<br/> CLSID\_MsRdpClient9NotSafeForScripting is defined as 8B918B82-7985-4C24-89DF-C33AD2BBFBCD<br/> |
| IID<br/>                      | IID\_IMsRdpExtendedSettings is defined as 302D8188-0052-4807-806A-362B628F9AC5<br/>                                                                                                                                                                                                                      |



## See also

<dl> <dt>

[**IMsRdpExtendedSettings**](imsrdpextendedsettings.md)
</dt> </dl>

 

 





