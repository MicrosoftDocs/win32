---
description: A termination handler ensures that a specific block of code is executed whenever flow of control leaves a particular guarded body of code. A termination handler consists of the following elements.
ms.assetid: 899e2939-e028-4be1-9f08-9a79bf97eb37
title: Termination Handling
ms.topic: article
ms.date: 05/31/2018
---

# Termination Handling

A *termination handler* ensures that a specific block of code is executed whenever flow of control leaves a particular guarded body of code. A termination handler consists of the following elements.

-   A guarded body of code
-   A block of termination code to be executed when the flow of control leaves the guarded body

Termination handlers are declared in language-specific syntax. Using the Microsoft C/C++ Optimizing Compiler, they are implemented using **\_\_try** and **\_\_finally**. For more information, see [Handler Syntax](handler-syntax.md).

The guarded body of code can be a block of code, a set of nested blocks, or an entire procedure or function. Whenever the guarded body is executed, the block of termination code will be executed. The only exception to this is when the thread terminates during execution of the guarded body (for example, if the [**ExitThread**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitthread) or [**ExitProcess**](/windows/win32/api/processthreadsapi/nf-processthreadsapi-exitprocess) function is called from within the guarded body).

The termination block is executed when the flow of control leaves the guarded body, regardless of whether the guarded body terminated normally or abnormally. The guarded body is considered to have terminated normally when the last statement in the block is executed and control proceeds sequentially into the termination block. Abnormal termination occurs when the flow of control leaves the guarded body due to an exception, or due to a control statement such as **return**, **goto**, **break**, or **continue**. The [**AbnormalTermination**](abnormaltermination.md) function can be called from within the termination block to determine whether the guarded body terminated normally.

 

 
