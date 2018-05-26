---
title: ITSRemoteProgram2 RemoteApplicationArgs property
description: The command-line arguments for the RemoteApp.
audience: developer
author: REDMOND\\markl
manager: REDMOND\\markl
ms.assetid: c1c36876-df3d-4ef9-a5ac-f623bc51fe7b
ms.prod: windows-server-dev
ms.technology: remote-desktop-services
ms.tgt_platform: multiple
keywords:
- RemoteApplicationArgs property Remote Desktop Services
- RemoteApplicationArgs property Remote Desktop Services , ITSRemoteProgram2 interface
- ITSRemoteProgram2 interface Remote Desktop Services , RemoteApplicationArgs property
- RemoteApplicationArgs property Remote Desktop Services , ITSRemoteProgram3 interface
- ITSRemoteProgram3 interface Remote Desktop Services , RemoteApplicationArgs property
topic_type:
- apiref
api_name:
- ITSRemoteProgram2.RemoteApplicationArgs
- ITSRemoteProgram2.put_RemoteApplicationArgs
- ITSRemoteProgram3.RemoteApplicationArgs
- ITSRemoteProgram3.put_RemoteApplicationArgs
api_location:
- MsTscAx.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
---

# ITSRemoteProgram2::RemoteApplicationArgs property

The command-line arguments for the RemoteApp.

This property is write-only.

## Syntax


```C++
HRESULT put_RemoteApplicationArgs(
  [in] BSTR bstrRemoteApplicationArgs
);
```



## Property value

The RemoteApp command-line arguments.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7<br/>                                                                   |
| Minimum supported server<br/> | Windows Server 2008<br/>                                                         |
| Type library<br/>             | <dl> <dt>MsTscAx.dll</dt> </dl> |
| DLL<br/>                      | <dl> <dt>MsTscAx.dll</dt> </dl> |



## See also

<dl> <dt>

[**ITSRemoteProgram3**](itsremoteprogram3.md)
</dt> <dt>

[**ITSRemoteProgram2**](itsremoteprogram2.md)
</dt> </dl>

 

 





