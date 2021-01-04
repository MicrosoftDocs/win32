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

 

 





