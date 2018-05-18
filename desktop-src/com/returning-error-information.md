---
title: Returning Error Information
description: Returning Error Information
ms.assetid: '4206f2e5-db01-458c-93cb-10c5cd4a4536'
---

# Returning Error Information

Using the COM error-handling interfaces and functions, you can return error information by performing the following the steps:

1.  Implement the [**ISupportErrorInfo**](42d33066-36b4-4a5b-aa5d-46682e560f32) interface.
2.  To create an instance of the generic error object, call the [**CreateErrorInfo**](6a9dd862-754a-48e3-8be5-d1fbd1d38f2b) function.
3.  To set its contents, use the [**ICreateErrorInfo**](2e7c5ad5-9018-413e-8826-ef752ebf302c) methods.
4.  To associate the error object with the current logical thread, call the [**SetErrorInfo**](8eaacfac-fc37-4eaa-870b-10b99d598d66) function.

The error handling interfaces create and manage an error object, which provides information about the error. The error object is not the same as the object that encountered the error. It is a separate object associated with the current thread of execution.

 

 




