---
title: Registering a COM Callback
description: Instead of polling for changes in the status of a job, you can register to receive notification when the job's status changes.
ms.assetid: '29350ea4-f7a9-4a42-a531-2cf623fe247b'
keywords: ["transfer job BITS , event notification", "registering for event notification BITS", "event notification BITS", "event notification BITS , callbacks", "notification events BITS"]
---

# Registering a COM Callback

Instead of [polling](polling-for-the-status-of-the-job.md) for changes in the status of a job, you can register to receive notification when the job's status changes. To receive notification, you must implement the [**IBackgroundCopyCallback2**](ibackgroundcopycallback2.md) interface. The interface contains the following methods that BITS calls, depending on your registration:

-   [**JobTransferred**](ibackgroundcopycallback-jobtransferred.md)
-   [**JobError**](ibackgroundcopycallback-joberror.md)
-   [**JobModification**](ibackgroundcopycallback-jobmodification.md)
-   [**FileTransferred**](ibackgroundcopycallback2-filetransferred.md)

For an example that implements the [**IBackgroundCopyCallback2**](ibackgroundcopycallback2.md) interface, see the example code in the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface topic.

The [**IBackgroundCopyCallback2**](ibackgroundcopycallback2.md) interface provides notification when a file is transferred. Typically, you use this method to validate the file, so that the file is available for peers to download; otherwise, the file is not available to peers until you call the [**IBackgroundCopyJob::Complete**](ibackgroundcopyjob-complete.md) method. To validate the file, call the [**IBackgroundCopyFile3::SetValidationState**](ibackgroundcopyfile3-setvalidationstate.md) method.

There are two methods for registering a COM callback: registering a callback object, or registering a callback class ID. Using a callback object is simpler and lower overhead; using a callback CLSID is more reliable, but more complicated. You can register either, both, or neither – BITS will use a callback object if one exists and can still be called, and will fall back to instantiating a new object based on a provided class ID if that fails.

### Registering a Callback Object

To register your implementation with BITS, call the [**IBackgroundCopyJob::SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md) method. To specify which methods BITS calls, call the [**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md)method.

The notification interface becomes invalid when your application terminates; BITS does not persist the notify interface. As a result, your application's initialization process should register existing jobs for which you want to receive notification. If you need to capture state and progress information that occurred since the last time your application was run, poll for state and progress information during application initialization.

Before exiting, your application should clear the callback interface pointer (**SetNotifyInterface(NULL)**). It is more efficient to clear the callback pointer than to let BITS discover that it is no longer valid.

Note that if more than one application calls the [**SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md) method to set the notification interface for the job, the last application to call the **SetNotifyInterface** method is the one that will receive notifications—the other applications will not receive notifications.

The following example shows how to register for notifications. The example assumes the [**IBackgroundCopyJob**](ibackgroundcopyjob.md) interface pointer is valid. For details on the CNotifyInterface example class used in the following example, see the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface.


```C++
HRESULT hr;
IBackgroundCopyJob* pJob;
CNotifyInterface *pNotify = new CNotifyInterface();

if (pNotify)
{
    hr = pJob->SetNotifyInterface(pNotify);
    if (SUCCEEDED(hr))
    {
        hr = pJob->SetNotifyFlags(BG_NOTIFY_JOB_TRANSFERRED | 
                                  BG_NOTIFY_JOB_ERROR );
    }
    pNotify->Release();
    pNotify = NULL;

    if (FAILED(hr))
    {
        //Handle error - unable to register callbacks.
    }
}
```



### Registering a Callback CLSID

To register a callback CLSID with BITS, call the [**IBackgroundCopyJob5::SetProperty**](ibackgroundcopyjob5-setproperty.md) method with the **BITS\_JOB\_PROPERTY\_NOTIFICATION\_CLSID** PropertyId. To specify which methods BITS calls, call the [**IBackgroundCopyJob::SetNotifyFlags**](ibackgroundcopyjob-setnotifyflags.md) method.

You must ensure that the notification CLSID is registered to an out-of-process COM server prior to registering the CLSID with a BITS job. Implementing a [COM server](https://msdn.microsoft.com/library/windows/desktop/ms690101.aspx ) is significantly more complicated than defining and passing a callback object, but offers several important advantages. A COM server allows BITS to maintain the association between a BITS job and your application’s code across system reboots, and for large or long-lived jobs. A COM server also allows your application to shut down completely while BITS continues executing transfers in the background, which can improve battery, CPU, and memory usage of the system.

To provide a notification you have registered to receive, BITS first attempts to call the corresponding method of any existing callback object you may have attached. If there is no existing object, or if that existing object has become disconnected (typically as a result of your application terminating), BITS will call CoCreateInstance using the notification CLSID to instantiate a new callback object, and will use that object for any further callbacks until it becomes disconnected or it is replaced by a new call to [**IBackgroundCopyJob::SetNotifyInterface**](ibackgroundcopyjob-setnotifyinterface.md).

Unlike callback objects, callback CLSID are persisted alongside their corresponding BITS job(s) if the BITS service or the system are shut down and restarted. Your application may clear any previously-set notification CLSID before exiting (or at any other time) by passing a new notification CLSID of GUID\_NULL, but your application may prefer to leave the notification CLSID registered if your application has registered to have COM start it in response to CoCreateInstance requests for your CLSID. Note that if more than one application sets the calls the **BITS\_JOB\_PROPERTY\_NOTIFICATION\_CLSID** property, the last CLSID to be set is the one that BITS will use to instantiate callback objects – the other CLSIDs will not be instantiated. Similarly, if one application registers a CLSID and another registers a callback object, the usual rules for the callback object taking precedence apply, and the CLSID will not be used unless the callback object is cleared or becomes disconnected.

The following example shows how to register for CLSID notifications. The example assumes the [**IBackgroundCopyJob5**](bits5-functions.md) interface pointer is valid, and that your application has already registered as an out-of-process COM Server which implements the CNotifyInterface class. For details on the CNotifyInterface example class used in the following example, see the [**IBackgroundCopyCallback**](ibackgroundcopycallback.md) interface.


```C++
HRESULT hr; 
IBackgroundCopyJob5* job; 
BITS_JOB_PROPERTY_VALUE propertyValue; 
propertyValue.ClsID = __uuidof(CNotifyInterface); 

hr = job->SetProperty(BITS_JOB_PROPERTY_NOTIFICATION_CLSID, propertyValue); 
if (SUCCEEDED(hr)) 
{ 
    hr = job->SetNotifyFlags(BG_NOTIFY_JOB_TRANSFERRED |  
                             BG_NOTIFY_JOB_ERROR); 
} 

if (FAILED(hr)) 
{ 
    // Handle error - unable to register callbacks. 
} 
```



 

 




