---
title: IJobRestartEventHandler OnJobRestart method
description: The AXE Core raises this event when a job is ending because the system is being restarted.
ms.assetid: '2290FC67-E1CB-4682-9A3B-9747A018538D'
keywords: ["OnJobRestart method Access Execution Engine", "OnJobRestart method Access Execution Engine , IJobRestartEventHandler interface", "IJobRestartEventHandler interface Access Execution Engine , OnJobRestart method"]
topic_type:
- apiref
api_name:
- IJobRestartEventHandler.OnJobRestart
api_location:
- AxeCore.dll
api_type:
- COM
---

# IJobRestartEventHandler::OnJobRestart method

The AXE Core raises this event when a job is ending because the system is being restarted.

## Syntax


```C++
virtual void OnJobRestart(
         Engine              *sender,
   const JobRestartEventArgs *e
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

The [**JobRestartEventArgs**](jobrestarteventargs.md) structure that contains information about the job restart event.

</dd> </dl>

## Return value

This method does not return a value.

## Remarks

Managed code uses the [**JobRestartEventHandler**](https://msdn.microsoft.com/library/windows/desktop/hh769329) delegate.

## Requirements



|                                     |                                                                                         |
|-------------------------------------|-----------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 7 \[desktop apps only\]<br/>                                              |
| Minimum supported server<br/> | Windows Server 2008 R2 \[desktop apps only\]<br/>                                 |
| Header<br/>                   | <dl> <dt>AxeHosting.h</dt> </dl> |
| DLL<br/>                      | <dl> <dt>AxeCore.dll</dt> </dl>  |



## See also

<dl> <dt>

[**IJobRestartEventHandler**](ijobrestarteventhandler.md)
</dt> <dt>

[**JobRestartEventArgs**](jobrestarteventargs.md)
</dt> <dt>

[**ExecuteJob**](engine-executejob.md)
</dt> </dl>

 

 





