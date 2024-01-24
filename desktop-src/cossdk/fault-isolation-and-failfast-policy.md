---
description: Fault Isolation and Failfast Policy
ms.assetid: 219c417c-a8a1-49eb-bc5a-702a16994d66
title: Fault Isolation and Failfast Policy
ms.topic: article
ms.date: 05/31/2018
---

# Fault Isolation and Failfast Policy

COM+ performs extensive internal integrity and consistency checks. If COM+ encounters an unexpected internal error condition, it immediately terminates the process. This policy, called *failfast*, facilitates fault containment and results in more reliable and robust systems.

Consider a case in which COM+ detects that one of its data structures is in a corrupted state. At this point, both the cause and the magnitude of the corruption are unknown and, unfortunately, COM+ cannot tell how far the damage has spread. However, even though COM+ is in an indeterminate state, it does not run in isolation. Like other DLLs, it is hosted in a process environment and shares a single address space with the main program executable and many other DLLs. Therefore, COM+ assumes that the entire process has been corrupted, and the process is immediately terminated to prevent it from spreading potentially corrupted information to other processes or, worse yet, from allowing corrupted data to be committed and made durable.

COM+ does not allow exceptions to propagate outside of a context. If an exception occurs while executing within a COM+ context and the application doesn't catch the exception before returning from the context, COM+ catches the exception and terminates the process. Using the failfast policy in this case is based on the assumption that the exception has put the process into an indeterminate state; it is not safe to continue processing.

As a developer or administrator, you should inspect the Event Viewer application log for details on any failfast action or serious application errors.

## Related topics

<dl> <dt>

[Finding the Source of an Error](finding-the-source-of-an-error.md)
</dt> <dt>

[How COM+ Modifies Return Values](how-com--modifies-return-values.md)
</dt> <dt>

[Interpreting Error Codes](interpreting-error-codes.md)
</dt> <dt>

[Strategies for Handling Errors in COM+](strategies-for-handling-errors-in-com-.md)
</dt> <dt>

[Troubleshooting](troubleshooting-the-com--crm.md)
</dt> </dl>

 

 



