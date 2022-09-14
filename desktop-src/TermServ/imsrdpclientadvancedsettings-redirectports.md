---
title: IMsRdpClientAdvancedSettings RedirectPorts property
description: Specifies if redirection of local ports (for example, COM and LPT) is allowed.
ms.assetid: 85e1e40d-8da7-4333-ae96-2bfa44479267
ms.tgt_platform: multiple
keywords:
- RedirectPorts property Remote Desktop Services
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , RedirectPorts property
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , RedirectPorts property
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , RedirectPorts property
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , RedirectPorts property
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , RedirectPorts property
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , RedirectPorts property
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , RedirectPorts property
- RedirectPorts property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , RedirectPorts property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.RedirectPorts
- IMsRdpClientAdvancedSettings.get_RedirectPorts
- IMsRdpClientAdvancedSettings.put_RedirectPorts
- IMsRdpClientAdvancedSettings2.RedirectPorts
- IMsRdpClientAdvancedSettings2.get_RedirectPorts
- IMsRdpClientAdvancedSettings2.put_RedirectPorts
- IMsRdpClientAdvancedSettings3.RedirectPorts
- IMsRdpClientAdvancedSettings3.get_RedirectPorts
- IMsRdpClientAdvancedSettings3.put_RedirectPorts
- IMsRdpClientAdvancedSettings4.RedirectPorts
- IMsRdpClientAdvancedSettings4.get_RedirectPorts
- IMsRdpClientAdvancedSettings4.put_RedirectPorts
- IMsRdpClientAdvancedSettings5.RedirectPorts
- IMsRdpClientAdvancedSettings5.get_RedirectPorts
- IMsRdpClientAdvancedSettings5.put_RedirectPorts
- IMsRdpClientAdvancedSettings6.RedirectPorts
- IMsRdpClientAdvancedSettings6.get_RedirectPorts
- IMsRdpClientAdvancedSettings6.put_RedirectPorts
- IMsRdpClientAdvancedSettings7.RedirectPorts
- IMsRdpClientAdvancedSettings7.get_RedirectPorts
- IMsRdpClientAdvancedSettings7.put_RedirectPorts
- IMsRdpClientAdvancedSettings8.RedirectPorts
- IMsRdpClientAdvancedSettings8.get_RedirectPorts
- IMsRdpClientAdvancedSettings8.put_RedirectPorts
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::RedirectPorts property

Specifies if redirection of local ports (for example, COM and LPT) is allowed.

This property is read/write.

## Syntax


```C++
HRESULT put_RedirectPorts(
  [in]  VARIANT_BOOL redirectPorts
);

HRESULT get_RedirectPorts(
  [out] VARIANT_BOOL *predirectPorts
);
```



## Property value

Set this parameter to **VARIANT\_TRUE** to allow redirection or **VARIANT\_FALSE** otherwise. **VARIANT\_TRUE** prompts the user to confirm allowing redirection at connection time, for security purposes.

## Error codes

Returns **S\_OK** if successful.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                        |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                  |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>          |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>          |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings is defined as 3c65b4ab-12b3-465b-acd4-b8dad3bff9e2<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings3**](imstscadvancedsettings-interface.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings4**](imsrdpclientadvancedsettings4.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings5**](imsrdpclientadvancedsettings5.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings6**](imsrdpclientadvancedsettings6.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings**](imsrdpclientadvancedsettings-interface.md)
</dt> </dl>

 

 





