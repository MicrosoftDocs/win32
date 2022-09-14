---
title: IMsRdpClientAdvancedSettings2 interface
description: Manages advanced client settings. Derives from the IMsRdpClientAdvancedSettings interface.
ms.assetid: 78cffdf5-bd99-4140-80b6-aa8632894487
ms.tgt_platform: multiple
keywords:
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings2
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings2 interface

Manages advanced client settings. Derives from the [**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md) interface. This interface includes methods to retrieve and set advanced (optional) properties for the Remote Desktop ActiveX control.

To obtain an instance of this interface, use the [**IMsTscAx::AdvancedSettings**](imstscax-advancedsettings.md) property to obtain an [**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md) interface pointer. Then call [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the **IMsTscAdvancedSettings** pointer, and pass **IID\_IMsRdpClientAdvancedSettings2** to **QueryInterface**.

## Members

The **IMsRdpClientAdvancedSettings2** interface inherits from [**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md). **IMsRdpClientAdvancedSettings2** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsRdpClientAdvancedSettings2** interface has these properties.



| Property                                                                                      | Access type           | Description                                                                                                                                           |
|:----------------------------------------------------------------------------------------------|:----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CanAutoReconnect**](imsrdpclientadvancedsettings2-canautoreconnect.md)<br/>         | Read-only<br/>  | Specifies whether the client control is able to reconnect automatically to the current session in the event of a network disconnection.<br/>    |
| [**EnableAutoReconnect**](imsrdpclientadvancedsettings2-enableautoreconnect.md)<br/>   | Read/write<br/> | Specifies whether to enable the client control to reconnect automatically to a session in the event of a network disconnection.<br/>            |
| [**MaxReconnectAttempts**](imsrdpclientadvancedsettings2-maxreconnectattempts.md)<br/> | Read/write<br/> | Specifies the number of times to try to reconnect during automatic reconnection. The valid values of this property are 0 to 200 inclusive.<br/> |



 

## Remarks

This interface has been extended by the following interfaces, with each new interface inheriting all the methods and properties of the previous interfaces:

-   [**IMsRdpClientAdvancedSettings3**](imstscadvancedsettings-interface.md)
-   [**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md)
-   [**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md)
-   [**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
-   [**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings2 is defined as 9ac42117-2b76-4320-aa44-0e616ab8437b<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md)
</dt> <dt>

[**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

