---
title: IMsRdpClientShell Launch method
description: Launches remote file content from Remote Desktop Web Access (RD Web Access) or from some other web portal.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: 'a0aa12e4-8b6f-4a3a-a6b8-f5def0b8bd90'
ms.prod: 'windows-server-dev'
ms.technology: 'remote-desktop-services'
ms.tgt_platform: multiple
keywords: ["Launch method Remote Desktop Services", "Launch method Remote Desktop Services , IMsRdpClientShell interface", "IMsRdpClientShell interface Remote Desktop Services , Launch method"]
topic_type:
- apiref
api_name:
- IMsRdpClientShell.Launch
api_location:
- MsTscAx.dll
api_type:
- COM
---

# IMsRdpClientShell::Launch method

Launches remote file content from Remote Desktop Web Access (RD Web Access) or from some other web portal.

## Syntax


```C++
HRESULT Launch();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows Vista<br/>                                                               |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |
| IID<br/>                      | IID\_IMsRdpClientShell is defined as d012ae6d-c19a-4bfe-b367-201f8911f134<br/>   |



## See also

<dl> <dt>

[**IMsRdpClientShell**](imsrdpclientshell.md)
</dt> </dl>

 

 





