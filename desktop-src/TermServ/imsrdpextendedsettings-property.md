---
title: IMsRdpExtendedSettings Property property
description: Contains a named property.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
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
ms.author: windowssdkdev
ms.topic: article
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

<dl> <dt>

<span id="ConnectToChildSession"></span><span id="connecttochildsession"></span><span id="CONNECTTOCHILDSESSION"></span>ConnectToChildSession
</dt> <dd> <dl> <dt>

**Data type**: **VT\_BOOL**
</dt> <dt>

**Access**: Read/Write
</dt> <dt>

**Can be changed after connection started**: Yes
</dt> <dt>

**Description**: Setting this property to **True** causes the client control to connect to the child session on the local machine instead of a remote server. If this property is set to **true**, you cannot connect to a remote server because all connections are redirected to localhost. For more information about child sessions, see [Child Sessions](child-sessions.md).
</dt> </dl> </dd> <dt>

<span id="DisableCredentialsDelegation"></span><span id="disablecredentialsdelegation"></span><span id="DISABLECREDENTIALSDELEGATION"></span>DisableCredentialsDelegation
</dt> <dd> <dl> <dt>

**Data type**: **VT\_BOOL**
</dt> <dt>

**Access**: Read/Write
</dt> <dt>

**Can be changed after connection started**: No
</dt> <dt>

**Description**: If **True**, credentials are not sent to the remote server.
</dt> </dl> </dd> <dt>

<span id="EnableFrameBufferRedirection"></span><span id="enableframebufferredirection"></span><span id="ENABLEFRAMEBUFFERREDIRECTION"></span>EnableFrameBufferRedirection
</dt> <dd> <dl> <dt>

**Data type**: **VT\_BOOL**
</dt> <dt>

**Access**: Read/Write
</dt> <dt>

**Can be changed after connection started**: No
</dt> <dt>

**Description**: If **True**, frame buffer redirection is attempted. For a loopback connection (the same computer is both client and server) frame buffer redirection allows the memory for the frame buffer to be shared between the sessions.
</dt> </dl> </dd> <dt>

<span id="EnableHardwareMode"></span><span id="enablehardwaremode"></span><span id="ENABLEHARDWAREMODE"></span>EnableHardwareMode
</dt> <dd> <dl> <dt>

**Data type**: **VT\_BOOL**
</dt> <dt>

**Access**: Write Only
</dt> <dt>

**Can be changed after connection started**: No
</dt> <dt>

**Description**: If **True**, hardware assist with graphics decoding is attempted.
</dt> </dl> </dd> <dt>

<span id="IgnoreCursors"></span><span id="ignorecursors"></span><span id="IGNORECURSORS"></span>IgnoreCursors
</dt> <dd> <dl> <dt>

**Data type**: **VT\_BOOL**
</dt> <dt>

**Access**: Write Only
</dt> <dt>

**Can be changed after connection started**: No
</dt> <dt>

**Description**: If **True**, cursors sent by the remote server are ignored.
</dt> </dl> </dd> <dt>

<span id="ZoomLevel"></span><span id="zoomlevel"></span><span id="ZOOMLEVEL"></span>ZoomLevel
</dt> <dd> <dl> <dt>

**Data type**: **VT\_UI4**
</dt> <dt>

**Access**: Read/Write
</dt> <dt>

**Can be changed after connection started**: Yes
</dt> <dt>

**Description**: Implements the Zoom feature by using the RDP ActiveX control. The Zoom feature is available from the **System** menu of RDP. The **ZoomLevel** property has no effect in RemoteApp mode and full-screen mode. [**IMsRdpClientAdvancedSettings::SmartSizing**](imsrdpclientadvancedsettings-smartsizing.md) and **ZoomLevel** are mutually exclusive. 
</dt> </dl> </dd> </dl>

## Requirements



|                                     |                                                                                                                                                                                                                                                                                                                |
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

 

 





