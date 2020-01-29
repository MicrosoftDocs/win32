---
title: Error Handling Strategies
description: Error Handling Strategies
ms.assetid: 8d03ede8-0661-43dc-adaf-3c1f5fc1687e
ms.topic: article
ms.date: 05/31/2018
---

# Error Handling Strategies

Because interface methods are virtual, it is not possible for a caller to know the full set of values that may be returned from any one call. One implementation of a method may return five values; another may return eight.

The documentation lists common values that may be returned for each method; these are the values that you must check for and handle in your code because they have special meanings. Other values may be returned, but because they are not meaningful, you do not need to write special code to handle them. A simple check for zero or nonzero is adequate.

## HRESULT Values

The return value of COM functions and methods is an **HRESULT**. The values of some HRESULTs have been changed in COM to eliminate all duplication and overlapping with the system error codes. Those that duplicate system error codes have been changed to FACILITY\_WIN32, and those that overlap remain in FACILITY\_NULL. Common **HRESULT** values and their values are listed in the following table.



| HRESULT                    | Value                 | Description                                                                                                                                        |
|----------------------------|-----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| E\_ABORT<br/>        | 0x80004004<br/> | The operation was aborted because of an unspecified error.<br/>                                                                              |
| E\_ACCESSDENIED<br/> | 0x80070005<br/> | A general access-denied error.<br/>                                                                                                          |
| E\_FAIL<br/>         | 0x80004005<br/> | An unspecified failure has occurred.<br/>                                                                                                    |
| E\_HANDLE<br/>       | 0x80070006<br/> | An invalid handle was used.<br/>                                                                                                             |
| E\_INVALIDARG<br/>   | 0x80070057<br/> | One or more arguments are invalid.<br/>                                                                                                      |
| E\_NOINTERFACE<br/>  | 0x80004002<br/> | The [**QueryInterface**](/windows/desktop/api/Unknwn/nf-unknwn-iunknown-queryinterface(q)) method did not recognize the requested interface. The interface is not supported.<br/> |
| E\_NOTIMPL<br/>      | 0x80004001<br/> | The method is not implemented.<br/>                                                                                                          |
| E\_OUTOFMEMORY<br/>  | 0x8007000E<br/> | The method failed to allocate necessary memory.<br/>                                                                                         |
| E\_PENDING<br/>      | 0x8000000A<br/> | The data necessary to complete the operation is not yet available.<br/>                                                                      |
| E\_POINTER<br/>      | 0x80004003<br/> | An invalid pointer was used.<br/>                                                                                                            |
| E\_UNEXPECTED<br/>   | 0x8000FFFF<br/> | A catastrophic failure has occurred.<br/>                                                                                                    |
| S\_FALSE<br/>        | 0x00000001<br/> | The method succeeded and returned the boolean value **FALSE**.<br/>                                                                          |
| S\_OK<br/>           | 0x00000000<br/> | The method succeeded. If a boolean return value is expected, the returned value is **TRUE**.<br/>                                            |



 

## Network Errors

If the first four digits of the error code are 8007, this indicates a system or network error. You can use the **net** command to decode these types of errors. To decode the error, first convert the last four digits of the hexadecimal error code to decimal. Then, at the command prompt, type the following, where decimal code is replaced with the return value you want to decode:

**net helpmsg <***decimal\_code***>**

The net command returns a description of the error. For example, if COM returns the error 8007054B, convert the 054B to decimal (1355). Then type the following:

**net helpmsg 1355**

The net command returns the error description: "The specified domain did not exist".

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

 





