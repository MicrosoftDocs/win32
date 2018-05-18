---
title: ICatAdm DelayedFilterCount property
description: Contains the current number of documents that were not indexed on the first try, for reasons such as sharing violations; for example, some other process locked the file when Indexing Service was trying to open it for indexing.
ms.assetid: '570ad1c2-c80e-4b27-a1ac-665366a3af3c'
keywords: ["DelayedFilterCount property Indexing Service", "DelayedFilterCount property Indexing Service , ICatAdm interface", "ICatAdm interface Indexing Service , DelayedFilterCount property"]
topic_type:
- apiref
api_name:
- ICatAdm.DelayedFilterCount
- ICatAdm.get_DelayedFilterCount
api_location:
- Ciodm.dll
api_type:
- COM
---

# ICatAdm::DelayedFilterCount property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the current number of documents that were not indexed on the first try, for reasons such as sharing violations; for example, some other process locked the file when Indexing Service was trying to open it for indexing.

This property is read-only.

## Syntax


```C++
HRESULT get_DelayedFilterCount(
  [out, retval] LONG *pVal
);
```



## Property value

The current number of documents that were not indexed.

## Remarks

Retrieving this property requires Indexing Service to be running. If it is not running, an error object is created with the **Number** property set to CI\_E\_NOT\_RUNNING.

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

[**ICatAdm**](icatadm.md)
</dt> </dl>

 

 





