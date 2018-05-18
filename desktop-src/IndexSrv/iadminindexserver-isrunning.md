---
title: IAdminIndexServer IsRunning method
description: Determines whether Indexing Service is currently running.
ms.assetid: '83974ab8-2424-4b66-a16d-fa10d29b1f0f'
keywords: ["IsRunning method Indexing Service", "IsRunning method Indexing Service , IAdminIndexServer interface", "IAdminIndexServer interface Indexing Service , IsRunning method"]
topic_type:
- apiref
api_name:
- IAdminIndexServer.IsRunning
api_location:
- Ciodm.dll
api_type:
- COM
---

# IAdminIndexServer::IsRunning method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Determines whether Indexing Service is currently running.

## Syntax


```C++
HRESULT IsRunning(
  [out, retval] VARIANT_BOOL *pfIsRunning
);
```



## Parameters

<dl> <dt>

*pfIsRunning* \[out, retval\]
</dt> <dd>

**VARIANT\_TRUE** if the indexing service is running, **VARIANT\_FALSE** otherwise.

</dd> </dl>

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

 

 





