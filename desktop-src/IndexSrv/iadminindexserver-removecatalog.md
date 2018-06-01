---
Description: Removes an existing catalog from the collection of catalog objects managed by an AdminIndexServer object. It can also delete the catalog directory from the system.
ms.assetid: 869505f4-c389-4955-9907-5cc319184574
title: IAdminIndexServer::RemoveCatalog method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAdminIndexServer::RemoveCatalog method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Removes an existing catalog from the collection of catalog objects managed by an AdminIndexServer object. It can also delete the catalog directory from the system.

## Syntax


```C++
HRESULT RemoveCatalog(
  [in] BSTR         bstrCatName,
  [in] VARIANT_BOOL fDelDirectory
);
```



## Parameters

<dl> <dt>

*bstrCatName* \[in\]
</dt> <dd>

The name of an existing catalog to be removed.

</dd> <dt>

*fDelDirectory* \[in\]
</dt> <dd>

To delete the directory and remove the catalog from the collection, set this to **VARIANT\_TRUE**. To remove the catalog from the collection but leave the directory intact, set this to **VARIANT\_FALSE**. Defaults to **VARIANT\_FALSE**.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Indexing Service must be stopped before a catalog can be removed.

## Examples


```VB
' Remove the directory "src" from catalogs to be indexed, but don't delete it.
objAdminIS.Stop   'Stop the indexing service
objAdminIS.RemoveCatalog("src")
objAdminIS.Start  'Start the indexing service up again
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

 

 




