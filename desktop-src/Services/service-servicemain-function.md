---
Description: 'When a service control program requests that a new service run, the Service Control Manager (SCM) starts the service and sends a start request to the control dispatcher.'
ms.assetid: 'e55e056f-7628-4e3d-9aea-b55c371b4287'
title: Service ServiceMain Function
---

# Service ServiceMain Function

When a service control program requests that a new service run, the Service Control Manager (SCM) starts the service and sends a start request to the control dispatcher. The control dispatcher creates a new thread to execute the [**ServiceMain**](servicemain.md) function for the service. For an example, see [Writing a ServiceMain Function](writing-a-servicemain-function.md).

The [**ServiceMain**](servicemain.md) function should perform the following tasks:

1.  Initialize all global variables.
2.  Call the [**RegisterServiceCtrlHandler**](registerservicectrlhandler.md) function immediately to register a [**Handler**](handler.md) function to handle control requests for the service. The return value of **RegisterServiceCtrlHandler** is a *service status handle* that will be used in calls to notify the SCM of the service status.
3.  Perform initialization. If the execution time of the initialization code is expected to be very short (less than one second), initialization can be performed directly in [**ServiceMain**](servicemain.md).

    If the initialization time is expected to be longer than one second, the service should use one of the following initialization techniques:

    -   Call the [**SetServiceStatus**](setservicestatus.md) function to report SERVICE\_RUNNING but accept no controls until initialization is finished. The service does this by calling **SetServiceStatus** with **dwCurrentState** set to SERVICE\_RUNNING and **dwControlsAccepted** set to 0 in the [**SERVICE\_STATUS**](service-status-str.md) structure. This ensures that the SCM will not send any control requests to the service before it is ready and frees the SCM to manage other services. This approach to initialization is recommended for performance, especially for autostart services.
    -   Report SERVICE\_START\_PENDING, accept no controls, and specify a wait hint. If your service's initialization code performs tasks that are expected to take longer than the initial wait hint value, your code must call the [**SetServiceStatus**](setservicestatus.md) function periodically (possibly with a revised wait hint) to indicate that progress is being made. Be sure to call **SetServiceStatus** only if the initialization is making progress. Otherwise the SCM can wait for your service to enter the SERVICE\_RUNNING state assuming that your service is making progress and block other services from starting. Do not call **SetServiceStatus** from a separate thread unless you are sure the thread performing the initialization is truly making progress.

        A service that uses this approach can also specify a check-point value and increment the value periodically during a lengthy initialization. The program that started the service can call [**QueryServiceStatus**](queryservicestatus.md) or [**QueryServiceStatusEx**](queryservicestatusex.md) to obtain the latest check-point value from the SCM and use the value to report incremental progress to the user.

4.  When initialization is complete, call [**SetServiceStatus**](setservicestatus.md) to set the service state to SERVICE\_RUNNING and specify the controls that the service is prepared to accept. For a list of controls, see the [**SERVICE\_STATUS**](service-status-str.md) structure.
5.  Perform the service tasks, or, if there are no pending tasks, return control to the caller. Any change in the service state warrants a call to [**SetServiceStatus**](setservicestatus.md) to report new status information.
6.  If an error occurs while the service is initializing or running, the service should call [**SetServiceStatus**](setservicestatus.md) to set the service state to SERVICE\_STOP\_PENDING if cleanup will be lengthy. After cleanup is complete, call **SetServiceStatus** to set the service state to SERVICE\_STOPPED from the last thread to terminate. Be sure to set the **dwServiceSpecificExitCode** and **dwWin32ExitCode** members of the [**SERVICE\_STATUS**](service-status-str.md) structure to identify the error.

## Related topics

<dl> <dt>

[Writing a ServiceMain Function](writing-a-servicemain-function.md)
</dt> </dl>

 

 



