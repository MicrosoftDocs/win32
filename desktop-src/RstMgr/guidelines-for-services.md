---
title: Guidelines for Services
description: Services should adhere to these guidelines to ensure that the Restart Manager can shut down and restart services if necessary to install updates. Applications can use the guidelines that are described in Guidelines for Applications.
ms.assetid: 69a98f82-71bb-4780-8a3f-294cc5629900
ms.topic: article
ms.date: 05/31/2018
---

# Guidelines for Services

Services should adhere to these guidelines to ensure that the Restart Manager can shut down and restart services if necessary to install updates. Applications can use the guidelines that are described in [Guidelines for Applications](guidelines-for-applications.md).

-   Services should be capable of being shut down and restarted using the [Service Control Manager](/windows/desktop/Services/service-control-manager) without requiring a system restart. The exceptions to this guideline are critical system processes that run in the context of lsass.exe or services.exe.
-   Restart Manager honors service dependencies. When a service is shut down and restarted, its dependent services are shut down and restarted.
-   Services should specify the recovery interval and reset period in the [Service Control Manager (SCM)](/windows/desktop/Services/service-control-manager). The recovery interval is the time, in msecs, after the last failure that the SCM waits before taking the recovery action. The reset period is the time, in seconds, after the last failure that the Service Control Manager waits before resetting the failure count to 0. Services can use [**ChangeServiceConfig2**](/windows/desktop/api/winsvc/nf-winsvc-changeserviceconfig2a) function to change the configuration settings.

    [Critical services](critical-system-services.md) should use the following recovery settings to specify that the service be restarted one minute after the first failure to restart the service, restarted two minutes after the second failure, and that the computer be restarted one minute after the third failure. The failure count is reset to 0 after 300 seconds.

    <dl> Recovery Actions: Restart/60000/Restart/120000/Reboot/60000 & Reset =300  
    </dl>

    [Critical services](critical-system-services.md) should be started before non-critical services. Services that are not critical services should use the following recovery settings to specify that the service be restarted two minutes after the first failure to restart the service. The service is not restarted after the second failure, and an administrator would need to intervene in this case. The failure count is reset to 0 after 900 seconds.

    <dl> Recovery Actions: Restart/120000/Restart/300000/None/0 & Reset = 900  
    </dl>

 

 