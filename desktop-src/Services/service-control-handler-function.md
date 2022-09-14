---
description: Each service has a control handler, the Handler function, that is invoked by the control dispatcher when the service process receives a control request from a service control program.
ms.assetid: 437334ed-05fa-4ab6-aab3-dc2739113e19
title: Service Control Handler Function
ms.topic: article
ms.date: 05/31/2018
---

# Service Control Handler Function

Each service has a control handler, the [**Handler**](/windows/desktop/api/Winsvc/nc-winsvc-lphandler_function) function, that is invoked by the control dispatcher when the service process receives a control request from a service control program. Therefore, this function executes in the context of the control dispatcher. For an example, see [Writing a Control Handler Function](writing-a-control-handler-function.md).

A service calls the [**RegisterServiceCtrlHandler**](/windows/desktop/api/Winsvc/nf-winsvc-registerservicectrlhandlera) or [**RegisterServiceCtrlHandlerEx**](/windows/desktop/api/Winsvc/nf-winsvc-registerservicectrlhandlerexa) function to register its service control handler function.

When the service control handler is invoked, the service must call the [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus) function to report its status to the SCM only if handling the control code causes the service status to change. If handling the control code does not cause the service status to change, it is not necessary to call **SetServiceStatus**.

A service control program can send control requests using the [**ControlService**](/windows/desktop/api/Winsvc/nf-winsvc-controlservice) function. All services must accept and process the **SERVICE\_CONTROL\_INTERROGATE** control code. You can enable or disable acceptance of the other control codes by calling [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus). To receive the **SERVICE\_CONTROL\_DEVICEEVENT** control code, you must call the [**RegisterDeviceNotification**](/windows/desktop/api/winuser/nf-winuser-registerdevicenotificationa) function. Services can also handle additional user-defined control codes.

If a service accepts the **SERVICE\_CONTROL\_STOP** control code, it must stop upon receipt, going to either the **SERVICE\_STOP\_PENDING** or **SERVICE\_STOPPED** state. After the SCM sends this control code, it will not send other control codes.

**Windows XP:** If the service returns **NO\_ERROR** and continues to run, it continues to receive control codes. This behavior changed starting with Windows Server 2003 and Windows XP with Service Pack 2 (SP2).

The control handler must return within 30 seconds, or the SCM returns an error. If a service must do lengthy processing when the service is executing the control handler, it should create a secondary thread to perform the lengthy processing, and then return from the control handler. This prevents the service from tying up the control dispatcher. For example, when handling the stop request for a service that takes a long time, create another thread to handle the stop process. The control handler should simply call [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus) with the **SERVICE\_STOP\_PENDING** message and return.

When the user shuts down the system, all control handlers that have called [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus) with the **SERVICE\_ACCEPT\_PRESHUTDOWN** control code receive the **SERVICE\_CONTROL\_PRESHUTDOWN** control code. The service control manager waits until the service stops or the specified preshutdown time-out value expires (this value can be set with the [**ChangeServiceConfig2**](/windows/desktop/api/Winsvc/nf-winsvc-changeserviceconfig2a) function). This control code should be used only in special circumstances, because a service that handles this notification blocks system shutdown until the service stops or the preshutdown time-out interval expires.

After the preshutdown notifications have been completed, all control handlers that have called [**SetServiceStatus**](/windows/desktop/api/Winsvc/nf-winsvc-setservicestatus) with the **SERVICE\_ACCEPT\_SHUTDOWN** control code receive the **SERVICE\_CONTROL\_SHUTDOWN** control code. They are notified in the order that they appear in the database of installed services. By default, a service has approximately 20 seconds to perform cleanup tasks before the system shuts down. After this time expires, system shutdown proceeds regardless of whether service shutdown is complete. Note that if the system is left in the shutdown state (not restarted or powered down), the service continues to run.

If the service requires more time to cleanup, it sends **STOP\_PENDING** status messages, along with a wait hint, so the service controller knows how long to wait before reporting to the system that service shutdown is complete. However, to prevent a service from stopping shutdown, there is a limit to how long the service controller waits. If the service is being shut down through the Services snap-in, the limit is 125 seconds, or 125,000 milliseconds. If the operating system is rebooting, the time limit is specified in the **WaitToKillServiceTimeout** value (in milliseconds) of the following registry key:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control**

> [!IMPORTANT]
> A service should not attempt to increase the time limit by modifying this value. If you do need to set **WaitToKillServiceTimeout** by hand, the value should be in milliseconds.

Customers require fast shutdown of the operating system. For example, if a computer running on UPS power cannot complete shutdown before the UPS runs out of power, data can be lost. Therefore, services should complete their cleanup tasks as quickly as possible. It is a good practice to minimize unsaved data by saving data on a regular basis, keeping track of the data that is saved to disk, and only saving your unsaved data on shutdown. Because the computer is being shut down, do not spend time releasing allocated memory or other system resources. If you need to notify a server that you are exiting, minimize the time spent waiting for a reply, because network problems could delay the shutdown of your service.

Note that during service shutdown, by default, the SCM does not take dependencies into consideration. The SCM enumerates the list of running services and sends the **SERVICE\_CONTROL\_SHUTDOWN** command. Therefore, a service may fail because another service it depends on has already stopped.

To set the shutdown order of services manually, create a multistring registry value that contains the service names in the order in which they should be shut down and assign it to the Control key's **PreshutdownOrder** value, as follows:

**HKEY\_LOCAL\_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\PreshutdownOrder="Shutdown Order"**

To set the shutdown order of dependent services from your application, use the [**SetProcessShutdownParameters**](/windows/desktop/api/processthreadsapi/nf-processthreadsapi-setprocessshutdownparameters) function. The SCM uses this function to give its handler 0x1E0 priority. The SCM sends **SERVICE\_CONTROL\_SHUTDOWN** notifications when its control handler is called and waits for the services to exit before returning from its control handler.

## Related topics

<dl> <dt>

[Writing a Control Handler Function](writing-a-control-handler-function.md)
</dt> </dl>

 

 
