---
title: COM Error Handling in Java and Visual Basic
description: COM Error Handling in Java and Visual Basic
ms.assetid: 1130a038-3c18-4530-a6d7-9f538352297f
ms.topic: article
ms.date: 05/31/2018
---

# COM Error Handling in Java and Visual Basic

There are three interfaces and three functions that can be used in COM to provide error handling when programming in Java or Microsoft Visual Basic. In Java and Visual Basic, the method call does not return an **HRESULT** as the return value. Instead, these languages use the COM interfaces and functions to obtain **HRESULT** values and to handle errors or exceptions. (Exceptions are events beyond the program's control, such as file problems or invalid parameters.)

The three interfaces that provide support for **HRESULT**s are listed and described briefly in the following table.



|  Interface                                                                        |  Description                                                                                                                    |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**ICreateErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-icreateerrorinfo)<br/>  | Sets error information.<br/>                                                                                   |
| [**IErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-ierrorinfo)<br/>        | Returns information from an error object.<br/>                                                                 |
| [**ISupportErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-isupporterrorinfo)<br/> | Identifies the object as supporting the [**IErrorInfo**](/windows/win32/api/oaidl/nn-oaidl-ierrorinfo) interface.<br/> |



 

The three functions that provide support for **HRESULT**s are listed and described briefly in the following table.



|    Interface       |       Description       |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-createerrorinfo)<br/> | Creates an instance of a generic error object.<br/>                                                                                                            |
| [**GetErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-geterrorinfo)<br/>    | Obtains the error information pointer set by the previous call to [**SetErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-seterrorinfo) in the current logical thread.<br/> |
| [**SetErrorInfo**](/windows/win32/api/oleauto/nf-oleauto-seterrorinfo)<br/>    | Sets the error information object for the current thread of execution.<br/>                                                                                    |



 

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

