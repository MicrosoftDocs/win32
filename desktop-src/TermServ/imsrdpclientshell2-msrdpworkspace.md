---
title: IMsRdpClientShell2 MsRdpWorkspace property
description: Retrieves a pointer to the IMsRdpWorkspace interface, which is used to manage RemoteApp and Desktop Connection credentials and connections.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 5d505ce0-18cf-4e38-b1b8-026303f7069b
ms.tgt_platform: multiple
keywords:
- MsRdpWorkspace property Remote Desktop Services
- MsRdpWorkspace property Remote Desktop Services , IMsRdpClientShell2 interface
- IMsRdpClientShell2 interface Remote Desktop Services , MsRdpWorkspace property
topic_type:
- apiref
api_name:
- IMsRdpClientShell2.MsRdpWorkspace
- IMsRdpClientShell2.get_MsRdpWorkspace
api_location:
- MsRdpWebAccess.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMsRdpClientShell2::MsRdpWorkspace property

Retrieves a pointer to the [**IMsRdpWorkspace**](imsrdpworkspace.md) interface, which is used to manage RemoteApp and Desktop Connection credentials and connections.

This property is read-only.

## Syntax


```C++
HRESULT get_MsRdpWorkspace(
  [out, retval] IMsRdpWorkspace **pVal
);
```



## Property value

The address of a pointer to the [**IMsRdpWorkspace**](imsrdpworkspace.md) interface.

## Remarks

The [**IMsRdpWorkspace**](imsrdpworkspace.md) interface is not exposed as a custom interface. It is accessible through [IDispatch](https://msdn.microsoft.com/library/windows/desktop/ms687285) methods only.

## Requirements



|                                     |                                                                                               |
|-------------------------------------|-----------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                          |
| Minimum supported server<br/> | Windows Server 2008 R2<br/>                                                             |
| DLL<br/>                      | <dl> <dt>MsRdpWebAccess.dll</dt> </dl> |



## See also

<dl> <dt>

[**IMsRdpClientShell2**](imsrdpclientshell2.md)
</dt> </dl>

 

 





