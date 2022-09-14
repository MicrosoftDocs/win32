---
title: IMsRdpClientNonScriptable5 RemoteMonitorLayoutMatchesLocal property
description: Specifies if the remote monitor layout is identical to the local monitor layout.
ms.assetid: 8F3C6650-870C-417C-82FC-E145FC360012
ms.tgt_platform: multiple
keywords:
- RemoteMonitorLayoutMatchesLocal property Remote Desktop Services
- RemoteMonitorLayoutMatchesLocal property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , RemoteMonitorLayoutMatchesLocal property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable5.RemoteMonitorLayoutMatchesLocal
- IMsRdpClientNonScriptable5.get_RemoteMonitorLayoutMatchesLocal
api_location:
- MsTscAx.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
---

# IMsRdpClientNonScriptable5::RemoteMonitorLayoutMatchesLocal property

Specifies if the remote monitor layout is identical to the local monitor layout. If this property contains **VARIANT\_TRUE**, the remote monitor layout is identical to the local monitor layout. If this property contains **VARIANT\_FALSE**, the remote and local monitors have different layouts.

This property is read-only.

## Syntax


```C++
HRESULT get_RemoteMonitorLayoutMatchesLocal(
  [out, retval] VARIANT_BOOL *pfRemoteMatchesLocal
);
```



## Property value

Receives the property value.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                             |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl>        |
| IID<br/>                      | IID\_IMsRdpClientNonScriptable5 is defined as 4f6996d5-d7b1-412c-b0ff-063718566907<br/> |



## See also

<dl> <dt>

[**IMsRdpClientNonScriptable5**](imsrdpclientnonscriptable5.md)
</dt> </dl>

 

 





