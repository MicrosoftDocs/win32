---
title: Returning Error Information
description: Returning Error Information
ms.assetid: 4206f2e5-db01-458c-93cb-10c5cd4a4536
ms.topic: article
ms.date: 05/31/2018
---

# Returning Error Information

Using the COM error-handling interfaces and functions, you can return error information by performing the following the steps:

1.  Implement the [**ISupportErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-isupporterrorinfo) interface.
2.  To create an instance of the generic error object, call the [**CreateErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-createerrorinfo) function.
3.  To set its contents, use the [**ICreateErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-icreateerrorinfo) methods.
4.  To associate the error object with the current logical thread, call the [**SetErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-seterrorinfo) function.

The error handling interfaces create and manage an error object, which provides information about the error. The error object is not the same as the object that encountered the error. It is a separate object associated with the current thread of execution.

 

 