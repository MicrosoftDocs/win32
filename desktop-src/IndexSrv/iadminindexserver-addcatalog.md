---
title: IAdminIndexServer AddCatalog method
description: Creates a new catalog to be used by Indexing Service that runs on the computer specified by the MachineName property.
ms.assetid: '5c70c48b-3dca-45ee-a11f-4554947ba96b'
keywords: ["AddCatalog method Indexing Service", "AddCatalog method Indexing Service , IAdminIndexServer interface", "IAdminIndexServer interface Indexing Service , AddCatalog method"]
topic_type:
- apiref
api_name:
- IAdminIndexServer.AddCatalog
api_location:
- Ciodm.dll
api_type:
- COM
---

# IAdminIndexServer::AddCatalog method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Creates a new catalog to be used by Indexing Service that runs on the computer specified by the [**MachineName**](iadminindexserver-machinename.md) property.

## Syntax


```C++
HRESULT AddCatalog(
  [in]          BSTR      bstrCatName,
  [in]          BSTR      bstrCatLocation,
  [out, retval] IDispatch **pIDsip
);
```



## Parameters

<dl> <dt>

*bstrCatName* \[in\]
</dt> <dd>

The name of the catalog. The catalog name cannot be reused on the same computer. Limited to 40 characters in length.

</dd> <dt>

*bstrCatLocation* \[in\]
</dt> <dd>

The full path name to a local nonremovable drive where the catalog is located.

</dd> <dt>

*pIDsip* \[out, retval\]
</dt> <dd>

The new catalog object if the create action is successful.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

Indexing Service must be stopped, using the [**Stop**](iadminindexserver-stop.md) method, before creating a new catalog. If the specified catalog location does not already exist, a catalog folder is created at the specified location.

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

 

 





