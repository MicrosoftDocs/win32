---
title: ICatAdm IsUpToDate property
description: Indicates whether the index is up to date.
ms.assetid: 9562c76b-3685-469f-b530-9a740e904e91
keywords:
- IsUpToDate property Indexing Service
- IsUpToDate property Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , IsUpToDate property
topic_type:
- apiref
api_name:
- ICatAdm.IsUpToDate
- ICatAdm.get_IsUpToDate
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

# ICatAdm::IsUpToDate property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Indicates whether the index is up to date.

This property is read-only.

## Syntax


```C++
HRESULT get_IsUpToDate(
  [out, retval] VARIANT_BOOL *pVal
);
```



## Property value

**VARIANT\_TRUE** if the catalog is up to date, otherwise **VARIANT\_FALSE**.

## Remarks

Retrieving this property requires Indexing Service to be running. If it is not running, an error object is created with the **Number** property set to CI\_E\_NOT\_RUNNING.

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

 

 





