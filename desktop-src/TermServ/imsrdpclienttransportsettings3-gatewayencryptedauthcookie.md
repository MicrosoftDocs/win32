---
title: IMsRdpClientTransportSettings3 GatewayEncryptedAuthCookie property
description: The encrypted authentication cookie.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'c9ab6667-327c-44f8-a10e-b048ea91980c'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GatewayEncryptedAuthCookie property Remote Desktop Services", "GatewayEncryptedAuthCookie property Remote Desktop Services , IMsRdpClientTransportSettings3 interface", "IMsRdpClientTransportSettings3 interface Remote Desktop Services , GatewayEncryptedAuthCookie property"]
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings3.GatewayEncryptedAuthCookie
- IMsRdpClientTransportSettings3.get_GatewayEncryptedAuthCookie
- IMsRdpClientTransportSettings3.put_GatewayEncryptedAuthCookie
api_location:
- MsTscAx.dll
api_type:
- COM
---

# IMsRdpClientTransportSettings3::GatewayEncryptedAuthCookie property

The encrypted authentication cookie. The size of the property is specified by the [**GatewayEncryptedAuthCookieSize**](imsrdpclienttransportsettings3-gatewayencryptedauthcookiesize.md) property.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayEncryptedAuthCookie(
  [in]          BSTR bstrEncryptedAuthCookie
);

HRESULT get_GatewayEncryptedAuthCookie(
  [out, retval] BSTR *pbstrEncryptedAuthCookie
);
```



## Property value

The new encrypted authentication cookie.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**GatewayEncryptedAuthCookieSize**](imsrdpclienttransportsettings3-gatewayencryptedauthcookiesize.md)
</dt> <dt>

[**IMsRdpClientTransportSettings3**](imsrdpclienttransportsettings3.md)
</dt> </dl>

 

 





