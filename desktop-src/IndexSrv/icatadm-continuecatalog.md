---
title: ICatAdm ContinueCatalog method
description: Starts the catalog and retrieves its previous state.
ms.assetid: '5105755b-6dbc-494e-9b83-4330e9ec616c'
keywords: ["ContinueCatalog method Indexing Service", "ContinueCatalog method Indexing Service , ICatAdm interface", "ICatAdm interface Indexing Service , ContinueCatalog method"]
topic_type:
- apiref
api_name:
- ICatAdm.ContinueCatalog
api_location:
- Ciodm.dll
api_type:
- COM
---

# ICatAdm::ContinueCatalog method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Starts the catalog and retrieves its previous state.

## Syntax


```C++
HRESULT ContinueCatalog(
  [out, retval] CatalogStateType *pdwOldState
);
```



## Parameters

<dl> <dt>

*pdwOldState* \[out, retval\]
</dt> <dd>

The previous state of the catalog. Can be any of the [**CICAT\_\* Constants**](cicat-constants.md).

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

[**ICatAdm**](icatadm.md)
</dt> </dl>

 

 





