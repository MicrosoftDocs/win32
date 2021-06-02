---
description: Asynchronous event notification is a technique that allows an application to constantly monitor events without monopolizing system resources.
ms.assetid: 69ec8ead-9073-4689-bc66-5134728ab147
ms.tgt_platform: multiple
title: Receiving Asynchronous Event Notifications
ms.topic: article
ms.date: 05/31/2018
---

# Receiving Asynchronous Event Notifications

Asynchronous event notification is a technique that allows an application to constantly monitor events without monopolizing system resources. Asynchronous event notifications have the same security limitations that other asynchronous calls have. You can make semisynchronous calls instead. For more information, see [Calling a Method](calling-a-method.md).

The queue of asynchronous events routed to a client has the potential to grow exceptionally large. Therefore, WMI implements a system-wide policy to avoid running out of memory. WMI either slows down events, or starts dropping events from the queue when the queue grows past a certain size.

WMI uses the [**LowThresholdOnEvents**](/windows/desktop/CIMWin32Prov/win32-wmisetting) and [**HighThresholdOnEvents**](/windows/desktop/CIMWin32Prov/win32-wmisetting) properties of the [**Win32\_WMISetting**](/windows/desktop/CIMWin32Prov/win32-wmisetting) class to set limits on out-of-memory avoidance. The minimum value indicates when WMI should start slowing event notification, and the maximum value indicates when to start dropping events. The default values for the low and high thresholds are 1000000 (10 MB) and 2000000 (20 MB). In addition, you can set the [**MaxWaitOnEvents**](/windows/desktop/CIMWin32Prov/win32-wmisetting) property to describe the amount of time WMI should wait before dropping events. The default value for **MaxWaitOnEvents** is 2000, or 2 seconds.

## Receiving Asynchronous Event Notifications in VBScript

The scripting calls to receive event notifications are essentially the same as all asynchronous calls with the same security issues. For more information, see [Making an Asynchronous Call with VBScript](making-an-asynchronous-call-with-vbscript.md).

**To receive asynchronous event notifications in VBScript**

