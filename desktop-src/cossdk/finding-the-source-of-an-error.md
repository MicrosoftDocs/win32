---
description: Finding the Source of an Error
ms.assetid: d7287cf1-9501-4d37-b022-b56c8008220c
title: Finding the Source of an Error
ms.topic: article
ms.date: 05/31/2018
---

# Finding the Source of an Error

You can diagnose the source and obtain a description of application errors by using COM+ and other tools. If you discover that the application error is caused by COM+, you can interpret the error message viewing the Winerror.h file or by using the Microsoft Visual C++ error utility.

If your server application is failing or causing unexpected behavior, you must first determine where the error occurred. The system Event Viewer tracks application, security, and system events. Many "silent" errors are recorded here. However, not all errors are shown in the Event Viewer.

You should first refer to the application log in the Event Viewer to check the application associated with the event message. (Because you can also archive event logs, you can track an event history of the error.) Double-clicking an entry in your log activates an **Event Properties** page, which provides further information about the system event.

For more information on debugging a COM+ application, see [Debugging COM+ Applications](debugging-com--applications.md).

## Related topics

<dl> <dt>

[Fault Isolation and Failfast Policy](fault-isolation-and-failfast-policy.md)
</dt> <dt>

[How COM+ Modifies Return Values](how-com--modifies-return-values.md)
</dt> <dt>

[Interpreting Error Codes](interpreting-error-codes.md)
</dt> <dt>

[Strategies for Handling Errors in COM+](strategies-for-handling-errors-in-com-.md)
</dt> <dt>

[Troubleshooting](troubleshooting-the-com--crm.md)
</dt> </dl>

 

 



