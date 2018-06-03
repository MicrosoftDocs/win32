---
title: IMsRdpClientShell IsRemoteProgramClientInstalled property
description: Retrieves whether the Remote Desktop Connection (RDC) client supports Windows Server 2008 R2 RemoteApp functionality.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: ce2fec74-c567-48e1-91d6-655c539d1fb9
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- IsRemoteProgramClientInstalled property Remote Desktop Services
- IsRemoteProgramClientInstalled property Remote Desktop Services , IMsRdpClientShell interface
- IMsRdpClientShell interface Remote Desktop Services , IsRemoteProgramClientInstalled property
topic_type:
- apiref
api_name:
- IMsRdpClientShell.IsRemoteProgramClientInstalled
- IMsRdpClientShell.get_IsRemoteProgramClientInstalled
api_location:
- MsTscAx.dll
api_type:
- COM
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IMsRdpClientShell::IsRemoteProgramClientInstalled property

Retrieves whether the Remote Desktop Connection (RDC) client supports Windows Server 2008 R2 RemoteApp functionality.

This property is read-only.

## Syntax


```C++
HRESULT get_IsRemoteProgramClientInstalled(
  [out] VARIANT_BOOL *pbClientInstalled
);
```



## Property value

Retrieves whether the Remote Desktop Connection (RDC) client supports RemoteApp functionality.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClientShell is defined as d012ae6d-c19a-4bfe-b367-201f8911f134<br/>   |



## See also

<dl> <dt>

[**IMsRdpClientShell**](imsrdpclientshell.md)
</dt> </dl>

 

 





