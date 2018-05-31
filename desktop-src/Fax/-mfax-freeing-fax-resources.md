---
Description: Under certain circumstances, it is the responsibility of the calling fax client application to manage allocated resources.
ms.assetid: a8371d98-8a66-484a-9179-4894ae0a7dfc
title: Freeing Fax Resources
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Freeing Fax Resources

Under certain circumstances, it is the responsibility of the calling fax client application to manage allocated resources. This is true for applications running in the Microsoft Win32 environment and for C/C++ applications in the Component Object Model (COM) implementation environment.

## In the Win32 Environment

The fax client application must deallocate the resources allocated by certain fax client function calls. This includes calls to the [**FaxCompleteJobParams**](-mfax-faxcompletejobparams.md) function and to functions that begin with **FaxEnum** or **FaxGet**. Call the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function to deallocate these resources.

Data should not be referenced if an application has dereferenced it by calling the [**FaxFreeBuffer**](-mfax-faxfreebuffer.md) function.

## In the COM Implementation Environment

If you are writing a C/C++ application, you must call the [SysFreeString](8f230ee3-5f6e-4cb9-a910-9c90b754dcd3) function to deallocate the resources associated with the buffer pointed to by all pVal parameters. This is because all property methods that retrieve properties (those that end with get\_*PropertyName*) allocate the memory required for the buffer.

For more information about creating and deallocating fax client objects, see the steps listed with each interface topic and the hierarchical diagram in [The Fax Client Object Model](-mfax-the-fax-client-object-model.md).

If you are writing a Microsoft Visual Basic application, it is not necessary to deallocate resources.

 

 



