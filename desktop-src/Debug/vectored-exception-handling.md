---
Description: Vectored exception handlers are an extension to structured exception handling.
ms.assetid: e4cf8a88-1bdf-4666-8653-fe2e86c4d8ef
title: Vectored Exception Handling
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Vectored Exception Handling

Vectored exception handlers are an extension to structured exception handling. An application can register a function to watch or handle all exceptions for the application. Vectored handlers are not frame-based, therefore, you can add a handler that will be called regardless of where you are in a call frame. Vectored handlers are called in the order that they were added, after the debugger gets a first chance notification, but before the system begins unwinding the stack.

To add a vectored continue handler, use the [**AddVectoredContinueHandler**](/windows/win32/WinBase/?branch=master) function. To remove this handler, use the [**RemoveVectoredContinueHandler**](/windows/win32/WinBase/?branch=master) function.

To add a vectored exception handler, use the [**AddVectoredExceptionHandler**](/windows/win32/WinBase/?branch=master) function. To remove this handler, use the [**RemoveVectoredExceptionHandler**](/windows/win32/WinBase/?branch=master) function.

 

 



