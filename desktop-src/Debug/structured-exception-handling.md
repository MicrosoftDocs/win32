---
description: An exception is an event that occurs during the execution of a program, and requires the execution of code outside the normal flow of control.
ms.assetid: '6b6326d8-6875-4146-a4e3-7873f4e400cb'
title: Structured Exception Handling
ms.topic: article
ms.date: 05/31/2018
---

# Structured Exception Handling

An *exception* is an event that occurs during the execution of a program, and requires the execution of code outside the normal flow of control. There are two kinds of exceptions: hardware exceptions and software exceptions. *Hardware exceptions* are initiated by the CPU. They can result from the execution of certain instruction sequences, such as division by zero or an attempt to access an invalid memory address. *Software exceptions* are initiated explicitly by applications or the operating system. For example, the system can detect when an invalid parameter value is specified.

*Structured exception handling* is a mechanism for handling both hardware and software exceptions. Therefore, your code will handle hardware and software exceptions identically. Structured exception handling enables you to have complete control over the handling of exceptions, provides support for debuggers, and is usable across all programming languages and machines. *Vectored exception handling* is an extension to structured exception handling.

The system also supports *termination handling*, which enables you to ensure that whenever a guarded body of code is executed, a specified block of termination code is also executed. The termination code is executed regardless of how the flow of control leaves the guarded body. For example, a termination handler can guarantee that clean-up tasks are performed even if an exception or some other error occurs while the guarded body of code is being executed.

-   [About Structured Exception Handling](about-structured-exception-handling.md)
-   [Using Structured Exception Handling](using-structured-exception-handling.md)
-   [Structured Exception Handling Reference](structured-exception-handling-reference.md)

 

 



