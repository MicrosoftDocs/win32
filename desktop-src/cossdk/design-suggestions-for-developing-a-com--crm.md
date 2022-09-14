---
description: Design Suggestions for Developing a COM+ CRM
ms.assetid: dde1b978-6d35-4a75-91fd-69dfcc6c43d2
title: Design Suggestions for Developing a COM+ CRM
ms.topic: article
ms.date: 05/31/2018
---

# Design Suggestions for Developing a COM+ CRM

Following are suggested steps for developing a COM+ CRM:

1.  Before starting development, set the transaction time-out to zero (using the Component Services administrative tool). Set the VTRACE1 registry flag (see [COM+ CRM Registry Settings](com--crm-registry-settings.md)) to see CRM warning and error messages on the debug trace.
2.  Determine which set of interfaces you need to use, structured (Variants) or non-structured. (See [COM+ CRM Interfaces](com--crm-interfaces.md).) This will depend on the language that you use to develop your CRM—for example, Microsoft Visual C++ or Microsoft Visual Basic.
3.  Develop the CRM worker first. Determine the information that is required in the log records. Define the types of log records required and their format.
4.  A debug CRM compensator is provided as part of the CRM samples (in the Windows SDK). This can be used temporarily when debugging the CRM worker in place of the real CRM compensator.
5.  When the CRM worker is working correctly, develop the real CRM compensator and replace the debug CRM compensator with the real CRM compensator.
6.  It may be desirable to initially not test the recovery case. If so, delete the CRM log file for the CRM server application each time before starting that CRM server application.

## Considerations

1.  **Write ahead.** The CRM worker component must write ahead; that is, it must write a log record indicating it is going to perform an action before actually performing that action. In addition, this log record must be forced to disk after the write and before the action is performed.
2.  **Isolation.** The CRM does not enforce isolation. The CRM design must provide isolation between multiple clients on separate transactions and must also consider the case prior to recovery.
3.  **Recovery in progress.** The CRM worker must handle the "recovery in progress" error code. See [Troubleshooting the COM+ CRM](troubleshooting-the-com--crm.md) for more information about this error code.
4.  **Error handling.** The CRM worker must cope with the case where the transaction is aborted earlier than expected. See the section [Error Handling in the COM+ CRM](error-handling-in-the-com--crm.md).
5.  **Recovery time.** The CRM compensator should be designed to perform recovery quickly so that new work for that CRM server application does not have to wait.
6.  **Idempotence.** It is possible that a CRM compensator might receive the same log record again, to undo or redo an action that has already been undone or redone. Actions that the CRM compensator might perform must be idempotent, which often means that the error codes returned from these actions should be ignored.
7.  **Initiation of recovery.** Recovery of a CRM server application is performed when that CRM server application starts up. However, there is no automatic startup of a CRM server application. The application developer should consider how both startup and recovery should be initiated.

## Related topics

<dl> <dt>

[COM+ Compensating Resource Manager Concepts](com--compensating-resource-manager-concepts.md)
</dt> </dl>

 

 



