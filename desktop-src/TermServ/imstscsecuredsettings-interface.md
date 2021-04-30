---
title: IMsTscSecuredSettings interface
description: Includes methods to retrieve and set properties of the Remote Desktop ActiveX control that are restricted to specific Internet Explorer URL security zones. | IMsTscSecuredSettings interface
ms.assetid: 1136dbc5-abe6-40e0-b44f-700a1460fbd2
ms.tgt_platform: multiple
keywords:
- IMsTscSecuredSettings interface Remote Desktop Services
- IMsTscSecuredSettings interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsTscSecuredSettings
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscSecuredSettings interface

Includes methods to retrieve and set properties of the Remote Desktop ActiveX control that are restricted to specific Internet Explorer URL security zones. Properties include those that specify the mode of the client control (full-screen mode or window mode) and the program to start upon connection to the Remote Desktop Session Host (RD Session Host) server. These methods are also available through the [**IMsRdpClientSecuredSettings**](imsrdpclientsecuredsettings-interface.md) interface.

## Members

The **IMsTscSecuredSettings** interface inherits from the [**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch) interface. **IMsTscSecuredSettings** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsTscSecuredSettings** interface has these properties.



| Property                                                              | Access type           | Description                                                                |
|:----------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------|
| [**FullScreen**](imstscsecuredsettings-fullscreen.md)<br/>     | Read/write<br/> | The full-screen state of the client control.<br/>                    |
| [**StartProgram**](imstscsecuredsettings-startprogram.md)<br/> | Read/write<br/> | The program to be started on the remote server upon connection.<br/> |
| [**WorkDir**](imstscsecuredsettings-workdir.md)<br/>           | Read/write<br/> | The working directory of the start program.<br/>                     |



 

## Remarks

Refer to [Providing for RDP Client Security](providing-for-rdp-client-security.md) for more information about the methods of this interface.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IDispatch**](/windows/win32/api/oaidl/nn-oaidl-idispatch)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

