---
Description: 'To send control requests to a running service, a service control program uses the ControlService function.'
ms.assetid: 'd6cdc876-8b74-460e-ad43-6455ddf428dd'
title: Service Control Requests
---

# Service Control Requests

To send control requests to a running service, a service control program uses the [**ControlService**](controlservice.md) function. This function specifies a control value that is passed to the [**HandlerEx**](handlerex.md) function of the specified service. This control value can be a user-defined code, or it can be one of the standard codes that enable the calling program to perform the following actions:

-   Stop a service (SERVICE\_CONTROL\_STOP).
-   Pause a service (SERVICE\_CONTROL\_PAUSE).
-   Resume executing a paused service (SERVICE\_CONTROL\_CONTINUE).
-   Retrieve updated status information from a service (SERVICE\_CONTROL\_INTERROGATE).

Each service specifies the control values that it will accept and process. To determine which of the standard control values are accepted by a service, use the [**QueryServiceStatusEx**](queryservicestatusex.md) function or specify the SERVICE\_CONTROL\_INTERROGATE control value in a call to the [**ControlService**](controlservice.md) function. The **dwControlsAccepted** member of the [**SERVICE\_STATUS**](service-status-str.md) structure returned by these functions indicates whether the service can be stopped, paused, or resumed. All services accept the SERVICE\_CONTROL\_INTERROGATE control value.

The [**QueryServiceStatusEx**](queryservicestatusex.md) function reports the most recent status for a specified service, but does not get an updated status from the service itself. Using the SERVICE\_CONTROL\_INTERROGATE control value in a call to [**ControlService**](controlservice.md) ensures that the status information returned is current.

## Related topics

<dl> <dt>

[Controlling a Service Using SC](controlling-a-service-using-sc.md)
</dt> </dl>

 

 



