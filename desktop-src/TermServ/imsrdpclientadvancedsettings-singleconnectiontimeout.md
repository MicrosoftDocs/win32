---
title: IMsRdpClientAdvancedSettings singleConnectionTimeout property
description: Specifies the maximum length of time, in seconds, that the client control waits for a connection to an IP address.
ms.assetid: 57fb2397-8229-4446-88fd-e75cb96c7ac5
ms.tgt_platform: multiple
keywords:
- singleConnectionTimeout property Remote Desktop Services
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , singleConnectionTimeout property
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , singleConnectionTimeout property
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , singleConnectionTimeout property
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , singleConnectionTimeout property
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , singleConnectionTimeout property
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , singleConnectionTimeout property
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , singleConnectionTimeout property
- singleConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , singleConnectionTimeout property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.singleConnectionTimeout
- IMsRdpClientAdvancedSettings.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings.put_singleConnectionTimeout
- IMsRdpClientAdvancedSettings2.singleConnectionTimeout
- IMsRdpClientAdvancedSettings2.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings2.put_singleConnectionTimeout
- IMsRdpClientAdvancedSettings3.singleConnectionTimeout
- IMsRdpClientAdvancedSettings3.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings3.put_singleConnectionTimeout
- IMsRdpClientAdvancedSettings4.singleConnectionTimeout
- IMsRdpClientAdvancedSettings4.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings4.put_singleConnectionTimeout
- IMsRdpClientAdvancedSettings5.singleConnectionTimeout
- IMsRdpClientAdvancedSettings5.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings5.put_singleConnectionTimeout
- IMsRdpClientAdvancedSettings6.singleConnectionTimeout
- IMsRdpClientAdvancedSettings6.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings6.put_singleConnectionTimeout
- IMsRdpClientAdvancedSettings7.singleConnectionTimeout
- IMsRdpClientAdvancedSettings7.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings7.put_singleConnectionTimeout
- IMsRdpClientAdvancedSettings8.singleConnectionTimeout
- IMsRdpClientAdvancedSettings8.get_singleConnectionTimeout
- IMsRdpClientAdvancedSettings8.put_singleConnectionTimeout
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::singleConnectionTimeout property

Specifies the maximum length of time, in seconds, that the client control waits for a connection to an IP address.

During connection, the control may attempt to connect to multiple IP addresses.

This property is read/write.

## Syntax


```C++
HRESULT put_singleConnectionTimeout(
  [in]  LONG singleConnectionTimeout
);

HRESULT get_singleConnectionTimeout(
  [out] LONG *psingleConnectionTimeout
);
```



## Property value

The new time, in seconds. The maximum value is 600.

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
</dt> <dt>

[**overallConnectionTimeout**](imsrdpclientadvancedsettings-overallconnectiontimeout.md)
</dt> </dl>

 

 





