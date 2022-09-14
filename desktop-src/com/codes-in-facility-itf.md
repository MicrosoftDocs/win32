---
title: Codes in FACILITY_ITF
description: Codes in FACILITY\_ITF
ms.assetid: 1f9f7b2c-a4e4-41c0-9ba5-b8bbf722e077
ms.topic: article
ms.date: 05/31/2018
---

# Codes in FACILITY\_ITF

**HRESULT**s with facilities such as FACILITY\_NULL and FACILITY\_RPC have universal meaning because they are defined at a single source: Microsoft. However, **HRESULT**s in FACILITY\_ITF are determined by the function or interface method from which they are returned. This means that the same 32-bit value in FACILITY\_ITF returned from two different interface methods might have different meanings.

The reason **HRESULT**s in FACILITY\_ITF can have different meanings in different interfaces is that **HRESULT**s are kept to an efficient data type size of 32 bits. Unfortunately, 32 bits is not large enough for the development of an error code allocation system that avoids conflicting codes allocated by different programmers at different times in different places (unlike the handling of interface identifiers and CLSIDs). As a result, the 32-bit **HRESULT** is structured such that Microsoft can define several universal error codes, while allowing other programmers to define new error codes without fear of conflict. The status code convention is as follows:

-   Status codes in facilities other than FACILITY\_ITF can be defined only by Microsoft.
-   Status codes in facility FACILITY\_ITF are defined solely by the developer of the interface or function that returns the status code. To avoid conflicting error codes, whoever defines the interface is responsible for coordinating and publishing the FACILITY\_ITF status codes associated with that interface.

All the COM-defined FACILITY\_ITF codes have a code value in the range of 0x0000-0x01FF. While it is legal to use any codes in FACILITY\_ITF, it is recommended that only code values in the range of 0x0200-0xFFFF be used. This recommendation is made as a means of reducing confusion with any COM-defined errors.

It is also recommended that developers define new functions and interfaces to return error codes as defined by COM and in facilities other than FACILITY\_ITF. In particular, interfaces that have any chance of being remoted using RPC in the future should define the FACILITY\_RPC codes as legal. E\_UNEXPECTED is a specific error code that most developers will want to make universally legal.

## Related topics

<dl> <dt>

[Error Handling in COM](error-handling-in-com.md)
</dt> </dl>

 

 




