---
title: IJobBeginEventHandler OnJobBegin method
description: The AXE Core raises this event when the job begins.
ms.assetid: 60606B5C-5DBC-43B5-8DDC-DDEE26B565BE
keywords:
- OnJobBegin method Access Execution Engine
- OnJobBegin method Access Execution Engine , IJobBeginEventHandler interface
- IJobBeginEventHandler interface Access Execution Engine , OnJobBegin method
topic_type:
- apiref
api_name:
- IJobBeginEventHandler.OnJobBegin
api_location:
- AxeCore.dll
api_type:
- COM
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# IJobBeginEventHandler::OnJobBegin method

The AXE Core raises this event when the job begins.

## Syntax


```C++
virtual void OnJobBegin(
         Engine            *sender,
   const JobBeginEventArgs *e
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

The [**JobBeginEventArgs**](jobbegineventargs.md) structure that contains information about the job begin event.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Managed code uses the [**JobBeginEventHandler**](axe-jobbegineventhandler_om) delegate.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IJobBeginEventHandler**](ijobbegineventhandler.md)
</dt> <dt>

[**JobBeginEventArgs**](jobbegineventargs.md)
</dt> <dt>

[**ExecuteJob**](engine-executejob.md)
</dt> </dl>

 

 





