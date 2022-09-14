---
description: Error Handling in the COM+ CRM
ms.assetid: 9de31fb5-31e9-494a-b61f-87bcff0d5085
title: Error Handling in the COM+ CRM
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling in the COM+ CRM

COM+ server applications implement a failfast policy. If a serious internal error is detected, the server application process exits and writes an error message to the Windows event log. This allows quick detection of problems and is possible due to the protection of application data by transaction processing. Always check the Windows event log for any errors from the CRM, either during development or during final deployment.

Basic errors in using the CRM interfaces, such as invalid arguments or sequence errors (for example, trying to write a log record before registering the CRM Compensator), return error codes and should not trigger failfast. For CRM development, you may choose to set the VTRACE1 registry key (see [COM+ CRM Registry Settings](com--crm-registry-settings.md)), which causes a message to appear in the debugger output window for each error.

Transient errors can also occur. These errors are typically caused by timing conditions and result in an error code being returned. The CRM developer should ensure that these error conditions are handled. For example, while writing a log record, the transaction could abort due to a time-out. The method then returns an error, which the caller should check for and handle appropriately.

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 



