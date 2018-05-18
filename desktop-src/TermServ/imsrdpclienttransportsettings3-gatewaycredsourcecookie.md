---
title: IMsRdpClientTransportSettings3 GatewayCredSourceCookie property
description: Specifies if the credential source is cookie based.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: '039459a3-7a83-444c-a0b4-46ef0dc5ddd0'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["GatewayCredSourceCookie property Remote Desktop Services", "GatewayCredSourceCookie property Remote Desktop Services , IMsRdpClientTransportSettings3 interface", "IMsRdpClientTransportSettings3 interface Remote Desktop Services , GatewayCredSourceCookie property"]
topic_type:
- apiref
api_name:
- IMsRdpClientTransportSettings3.GatewayCredSourceCookie
- IMsRdpClientTransportSettings3.get_GatewayCredSourceCookie
- IMsRdpClientTransportSettings3.put_GatewayCredSourceCookie
api_location:
- MsTscAx.dll
api_type:
- COM
---

# IMsRdpClientTransportSettings3::GatewayCredSourceCookie property

Specifies if the credential source is cookie based. Contains one if the credential source is cookie-based or zero otherwise.

This property is read/write.

## Syntax


```C++
HRESULT put_GatewayCredSourceCookie(
  [in]          ULONG ulProxyCredSourceCookie
);

HRESULT get_GatewayCredSourceCookie(
  [out, retval] ULONG *pulProxyCredSourceCookie
);
```



## Property value

A **ULONG** value that specifies if the credential source is cookie based.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClientTransportSettings3**](imsrdpclienttransportsettings3.md)
</dt> </dl>

 

 





