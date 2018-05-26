---
title: ICatAdm GetScopeByAlias method
description: Retrieves an existing scope object by alias or alternative friendly name for the scope.
ms.assetid: 32bbeaaf-3f9f-49f6-89a1-40c1bc67e626
keywords:
- GetScopeByAlias method Indexing Service
- GetScopeByAlias method Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , GetScopeByAlias method
topic_type:
- apiref
api_name:
- ICatAdm.GetScopeByAlias
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

# ICatAdm::GetScopeByAlias method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves an existing scope object by alias or alternative friendly name for the scope.

## Syntax


```C++
HRESULT GetScopeByAlias(
  [in]          BSTR      bstrAlias,
  [out, retval] IDispatch **pIDisp
);
```



## Parameters

<dl> <dt>

*bstrAlias* \[in\]
</dt> <dd>

The alias of an existing scope.

</dd> <dt>

*pIDisp* \[out, retval\]
</dt> <dd>

The returned CatAdm scope object.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The scope name must refer to a valid scope. If the name is not valid, an error object is created with the **Number** property set to ERROR\_NOT\_FOUND. The alias of a scope is defined by the [**Alias**](iscopeadm-alias.md) property of the scope's ScopeAdm object.

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

 

 





