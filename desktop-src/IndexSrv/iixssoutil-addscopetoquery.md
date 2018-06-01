---
Description: Adds a search path to the Query property of the Query object.
ms.assetid: 8aa75451-81d4-4180-aff2-4f98d1f947da
title: IixssoUtil::AddScopeToQuery method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IixssoUtil::AddScopeToQuery method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Adds a search path to the Query property of the Query object.

Do not confuse this with [**IScopeAdm**](iscopeadm.md), which is the Indexing Service administration object that defines the paths to index.

## Syntax


```C++
HRESULT AddScopeToQuery(
  [in]           IDispatch *pDisp,
  [in]           BSTR      pwszScope,
  [in, optional] BSTR      pwszDepth
);
```



## Parameters

<dl> <dt>

*pDisp* \[in\]
</dt> <dd>

The Query object using this scope.

</dd> <dt>

*pwszScope* \[in\]
</dt> <dd>

The physical or virtual path of the scope to be added.

</dd> <dt>

*pwszDepth* \[in, optional\]
</dt> <dd>

Indicates whether the scope covers only the named directory ("shallow") or the named directory and all its subdirectories ("deep").

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

When you first create an instance of the Query object or when you reset it, Query defaults to the entire catalog. The first time you call **AddScopeToQuery**, the specified scope replaces the default value. Subsequent calls to **AddScopeToQuery** append the additional scopes to a collection of scopes.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoUtil**](iixssoutil.md)
</dt> </dl>

 

 




