---
Description: Completes an asynchronous request to unregister a work queue with a Multimedia Class Scheduler Service (MMCSS) task.
ms.assetid: 0E8F9BF6-AC1E-4FC0-BFAE-F292C4859F1F
title: RtwqEndUnregisterWorkQueueWithMMCSS function
ms.topic: reference
ms.date: 05/31/2018
topic_type: 
- APIRef
- kbSyntax
api_name: 
- RtwqEndUnregisterWorkQueueWithMMCSS
api_type: 
- DllExport
api_location: 
- RTWorkQ.dll
---

# RtwqEndUnregisterWorkQueueWithMMCSS function

Completes an asynchronous request to unregister a work queue with a Multimedia Class Scheduler Service (MMCSS) task.

## Syntax


```C++
HRESULT WINAPI RtwqEndUnregisterWorkQueueWithMMCSS(
    IMFAsyncResult  *pResult 
);
```



## Parameters

<dl> <dt>

*pResult* 
</dt> <dd>

Pointer to the [**IMFAsyncResult**](https://msdn.microsoft.com/en-us/library/ms700196(v=VS.85).aspx) interface. Pass in the same pointer that your callback object received in the [**IRtwqAsyncCallback::Invoke**](https://msdn.microsoft.com/en-us/library/Dn448446(v=VS.85).aspx) method.

</dd> </dl>

## Return value

If this function succeeds, it returns **S\_OK**. Otherwise, it returns an **HRESULT** error code.

## Requirements



|                                     |                                                                                        |
|-------------------------------------|----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 8.1 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server 2012 R2 \[desktop apps only\]<br/>                                |
| Header<br/>                   | <dl> <dt>None</dt> </dl>        |
| Library<br/>                  | <dl> <dt>Rtworkq.lib</dt> </dl> |
| DLL<br/>                      | <dl> <dt>RTWorkQ.dll</dt> </dl> |



 

 




