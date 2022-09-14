---
title: IMsRdpClientAdvancedSettings minInputSendInterval property
description: Specifies the minimum interval, in milliseconds, between the sending of mouse events.
ms.assetid: d186c05f-0b45-47bd-8a8e-e1f9baf2bd75
ms.tgt_platform: multiple
keywords:
- minInputSendInterval property Remote Desktop Services
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , minInputSendInterval property
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , minInputSendInterval property
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , minInputSendInterval property
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , minInputSendInterval property
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , minInputSendInterval property
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , minInputSendInterval property
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , minInputSendInterval property
- minInputSendInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , minInputSendInterval property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.minInputSendInterval
- IMsRdpClientAdvancedSettings.get_minInputSendInterval
- IMsRdpClientAdvancedSettings.put_minInputSendInterval
- IMsRdpClientAdvancedSettings2.minInputSendInterval
- IMsRdpClientAdvancedSettings2.get_minInputSendInterval
- IMsRdpClientAdvancedSettings2.put_minInputSendInterval
- IMsRdpClientAdvancedSettings3.minInputSendInterval
- IMsRdpClientAdvancedSettings3.get_minInputSendInterval
- IMsRdpClientAdvancedSettings3.put_minInputSendInterval
- IMsRdpClientAdvancedSettings4.minInputSendInterval
- IMsRdpClientAdvancedSettings4.get_minInputSendInterval
- IMsRdpClientAdvancedSettings4.put_minInputSendInterval
- IMsRdpClientAdvancedSettings5.minInputSendInterval
- IMsRdpClientAdvancedSettings5.get_minInputSendInterval
- IMsRdpClientAdvancedSettings5.put_minInputSendInterval
- IMsRdpClientAdvancedSettings6.minInputSendInterval
- IMsRdpClientAdvancedSettings6.get_minInputSendInterval
- IMsRdpClientAdvancedSettings6.put_minInputSendInterval
- IMsRdpClientAdvancedSettings7.minInputSendInterval
- IMsRdpClientAdvancedSettings7.get_minInputSendInterval
- IMsRdpClientAdvancedSettings7.put_minInputSendInterval
- IMsRdpClientAdvancedSettings8.minInputSendInterval
- IMsRdpClientAdvancedSettings8.get_minInputSendInterval
- IMsRdpClientAdvancedSettings8.put_minInputSendInterval
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::minInputSendInterval property

Specifies the minimum interval, in milliseconds, between the sending of mouse events.

This property is read/write.

## Syntax


```C++
HRESULT put_minInputSendInterval(
  [in]  LONG minInputSendInterval
);

HRESULT get_minInputSendInterval(
  [out] LONG *pminInputSendInterval
);
```



## Property value

The new interval, in milliseconds. The default value is 100.

## Error codes

Returns **S\_OK** if successful.

## Remarks

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|-------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                            |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                               |
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

 

 





