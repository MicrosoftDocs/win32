---
Description: To send control requests to a running service, a service control program uses the ControlService function.
ms.assetid: d6cdc876-8b74-460e-ad43-6455ddf428dd
title: Service Control Requests
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Service Control Requests

To send control requests to a running service, a service control program uses the [**ControlService**](/windows/win32/Winsvc/nf-winsvc-controlservice?branch=master) function. This function specifies a control value that is passed to the [**HandlerEx**](/windows/win32/WinSvc/nc-winsvc-lphandler_function_ex?branch=master) function of the specified service. This control value can be a user-defined code, or it can be one of the standard codes that enable the calling program to perform the following actions:

-   Stop a service (SERVICE\_CONTROL\_STOP).
-   Pause a service (SERVICE\_CONTROL\_PAUSE).
-   Resume executing a paused service (SERVICE\_CONTROL\_CONTINUE).
-   Retrieve updated status information from a service (SERVICE\_CONTROL\_INTERROGATE).

Each service specifies the control values that it will accept and process. To determine which of the standard control values are accepted by a service, use the [**QueryServiceStatusEx**](/windows/win32/Winsvc/nf-winsvc-queryservicestatusex?branch=master) function or specify the SERVICE\_CONTROL\_INTERROGATE control value in a call to the [**ControlService**](/windows/win32/Winsvc/nf-winsvc-controlservice?branch=master) function. The **dwControlsAccepted** member of the [**SERVICE\_STATUS**](/windows/win32/Winsvc/ns-winsvc-_service_status?branch=master) structure returned by these functions indicates whether the service can be stopped, paused, or resumed. All services accept the SERVICE\_CONTROL\_INTERROGATE control value.

The [**QueryServiceStatusEx**](/windows/win32/Winsvc/nf-winsvc-queryservicestatusex?branch=master) function reports the most recent status for a specified service, but does not get an updated status from the service itself. Using the SERVICE\_CONTROL\_INTERROGATE control value in a call to [**ControlService**](/windows/win32/Winsvc/nf-winsvc-controlservice?branch=master) ensures that the status information returned is current.

## Related topics

<dl> <dt>

[Controlling a Service Using SC](controlling-a-service-using-sc.md)
</dt> </dl>

 

 



