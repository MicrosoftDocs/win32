---
title: Retrieving Error Information
description: Retrieving Error Information
ms.assetid: 51a0e401-43f2-4738-9799-a96e2580a29f
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Error Information

Using the COM error-handling interfaces and functions, you can retrieve error information as follows:

1.  Check whether the returned value represents an error that the object is prepared to handle.
2.  Call [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) to get a pointer to the [**ISupportErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-isupporterrorinfo) interface. Then call [**ISupportErrorInfo::InterfaceSupportsErrorInfo**](/windows/win32/api/oaidl/nf-oaidl-isupporterrorinfo-interfacesupportserrorinfo) to verify that the error was raised by the object that returned it and that the error object pertains to the current error and not to a previous call.
3.  To get a pointer to the error object, call the [**GetErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-geterrorinfo) function.
4.  To retrieve information from the error object, use the [**IErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-ierrorinfo) methods.

If the object is not prepared to handle the error but needs to propagate the error information further down the call chain, it should simply pass the return value to its caller. Because the [**GetErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-geterrorinfo) function clears the error information and passes ownership of the error object to the caller, the function should be called only by the object that handles the error.

 

 