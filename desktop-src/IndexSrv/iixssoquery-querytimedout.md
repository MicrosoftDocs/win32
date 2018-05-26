---
title: IixssoQuery QueryTimedOut property
description: Warns that Indexing Service exceeded the time limit for execution as specified by the MaxQueryExecutionTime set by administrators for Indexing Service.
ms.assetid: 094a3cc4-4bd8-4d78-bb4d-0827184f05de
keywords:
- QueryTimedOut property Indexing Service
- QueryTimedOut property Indexing Service , IixssoQuery interface
- IixssoQuery interface Indexing Service , QueryTimedOut property
topic_type:
- apiref
api_name:
- IixssoQuery.QueryTimedOut
- IixssoQuery.get_QueryTimedOut
api_location:
- Ixsso.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IixssoQuery::QueryTimedOut property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Warns that Indexing Service exceeded the time limit for execution as specified by the **[MaxQueryExecutionTime](maxqueryexecutiontime.md)** set by administrators for Indexing Service.

This property is read-only.

## Syntax


```C++
HRESULT get_QueryTimedOut(
  [out, retval] VARIANT_BOOL *val
);
```



## Property value

**VARIANT\_TRUE** if the query timed out before it finished processing, **VARIANT\_FALSE** otherwise.

## Remarks

You must call the [**CreateRecordset**](iixssoquery-createrecordset.md) method before using this property.

## Requirements



|                                     |                                                                                      |
|-------------------------------------|--------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 2000 Professional \[desktop apps only\]<br/>                           |
| Minimum supported server<br/> | Windows 2000 Server \[desktop apps only\]<br/>                                 |
| End of client support<br/>    | Windows 7<br/>                                                                 |
| End of server support<br/>    | Windows Server 2008 R2<br/>                                                    |
| DLL<br/>                      | <dl> <dt>Ixsso.dll</dt> </dl> |



## See also

<dl> <dt>

[**IixssoQuery**](iixssoquery.md)
</dt> </dl>

 

 





