---
title: Retrieving Error Information
description: Describes how to retrieve error information.
ms.assetid: 0bd640a4-e93f-4201-8789-61ba7178ce15
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Retrieving Error Information

## To retrieve error information

1.  Check whether the returned value represents an error that the object is prepared to handle.

2.  Call **QueryInterface** to get a pointer to the [**ISupportErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-isupporterrorinfo)interface. Then, call [InterfaceSupportsErrorInfo](https://msdn.microsoft.com/windows/desktop/A54EF18D-EE3F-4483-AC4A-99D758F0960A) to verify that the error was raised by the object that returned it and that the error object pertains to the current error, and not to a previous call.

3.  To get a pointer to the error object, call the [GetErrorInfo](https://msdn.microsoft.com/windows/desktop/03317526-8C4F-4173-BC10-110C8112676A) function.

4.  To retrieve information from the error object, use the [**IErrorInfo**](/previous-versions/windows/desktop/api/oaidl/nn-oaidl-ierrorinfo) methods.

The following figure illustrates this procedure.

![isupporterrorinfo](images/oa03-02.png)

If the object is not prepared to handle the error, but needs to propagate the error information further down the call chain, it should simply pass the return value to its caller. Because the [GetErrorInfo](https://msdn.microsoft.com/windows/desktop/03317526-8C4F-4173-BC10-110C8112676A) function clears the error information and passes ownership of the error object to the caller, the function should be called only by the object that handles the error.

## Related topics

<dl> <dt>

[Error Handling Interfaces](error-handling-interfaces.md)
</dt> </dl>

 

 




