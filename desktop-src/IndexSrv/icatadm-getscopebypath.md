---
title: ICatAdm GetScopeByPath method
description: Retrieves an existing scope object by path.
ms.assetid: d15f294a-2e0e-4cbc-9e3c-47e2bd504539
keywords:
- GetScopeByPath method Indexing Service
- GetScopeByPath method Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , GetScopeByPath method
topic_type:
- apiref
api_name:
- ICatAdm.GetScopeByPath
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
api_location:
- Ciodm.dll
api_type:
- COM
---

# ICatAdm::GetScopeByPath method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves an existing scope object by path.

## Syntax


```C++
HRESULT GetScopeByPath(
  [in]          BSTR      bstrPath,
  [out, retval] IDispatch **pIDisp
);
```



## Parameters

<dl> <dt>

*bstrPath* \[in\]
</dt> <dd>

The name of an existing scope. The scope path must be a valid local or universal naming convention (UNC) path.

</dd> <dt>

*pIDisp* \[out, retval\]
</dt> <dd>

The returned CatAdm scope object.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The scope name must refer to a valid scope. If the scope path is not valid, an error object is created with the **Number** property set to ERROR\_NOT\_FOUND.

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

[**ICatAdm**](icatadm.md)
</dt> </dl>

 

 





