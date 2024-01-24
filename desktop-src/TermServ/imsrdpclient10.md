---
title: IMsRdpClient10 interface
description: Provides the methods and properties needed to configure and use the client control. Derives from the IMsRdpClient9 interface.
ms.assetid: 601f70aa-85f1-4180-921b-9f1bb31d4def
ms.tgt_platform: multiple
keywords:
- IMsRdpClient10 interface Remote Desktop Services
- IMsRdpClient10 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClient10
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient10 interface

Provides the methods and properties needed to configure and use the client control. Derives from the [**IMsRdpClient9**](imsrdpclient9.md) interface.

## Members

The **IMsRdpClient10** interface inherits from [**IMsRdpClient9**](imsrdpclient9.md). **IMsRdpClient10** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **IMsRdpClient10** interface has these methods.



| Method                                                                             | Description                                                                         |
|:-----------------------------------------------------------------------------------|:------------------------------------------------------------------------------------|
| [**attachEvent**](imsrdpclient9-attachevent.md)                                   | Attaches an event.<br/>                                                       |
| [**detachEvent**](imsrdpclient9-detachevent.md)                                   | Detaches an event.<br/>                                                       |
| [**GetErrorDescription**](imsrdpclient5-geterrordescription.md)                   | Retrieves the error description for the session disconnect events.<br/>       |
| [**GetStatusText**](imsrdpclient7-getstatustext.md)                               | Retrieves the status text for the specified status code.<br/>                 |
| [**GetVirtualChannelOptions**](imsrdpclient-getvirtualchanneloptions.md)          | Retrieves the options set for a virtual channel.<br/>                         |
| [**Reconnect**](imsrdpclient8-reconnect.md)                                       | Reconnects to the remote session with the new desktop width and height.<br/>  |
| [**RequestClose**](imsrdpclient-requestclose.md)                                  | Requests a graceful shutdown of the Remote Desktop ActiveX control.<br/>      |
| [**SendRemoteAction**](imsrdpclient8-sendremoteaction.md)                         | Causes an action to be performed in the remote session.<br/>                  |
| [**SetVirtualChannelOptions**](imsrdpclient-setvirtualchanneloptions.md)          | Sets the virtual channel options for the Remote Desktop ActiveX control.<br/> |
| [**SyncSessionDisplaySettings**](imsrdpclient9-syncsessiondisplaysettings.md)     | Synchronizes session display settings.<br/>                                   |
| [**UpdateSessionDisplaySettings**](/previous-versions/windows/desktop/legacy/mt703457(v=vs.85)) | Updates session display settings.<br/>                                        |



 

### Properties

The **IMsRdpClient10** interface has these properties.



