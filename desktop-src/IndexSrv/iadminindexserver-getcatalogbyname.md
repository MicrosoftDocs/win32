---
Description: Retrieves an existing catalog object from a catalog collection, given its name.
ms.assetid: 11a10912-3c17-4c61-ad55-7ce7597b4faf
title: IAdminIndexServer::GetCatalogByName method
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAdminIndexServer::GetCatalogByName method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves an existing catalog object from a catalog collection, given its name.

## Syntax


```C++
HRESULT GetCatalogByName(
  [in]          BSTR      bstrCatalogName,
  [out, retval] IDispatch **pDisp
);
```



## Parameters

<dl> <dt>

*bstrCatalogName* \[in\]
</dt> <dd>

The name of an existing catalog.

</dd> <dt>

*pDisp* \[out, retval\]
</dt> <dd>

The CatAdm object that represents the catalog. See [**ICatAdm**](icatadm.md).

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method expects an existing catalog name. When you attempt to retrieve a nonexistent catalog object, Indexing Service returns an error object with the **Number** property set to ERROR\_NOT\_FOUND.

## Examples


```VB
' Get a catalog object named "Sources"
Set objCatAdm = objAdminIS.GetCatalogByName("Sources")
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

 

 




