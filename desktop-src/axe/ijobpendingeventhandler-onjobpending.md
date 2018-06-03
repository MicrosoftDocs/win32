---
title: IJobPendingEventHandler OnJobPending method
description: The AXE Core raises this event when the job is blocked because another job is currently running.
ms.assetid: 2942FB92-00E3-4CF8-B307-2E6B1EB51606
keywords:
- OnJobPending method Access Execution Engine
- OnJobPending method Access Execution Engine , IJobPendingEventHandler interface
- IJobPendingEventHandler interface Access Execution Engine , OnJobPending method
topic_type:
- apiref
api_name:
- IJobPendingEventHandler.OnJobPending
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

# IJobPendingEventHandler::OnJobPending method

The AXE Core raises this event when the job is blocked because another job is currently running.

## Syntax


```C++
virtual void OnJobPending(
         Engine              *sender,
   const JobPendingEventArgs *e
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

The [**JobPendingEventArgs**](jobpendingeventargs.md) structure that contains information about the job pending event.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Managed code uses the [**JobPendingEventHandler**](https://www.bing.com/search?q=**JobPendingEventHandler**) delegate.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IJobPendingEventHandler**](ijobpendingeventhandler.md)
</dt> <dt>

[**JobPendingEventArgs**](jobpendingeventargs.md)
</dt> <dt>

[**ExecuteJob**](engine-executejob.md)
</dt> </dl>

 

 