1.  Create a sink object by calling [WScript.CreateObject](/previous-versions//xzysf6hc(v=vs.85)) and specifying the progid of "WbemScripting" and the object type of [**SWbemSink**](swbemsink.md). The sink object receives the notifications.
2.  Write a subroutine for each event you want to handle. The following table lists the [**SWbemSink**](swbemsink.md) events.

    

    | Event                                            | Meaning                                                                                                                         |
    |--------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------|
    | [**OnObjectReady**](swbemsink-onobjectready.md) | Reports the returns of an object to the sink. Using this call returns one object each time until the operation is complete.     |
    | [**OnCompleted**](swbemsink-oncompleted.md)     | Reports when an asynchronous call is complete. This event never occurs if the operation is indefinite.                          |
    | [**OnObjectPut**](swbemsink-onobjectput.md)     | Reports the completion of an asynchronous put operation. This event returns the object path of the instance or the saved class. |
    | [**OnProgress**](swbemsink-onprogress.md)       | Reports the status of an asynchronous call that is in progress. Not all providers support interim progress reports.             |
    | [**Cancel**](swbemsink-cancel.md)               | Cancels all of the outstanding asynchronous operations associated with this object sink.                                        |

    

     

The following VBScript code example notifies the deletion of processes with a 10 second polling interval. In this script, the subroutine SINK\_OnObjectReady handles the event occurrence. In the example, the sink object is named "Sink", however you can name this object as you choose.


```VB
strComputer = "." 
Set objWMIService = GetObject("winmgmts:\\" & strComputer & "\root\CIMV2") 
Set MySink = WScript.CreateObject( _
    "WbemScripting.SWbemSink","SINK_")

objWMIservice.ExecNotificationQueryAsync MySink, _
    "SELECT * FROM __InstanceDeletionEvent" _
    & " WITHIN 10 WHERE TargetInstance ISA 'Win32_Process'"


WScript.Echo "Waiting for events..."

While (True)
    Wscript.Sleep(1000)
Wend

Sub SINK_OnObjectReady(objObject, objAsyncContext)
    Wscript.Echo "__InstanceDeletionEvent event has occurred."
End Sub

Sub SINK_OnCompleted(objObject, objAsyncContext)
    WScript.Echo "Event call complete."
End Sub
```



## Receiving Asynchronous Event Notifications in C++

To perform asynchronous notification, you create a separate thread solely to monitor and receive events from Windows Management Instrumentation (WMI). When that thread receives a message, the thread notifies your main application.

By dedicating a separate thread, you permit your main process to perform other activities while waiting for an event to arrive. Asynchronous delivery of notifications improves performance but may provide less security than you want. In C++, you have the option of using the [**IWbemUnsecuredApartment**](/windows/desktop/api/Wbemcli/nn-wbemcli-iwbemunsecuredapartment) interface or performing access checks on security descriptors. For more information, see [Setting Security on an Asynchronous Call](setting-security-on-an-asynchronous-call.md).

**To set up asynchronous event notifications**

1.  Before initializing any asynchronous notifications, ensure your out-of-memory avoidance parameters are set correctly in [**Win32\_WMISetting**](/windows/desktop/CIMWin32Prov/win32-wmisetting).

2.  Determine what kind of events you want to receive.

    WMI supports intrinsic and extrinsic events. An intrinsic event is an event predefined by WMI, whereas an extrinsic event is an event defined by a third party provider. For more information, see [Determining the Type of Event to Receive](determining-the-type-of-event-to-receive.md).

The following procedure describes how to receive asynchronous event notifications in C++.

**To receive asynchronous event notifications in C++**

1.  Set up your application with calls to the [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) functions.

    Calling [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) initializes COM, while [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity) grants WMI the permission to call into the process of the consumer. The **CoInitializeEx** function also grants you the ability to program a multithreaded application, which is necessary for asynchronous notification. For more information, see [Maintaining WMI Security](maintaining-wmi-security.md).

    The code in this topic requires the following references and \#include statements to compile correctly.

    ```C++
    #define _WIN32_DCOM
    #include <iostream>
    using namespace std;
    #include <wbemidl.h>
    ```

    

    The following code example describes how to set up the temporary event consumer with calls to [**CoInitializeEx**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializeex) and [**CoInitializeSecurity**](/windows/win32/api/combaseapi/nf-combaseapi-coinitializesecurity).

    ```C++
    void main(int argc, char **argv)
    {
        HRESULT hr = 0;
        hr = CoInitializeEx (0, COINIT_MULTITHREADED);
        hr = CoInitializeSecurity (NULL, 
           -1, 
           NULL, 
           NULL,   
           RPC_C_AUTHN_LEVEL_NONE, 
           RPC_C_IMP_LEVEL_IMPERSONATE, 
           NULL,
           EOAC_NONE,
           NULL); 

        if (FAILED(hr))
        {
           CoUninitialize();
           cout << "Failed to initialize security. Error code = 0x"
               << hex << hr << endl;
           return;
        }

    // ...
    }
    ```

    

2.  Create a sink object through the [**IWbemObjectSink**](iwbemobjectsink.md) interface.

    WMI uses [**IWbemObjectSink**](iwbemobjectsink.md) to send event notifications and to report status on an asynchronous operation or event notification.

3.  Register your event consumer with a call to the [**IWbemServices::ExecNotificationQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationqueryasync) method.

    Make sure that the *pResponseHandler* parameter points to the sink object created in the preceding step.

    The purpose of registration is to receive only the required notifications. Receiving superfluous notifications wastes processing and delivery time; and does not use the filtering ability of WMI to the fullest potential.

    However, a temporary consumer can receive more than one type of event. In this case, a temporary consumer must make separate calls to [**IWbemServices::ExecNotificationQueryAsync**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-execnotificationqueryasync) for each event type. For example, a consumer might require notification when new processes are created (an instance creation event or [**\_\_InstanceCreationEvent**](--instancecreationevent.md)) and for changes to certain registry keys (a registry event such as [**RegistryKeyChangeEvent**](/previous-versions/windows/desktop/regprov/registrykeychangeevent)). Therefore, the consumer makes one call to [**ExecNotificationQueryAsync**](swbemservices-execnotificationqueryasync.md) to register for instance creation events and another call to **ExecNotificationQueryAsync** to register for registry events.

    If you choose to create an event consumer that registers for multiple events, you should avoid registering multiple classes with the same sink. Instead, use a separate sink for each class of registered event. Having a dedicated sink simplifies processing and aids in maintenance, allowing you to cancel one registration without affecting the others.

4.  Perform any necessary activities in your event consumer.

    This step should contain most of your code and include such activities as displaying events to a user interface.

5.  When finished, unregister the temporary event consumer with a call to the [**IWbemServices::CancelAsyncCall**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-cancelasynccall) event.

    Regardless of whether the call to [**CancelAsyncCall**](/windows/desktop/api/WbemCli/nf-wbemcli-iwbemservices-cancelasynccall) succeeds or fails, do not delete the sink object until the object reference count reaches zero. For more information, see [Calling a Method](calling-a-method.md).

 

 
