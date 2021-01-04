---
title: IMsRdpClientAdvancedSettings keepAliveInterval property
description: Specifies an interval, in milliseconds, at which the client sends keep-alive messages to the server.
ms.assetid: 0d1b7d8f-f81c-4591-bb08-adab307e87fe
ms.tgt_platform: multiple
keywords:
- keepAliveInterval property Remote Desktop Services
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , keepAliveInterval property
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , keepAliveInterval property
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , keepAliveInterval property
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , keepAliveInterval property
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , keepAliveInterval property
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , keepAliveInterval property
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , keepAliveInterval property
- keepAliveInterval property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , keepAliveInterval property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.keepAliveInterval
- IMsRdpClientAdvancedSettings.get_keepAliveInterval
- IMsRdpClientAdvancedSettings.put_keepAliveInterval
- IMsRdpClientAdvancedSettings2.keepAliveInterval
- IMsRdpClientAdvancedSettings2.get_keepAliveInterval
- IMsRdpClientAdvancedSettings2.put_keepAliveInterval
- IMsRdpClientAdvancedSettings3.keepAliveInterval
- IMsRdpClientAdvancedSettings3.get_keepAliveInterval
- IMsRdpClientAdvancedSettings3.put_keepAliveInterval
- IMsRdpClientAdvancedSettings4.keepAliveInterval
- IMsRdpClientAdvancedSettings4.get_keepAliveInterval
- IMsRdpClientAdvancedSettings4.put_keepAliveInterval
- IMsRdpClientAdvancedSettings5.keepAliveInterval
- IMsRdpClientAdvancedSettings5.get_keepAliveInterval
- IMsRdpClientAdvancedSettings5.put_keepAliveInterval
- IMsRdpClientAdvancedSettings6.keepAliveInterval
- IMsRdpClientAdvancedSettings6.get_keepAliveInterval
- IMsRdpClientAdvancedSettings6.put_keepAliveInterval
- IMsRdpClientAdvancedSettings7.keepAliveInterval
- IMsRdpClientAdvancedSettings7.get_keepAliveInterval
- IMsRdpClientAdvancedSettings7.put_keepAliveInterval
- IMsRdpClientAdvancedSettings8.keepAliveInterval
- IMsRdpClientAdvancedSettings8.get_keepAliveInterval
- IMsRdpClientAdvancedSettings8.put_keepAliveInterval
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::keepAliveInterval property

Specifies an interval, in milliseconds, at which the client sends keep-alive messages to the server.

A group policy setting that specifies whether persistent client connections to the server are allowed can override this property setting.

This property is read/write.

## Syntax


```C++
HRESULT put_keepAliveInterval(
  [in]  LONG keepAliveInterval
);

HRESULT get_keepAliveInterval(
  [out] LONG *pkeepAliveInterval
);
```



## Property value

The new interval, in milliseconds. The default value of the property is zero, which disables keep-alive messages. The minimum valid value of this property is 10,000, which represents 10 seconds.

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

 

 





