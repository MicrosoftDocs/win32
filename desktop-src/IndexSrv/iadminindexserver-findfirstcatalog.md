---
title: IAdminIndexServer FindFirstCatalog method
description: Determines whether a catalog exists. It also initializes the enumeration of catalogs, enabling you to find additional catalogs using the FindNextCatalog method.
ms.assetid: 8be963c4-7d33-4ec3-adaf-21b27c9ba54c
keywords:
- FindFirstCatalog method Indexing Service
- FindFirstCatalog method Indexing Service , IAdminIndexServer interface
- IAdminIndexServer interface Indexing Service , FindFirstCatalog method
topic_type:
- apiref
api_name:
- IAdminIndexServer.FindFirstCatalog
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

# IAdminIndexServer::FindFirstCatalog method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Determines whether a catalog exists. It also initializes the enumeration of catalogs, enabling you to find additional catalogs using the [**FindNextCatalog**](iadminindexserver-findnextcatalog.md) method.

## Syntax


```C++
HRESULT FindFirstCatalog(
  [out, retval] VARIANT_BOOL *pfFound
);
```



## Parameters

<dl> <dt>

*pfFound* \[out, retval\]
</dt> <dd>

**VARIANT\_TRUE** if catalog was found, otherwise **VARIANT\_FALSE**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

If this method finds a catalog, use [**GetCatalog**](iadminindexserver-getcatalog.md) to retrieve the catalog object. To find additional catalogs, if any, use the [**FindNextCatalog**](iadminindexserver-findnextcatalog.md) method after using **FindFirstCatalog**.

## Examples


```VB
Set objCatAdmin = CreateObject("Microsoft.ISAdm")
' Find the first catalog
bFound = objCatAdmin.FindFirstCatalog()
If (bFound) 
   Set objCatAdm = objAdminIS.GetCatalog()
'   Work with this catalog
'   Free this catalog object
   Set objCatAdm = Nothing
EndIf 
```



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

 

 





