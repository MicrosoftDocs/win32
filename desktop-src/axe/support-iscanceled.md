---
title: Support IsCanceled method
description: Determines if there has been a request for the assessment to cancel its operation.
ms.assetid: 472A845B-46A6-45C6-A52F-AB6D739B5E5E
keywords:
- IsCanceled method Access Execution Engine
- IsCanceled method Access Execution Engine , Support interface
- Support interface Access Execution Engine , IsCanceled method
topic_type:
- apiref
api_name:
- Support.IsCanceled
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

# Support::IsCanceled method

Determines if there has been a request for the assessment to cancel its operation.

## Syntax


```C++
virtual HRESULT IsCanceled(
  [out] BOOL *cancelAssessment
) const = 0;
```



## Parameters

<dl> <dt>

*cancelAssessment* \[out\]
</dt> <dd>

A Boolean value that indicates whether the solution has requested that the assessment stop its operation.

</dd> </dl>

## Return value

If the function succeeds, it returns **S\_OK**. If it fails, it returns an error value.

## Remarks

This method enables an assessment to poll for cancellation requests. Polling is not the preferred method for detecting a cancellation request. An assessment will perform better if it waits on a cancel event created by the Axe engine that is signaled by the engine when the request is received from the solution application.

Managed code uses the [**Support.Canceled**](https://www.bing.com/search?q=**Support.Canceled**) property.

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

[**GetCancelEvent**](support-getcancelevent.md)
</dt> </dl>

 

 





