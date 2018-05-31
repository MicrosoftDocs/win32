---
title: ICatAdm RemoveScope method
description: Removes an existing scope from the collection of scope objects managed by a CatAdm object.
ms.assetid: f7f156f8-ef76-4f94-aa25-8d87d32a2848
keywords:
- RemoveScope method Indexing Service
- RemoveScope method Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , RemoveScope method
topic_type:
- apiref
api_name:
- ICatAdm.RemoveScope
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

# ICatAdm::RemoveScope method

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Removes an existing scope from the collection of scope objects managed by a CatAdm object.

## Syntax


```C++
HRESULT RemoveScope(
  [in] BSTR bstrScopePath
);
```



## Parameters

<dl> <dt>

*bstrScopePath* \[in\]
</dt> <dd>

The existing scope to be removed.

</dd> </dl>

## Return value

If this method succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Remarks

This method does not validate the path of the scope. Attempting to remove the path of a nonexistent scope results in the creation of an error object with the **Number** property set to ERROR\_NOT\_FOUND.

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

 

 





