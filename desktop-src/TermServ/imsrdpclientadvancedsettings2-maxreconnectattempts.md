---
title: IMsRdpClientAdvancedSettings2 MaxReconnectAttempts property
description: Specifies the number of times to try to reconnect during automatic reconnection.
ms.assetid: 24bfd3b6-d2de-4e46-8b5f-a4702c18a93c
ms.tgt_platform: multiple
keywords:
- MaxReconnectAttempts property Remote Desktop Services
- MaxReconnectAttempts property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , MaxReconnectAttempts property
- MaxReconnectAttempts property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , MaxReconnectAttempts property
- MaxReconnectAttempts property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , MaxReconnectAttempts property
- MaxReconnectAttempts property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , MaxReconnectAttempts property
- MaxReconnectAttempts property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , MaxReconnectAttempts property
- MaxReconnectAttempts property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , MaxReconnectAttempts property
- MaxReconnectAttempts property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , MaxReconnectAttempts property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings2.MaxReconnectAttempts
- IMsRdpClientAdvancedSettings2.get_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings2.put_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings3.MaxReconnectAttempts
- IMsRdpClientAdvancedSettings3.get_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings3.put_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings4.MaxReconnectAttempts
- IMsRdpClientAdvancedSettings4.get_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings4.put_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings5.MaxReconnectAttempts
- IMsRdpClientAdvancedSettings5.get_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings5.put_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings6.MaxReconnectAttempts
- IMsRdpClientAdvancedSettings6.get_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings6.put_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings7.MaxReconnectAttempts
- IMsRdpClientAdvancedSettings7.get_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings7.put_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings8.MaxReconnectAttempts
- IMsRdpClientAdvancedSettings8.get_MaxReconnectAttempts
- IMsRdpClientAdvancedSettings8.put_MaxReconnectAttempts
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings2::MaxReconnectAttempts property

Specifies the number of times to try to reconnect during automatic reconnection.

This property is read/write.

## Syntax


```C++
HRESULT put_MaxReconnectAttempts(
  [in]  LONG MaxReconnectAttempts
);

HRESULT get_MaxReconnectAttempts(
  [out] LONG *pMaxReconnectAttempts
);
```



## Property value

The new number of retries. The valid values are 0 to 200, inclusive.

## Error codes

Return **S\_OK** if successful.

## Remarks

This property cannot be set when the control is connected.

For more information about Remote Desktop Web Connection, see [Requirements for Remote Desktop Web Connection](requirements-for-remote-desktop-web-connection.md).

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                                         |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                                   |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings2 is defined as 9ac42117-2b76-4320-aa44-0e616ab8437b<br/> |



## See also

<dl> <dt>

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

[**IMsRdpClientAdvancedSettings2**](imsrdpclientadvancedsettings2.md)
</dt> </dl>

 

 





