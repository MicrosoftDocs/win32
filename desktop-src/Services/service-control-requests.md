---
description: To send control requests to a running service, a service control program uses the ControlService function.
ms.assetid: d6cdc876-8b74-460e-ad43-6455ddf428dd
title: Service Control Requests
ms.topic: article
ms.date: 05/31/2018
---

# Service Control Requests

To send control requests to a running service, a service control program uses the [**ControlService**](/windows/desktop/api/Winsvc/nf-winsvc-controlservice) function. This function specifies a control value that is passed to the [**HandlerEx**](/windows/desktop/api/WinSvc/nc-winsvc-lphandler_function_ex) function of the specified service. This control value can be a user-defined code, or it can be one of the standard codes that enable the calling program to perform the following actions:

-   Stop a service (SERVICE\_CONTROL\_STOP).
-   Pause a service (SERVICE\_CONTROL\_PAUSE).
-   Resume executing a paused service (SERVICE\_CONTROL\_CONTINUE).
-   Retrieve updated status information from a service (SERVICE\_CONTROL\_INTERROGATE).

Each service specifies the control values that it will accept and process. To determine which of the standard control values are accepted by a service, use the [**QueryServiceStatusEx**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicestatusex) function or specify the SERVICE\_CONTROL\_INTERROGATE control value in a call to the [**ControlService**](/windows/desktop/api/Winsvc/nf-winsvc-controlservice) function. The **dwControlsAccepted** member of the [**SERVICE\_STATUS**](/windows/desktop/api/Winsvc/ns-winsvc-service_status) structure returned by these functions indicates whether the service can be stopped, paused, or resumed. All services accept the SERVICE\_CONTROL\_INTERROGATE control value.

The [**QueryServiceStatusEx**](/windows/desktop/api/Winsvc/nf-winsvc-queryservicestatusex) function reports the most recent status for a specified service, but does not get an updated status from the service itself. Using the SERVICE\_CONTROL\_INTERROGATE control value in a call to [**ControlService**](/windows/desktop/api/Winsvc/nf-winsvc-controlservice) ensures that the status information returned is current.

## Related topics

<dl> <dt>

[Controlling a Service Using SC](controlling-a-service-using-sc.md)
</dt> </dl>

 

 



