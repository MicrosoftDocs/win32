---
title: IMsTscAx SecuredSettingsEnabled property
description: Indicates whether the IMsTscSecuredSettings interface is available. That is, whether the webpage containing the control is currently in one of the allowed Internet Explorer URL security zones.
ms.assetid: 0747eab0-9d62-4c10-b02d-fc65ca2f752e
ms.tgt_platform: multiple
keywords:
- SecuredSettingsEnabled property Remote Desktop Services
- SecuredSettingsEnabled property Remote Desktop Services , IMsTscAx interface
- IMsTscAx interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient interface
- IMsRdpClient interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient2 interface
- IMsRdpClient2 interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient3 interface
- IMsRdpClient3 interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient4 interface
- IMsRdpClient4 interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient5 interface
- IMsRdpClient5 interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient6 interface
- IMsRdpClient6 interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , SecuredSettingsEnabled property
- SecuredSettingsEnabled property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , SecuredSettingsEnabled property
topic_type:
- apiref
api_name:
- IMsTscAx.SecuredSettingsEnabled
- IMsTscAx.get_SecuredSettingsEnabled
- IMsRdpClient.SecuredSettingsEnabled
- IMsRdpClient.get_SecuredSettingsEnabled
- IMsRdpClient2.SecuredSettingsEnabled
- IMsRdpClient2.get_SecuredSettingsEnabled
- IMsRdpClient3.SecuredSettingsEnabled
- IMsRdpClient3.get_SecuredSettingsEnabled
- IMsRdpClient4.SecuredSettingsEnabled
- IMsRdpClient4.get_SecuredSettingsEnabled
- IMsRdpClient5.SecuredSettingsEnabled
- IMsRdpClient5.get_SecuredSettingsEnabled
- IMsRdpClient6.SecuredSettingsEnabled
- IMsRdpClient6.get_SecuredSettingsEnabled
- IMsRdpClient7.SecuredSettingsEnabled
- IMsRdpClient7.get_SecuredSettingsEnabled
- IMsRdpClient8.SecuredSettingsEnabled
- IMsRdpClient8.get_SecuredSettingsEnabled
- IMsRdpClient9.SecuredSettingsEnabled
- IMsRdpClient9.get_SecuredSettingsEnabled
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsTscAx::SecuredSettingsEnabled property

Indicates whether the [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface is available. That is, whether the webpage containing the control is currently in one of the allowed Internet Explorer URL security zones.

This property is read-only.

## Syntax


```C++
HRESULT get_SecuredSettingsEnabled(
  [out] BOOL *pSecuredSettingsEnabled
);
```



## Property value

The value of this parameter is **TRUE** if the interface is available, and **FALSE** otherwise.

## Error codes

Returns **S\_OK** if successful.

## Remarks

Use this method to query whether the [**IMsTscSecuredSettings**](imstscsecuredsettings-interface.md) interface is available before retrieving the [**SecuredSettings**](imstscax-securedsettings.md) property.

Refer to [Providing for RDP Client Security](providing-for-rdp-client-security.md) for a list of restricted URL security zones.

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

 

 





