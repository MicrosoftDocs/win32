---
title: IAdminIndexServer GetLongProperty method
description: Retrieves a content index registry value of type REG\_DWORD, as described in Registry Entries.
ms.assetid: '1bea8e7b-b30a-45e9-a148-6c2b52c93c03'
keywords: ["GetLongProperty method Indexing Service", "GetLongProperty method Indexing Service , IAdminIndexServer interface", "IAdminIndexServer interface Indexing Service , GetLongProperty method"]
topic_type:
- apiref
api_name:
- IAdminIndexServer.GetLongProperty
api_location:
- Ciodm.dll
api_type:
- COM
---

# IAdminIndexServer::GetLongProperty method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves a content index registry value of type **REG\_DWORD**, as described in [Registry Entries](registry-entries.md).

## Syntax


```C++
HRESULT GetLongProperty(
  [in]          BSTR bstrPropName,
  [out, retval] LONG *plVal
);
```



## Parameters

<dl> <dt>

*bstrPropName* \[in\]
</dt> <dd>

The name of an existing Indexing Service registry value.

</dd> <dt>

*plVal* \[out, retval\]
</dt> <dd>

The retrieved property value.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The registry value name must already exist for the Indexing Service entry. Attempting to retrieve the value of a nonexistent property results in the creation of an error object with the **Number** property set to E\_FAIL.

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

 

 





