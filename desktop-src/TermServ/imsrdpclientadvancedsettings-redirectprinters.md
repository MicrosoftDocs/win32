---
title: IMsRdpClientAdvancedSettings RedirectPrinters property
description: Specifies if redirection of printers is allowed.
ms.assetid: 7d4f28a7-a99d-4d0b-ab51-832a78881900
ms.tgt_platform: multiple
keywords:
- RedirectPrinters property Remote Desktop Services
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , RedirectPrinters property
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , RedirectPrinters property
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , RedirectPrinters property
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , RedirectPrinters property
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , RedirectPrinters property
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , RedirectPrinters property
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , RedirectPrinters property
- RedirectPrinters property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , RedirectPrinters property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.RedirectPrinters
- IMsRdpClientAdvancedSettings.get_RedirectPrinters
- IMsRdpClientAdvancedSettings.put_RedirectPrinters
- IMsRdpClientAdvancedSettings2.RedirectPrinters
- IMsRdpClientAdvancedSettings2.get_RedirectPrinters
- IMsRdpClientAdvancedSettings2.put_RedirectPrinters
- IMsRdpClientAdvancedSettings3.RedirectPrinters
- IMsRdpClientAdvancedSettings3.get_RedirectPrinters
- IMsRdpClientAdvancedSettings3.put_RedirectPrinters
- IMsRdpClientAdvancedSettings4.RedirectPrinters
- IMsRdpClientAdvancedSettings4.get_RedirectPrinters
- IMsRdpClientAdvancedSettings4.put_RedirectPrinters
- IMsRdpClientAdvancedSettings5.RedirectPrinters
- IMsRdpClientAdvancedSettings5.get_RedirectPrinters
- IMsRdpClientAdvancedSettings5.put_RedirectPrinters
- IMsRdpClientAdvancedSettings6.RedirectPrinters
- IMsRdpClientAdvancedSettings6.get_RedirectPrinters
- IMsRdpClientAdvancedSettings6.put_RedirectPrinters
- IMsRdpClientAdvancedSettings7.RedirectPrinters
- IMsRdpClientAdvancedSettings7.get_RedirectPrinters
- IMsRdpClientAdvancedSettings7.put_RedirectPrinters
- IMsRdpClientAdvancedSettings8.RedirectPrinters
- IMsRdpClientAdvancedSettings8.get_RedirectPrinters
- IMsRdpClientAdvancedSettings8.put_RedirectPrinters
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::RedirectPrinters property

Specifies if redirection of printers is allowed.

This property is read/write.

## Syntax


```C++
HRESULT put_RedirectPrinters(
  [in]  VARIANT_BOOL redirectPrinters
);

HRESULT get_RedirectPrinters(
  [out] VARIANT_BOOL *predirectPrinters
);
```



## Property value

Set this parameter to **VARIANT\_TRUE** to allow redirection or **VARIANT\_FALSE** otherwise.

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

 

 





