---
title: COM Error Handling in Java and Visual Basic
description: COM Error Handling in Java and Visual Basic
ms.assetid: '1130a038-3c18-4530-a6d7-9f538352297f'
---

# COM Error Handling in Java and Visual Basic

There are three interfaces and three functions that can be used in COM to provide error handling when programming in Java or Microsoft Visual Basic. In Java and Visual Basic, the method call does not return an **HRESULT** as the return value. Instead, these languages use the COM interfaces and functions to obtain **HRESULT** values and to handle errors or exceptions. (Exceptions are events beyond the program's control, such as file problems or invalid parameters.)

The three interfaces that provide support for **HRESULT**s are listed and described briefly in the following table.



|                                                                          |                                                                                                                      |
|--------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------|
| [**ICreateErrorInfo**](2e7c5ad5-9018-413e-8826-ef752ebf302c)<br/>  | Sets error information.<br/>                                                                                   |
| [**IErrorInfo**](4dda6909-2d9a-4727-ae0c-b5f90dcfa447)<br/>        | Returns information from an error object.<br/>                                                                 |
| [**ISupportErrorInfo**](42d33066-36b4-4a5b-aa5d-46682e560f32)<br/> | Identifies the object as supporting the [**IErrorInfo**](4dda6909-2d9a-4727-ae0c-b5f90dcfa447) interface.<br/> |



 

The three functions that provide support for **HRESULT**s are listed and described briefly in the following table.



|                                                                        |                                                                                                                                                                      |
|------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**CreateErrorInfo**](6a9dd862-754a-48e3-8be5-d1fbd1d38f2b)<br/> | Creates an instance of a generic error object.<br/>                                                                                                            |
| [**GetErrorInfo**](03317526-8c4f-4173-bc10-110c8112676a)<br/>    | Obtains the error information pointer set by the previous call to [**SetErrorInfo**](8eaacfac-fc37-4eaa-870b-10b99d598d66) in the current logical thread.<br/> |
| [**SetErrorInfo**](8eaacfac-fc37-4eaa-870b-10b99d598d66)<br/>    | Sets the error information object for the current thread of execution.<br/>                                                                                    |



 

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

 





