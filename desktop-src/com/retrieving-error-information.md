---
title: Retrieving Error Information
description: Retrieving Error Information
ms.assetid: 51a0e401-43f2-4738-9799-a96e2580a29f
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Error Information

Using the COM error-handling interfaces and functions, you can retrieve error information as follows:

1.  Check whether the returned value represents an error that the object is prepared to handle.
2.  Call [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q,)) to get a pointer to the [**ISupportErrorInfo**](https://msdn.microsoft.com/windows/desktop/42d33066-36b4-4a5b-aa5d-46682e560f32) interface. Then call [**ISupportErrorInfo::InterfaceSupportsErrorInfo**](https://msdn.microsoft.com/windows/desktop/a54ef18d-ee3f-4483-ac4a-99d758f0960a) to verify that the error was raised by the object that returned it and that the error object pertains to the current error and not to a previous call.
3.  To get a pointer to the error object, call the [**GetErrorInfo**](https://msdn.microsoft.com/windows/desktop/03317526-8c4f-4173-bc10-110c8112676a) function.
4.  To retrieve information from the error object, use the [**IErrorInfo**](https://msdn.microsoft.com/windows/desktop/4dda6909-2d9a-4727-ae0c-b5f90dcfa447) methods.

If the object is not prepared to handle the error but needs to propagate the error information further down the call chain, it should simply pass the return value to its caller. Because the [**GetErrorInfo**](https://msdn.microsoft.com/windows/desktop/03317526-8c4f-4173-bc10-110c8112676a) function clears the error information and passes ownership of the error object to the caller, the function should be called only by the object that handles the error.

 

 




