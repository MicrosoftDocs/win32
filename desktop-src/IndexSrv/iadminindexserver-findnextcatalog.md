---
Description: Enumerates the collection of catalogs for Indexing Service from the current location and checks whether another catalog exists. Before calling this method, call FindFirstCatalog to initialize catalog enumeration.
ms.assetid: 7c95f766-9388-46bb-8159-a13a7a891d33
title: IAdminIndexServer::FindNextCatalog method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAdminIndexServer::FindNextCatalog method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Enumerates the collection of catalogs for Indexing Service from the current location and checks whether another catalog exists. Before calling this method, call [**FindFirstCatalog**](iadminindexserver-findfirstcatalog.md) to initialize catalog enumeration.

## Syntax


```C++
HRESULT FindNextCatalog(
  [out, retval] VARIANT_BOOL *pfFound
);
```



## Parameters

<dl> <dt>

*pfFound* \[out, retval\]
</dt> <dd>

**VARIANT\_TRUE** if next catalog was found, **VARIANT\_FALSE** otherwise.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If this method finds another catalog, use [**GetCatalog**](iadminindexserver-getcatalog.md) to retrieve the catalog object.

## Examples


```VB
' Enumerate through the catalogs
Do While (objAdminIS.FindNextCatalog() ) 
   Set objCatAdm = objAdminIS.GetCatalog() 
   ' Use objCatAdm
   ' Free the catalog object
   Set objCatAdm = Nothing
Loop
```



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

 

 




