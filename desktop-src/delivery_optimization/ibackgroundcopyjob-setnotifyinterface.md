---
title: IBackgroundCopyJob SetNotifyInterface method (Deliveryoptimization.h)
description: Identifies your implementation of the IBackgroundCopyCallback interface to DO. Use the IBackgroundCopyCallback interface to receive notification of job-related events.
ms.assetid: 792211FC-440E-4D2C-A6C7-CE9EFB86571C
keywords:
- SetNotifyInterface method
- SetNotifyInterface method, IBackgroundCopyJob interface
- IBackgroundCopyJob interface, SetNotifyInterface method
topic_type:
- apiref
api_name:
- IBackgroundCopyJob.SetNotifyInterface
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob::SetNotifyInterface method

Identifies your implementation of the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface to DO. Use the **IBackgroundCopyCallback** interface to receive notification of job-related events.

## Syntax


```C++
HRESULT SetNotifyInterface(
   IUnknown *pNotifyInterface
);
```



## Parameters

<dl> <dt>

*pNotifyInterface* 
</dt> <dd>

An [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface pointer. To remove the current callback interface pointer, set this parameter to **NULL**.

</dd> </dl>

## Return value

This method returns the following **HRESULT** values, as well as others.



| Return code                                                                              | Description                                                     |
|------------------------------------------------------------------------------------------|-----------------------------------------------------------------|
| <dl> <dt>****S_OK****</dt> </dl> | Notification interface pointer was successfully set.<br/> |



 

## Remarks

Call this method only if you implement the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface. Use the **SetNotifyInterface** method in conjunction with the [**SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md) method to specify the type of notification that you want to receive.

The notification interface becomes invalid when your application terminates; DO does not persist the notify interface. As a result, your application's initialization process should call the **SetNotifyInterface** method on those existing jobs for which you want to receive notification. If you need to capture state and progress information that occurred since the last time your application was run, poll for state and progress information during application initialization.

Only the job owner/creator or an administrator can register for notifications.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyJob is defined as 37668D37-507E-4160-9316-26306D150B12<br/>               |



## See also

<dl> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IBackgroundCopyCallback**](ibackgroundcopycallback.md)
</dt> <dt>

[**IBackgroundCopyJob::GetNotifyInterface**](ibackgroundcopyjob-getnotifyinterface.md)
</dt> <dt>

[**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md)
</dt> </dl>

 

 





