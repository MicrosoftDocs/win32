---
Description: 'Services are generally written as console applications.'
ms.assetid: 'ed6945fc-ac08-4776-8d75-d33e8df3882a'
title: Service Entry Point
---

# Service Entry Point

Services are generally written as console applications. The entry point of a console application is its **main** function. The **main** function receives arguments from the **ImagePath** value from the registry key for the service. For more information, see the Remarks section of the [**CreateService**](createservice.md) function.

When the SCM starts a service program, it waits for it to call the [**StartServiceCtrlDispatcher**](startservicectrldispatcher.md) function. Use the following guidelines.

-   A service of type SERVICE\_WIN32\_OWN\_PROCESS should call [**StartServiceCtrlDispatcher**](startservicectrldispatcher.md) immediately, from its main thread. You can perform any initialization after the service starts, as described in [Service ServiceMain Function](service-servicemain-function.md).
-   If the service type is SERVICE\_WIN32\_SHARE\_PROCESS and there is common initialization for all services in the program, you can perform the initialization in the main thread before calling [**StartServiceCtrlDispatcher**](startservicectrldispatcher.md), as long as it takes less than 30 seconds. Otherwise, you must create another thread to do the common initialization, while the main thread calls **StartServiceCtrlDispatcher**. You should still perform any service-specific initialization after the service starts.

The [**StartServiceCtrlDispatcher**](startservicectrldispatcher.md) function takes a [**SERVICE\_TABLE\_ENTRY**](service-table-entry-str.md) structure for each service contained in the process. Each structure specifies the service name and the entry point for the service. For an example, see [Writing a Service Program's main Function](writing-a-service-program-s-main-function.md).

If [**StartServiceCtrlDispatcher**](startservicectrldispatcher.md) succeeds, the calling thread does not return until all running services in the process have entered the SERVICE\_STOPPED state. The SCM sends control requests to this thread through a named pipe. The thread acts as a control dispatcher, performing the following tasks:

-   Create a new thread to call the appropriate entry point when a new service is started.
-   Call the appropriate [handler function](service-control-handler-function.md) to handle service control requests.

## Related topics

<dl> <dt>

[Writing a Service Program's main Function](writing-a-service-program-s-main-function.md)
</dt> </dl>

 

 



