---
title: ICatAdm FilteredDocumentCount property
description: Contains the number of documents indexed since the last time Indexing Service was started.
ms.assetid: 8f36fb52-4263-427c-85ef-59bb10198ef4
keywords:
- FilteredDocumentCount property Indexing Service
- FilteredDocumentCount property Indexing Service , ICatAdm interface
- ICatAdm interface Indexing Service , FilteredDocumentCount property
topic_type:
- apiref
api_name:
- ICatAdm.FilteredDocumentCount
- ICatAdm.get_FilteredDocumentCount
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

# ICatAdm::FilteredDocumentCount property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the number of documents indexed since the last time Indexing Service was started.

This property is read-only.

## Syntax


```C++
HRESULT get_FilteredDocumentCount(
  [out, retval] LONG *pVal
);
```



## Property value

The number of documents indexed.

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

 

 





