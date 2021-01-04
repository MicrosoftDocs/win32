---
title: IMsTscAx SecuredSettings property
description: Retrieves an IMsTscSecuredSettings interface pointer.
ms.assetid: 64d4059b-e617-449d-a733-c19c1d281132
ms.tgt_platform: multiple
keywords:
- SecuredSettings property Remote Desktop Services
- SecuredSettings property Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , SecuredSettings property
- SecuredSettings property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , SecuredSettings property
topic_type:
- apiref
api_name:
- IMsTscAx.SecuredSettings
- IMsTscAx.get_SecuredSettings
- IMsRdpClient.SecuredSettings
- IMsRdpClient.get_SecuredSettings
- IMsRdpClient2.SecuredSettings
- IMsRdpClient2.get_SecuredSettings
- IMsRdpClient3.SecuredSettings
- IMsRdpClient3.get_SecuredSettings
- IMsRdpClient4.SecuredSettings
- IMsRdpClient4.get_SecuredSettings
- IMsRdpClient5.SecuredSettings
- IMsRdpClient5.get_SecuredSettings
- IMsRdpClient6.SecuredSettings
- IMsRdpClient6.get_SecuredSettings
- IMsRdpClient7.SecuredSettings
- IMsRdpClient7.get_SecuredSettings
- IMsRdpClient8.SecuredSettings
- IMsRdpClient8.get_SecuredSettings
- IMsRdpClient9.SecuredSettings
- IMsRdpClient9.get_SecuredSettings
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::SecuredSettings property

Retrieves an [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface pointer.

This property is read-only.

## Syntax


```C++
HRESULT get_SecuredSettings(
  [out] IMsTscSecuredSettings **ppSecuredSettings
);
```



## Property value

An [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface pointer.

## Error codes

Return **S\_OK** if successful.

## Remarks

If the control is hosted in a webpage and the current Internet Explorer URL security zone does not permit the retrieval of the interface address, this method returns **E\_FAIL**.

Refer to [**SecuredSettingsEnabled**](imstscax-securedsettingsenabled.md) for restrictions on the availability of the [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsTscAx is defined as 8C11EFAE-92C3-11D1-BC1E-00C04FA31489<br/>            |



## See also

<dl> <dt>

[**IMsRdpClient**](imsrdpclient-interface.md)
</dt> <dt>

[**IMsRdpClient2**](imsrdpclient2.md)
</dt> <dt>

[**IMsRdpClient3**](imsrdpclient3.md)
</dt> <dt>

[**IMsRdpClient4**](imsrdpclient4.md)
</dt> <dt>

[**IMsRdpClient5**](imsrdpclient5.md)
</dt> <dt>

[**IMsRdpClient6**](imsrdpclient6.md)
</dt> <dt>

[**IMsRdpClient7**](imsrdpclient7.md)
</dt> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**IMsTscAx**](imstscax-interface.md)
</dt> <dt>

[**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md)
</dt> </dl>

 

 





