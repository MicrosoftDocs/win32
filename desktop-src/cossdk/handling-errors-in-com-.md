---
description: The most problematic part of writing components is dealing with possible errors.
ms.assetid: 12f41eef-9953-4125-8490-07ff64967f95
title: Handling Errors in COM+
ms.topic: article
ms.date: 05/31/2018
---

# Handling Errors in COM+

The most problematic part of writing components is dealing with possible errors. Trying to determine what can go wrong and what to do about it can be challenging under the best conditions. Common errors that your component might check for and handle are failed network connections, security errors, and failures associated with unreachable objects.

Additionally, you can develop your own error codes to report interface-specific errors such as when a business rule has been violated.

In keeping with the COM+ programming model, an object can (and often does) call interface methods on other objects to perform work. Because programmers can write components in different programming languages, COM+ requires that all error-handling mechanisms be language-neutral, for example: HRESULTs and [**ErrorInfo**](errorinfo.md) collections.

This section includes topics, described in the following table, that discuss techniques for handling errors in COM+ applications, features in COM+ that affect failure behavior, and suggestions for diagnosing COM+ errors.



| Topic                                                                                           | Description                                                                                                                                                 |
|-------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Strategies for Handling Errors in COM+](strategies-for-handling-errors-in-com-.md)<br/> | Lists and describes basic guidelines for handling errors in COM+, including when to use HRESULTs and [**ErrorInfo**](errorinfo.md) collections.<br/> |
| [How COM+ Modifies Return Values](how-com--modifies-return-values.md)<br/>               | Identifies the single condition in which COM+ converts a standard HRESULT to a COM+ error code before passing it back to the caller.<br/>             |
| [Fault Isolation and Failfast Policy](fault-isolation-and-failfast-policy.md)<br/>       | Shows how fault isolation and the failfast policy affect COM+ behavior.<br/>                                                                          |
| [Finding the Source of an Error](finding-the-source-of-an-error.md)<br/>                 | Describes how you can diagnose the source and obtain a description of application errors. <br/>                                                       |
| [Interpreting Error Codes](interpreting-error-codes.md)<br/>                             | Identifies the predominant error-handling mechanism for Microsoft Visual C++, the Java language, and Microsoft Visual Basic. <br/>                    |
| [Troubleshooting](troubleshooting.md)<br/>                                               | Provides additional assistance in diagnosing errors.<br/>                                                                                             |
| [Contacting Support](contacting-support.md)<br/>                                         | Identifies important problem-solving information you should provide when contacting support.<br/>                                                     |



 

For detailed information on handling errors associated with various COM+ services, see the following sections:

-   [Speeding Transactions by Notifying the Root Object](speeding-transactions-by-notifying-the-root-object.md)
-   [Handling Errors](handling-errors-in-queued-components.md) (for queued components)

## Related topics

<dl> <dt>

[Debugging COM+ Applications](debugging-com--applications.md)
</dt> </dl>

 

 




