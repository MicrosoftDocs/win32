---
title: Returning Error Information
description: Returning Error Information
ms.assetid: 4206f2e5-db01-458c-93cb-10c5cd4a4536
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Returning Error Information

Using the COM error-handling interfaces and functions, you can return error information by performing the following the steps:

1.  Implement the [**ISupportErrorInfo**](https://msdn.microsoft.com/en-us/library/ms221083(v=VS.71).aspx) interface.
2.  To create an instance of the generic error object, call the [**CreateErrorInfo**](https://msdn.microsoft.com/en-us/library/ms221316(v=VS.71).aspx) function.
3.  To set its contents, use the [**ICreateErrorInfo**](https://msdn.microsoft.com/en-us/library/ms221072(v=VS.71).aspx) methods.
4.  To associate the error object with the current logical thread, call the [**SetErrorInfo**](https://msdn.microsoft.com/en-us/library/ms221409(v=VS.71).aspx) function.

The error handling interfaces create and manage an error object, which provides information about the error. The error object is not the same as the object that encountered the error. It is a separate object associated with the current thread of execution.

 

 




