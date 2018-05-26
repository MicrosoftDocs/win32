---
title: Raising Exceptions During Invoke
description: When you implement Invoke, errors can be communicated either through the normal return value or by raising an exception. An exception is a special situation that is normally handled by jumping to the nearest routine enclosing the exception handler.
ms.assetid: 5afc97ac-4a6d-4bfc-8fb2-5e53b6c6d53f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Raising Exceptions During Invoke

When you implement [**Invoke**](/windows/previous-versions/oaidl/nf-oaidl-idispatch-invoke?branch=master), errors can be communicated either through the normal return value or by raising an exception. An exception is a special situation that is normally handled by jumping to the nearest routine enclosing the exception handler.

To raise an exception, **IDispatch::Invoke** returns DISP\_E\_EXCEPTION and fills the structure passed through pExcepInfo with information about the cause of the exception or error. You can use the information to understand the cause of the exception and proceed as necessary.

The exception information structure includes an error code number that identifies the kind of exception (a string that describes the error in a human-readable way). It also includes a Help file and a Help context number that can be passed to Windows Help for details about the error. At a minimum, the error code number must be filled with a valid number.

If you consider [**IDispatch**](/windows/previous-versions/oaidl/nn-oaidl-idispatch?branch=master) another way to call C++ methods in an interface, EXCEPINFO models the raising of an exception or **longjmp()** call by such a method.

 

 




