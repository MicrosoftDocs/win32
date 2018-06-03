---
title: ThreadingModel enumeration
description: Specify the threading model the engine should use when invoking callbacks provided by the solution.
ms.assetid: 2B5A1D7E-0A1F-4D0F-8A2B-BB3B7ABD34FF
keywords:
- ThreadingModel enumeration Access Execution Engine
topic_type:
- apiref
api_name:
- ThreadingModel
api_location:
- AxeHosting.h
api_type:
- HeaderDef
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: enumeration
ms.date: 05/31/2018
---

# ThreadingModel enumeration

Specify the threading model the engine should use when invoking callbacks provided by the solution.

## Syntax


```C++
enum ThreadingModel {
  ThreadingModelNone  = 0, 
  ThreadingModelFree, 
  ThreadingModelAPC 

};
```



## Constants

<dl> <dt>

<span id="ThreadingModelNone"></span><span id="threadingmodelnone"></span><span id="THREADINGMODELNONE"></span>**ThreadingModelNone**
</dt> <dd>

No threading model was specified. This is an invalid value.

</dd> <dt>

<span id="ThreadingModelFree"></span><span id="threadingmodelfree"></span><span id="THREADINGMODELFREE"></span>**ThreadingModelFree**
</dt> <dd>

The AXE engine invokes each callback directly from the context of a thread created and managed by the engine. This may or may not be the same thread for each callback.

</dd> <dt>

<span id="ThreadingModelAPC"></span><span id="threadingmodelapc"></span><span id="THREADINGMODELAPC"></span>**ThreadingModelAPC**
</dt> <dd>

The AXE engine will use Asynchronous Procedure Calls to execute a callback. The thread that registered the callbacks will be the thread that is invoked when a callback is executed.

</dd> </dl>

## Remarks

Managed code uses the [**ThreadingModel**](https://www.bing.com/search?q=**ThreadingModel**) enum.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |



 

 





