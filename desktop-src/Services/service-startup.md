---
description: To start a service or driver service, the service control program uses the StartService function.
ms.assetid: 7d2ee779-1554-436a-a65c-f0322745f46a
title: Service Startup
ms.topic: article
ms.date: 05/31/2018
---

# Service Startup

To start a service or driver service, the service control program uses the [**StartService**](/windows/desktop/api/Winsvc/nf-winsvc-startservicea) function. The **StartService** function fails if the database is locked. If this occurs, the service control program should wait a few seconds and call **StartService** again. It can check the current lock status of the database by calling the [**QueryServiceLockStatus**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicelockstatusa) function.

If the service control program is starting a service, it can use the [**StartService**](/windows/desktop/api/Winsvc/nf-winsvc-startservicea) function to specify an array of arguments to be passed to the service's [**ServiceMain**](/windows/win32/api/winsvc/nc-winsvc-lpservice_main_functiona) function. The **StartService** function returns after a new thread is created to execute the **ServiceMain** function. The service control program can retrieve the status of the newly started service in a [**SERVICE\_STATUS**](/windows/desktop/api/Winsvc/ns-winsvc-service_status) structure by calling the [**QueryServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicestatus) function. During initialization, the **dwCurrentState** member should be SERVICE\_START\_PENDING. The **dwWaitHint** member is a time interval, in milliseconds, that indicates how long the service control program should wait before calling **QueryServiceStatus** again. When the initialization is complete, the service changes **dwCurrentState** to SERVICE\_RUNNING.

The service control manager does not support passing custom environment variables to a service at startup. Also, the service control manager does not detect and pass on changes to environment variables as the service is running. Instead of making a service dependent on an environment variable, use registry values or [**ServiceMain**](/windows/win32/api/winsvc/nc-winsvc-lpservice_main_functiona) arguments.

The following is a simplified overview of what happens when a typical service is started by the service control manager:

-   The SCM reads the service path from the registry and prepares to start the service. This includes acquiring the service lock. Any attempt to start another service while the service lock is held will block until the service lock is released.
-   The SCM starts the process and waits until either the child process exits (indicating a failure) or reports the SERVICE\_RUNNING status.
-   The application performs its very simple initialization and calls the [**StartServiceCtrlDispatcher**](/windows/desktop/api/Winsvc/nf-winsvc-startservicectrldispatchera) function.
-   [**StartServiceCtrlDispatcher**](/windows/desktop/api/Winsvc/nf-winsvc-startservicectrldispatchera) connects to the service control manager and starts a second thread that calls the [**ServiceMain**](/windows/win32/api/winsvc/nc-winsvc-lpservice_main_functiona) function for the service. **ServiceMain** should report SERVICE\_RUNNING as soon as possible.
-   When the service control manager is notified that the service is running, it releases the service lock.

If service does not update its status within 80 seconds, plus the last wait hint, the service control manager determines that the service has stopped responding. The service control manager will log an event and stop the service.

If the program is starting a driver service, [**StartService**](/windows/desktop/api/Winsvc/nf-winsvc-startservicea) returns after the device driver has completed its initialization.

For more information, see [Starting a Service](starting-a-service.md).

 

 
