---
title: IAdminIndexServer GetSZProperty method
description: Retrieves a content index registry value of type REG\_SZ, as described in Registry Entries.
ms.assetid: f7124f32-dcfe-4af4-9ab8-d23e8cf59e73
keywords:
- GetSZProperty method Indexing Service
- GetSZProperty method Indexing Service , IAdminIndexServer interface
- IAdminIndexServer interface Indexing Service , GetSZProperty method
topic_type:
- apiref
api_name:
- IAdminIndexServer.GetSZProperty
api_location:
- Ciodm.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# IAdminIndexServer::GetSZProperty method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Retrieves a content index registry value of type **REG\_SZ**, as described in [Registry Entries](registry-entries.md).

## Syntax


```C++
HRESULT GetSZProperty(
  [in]          BSTR bstrPropName,
  [out, retval] BSTR *pbstrVal
);
```



## Parameters

<dl> <dt>

*bstrPropName* \[in\]
</dt> <dd>

The name of an existing registry value.

</dd> <dt>

*pbstrVal* \[out, retval\]
</dt> <dd>

The retrieved value.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

The registry value name must already exist for the Indexing Service entry. Attempting to retrieve the value of a nonexistent property results in the creation of an error object with the **Number** property set to E\_FAIL.

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

 

 