| Property                                                                             | Access type           | Description                                                                                                                                                                                                |
|:-------------------------------------------------------------------------------------|:----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**AdvancedSettings2**](imsrdpclient-advancedsettings2.md)<br/>               | Read-only<br/>  | Retrieves a pointer to the [**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md) interface. The interface can be used to set advanced settings for the client control.<br/> |
| [**AdvancedSettings3**](imsrdpclient2-advancedsettings3.md)<br/>              | Read-only<br/>  | Retrieves a pointer to the [**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md) interface. The interface can be used to set advanced settings for the client control.<br/>         |
| [**AdvancedSettings4**](imsrdpclient3-advancedsettings4.md)<br/>              | Read-only<br/>  | Retrieves a pointer to the [**IMsRdpClientAdvancedSettings3**](imsrdpclientadvancedsettings3.md) interface.<br/>                                                                                    |
| [**AdvancedSettings5**](imsrdpclient4-advancedsettings5.md)<br/>              | Read-only<br/>  | Retrieves a pointer to an [**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md) interface.<br/>                                                                                     |
| [**AdvancedSettings6**](imsrdpclient5-advancedsettings6.md)<br/>              | Read-only<br/>  | Retrieves the [**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md) interface.<br/>                                                                                                 |
| [**AdvancedSettings7**](imsrdpclient6-advancedsettings7.md)<br/>              | Read-only<br/>  | Retrieves the [**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings5.md) interface.<br/>                                                                                                 |
| [**AdvancedSettings8**](imsrdpclient7-advancedsettings8.md)<br/>              | Read-only<br/>  | Retrieves an object that supports the [**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md) interface.<br/>                                                                         |
| [**AdvancedSettings9**](imsrdpclient8-advancedsettings9.md)<br/>              | Read-only<br/>  | Contains an object that supports the [**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md) interface.<br/>                                                                          |
| [**ColorDepth**](imsrdpclient-colordepth.md)<br/>                             | Read/write<br/> | The color depth (in bits per pixel) for the control's connection.<br/>                                                                                                                               |
| [**ConnectedStatusText**](imsrdpclient2-connectedstatustext.md)<br/>          | Read/write<br/> | Contains the text that is displayed in the client area of the control while the control is in the connected state.<br/>                                                                              |
| [**ExtendedDisconnectReason**](imsrdpclient-extendeddisconnectreason.md)<br/> | Read-only<br/>  | Contains extended information about the control's reason for disconnection.<br/>                                                                                                                     |
| [**FullScreen**](imsrdpclient-fullscreen.md)<br/>                             | Read/write<br/> | Determines whether the client control is in full-screen mode.<br/>                                                                                                                                   |
| [**MsRdpClientShell**](imsrdpclient5-msrdpclientshell.md)<br/>                | Read-only<br/>  | Retrieves the scriptable client setting interface [**IMsRdpClientShell**](imsrdpclientshell.md).<br/>                                                                                               |
| [**RemoteProgram**](imsrdpclient5-remoteprogram.md)<br/>                      | Read-only<br/>  | Retrieves an object that supports the [**ITSRemoteProgram**](itsremoteprogram.md) interface.<br/>                                                                                                   |
| [**RemoteProgram2**](imsrdpclient7-remoteprogram2.md)<br/>                    | Read-only<br/>  | Retrieves an object that supports the [**ITSRemoteProgram2**](itsremoteprogram2.md) interface.<br/>                                                                                                 |
| [**RemoteProgram3**](imsrdpclient10-remoteprogram3.md)<br/>                   | Read-only<br/>  | An object that supports the [**ITSRemoteProgram3**](itsremoteprogram3.md) interface.<br/>                                                                                                           |
| [**SecuredSettings2**](imsrdpclient-securedsettings2.md)<br/>                 | Read-only<br/>  | Retrieves a pointer to the [**IMsRdpClientSecuredSettings**](imsrdpclientsecuredsettings-interface.md) interface. This interface can be used to set secured settings for the client control.<br/>   |
| [**SecuredSettings3**](imsrdpclient7-securedsettings3.md)<br/>                | Read-only<br/>  | Retrieves an object that supports the [**IMsRdpClientSecuredSettings2**](imsrdpclientsecuredsettings2.md) interface.<br/>                                                                           |
| [**TransportSettings**](imsrdpclient5-transportsettings.md)<br/>              | Read-only<br/>  | Retrieves what was passed through a script to the [**IMsRdpClientTransportSettings**](imsrdpclienttransportsettings.md) interface.<br/>                                                             |
| [**TransportSettings2**](imsrdpclient6-transportsettings2.md)<br/>            | Read-only<br/>  | Retrieves the [**IMsRdpClientTransportSettings2**](imsrdpclienttransportsettings2.md) interface.<br/>                                                                                               |
| [**TransportSettings3**](imsrdpclient7-transportsettings3.md)<br/>            | Read-only<br/>  | Retrieves an object that supports the [**IMsRdpClientTransportSettings3**](imsrdpclienttransportsettings3.md) interface.<br/>                                                                       |
| [**TransportSettings4**](imsrdpclient9-transportsettings4.md)<br/>            | Read-only<br/>  | Retrieves an object that supports the [**IMsRdpClientTransportSettings4**](imsrdpclienttransportsettings4.md) interface.<br/>                                                                       |



 

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                                                                                                                              |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                                                                                                                           |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                   |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>                                                                                                   |
| CLSID<br/>                    | CLSID\_MsRdpClient10 is defined as C0EFA91A-EEB7-41C7-97FA-F0ED645EFB24<br/> CLSID\_MsRdpClient10NotSafeForScripting is defined as A0C63C30-F08D-4AB4-907C-34905D770C7D<br/> |
| IID<br/>                      | IID\_IMsRdpClient10 is defined as 7ED92C39-EB38-4927-A70A-708AC5A59321<br/>                                                                                                        |



## See also

<dl> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient7**](imsrdpclient7.md)
</dt> <dt>

[**IMsRdpClient6**](imsrdpclient6.md)
</dt> <dt>

[**IMsRdpClient5**](imsrdpclient5.md)
</dt> <dt>

[**IMsRdpClient4**](imsrdpclient4.md)
</dt> <dt>

[**IMsRdpClient3**](imsrdpclient3.md)
</dt> <dt>

[**IMsRdpClient2**](imsrdpclient2.md)
</dt> <dt>

[**IMsRdpClient**](imsrdpclient-interface.md)
</dt> <dt>

[**IMsTscAx**](imstscax-interface.md)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

