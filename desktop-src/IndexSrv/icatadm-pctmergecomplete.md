---
title: ICatAdm PctMergeComplete property
description: Contains the percentage of the merge process completed.
ms.assetid: '7896ea22-06ec-4c52-ac02-6d401652ec6c'
keywords: ["PctMergeComplete property Indexing Service", "PctMergeComplete property Indexing Service , ICatAdm interface", "ICatAdm interface Indexing Service , PctMergeComplete property"]
topic_type:
- apiref
api_name:
- ICatAdm.PctMergeComplete
- ICatAdm.get_PctMergeComplete
api_location:
- Ciodm.dll
api_type:
- COM
---

# ICatAdm::PctMergeComplete property

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

Contains the percentage of the merge process completed.

This property is read-only.

## Syntax


```C++
HRESULT get_PctMergeComplete(
  [out, retval] LONG *pVal
);
```



## Property value

The percentage completed.

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

 

 





