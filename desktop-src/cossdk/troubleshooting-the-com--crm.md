---
description: Troubleshooting the COM+ CRM
ms.assetid: 4d2d9372-b540-4e08-9b57-8687802610b6
title: Troubleshooting the COM+ CRM
ms.topic: article
ms.date: 05/31/2018
---

# Troubleshooting the COM+ CRM

Following are the most common problems encountered when developing and using the COM+ CRM:

-   **Event log messages.** If the CRM server application encounters a serious internal error, it will failfast (terminate the CRM server application process) and write a message to the Windows event log. Please refer to the event log if any problems are encountered.

-   **Exceptions from the CRM Compensator.** The CRM infrastructure creates the CRM Compensator and passes it the transaction outcome notifications and the log records written by the CRM Worker. If the CRM Compensator returns an error or throws an exception, it is caught by the CRM infrastructure and causes a failfast. A message in the event log indicates that an exception was received from the CRM Compensator. It is possible to force these exceptions to be ignored. (See [COM+ CRM Registry Settings](com--crm-registry-settings.md).) Exceptions from the CRM Compensator most likely mean a problem in the specific CRM Compensator component and not in the CRM infrastructure itself.

-   **Recovery trace.** The recovery trace can be very useful to determine problems during recovery. For information about enabling recovery trace, see [COM+ CRM Registry Settings](com--crm-registry-settings.md).

-   **Trying to run with the CRM not enabled.** It is not sufficient simply to place the CRM Worker and CRM Compensator components into the COM+ server application. Support for CRMs must be specifically enabled for the specific COM+ server application using the **Enable compensating resource managers** option on the **Advanced** tab of the COM+ application's property pages. (See [Configuring COM+ CRM Components](configuring-com--crm-components.md) for more information.) If an attempt is made to use a CRM inside a server application that does not have the CRM enabled, an error code is returned to the CRM Worker.

-   **Trying to run CRMs in client processes.** CRMs do not run in client processes; they must run in a COM+ server application process. CRM components can be placed in a library package for use by multiple COM+ server applications, but they are not available for use within client processes. Attempting to use the CRM interfaces inside a client process returns an error code to the CRM Worker.

-   **Recovery in progress.** Recovery starts when a CRM server application starts. However, recovery occurs in the background during the normal processing of the CRM server application. The CRM Worker can be created prior to recovery being completed. CRMs cannot be used in a CRM server application process until recovery has been successfully completed. In this case, the CRM Worker receives a "recovery in progress" error code as it tries to register the CRM Compensator. The CRM Worker should poll or otherwise delay until recovery has been completed. The recovery time is specific to a particular type of CRM, and this should be considered when designing the CRM. Long duration recoveries are not desirable.

-   **Security on the CRM log file.** If access to the CRM log file is denied, please see [COM+ CRM Security Considerations](com--crm-security-considerations.md) for a description of how security is set on the CRM log file.

-   **In-doubt transactions.** In rare cases, a DTC transaction might go into the in-doubt state; that is, the DTC cannot determine the transaction outcome. For these cases, during recovery, the CRM maintains the log records for that transaction in the CRM log file. When the in-doubt transaction has been resolved by the DTC, performing another CRM recovery completes the transaction.

-   **Creation and release of CRM Compensator.** The first time a CRM Compensator is registered by a CRM Worker, it is created by the CRM infrastructure and queried to determine which of the CRM Compensator interfaces it supports. It is then immediately released. CRM Compensators need to support the ability to be created and released without having had any intervening method calls. If the CRM Compensator cannot be created correctly, perhaps due to incorrect COM registration, or if it does not support at least one of the correct CRM Compensator interfaces, an error code is returned to the CRM Worker.

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 



