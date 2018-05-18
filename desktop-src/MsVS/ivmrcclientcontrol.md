---
title: VMRCClientControl interface
description: VMRCClientControl interface
ms.assetid: '243d3fa2-8a7d-42d0-8c8a-7ffd28f4aec2'
keywords: ["VMRCClientControl interface Virtual Server", "VMRCClientControl interface Virtual Server , described"]
topic_type:
- apiref
api_name:
- VMRCClientControl
api_location:
- VMRCClientControl.lib
- VMRCClientControl.dll
api_type:
- COM
---

# VMRCClientControl interface

## Members

The **VMRCClientControl** interface inherits from IDispatch and IUnknown. **VMRCClientControl** also has these types of members:

-   [Methods](#methods)
-   [Properties](#properties)

### Methods

The **VMRCClientControl** interface has these methods.



| Method                                                              | Description                                                                                                       |
|:--------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------|
| [**AboutBox**](ivmrcclientcontrol-aboutbox.md)                     | Displays the control's copyright and version information in a dialog box.<br/>                              |
| [**AdminDisplay**](ivmrcclientcontrol-admindisplay.md)             | Displays the control's administrative information screen.<br/>                                              |
| [**Connect**](ivmrcclientcontrol-connect.md)                       | Disconnects the control from the current VMRC server (if necessary) and connects to a new VMRC server.<br/> |
| [**Disconnect**](ivmrcclientcontrol-disconnect.md)                 | Disconnects the control from the current VMRC server.<br/>                                                  |
| [**Refresh**](ivmrcclientcontrol-refresh.md)                       | Updates the control's client window.<br/>                                                                   |
| [**SendKeySequence**](ivmrcclientcontrol-sendkeysequence.md)       | Simulates a sequence of keys typed in the guest with the current input focus.<br/>                          |
| [**ShowConnectionInfo**](ivmrcclientcontrol-showconnectioninfo.md) | Displays the control's connection information screen.<br/>                                                  |



 

### Properties

The **VMRCClientControl** interface has these properties.



| Property                                                                         | Access type           | Description                                                                                              |
|:---------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------------------------|
| [**AdministratorMode**](ivmrcclientcontrol-administratormode.md)<br/>     | Read/write<br/> | Indicates whether the administrator features of the client are enabled.<br/>                       |
| [**AutoSize**](ivmrcclientcontrol-autosize.md)<br/>                       | Read/write<br/> | Indicates whether if the control determines its own size.<br/>                                     |
| [**Enabled**](ivmrcclientcontrol-enabled.md)<br/>                         | Read/write<br/> | Indicates whether the control is enabled.<br/>                                                     |
| [**HostKey**](ivmrcclientcontrol-hostkey.md)<br/>                         | Read/write<br/> | The key identifier for the current Host Key.<br/>                                                  |
| [**MenuBackColor**](ivmrcclientcontrol-menubackcolor.md)<br/>             | Read/write<br/> | The client's menu background color in HTML hex string format.<br/>                                 |
| [**MenuEnabled**](ivmrcclientcontrol-menuenabled.md)<br/>                 | Read/write<br/> | Indicates whether the client's menu is displayed.<br/>                                             |
| [**MenuFontColor**](ivmrcclientcontrol-menufontcolor.md)<br/>             | Read/write<br/> | The client's menu font color in HTML hex string format.<br/>                                       |
| [**MenuFontFace**](ivmrcclientcontrol-menufontface.md)<br/>               | Read/write<br/> | The client's menu font face.<br/>                                                                  |
| [**MenuFontSize**](ivmrcclientcontrol-menufontsize.md)<br/>               | Read/write<br/> | The client's menu font size.<br/>                                                                  |
| [**MenuHeight**](ivmrcclientcontrol-menuheight.md)<br/>                   | Read/write<br/> | The height of the client's menu in pixels.<br/>                                                    |
| [**ReadyState**](ivmrcclientcontrol-readystate.md)<br/>                   | Read/write<br/> | The control's current readiness state.<br/>                                                        |
| [**ReducedColorsMode**](ivmrcclientcontrol-reducedcolorsmode.md)<br/>     | Read/write<br/> | Indicates whether the client's reduced colors mode is enabled.<br/>                                |
| [**ServerAddress**](ivmrcclientcontrol-serveraddress.md)<br/>             | Read/write<br/> | The network address of the VMRC server.<br/>                                                       |
| [**ServerDisplayHeight**](ivmrcclientcontrol-serverdisplayheight.md)<br/> | Read-only<br/>  | The height of the video display area in pixels.<br/>                                               |
| [**ServerDisplayName**](ivmrcclientcontrol-serverdisplayname.md)<br/>     | Read/write<br/> | The name of the virtual machine to be displayed.<br/>                                              |
| [**ServerDisplayWidth**](ivmrcclientcontrol-serverdisplaywidth.md)<br/>   | Read-only<br/>  | The width of the video display area in pixels.<br/>                                                |
| [**ServerPort**](ivmrcclientcontrol-serverport.md)<br/>                   | Read/write<br/> | The TCP port of the VMRC server.<br/>                                                              |
| [**ShrinkEnabled**](ivmrcclientcontrol-shrinkenabled.md)<br/>             | Read/write<br/> | Indicates whether the client's window stretches its contents to fit its size.<br/>                 |
| [**State**](ivmrcclientcontrol-state.md)<br/>                             | Read-only<br/>  | The state of the current connection to the VMRC server.<br/>                                       |
| [**UserDomain**](ivmrcclientcontrol-userdomain.md)<br/>                   | Write-only<br/> | The network domain to use for authenticating credentials with the VMRC server.<br/>                |
| [**UserName**](ivmrcclientcontrol-username.md)<br/>                       | Write-only<br/> | The network user account name to use for authenticating credentials with the VMRC server.<br/>     |
| [**UserPassword**](ivmrcclientcontrol-userpassword.md)<br/>               | Write-only<br/> | The network user account password to use for authenticating credentials with the VMRC server.<br/> |
| [**ViewOnlyMode**](ivmrcclientcontrol-viewonlymode.md)<br/>               | Read/write<br/> | Indicates whether the client's view-only mode is enabled.<br/>                                     |



 

## Requirements



|                    |                                                                                                  |
|--------------------|--------------------------------------------------------------------------------------------------|
| Header<br/>  | <dl> <dt>VMRCClientControl.h</dt> </dl>   |
| Library<br/> | <dl> <dt>VMRCClientControl.lib</dt> </dl> |



 

 





