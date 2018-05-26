---
title: IAdminIndexServer IsPaused method
description: Determines whether the Indexing Service is currently paused.
ms.assetid: 25b913a9-ecbf-452c-9dc6-03503e83dfe8
keywords:
- IsPaused method Indexing Service
- IsPaused method Indexing Service , IAdminIndexServer interface
- IAdminIndexServer interface Indexing Service , IsPaused method
topic_type:
- apiref
api_name:
- IAdminIndexServer.IsPaused
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

# IAdminIndexServer::IsPaused method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Determines whether the Indexing Service is currently paused.

## Syntax


```C++
HRESULT IsPaused(
  [out, retval] VARIANT_BOOL *pfIsPaused
);
```



## Parameters

<dl> <dt>

*pfIsPaused* \[out, retval\]
</dt> <dd>

**VARIANT\_TRUE** if Indexing Service is paused, otherwise **VARIANT\_FALSE**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

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

 

 





