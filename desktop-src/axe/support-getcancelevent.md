---
title: Support GetCancelEvent method
description: Retrieves the handle to an event that Axe signals when a solution requests the assessment should stop running.
ms.assetid: 0107982B-4BD4-448A-A558-C879778D2DE4
keywords:
- GetCancelEvent method Access Execution Engine
- GetCancelEvent method Access Execution Engine , Support interface
- Support interface Access Execution Engine , GetCancelEvent method
topic_type:
- apiref
api_name:
- Support.GetCancelEvent
api_location:
- AxeCore.dll
api_type:
- COM
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Support::GetCancelEvent method

Retrieves the handle to an event that Axe signals when a solution requests the assessment should stop running.

## Syntax


```C++
virtual HRESULT GetCancelEvent(
  [out] HANDLE *cancelEventHandle
) const = 0;
```



## Parameters

<dl> <dt>

*cancelEventHandle* \[out\]
</dt> <dd>

A pointer to the handle for the cancel event object.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method enables an assessment to get access to the event object when a solution requests the assessment stop running. The assessment should immediately respond by calling [**ReportProgress**](support-reportprogress-overl.md) with a *ProgressType* value of **ProgressTypeCancelling** to acknowledge receipt of the cancellation request. Otherwise, the engine will inform the solution application that the assessment was not cancelled. After acknowledging that the assessment has received the notification to cancel, the assessment should immediately begin cleaning up and ending its operation.

Using the wait handle to be notified asynchronously when the assessment is being aborted is the preferred method for detecting a cancellation request.

Managed code uses [**Support.CancelEvent**](https://www.bing.com/search?q=**Support.CancelEvent**) property.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeRuntime.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**Support**](support.md)
</dt> <dt>

[**ReportProgress**](support-reportprogress-overl.md)
</dt> <dt>

[**ProgressType**](progresstype.md)
</dt> <dt>

[**IsCanceled**](support-iscanceled.md)
</dt> </dl>

 

 





