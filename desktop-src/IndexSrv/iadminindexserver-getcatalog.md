---
title: IAdminIndexServer GetCatalog method
description: Retrieves the current catalog object.
ms.assetid: '25612439-6cb6-47e8-ad75-eede90cc32fb'
keywords: ["GetCatalog method Indexing Service", "GetCatalog method Indexing Service , IAdminIndexServer interface", "IAdminIndexServer interface Indexing Service , GetCatalog method"]
topic_type:
- apiref
api_name:
- IAdminIndexServer.GetCatalog
api_location:
- Ciodm.dll
api_type:
- COM
---

# IAdminIndexServer::GetCatalog method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves the current catalog object.

## Syntax


```C++
HRESULT GetCatalog(
  [out, retval] IDispatch **pIDisp
);
```



## Parameters

<dl> <dt>

*pIDisp* \[out, retval\]
</dt> <dd>

The CatAdm object that represents the current catalog. See [**ICatAdm**](icatadm.md).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method assumes that the catalog exists and has been found by enumerating an administration object's collection of catalogs using [**FindFirstCatalog**](iadminindexserver-findfirstcatalog.md) or [**FindNextCatalog**](iadminindexserver-findnextcatalog.md).

## Examples

For an example, see [**FindFirstCatalog**](iadminindexserver-findfirstcatalog.md) and [**FindNextCatalog**](iadminindexserver-findnextcatalog.md).

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

 

 





