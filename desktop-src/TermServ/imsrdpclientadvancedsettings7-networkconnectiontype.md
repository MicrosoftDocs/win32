---
title: IMsRdpClientAdvancedSettings7 NetworkConnectionType property
description: Gets or sets the type of network connection used between the client and server. The network connection type information passed on to the server helps the server tune several parameters based on the network connection type.
ms.assetid: 4dd4fa17-f121-412d-a30d-1c01f4c892b0
ms.tgt_platform: multiple
keywords:
- NetworkConnectionType property Remote Desktop Services
- NetworkConnectionType property Remote Desktop Services , IMsRdpClientAdvancedSettings7 interface
- IMsRdpClientAdvancedSettings7 interface Remote Desktop Services , NetworkConnectionType property
- NetworkConnectionType property Remote Desktop Services , IMsRdpClientAdvancedSettings8 interface
- IMsRdpClientAdvancedSettings8 interface Remote Desktop Services , NetworkConnectionType property
topic_type:
- apiref
api_name:
- IMsRdpClientAdvancedSettings7.NetworkConnectionType
- IMsRdpClientAdvancedSettings7.get_NetworkConnectionType
- IMsRdpClientAdvancedSettings7.put_NetworkConnectionType
- IMsRdpClientAdvancedSettings8.NetworkConnectionType
- IMsRdpClientAdvancedSettings8.get_NetworkConnectionType
- IMsRdpClientAdvancedSettings8.put_NetworkConnectionType
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientAdvancedSettings7::NetworkConnectionType property

Gets or sets the type of network connection used between the client and server. The network connection type information passed on to the server helps the server tune several parameters based on the network connection type.

This property is read/write.

## Syntax


```C++
HRESULT put_NetworkConnectionType(
  [in]          UINT connectionType
);

HRESULT get_NetworkConnectionType(
  [out, retval] UINT *pConnectionType
);
```



## Property value

The network connection type.

<dt>

<span id="CONNECTION_TYPE_MODEM"></span><span id="connection_type_modem"></span>

<span id="CONNECTION_TYPE_MODEM"></span><span id="connection_type_modem"></span>**CONNECTION\_TYPE\_MODEM** (1 (0x1))


</dt> <dd>

Modem (56 Kbps)

</dd> <dt>

<span id="CONNECTION_TYPE_BROADBAND_LOW"></span><span id="connection_type_broadband_low"></span>

<span id="CONNECTION_TYPE_BROADBAND_LOW"></span><span id="connection_type_broadband_low"></span>**CONNECTION\_TYPE\_BROADBAND\_LOW** (2 (0x2))


</dt> <dd>

Low-speed broadband (256 Kbps to 2 Mbps)

</dd> <dt>

<span id="CONNECTION_TYPE_SATELLITE"></span><span id="connection_type_satellite"></span>

<span id="CONNECTION_TYPE_SATELLITE"></span><span id="connection_type_satellite"></span>**CONNECTION\_TYPE\_SATELLITE** (3 (0x3))


</dt> <dd>

Satellite (2 Mbps to 16 Mbps, with high latency)

</dd> <dt>

<span id="CONNECTION_TYPE_BROADBAND_HIGH"></span><span id="connection_type_broadband_high"></span>

<span id="CONNECTION_TYPE_BROADBAND_HIGH"></span><span id="connection_type_broadband_high"></span>**CONNECTION\_TYPE\_BROADBAND\_HIGH** (4 (0x4))


</dt> <dd>

High-speed broadband (2 Mbps to 10 Mbps)

</dd> <dt>

<span id="CONNECTION_TYPE_WAN"></span><span id="connection_type_wan"></span>

<span id="CONNECTION_TYPE_WAN"></span><span id="connection_type_wan"></span>**CONNECTION\_TYPE\_WAN** (5 (0x5))


</dt> <dd>

Wide area network (WAN) (10 Mbps or higher, with high latency)

</dd> <dt>

<span id="CONNECTION_TYPE_LAN"></span><span id="connection_type_lan"></span>

<span id="CONNECTION_TYPE_LAN"></span><span id="connection_type_lan"></span>**CONNECTION\_TYPE\_LAN** (6 (0x6))


</dt> <dd>

Local area network (LAN) (10 Mbps or higher)

</dd> </dl>

## Requirements



| Requirement | Value |
|-------------------------------------|--------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                             |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                                |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>           |
| IID<br/>                      | IID\_IMsRdpClientAdvancedSettings7 is defined as 26036036-4010-4578-8091-0db9a1edf9c3<br/> |



## See also

<dl> <dt>

[**IMsRdpClientAdvancedSettings8**](imsrdpclientadvancedsettings8.md)
</dt> <dt>

[**IMsRdpClientAdvancedSettings7**](imsrdpclientadvancedsettings7.md)
</dt> </dl>

 

 





