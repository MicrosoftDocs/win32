---
title: IMsRdpClientAdvancedSettings3 interface
description: Manages advanced client settings. Derives from the IMsRdpClientAdvancedSettings2 interface.
ms.assetid: bfa9cf74-5943-45ca-9259-3ef0cc9ab2ab
ms.tgt_platform: multiple
keywords:
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings3
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings3 interface

Manages advanced client settings. Derives from the [**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md) interface. This interface includes methods to retrieve and set advanced (optional) properties for the Remote Desktop ActiveX control.

To obtain an instance of this interface, use the [**IMsTscAx::AdvancedSettings**](imstscax-advancedsettings.md) property to obtain an [**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md) interface pointer. Then call [**QueryInterface**](/windows/desktop/api/unknwn/nf-unknwn-iunknown-queryinterface(q)) on the **IMsTscAdvancedSettings** pointer, and pass **IID\_IMsRdpClientAdvancedSettings3** to **QueryInterface**.

## Members

The **IMsRdpClientAdvancedSettings3** interface inherits from [**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md). **IMsRdpClientAdvancedSettings3** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsRdpClientAdvancedSettings3** interface has these properties.



| Property                                                                                                            | Access type           | Description                                                                            |
|:--------------------------------------------------------------------------------------------------------------------|:----------------------|:---------------------------------------------------------------------------------------|
| [**ConnectionBarShowMinimizeButton**](imsrdpclientadvancedsettings3-connectionbarshowminimizebutton.md)<br/> | Read/write<br/> | Specifies whether to display the **Minimize** button on the connection bar.<br/> |
| [**ConnectionBarShowRestoreButton**](imsrdpclientadvancedsettings3-connectionbarshowrestorebutton.md)<br/>   | Read/write<br/> | Specifies whether to display the **Restore** button on the connection bar.<br/>  |



 

## Remarks

This interface has been extended by the following interfaces, with each new interface inheriting all the methods and properties of the previous interfaces:

-   [**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md)
-   [**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md)
-   [**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
-   [**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
-   [**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings3 is defined as 19cd856b-c542-4c53-acee-f127e3be1a59<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md)
</dt> <dt>

[**IMsTscAdvancedSettings**](imstscadvancedsettings-interface.md)
</dt> <dt>

[Remote Desktop Web Connection Reference](remote-desktop-web-connection-reference.md)
</dt> </dl>

 

