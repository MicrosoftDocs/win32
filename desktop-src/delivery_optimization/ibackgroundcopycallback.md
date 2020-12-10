---
title: IBackgroundCopyCallback interface (Deliveryoptimization.h)
description: Implement the IBackgroundCopyCallback interface to receive notification that a job is complete, has been modified, or is in error. Clients use this interface instead of polling for the status of the job.
ms.assetid: CF85D852-1B4E-4BC2-B6A6-0035ED3C439C
keywords:
- IBackgroundCopyCallback interface
- IBackgroundCopyCallback interface, described
topic_type:
- apiref
api_name:
- IBackgroundCopyCallback
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyCallback interface

Implement the **IBackgroundCopyCallback** interface to receive notification that a job is complete, has been modified, or is in error. Clients use this interface instead of polling for the status of the job.

## Members

The **IBackgroundCopyCallback** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IBackgroundCopyCallback** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBackgroundCopyCallback** interface has these methods.



| Method                                                                    | Description                                                                       |
|:--------------------------------------------------------------------------|:----------------------------------------------------------------------------------|
| [**JobError**](ibackgroundcopycallback-joberror-method.md)               | Called when an error occurs.<br/>                                           |
| [**JobModification**](ibackgroundcopycallback-jobmodification-method.md) | Called when a job is modified.<br/>                                         |
| [**JobTransferred**](ibackgroundcopycallback-jobtransferred.md)          | Called when all of the files in the job have successfully transferred.<br/> |



 

## Remarks

To receive notifications, call the [**IBackgroundCopyJob::SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md) method to specify the interface pointer to your **IBackgroundCopyCallback** implementation. To specify which notifications you want to receive, call the [**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md) method.

DO will call your callbacks as long as the interface pointer is valid. The notification interface is no longer valid when your application terminates; DO does not persist the notify interface. As a result, your application's initialization process should call the [**SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md) method on those existing jobs for which you want to receive notification.

## Requirements



| Requirement | Value |
|-------------------------------------|-----------------------------------------------------------------------------------------------------|
| Minimum supported client<br/> | Windows 10, version 1709 \[desktop apps only\]<br/>                                           |
| Minimum supported server<br/> | Windows Server, version 1709 \[desktop apps only\]<br/>                                       |
| Header<br/>                   | <dl> <dt>Deliveryoptimization.h</dt> </dl>   |
| IDL<br/>                      | <dl> <dt>DeliveryOptimization.idl</dt> </dl> |
| Library<br/>                  | <dl> <dt>Dosvc.lib</dt> </dl>                |
| DLL<br/>                      | <dl> <dt>Dosvc.dll</dt> </dl>                |
| IID<br/>                      | IID_IBackgroundCopyCallback is defined as 97EA99C7-0186-4AD4-8DF9-C5B4E0ED6B22<br/>          |



## See also

<dl> <dt>

[**IBackgroundCopyJob**](ibackgroundcopyjob-.md)
</dt> <dt>

[**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md)
</dt> <dt>

[**IBackgroundCopyJob::SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md)
</dt> </dl>

 

