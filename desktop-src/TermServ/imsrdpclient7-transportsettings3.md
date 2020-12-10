---
title: IMsRdpClient7 TransportSettings3 property
description: Retrieves an object that supports the IMsRdpClientTransportSettings3 interface.
ms.assetid: d11f0943-241e-44cd-a98c-595916ab0718
ms.tgt_platform: multiple
keywords:
- TransportSettings3 property Remote Desktop Services
- TransportSettings3 property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , TransportSettings3 property
- TransportSettings3 property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , TransportSettings3 property
- TransportSettings3 property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , TransportSettings3 property
- TransportSettings3 property Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , TransportSettings3 property
topic_type:
- apiref
api_name:
- IMsRdpClient7.TransportSettings3
- IMsRdpClient7.get_TransportSettings3
- IMsRdpClient8.TransportSettings3
- IMsRdpClient8.get_TransportSettings3
- IMsRdpClient9.TransportSettings3
- IMsRdpClient9.get_TransportSettings3
- IMsRdpClient10.TransportSettings3
- IMsRdpClient10.get_TransportSettings3
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient7::TransportSettings3 property

Retrieves an object that supports the [**IMsRdpClientTransportSettings3**](imsrdpclienttransportsettings3.md) interface.

This property is read-only.

## Syntax


```C++
HRESULT get_TransportSettings3(
  [out, retval] IMsRdpClientTransportSettings3 **ppXportSet3
);
```



## Property value

The address of an [**IMsRdpClientTransportSettings3**](imsrdpclienttransportsettings3.md) interface pointer that receives the object.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                      |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClient7 is defined as b2a5b5ce-3461-444a-91d4-add26d070638<br/>       |



## See also

<dl> <dt>

[**IMsRdpClient7**](imsrdpclient7.md)
</dt> <dt>

[**IMsRdpClient8**](imsrdpclient8.md)
</dt> <dt>

[**IMsRdpClient9**](imsrdpclient9.md)
</dt> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> </dl>

 

 





