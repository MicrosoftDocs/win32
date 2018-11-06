---
Description: Vectored exception handlers are an extension to structured exception handling.
ms.assetid: e4cf8a88-1bdf-4666-8653-fe2e86c4d8ef
title: Vectored Exception Handling
ms.topic: article
ms.date: 05/31/2018
---

# Vectored Exception Handling

Vectored exception handlers are an extension to structured exception handling. An application can register a function to watch or handle all exceptions for the application. Vectored handlers are not frame-based, therefore, you can add a handler that will be called regardless of where you are in a call frame. Vectored handlers are called in the order that they were added, after the debugger gets a first chance notification, but before the system begins unwinding the stack.

To add a vectored continue handler, use the [**AddVectoredContinueHandler**](https://msdn.microsoft.com/en-us/library/ms679273(v=VS.85).aspx) function. To remove this handler, use the [**RemoveVectoredContinueHandler**](https://msdn.microsoft.com/en-us/library/ms680567(v=VS.85).aspx) function.

To add a vectored exception handler, use the [**AddVectoredExceptionHandler**](https://msdn.microsoft.com/en-us/library/ms679274(v=VS.85).aspx) function. To remove this handler, use the [**RemoveVectoredExceptionHandler**](https://msdn.microsoft.com/en-us/library/ms680571(v=VS.85).aspx) function.

 

 



