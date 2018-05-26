---
title: IAdminIndexServer Start method
description: Initiates Indexing Service on the computer named in the MachineName property (if Indexing Service is not already running).
ms.assetid: cbea617d-2462-4361-89ad-d4b975a04e9a
keywords:
- Start method Indexing Service
- Start method Indexing Service , IAdminIndexServer interface
- IAdminIndexServer interface Indexing Service , Start method
topic_type:
- apiref
api_name:
- IAdminIndexServer.Start
api_location:
- Ciodm.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IAdminIndexServer::Start method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Initiates Indexing Service on the computer named in the [**MachineName**](iadminindexserver-machinename.md) property (if Indexing Service is not already running).

## Syntax


```C++
HRESULT Start();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Any failure encountered when trying to start Indexing Service results in the creation of an error object. A call to this method does not return until the Indexing Service has finished starting.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ciodm.dll</dt> </dl> |



## See also

<dl> <dt>

[**IAdminIndexServer**](iadminindexserver.md)
</dt> </dl>

 

 





