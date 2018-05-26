---
title: IMsRdpClientNonScriptable5 RemoteMonitorCount property
description: Specifies the number of remote monitors.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: AFBF233D-44B2-4E6E-8C0C-A234F25B6111
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- RemoteMonitorCount property Remote Desktop Services
- RemoteMonitorCount property Remote Desktop Services , IMsRdpClientNonScriptable5 interface
- IMsRdpClientNonScriptable5 interface Remote Desktop Services , RemoteMonitorCount property
topic_type:
- apiref
api_name:
- IMsRdpClientNonScriptable5.RemoteMonitorCount
- IMsRdpClientNonScriptable5.get_RemoteMonitorCount
api_location:
- MsTscAx.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# IMsRdpClientNonScriptable5::RemoteMonitorCount property

Specifies the number of remote monitors.

This property is read-only.

## Syntax


```C++
HRESULT get_RemoteMonitorCount(
  [out, retval] ULONG *pcRemoteMonitors
);
```



## Property value

Receives the property value.

## Requirements



|                                     |                                                                                               |
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

 

 





