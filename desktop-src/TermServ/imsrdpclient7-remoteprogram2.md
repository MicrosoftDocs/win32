---
title: IMsRdpClient7 RemoteProgram2 property
description: Retrieves an object that supports the ITSRemoteProgram2 interface.
ms.assetid: fabdc933-c941-487f-9e49-c20a39e0c86e
ms.tgt_platform: multiple
keywords:
- RemoteProgram2 property Remote Desktop Services
- RemoteProgram2 property Remote Desktop Services , IMsRdpClient7 interface
- IMsRdpClient7 interface Remote Desktop Services , RemoteProgram2 property
- RemoteProgram2 property Remote Desktop Services , IMsRdpClient8 interface
- IMsRdpClient8 interface Remote Desktop Services , RemoteProgram2 property
- RemoteProgram2 property Remote Desktop Services , IMsRdpClient9 interface
- IMsRdpClient9 interface Remote Desktop Services , RemoteProgram2 property
- RemoteProgram2 property Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , RemoteProgram2 property
topic_type:
- apiref
api_name:
- IMsRdpClient7.RemoteProgram2
- IMsRdpClient7.get_RemoteProgram2
- IMsRdpClient8.RemoteProgram2
- IMsRdpClient8.get_RemoteProgram2
- IMsRdpClient9.RemoteProgram2
- IMsRdpClient9.get_RemoteProgram2
- IMsRdpClient10.RemoteProgram2
- IMsRdpClient10.get_RemoteProgram2
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient7::RemoteProgram2 property

Retrieves an object that supports the [**ITSRemoteProgram2**](itsremoteprogram2.md) interface.

This property is read-only.

## Syntax


```C++
HRESULT get_RemoteProgram2(
  [out, retval] ITSRemoteProgram2 **ppRemoteProgram
);
```



## Property value

The address of an [**ITSRemoteProgram2**](itsremoteprogram2.md) interface pointer that receives the object.

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

 

 





