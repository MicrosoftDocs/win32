---
title: IMsRdpClientAdvancedSettings shutdownTimeout property
description: Specifies the length of time, in seconds, to wait for the server to respond to a disconnection request.
ms.assetid: 3fa935dc-d4b0-433b-ab67-a644fcf09006
ms.tgt_platform: multiple
keywords:
- shutdownTimeout property Remote Desktop Services
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , shutdownTimeout property
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , shutdownTimeout property
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , shutdownTimeout property
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , shutdownTimeout property
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , shutdownTimeout property
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , shutdownTimeout property
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , shutdownTimeout property
- shutdownTimeout property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , shutdownTimeout property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.shutdownTimeout
- IMsRdpClientAdvancedSettings.get_shutdownTimeout
- IMsRdpClientAdvancedSettings.put_shutdownTimeout
- IMsRdpClientAdvancedSettings2.shutdownTimeout
- IMsRdpClientAdvancedSettings2.get_shutdownTimeout
- IMsRdpClientAdvancedSettings2.put_shutdownTimeout
- IMsRdpClientAdvancedSettings3.shutdownTimeout
- IMsRdpClientAdvancedSettings3.get_shutdownTimeout
- IMsRdpClientAdvancedSettings3.put_shutdownTimeout
- IMsRdpClientAdvancedSettings4.shutdownTimeout
- IMsRdpClientAdvancedSettings4.get_shutdownTimeout
- IMsRdpClientAdvancedSettings4.put_shutdownTimeout
- IMsRdpClientAdvancedSettings5.shutdownTimeout
- IMsRdpClientAdvancedSettings5.get_shutdownTimeout
- IMsRdpClientAdvancedSettings5.put_shutdownTimeout
- IMsRdpClientAdvancedSettings6.shutdownTimeout
- IMsRdpClientAdvancedSettings6.get_shutdownTimeout
- IMsRdpClientAdvancedSettings6.put_shutdownTimeout
- IMsRdpClientAdvancedSettings7.shutdownTimeout
- IMsRdpClientAdvancedSettings7.get_shutdownTimeout
- IMsRdpClientAdvancedSettings7.put_shutdownTimeout
- IMsRdpClientAdvancedSettings8.shutdownTimeout
- IMsRdpClientAdvancedSettings8.get_shutdownTimeout
- IMsRdpClientAdvancedSettings8.put_shutdownTimeout
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::shutdownTimeout property

Specifies the length of time, in seconds, to wait for the server to respond to a disconnection request.

If the server does not reply within the specified time, the client control disconnects.

This property is read/write.

## Syntax


```C++
HRESULT put_shutdownTimeout(
  [in]  LONG shutdownTimeout
);

HRESULT get_shutdownTimeout(
  [out] LONG *pshutdownTimeout
);
```



## Property value

The new time, in seconds. The default value of the property is 10. The maximum value is 600, which represents 10 minutes.

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

 

 





