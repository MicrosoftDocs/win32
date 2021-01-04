---
title: IMsRdpClientAdvancedSettings overallConnectionTimeout property
description: Specifies the total length of time, in seconds, that the client control waits for a connection to complete.
ms.assetid: 02fb24e1-b5e4-4d8e-a1c2-a9bd62a69bed
ms.tgt_platform: multiple
keywords:
- overallConnectionTimeout property Remote Desktop Services
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , overallConnectionTimeout property
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , overallConnectionTimeout property
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , overallConnectionTimeout property
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , overallConnectionTimeout property
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , overallConnectionTimeout property
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , overallConnectionTimeout property
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , overallConnectionTimeout property
- overallConnectionTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , overallConnectionTimeout property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.overallConnectionTimeout
- IMsRdpClientAdvancedSettings.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings.put_overallConnectionTimeout
- IMsRdpClientAdvancedSettings2.overallConnectionTimeout
- IMsRdpClientAdvancedSettings2.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings2.put_overallConnectionTimeout
- IMsRdpClientAdvancedSettings3.overallConnectionTimeout
- IMsRdpClientAdvancedSettings3.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings3.put_overallConnectionTimeout
- IMsRdpClientAdvancedSettings4.overallConnectionTimeout
- IMsRdpClientAdvancedSettings4.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings4.put_overallConnectionTimeout
- IMsRdpClientAdvancedSettings5.overallConnectionTimeout
- IMsRdpClientAdvancedSettings5.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings5.put_overallConnectionTimeout
- IMsRdpClientAdvancedSettings6.overallConnectionTimeout
- IMsRdpClientAdvancedSettings6.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings6.put_overallConnectionTimeout
- IMsRdpClientAdvancedSettings7.overallConnectionTimeout
- IMsRdpClientAdvancedSettings7.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings7.put_overallConnectionTimeout
- IMsRdpClientAdvancedSettings8.overallConnectionTimeout
- IMsRdpClientAdvancedSettings8.get_overallConnectionTimeout
- IMsRdpClientAdvancedSettings8.put_overallConnectionTimeout
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::overallConnectionTimeout property

Specifies the total length of time, in seconds, that the client control waits for a connection to complete.

If the specified time elapses before connection completes, the control disconnects and calls the [**IMsTscAxEvents::OnDisconnected**](imstscaxevents-ondisconnected.md) method.

This property is read/write.

## Syntax


```C++
HRESULT put_overallConnectionTimeout(
  [in]  LONG overallConnectionTimeout
);

HRESULT get_overallConnectionTimeout(
  [out] LONG *poverallConnectionTimeout
);
```



## Property value

The new time, in seconds. The maximum value is 600, which represents 10 minutes.

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

[**singleConnectionTimeout**](imsrdpclientadvancedsettings-singleconnectiontimeout.md)
</dt> </dl>

 

 





