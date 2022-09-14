---
title: IMsRdpClientTransportSettings2 interface
description: Manages client transport settings for the Remote Desktop Gateway (RD Gateway) server. | IMsRdpClientTransportSettings2 interface
ms.assetid: 4f9f1905-2693-4666-9f6f-6e00b1eb6a0f
ms.tgt_platform: multiple
keywords:
- IMsRdpClientTransportSettings2 interface Remote Desktop Services
- IMsRdpClientTransportSettings2 interface Remote Desktop Services , described
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings2
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings2 interface

Manages client transport settings for the Remote Desktop Gateway (RD Gateway) server.

## Members

The **IMsRdpClientTransportSettings2** interface inherits from [**IMsRdpClientTransportSettings**](imsrdpclienttransportsettings.md). **IMsRdpClientTransportSettings2** also has these types of members:

-   [Properties](#properties)

### Properties

The **IMsRdpClientTransportSettings2** interface has these properties.



| Property                                                                                                    | Access type           | Description                                                                                       |
|:------------------------------------------------------------------------------------------------------------|:----------------------|:--------------------------------------------------------------------------------------------------|
| [**GatewayCredSharing**](imsrdpclienttransportsettings2-gatewaycredsharing.md)<br/>                  | Read/write<br/> | Indicates whether the single sign-on feature for RD Gateway is enabled.<br/>                |
| [**GatewayDomain**](imsrdpclienttransportsettings2-gatewaydomain.md)<br/>                            | Read/write<br/> | The domain name that a user provides to connect to the RD Gateway server.<br/>              |
| [**GatewayEncryptedOtpCookie**](imsrdpclienttransportsettings2-gatewaypreauthserveraddr.md)<br/>     | Read/write<br/> | The encrypted OTP cookie.<br/>                                                              |
| [**GatewayEncryptedOtpCookieSize**](imsrdpclienttransportsettings2-gatewaypreauthserveraddr.md)<br/> | Read/write<br/> | The size, in bytes, of the encrypted OTP cookie.<br/>                                       |
| [**GatewayPassword**](imsrdpclienttransportsettings2-gatewaypassword.md)<br/>                        | Write-only<br/> | The password that a user provides to connect to the RD Gateway server.<br/>                 |
| [**GatewayPreAuthRequirement**](imsrdpclienttransportsettings2-gatewaypreauthrequirement.md)<br/>    | Read/write<br/> | Indicates whether the RD Gateway one-time password (OTP) feature is enabled.<br/>           |
| [**GatewayPreAuthServerAddr**](imsrdpclienttransportsettings2-gatewaypreauthserveraddr.md)<br/>      | Read/write<br/> | The web address of the pre-authentication server.<br/>                                      |
| [**GatewaySupportUrl**](imsrdpclienttransportsettings2-gatewaypreauthserveraddr.md)<br/>             | Read/write<br/> | The web address of the site that provides technical support for the RD Gateway server.<br/> |
| [**GatewayUsername**](imsrdpclienttransportsettings2-gatewayusername.md)<br/>                        | Read/write<br/> | The user name that a user provides to connect to the RD Gateway server.<br/>                |



 

## Requirements



| Requirement | Value |
|-------------------------------------|---------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista with SP1<br/>                                                                 |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                    |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>            |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>            |
| IID<br/>                      | IID\_IMsRdpClientTransportSettings2 is defined as 67341688-D606-4c73-A5D2-2E0489009319<br/> |



## See also

<dl> <dt>

[**IMsRdpClientTransportSettings**](imsrdpclienttransportsettings.md)
</dt> </dl>

 

 





