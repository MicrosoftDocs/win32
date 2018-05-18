---
title: IAdminIndexServer Pause method
description: Pauses Indexing Service.
ms.assetid: '0c709ce8-1b60-4297-a786-018edbf184f4'
keywords: ["Pause method Indexing Service", "Pause method Indexing Service , IAdminIndexServer interface", "IAdminIndexServer interface Indexing Service , Pause method"]
topic_type:
- apiref
api_name:
- IAdminIndexServer.Pause
api_location:
- Ciodm.dll
api_type:
- COM
---

# IAdminIndexServer::Pause method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Pauses Indexing Service.

## Syntax


```C++
HRESULT Pause();
```



## Parameters

This method has no parameters.

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ciodm.dll</dt> </dl> |



## See also

<dl> <dt>

[**IAdminIndexServer**](iadminindexserver.md)
</dt> </dl>

 

 





