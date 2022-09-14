---
title: IMsRdpClientAdvancedSettings LoadBalanceInfo property
description: Specifies the load balancing cookie that will be placed in the X.224 Connection Request packet in the Remote Desktop Session Host (RD Session Host) server protocol connection sequence.
ms.assetid: 25f12a2e-00a2-42a8-afd3-81efcd94da94
ms.tgt_platform: multiple
keywords:
- LoadBalanceInfo property Remote Desktop Services
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings interface
- IMsRdpClientAdvancedSettings interface Remote Desktop Services , LoadBalanceInfo property
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings2 interface
- IMsRdpClientAdvancedSettings2 interface Remote Desktop Services , LoadBalanceInfo property
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings3 interface
- IMsRdpClientAdvancedSettings3 interface Remote Desktop Services , LoadBalanceInfo property
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings4 interface
- IMsRdpClientAdvancedSettings4 interface Remote Desktop Services , LoadBalanceInfo property
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings5 interface
- IMsRdpClientAdvancedSettings5 interface Remote Desktop Services , LoadBalanceInfo property
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings6 interface
- IMsRdpClientAdvancedSettings6 interface Remote Desktop Services , LoadBalanceInfo property
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , LoadBalanceInfo property
- LoadBalanceInfo property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , LoadBalanceInfo property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings.LoadBalanceInfo
- IMsRdpClientAdvancedSettings.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings.put_LoadBalanceInfo
- IMsRdpClientAdvancedSettings2.LoadBalanceInfo
- IMsRdpClientAdvancedSettings2.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings2.put_LoadBalanceInfo
- IMsRdpClientAdvancedSettings3.LoadBalanceInfo
- IMsRdpClientAdvancedSettings3.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings3.put_LoadBalanceInfo
- IMsRdpClientAdvancedSettings4.LoadBalanceInfo
- IMsRdpClientAdvancedSettings4.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings4.put_LoadBalanceInfo
- IMsRdpClientAdvancedSettings5.LoadBalanceInfo
- IMsRdpClientAdvancedSettings5.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings5.put_LoadBalanceInfo
- IMsRdpClientAdvancedSettings6.LoadBalanceInfo
- IMsRdpClientAdvancedSettings6.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings6.put_LoadBalanceInfo
- IMsRdpClientAdvancedSettings7.LoadBalanceInfo
- IMsRdpClientAdvancedSettings7.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings7.put_LoadBalanceInfo
- IMsRdpClientAdvancedSettings8.LoadBalanceInfo
- IMsRdpClientAdvancedSettings8.get_LoadBalanceInfo
- IMsRdpClientAdvancedSettings8.put_LoadBalanceInfo
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings::LoadBalanceInfo property

Specifies the load balancing cookie that will be placed in the X.224 Connection Request packet in the Remote Desktop Session Host (RD Session Host) server protocol connection sequence.

This property is read/write.

## Syntax


```C++
HRESULT put_LoadBalanceInfo(
  [in]  BSTR newLBInfo
);

HRESULT get_LoadBalanceInfo(
  [out] BSTR *pLBInfo
);
```



## Property value

Pointer to the new cookie. For more information, see the remarks section.

## Error codes

Returns **S\_OK** if successful.

## Remarks

The load balancing information is used by load balancing routers to choose the best server for the client when using farms of RD Session Host servers. The RD Session Host server itself does not use this information and will discard it.

The cookie uses the following, case-sensitive, syntax:

**Cookie: msts=***IpAddressAndPortNumber***\\r\\n**

Where *IpAddressAndPortNumber* is the IP address and port number, in network byte order.

For example, the cookie used to access the IP address of 172.31.249.216, port number 3389 is as follows:

**Cookie: msts=3640205228.15629.0000\\r\\n**

The final four zeros are optional and are reserved. The final decimal point is required, as are the trailing carriage return and linefeed. The length of the string, in characters, must be an even multiple of 2, so add a space if necessary.

If no cookie is supplied, the default is **Cookie: mstshash=***UserName***\\r\\n**.

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

 

 





