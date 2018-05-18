---
title: ICatAdm WordListCount property
description: Contains the number of word lists that currently exist in memory.
ms.assetid: 'a6b5e2cd-6709-4563-af6c-0e213e4af6fc'
keywords: ["WordListCount property Indexing Service", "WordListCount property Indexing Service , ICatAdm interface", "ICatAdm interface Indexing Service , WordListCount property"]
topic_type:
- apiref
api_name:
- ICatAdm.WordListCount
- ICatAdm.get_WordListCount
api_location:
- Ciodm.dll
api_type:
- COM
---

# ICatAdm::WordListCount property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the number of word lists that currently exist in memory.

This property is read-only.

## Syntax


```C++
HRESULT get_WordListCount(
  [out, retval] LONG *pVal
);
```



## Property value

The number of word lists.

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

 

 





