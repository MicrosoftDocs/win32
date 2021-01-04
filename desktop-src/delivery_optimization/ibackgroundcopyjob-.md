---
title: IBackgroundCopyJob interface (Deliveryoptimization.h)
description: Use the IBackgroundCopyJob interface to add files to the job, set the priority level of the job, determine the state of the job, and to start and stop the job.
ms.assetid: 0D1EAC8D-0013-4FBC-A07F-14CD5D709549
keywords:
- IBackgroundCopyJob interface
- IBackgroundCopyJob interface, described
topic_type:
- apiref
api_name:
- IBackgroundCopyJob
api_location:
- dosvc.dll
api_type:
- COM
ms.topic: reference
ms.date: 05/31/2018
ROBOTS: INDEX,FOLLOW
---

# IBackgroundCopyJob interface

Use the [**IBackgroundCopyJob**](https://www.bing.com/search?q=**IBackgroundCopyJob**) interface to add files to the job, set the priority level of the job, determine the state of the job, and to start and stop the job.

To create a job, call the [**IBackgroundCopyManager::CreateJob**](ibackgroundcopymanager-createjob.md) method. To get an [**IBackgroundCopyJob**](https://www.bing.com/search?q=**IBackgroundCopyJob**) interface pointer to an existing job, call the [**IBackgroundCopyManager::GetJob**](ibackgroundcopymanager-getjob.md) method.

## Members

The **IBackgroundCopyJob** interface inherits from the [**IUnknown**](/windows/desktop/api/unknwn/nn-unknwn-iunknown) interface. **IBackgroundCopyJob** also has these types of members:

-   [Methods](#methods)

### Methods

The **IBackgroundCopyJob** interface has these methods.



| Method                                                                  | Description                                                                                                                                                                                                                       |
|:------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Cancel**](ibackgroundcopyjob-cancel.md)                             | Cancels the job and removes temporary files from the client.<br/>                                                                                                                                                           |
| [**Complete**](ibackgroundcopyjob-complete.md)                         | Ends the job and saves the transferred files on the client.<br/>                                                                                                                                                            |
| [**EnumFiles**](ibackgroundcopyjob-enumfiles.md)                       | Returns an interface pointer to an enumerator object that you use to enumerate the files in the job.<br/>                                                                                                                   |
| [**GetDisplayName**](ibackgroundcopyjob-getdisplayname.md)             | Retrieves the display name that identifies the job.<br/>                                                                                                                                                                    |
| [**GetError**](ibackgroundcopyjob-geterror.md)                         | Retrieves an interface pointer to the error object after an error occurs.<br/>                                                                                                                                              |
| [**GetId**](ibackgroundcopyjob-getid.md)                               | Retrieves the identifier of the job in the queue.<br/>                                                                                                                                                                      |
| [**GetNoProgressTimeout**](ibackgroundcopyjob-getnoprogresstimeout.md) | Retrieves the length of time that DO continues to try to transfer the file after encountering a transient error condition.<br/>                                                                                             |
| [**GetNotifyFlags**](ibackgroundcopyjob-getnotifyflags.md)             | Retrieves the event notification (callback) flags you have set for your application.<br/>                                                                                                                                   |
| [**GetNotifyInterface**](ibackgroundcopyjob-getnotifyinterface.md)     | Retrieves a pointer to your implementation of the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface (callbacks).<br/>                                                                                    |
| [**GetPriority**](ibackgroundcopyjob-getpriority.md)                   | Retrieves the priority level you have set for the job.<br/>                                                                                                                                                                 |
| [**GetProgress**](ibackgroundcopyjob-getprogress.md)                   | Retrieves job-related progress information, such as the number of bytes and files transferred to the client.<br/>                                                                                                           |
| [**GetState**](ibackgroundcopyjob-getstate.md)                         | Retrieves the state of the job.<br/>                                                                                                                                                                                        |
| [**GetTimes**](ibackgroundcopyjob-gettimes.md)                         | Retrieves time stamps for activities related to the job, such as the time the job was created.<br/>                                                                                                                         |
| [**GetType**](ibackgroundcopyjob-gettype.md)                           | Retrieves the type of transfer being performed, such as a file download.<br/>                                                                                                                                               |
| [**Resume**](ibackgroundcopyjob-resume.md)                             | Starts a new job or restarts a suspended job.<br/>                                                                                                                                                                          |
| [**SetNoProgressTimeout**](ibackgroundcopyjob-setnoprogresstimeout.md) | Specifies the length of time that DO continues to try to transfer the file after encountering a transient error condition.<br/>                                                                                             |
| [**SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md)             | Specifies the type of event notification to receive.<br/>                                                                                                                                                                   |
| [**SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md)     | Specifies a pointer to your implementation of the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface (callbacks). The interface receives notification based on the event notification flags you set.<br/> |
| [**SetPriority**](ibackgroundcopyjob-setpriority.md)                   | Specifies the priority of the job relative to other jobs in the transfer queue.<br/>                                                                                                                                        |
| [**Suspend**](ibackgroundcopyjob-suspend.md)                           | Pauses the job.<br/>                                                                                                                                                                                                        |



 

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

[**IBackgroundCopyFile**](ibackgroundcopyfile.md)
</dt> <dt>

[**IBackgroundCopyManager**](ibackgroundcopymanager.md)
</dt> </dl>

 

