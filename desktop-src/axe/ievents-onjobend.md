---
title: IJobEndEventHandler OnJobEnd method
description: The AXE Core raises this event when the job has ended.
ms.assetid: 366B5997-7D07-47A2-BBED-A8358E9A23FE
keywords:
- OnJobEnd method Access Execution Engine
- OnJobEnd method Access Execution Engine , IJobEndEventHandler interface
- IJobEndEventHandler interface Access Execution Engine , OnJobEnd method
topic_type:
- apiref
api_name:
- IJobEndEventHandler.OnJobEnd
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

# IJobEndEventHandler::OnJobEnd method

The AXE Core raises this event when the job has ended. This event is raised when all the assessments have finished, all results have been processed, and AXE has completed publishing the results. After this event has been received by a solution, another job can be started.

## Syntax


```C++
virtual void OnJobEnd(
         Engine          *sender,
   const JobEndEventArgs *e
) = 0;
```



## Parameters

<dl> <dt>

*sender* 
</dt> <dd>

The [**Engine**](engine-if.md) object that raised the event.

</dd> <dt>

*e* 
</dt> <dd>

The [**JobEndEventArgs**](jobendeventargs.md) structure that contains information about the job end event.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Managed code uses the [**JobEndEventHandler**](https://www.bing.com/search?q=**JobEndEventHandler**) delegate.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IJobEndEventHandler**](ijobendeventhandler.md)
</dt> <dt>

[**JobEndEventArgs**](jobendeventargs.md)
</dt> </dl>

 

 





