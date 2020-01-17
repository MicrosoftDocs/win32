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



|                                                                          |                                                                                                                      |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**ICreateErrorInfo**](https://msdn.microsoft.com/library/ms221072(v=VS.71).aspx)<br/>  | Sets error information.<br/>                                                                                   |
| [**IErrorInfo**](https://msdn.microsoft.com/library/ms221233(v=VS.71).aspx)<br/>        | Returns information from an error object.<br/>                                                                 |
| [**ISupportErrorInfo**](https://msdn.microsoft.com/library/ms221083(v=VS.71).aspx)<br/> | Identifies the object as supporting the [**IErrorInfo**](https://msdn.microsoft.com/library/ms221233(v=VS.71).aspx) interface.<br/> |



 

The three functions that provide support for **HRESULT**s are listed and described briefly in the following table.



|                                                                        |                                                                                                                                                                      |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateErrorInfo**](https://msdn.microsoft.com/library/ms221316(v=VS.71).aspx)<br/> | Creates an instance of a generic error object.<br/>                                                                                                            |
| [**GetErrorInfo**](https://msdn.microsoft.com/library/ms221032(v=VS.71).aspx)<br/>    | Obtains the error information pointer set by the previous call to [**SetErrorInfo**](https://msdn.microsoft.com/library/ms221409(v=VS.71).aspx) in the current logical thread.<br/> |
| [**SetErrorInfo**](https://msdn.microsoft.com/library/ms221409(v=VS.71).aspx)<br/>    | Sets the error information object for the current thread of execution.<br/>                                                                                    |



 

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

 





