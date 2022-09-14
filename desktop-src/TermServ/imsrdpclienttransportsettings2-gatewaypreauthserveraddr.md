---
title: IMsRdpClientTransportSettings2 GatewayPreAuthServerAddr property
description: Specifies or retrieves the web address of the pre-authentication server, which is used for the Remote Desktop Gateway (RD Gateway) one-time password (OTP) feature.
ms.assetid: 14edad82-ab19-46fe-b878-d34298763c56
ms.tgt_platform: multiple
keywords:
- GatewayPreAuthServerAddr property Remote Desktop Services
- GatewayPreAuthServerAddr property Remote Desktop Services , IMsRdpClientTransportSettings2 interface
- IMsRdpClientTransportSettings2 interface Remote Desktop Services , GatewayPreAuthServerAddr property
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings2.GatewayPreAuthServerAddr
- IMsRdpClientTransportSettings2.get_GatewayPreAuthServerAddr
- IMsRdpClientTransportSettings2.put_GatewayPreAuthServerAddr
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientTransportSettings2::GatewayPreAuthServerAddr property

Specifies or retrieves the web address of the pre-authentication server, which is used for the Remote Desktop Gateway (RD Gateway) one-time password (OTP) feature.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayPreAuthServerAddr(
  [in]  BSTR bstrProxyPreAuthServerAddr
);

HRESULT get_GatewayPreAuthServerAddr(
  [out] BSTR *pbstrProxyPreAuthServerAddr
);
```



## Property value

The web address of the pre-authentication server; for example, the web address of the Microsoft Internet Security and Acceleration (ISA) server. Specify the web address by using the format "https://*HostName*.*DomainName*.com/*WebsiteName*" or "https://*HostName*.*DomainName*.com/*WebsiteName*".

## Error codes

Returns **S\_OK** if successful.

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
</dt> <dt>

[**IMsRdpClientTransportSettings2**](imsrdpclienttransportsettings2.md)
</dt> </dl>

 

 





