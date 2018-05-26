---
Description: Try-except exception handler blocks protect all calls to the fax service provider (FSP) functions.
ms.assetid: db572ca9-677b-4d90-8322-b9fcb1d80c1c
title: Handling Exceptions
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Handling Exceptions

**Try-except** exception handler blocks protect all calls to the fax service provider (FSP) functions. If the fax service detects an exception in the FSP DLL, the service will consider the operation as failed and will proceed accordingly, as if the FSP function returned **FALSE**.

It is recommended that FSPs also use **try-except** blocks to catch errors and then handle them in an appropriate manner. For more information, see [Structured Exception Handling](http://msdn.microsoft.com/library/en-us/debug/base/structured_exception_handling.asp).

 

 



