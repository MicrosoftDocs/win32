---
title: IMsRdpClient10 RemoteProgram3 property
description: An object that supports the ITSRemoteProgram3 interface.
ms.assetid: afb26152-32eb-45de-a228-a6f7ca7eea2b
ms.tgt_platform: multiple
keywords:
- RemoteProgram3 property Remote Desktop Services
- RemoteProgram3 property Remote Desktop Services , IMsRdpClient10 interface
- IMsRdpClient10 interface Remote Desktop Services , RemoteProgram3 property
topic_type:
- apiref
api_name:
- IMsRdpClient10.RemoteProgram3
- IMsRdpClient10.get_RemoteProgram3
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClient10::RemoteProgram3 property

An object that supports the [**ITSRemoteProgram3**](itsremoteprogram3.md) interface.

This property is read-only.

## Syntax


```C++
HRESULT get_RemoteProgram3(
  [out, retval] ITSRemoteProgram3 **ppRemoteProgram
);
```



## Property value

Returns an [**ITSRemoteProgram3**](itsremoteprogram3.md) interface pointer.

## Requirements



| Requirement | Value |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10 \[desktop apps only\]<br/>                                            |
| Minimum supported server<br/> | Windows Server 2016<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClient10**](imsrdpclient10.md)
</dt> </dl>

 

 





