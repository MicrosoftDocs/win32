---
title: Base Types
description: To prevent the problems that implementation-dependent data types can cause on different computer architectures, MIDL defines its own base data types.
ms.assetid: 0b2778c7-8cee-415f-bb5e-01f6c9eedc70
ms.topic: article
ms.date: 05/31/2018
---

# Base Types

To prevent the problems that implementation-dependent data types can cause on different computer architectures, MIDL defines its own base data types.



| Base type                         | Description                                                                                                                                                         |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**boolean**](https://docs.microsoft.com/windows/desktop/Midl/boolean)       | A data item that can have the value **TRUE** or **FALSE**.                                                                                                          |
| [**byte**](https://docs.microsoft.com/windows/desktop/Midl/byte)             | An 8-bit data item guaranteed to be transmitted without any change.                                                                                                 |
| [**char**](https://docs.microsoft.com/windows/desktop/Midl/char-idl)         | An 8-bit unsigned character data item.                                                                                                                              |
| [**double**](https://docs.microsoft.com/windows/desktop/Midl/double)         | A 64-bit floating-point number.                                                                                                                                     |
| [**float**](https://docs.microsoft.com/windows/desktop/Midl/float)           | A 32-bit floating-point number.                                                                                                                                     |
| [**handle\_t**](https://docs.microsoft.com/windows/desktop/Midl/handle-t)    | A primitive handle that can be used for RPC binding or data serializing.                                                                                            |
| [**hyper**](https://docs.microsoft.com/windows/desktop/Midl/hyper)           | A 64-bit integer that can be declared as either [**signed**](https://docs.microsoft.com/windows/desktop/Midl/signed) or [**unsigned**](https://docs.microsoft.com/windows/desktop/Midl/unsigned) Can also be referred to as **\_int64**.                  |
| [**int**](https://docs.microsoft.com/windows/desktop/Midl/int)               | A 32-bit integer that can be declared as either **signed** or **unsigned**.                                                                                         |
| [**\_\_int3264**](https://docs.microsoft.com/windows/desktop/Midl/--int3264) | A keyword that specifies an integral type that has either 32-bit or 64-bit properties.                                                                              |
| [**long**](https://docs.microsoft.com/windows/desktop/Midl/long)             | A modifier for **int** that indicates a 32-bit integer. Can be declared as either **signed** or **unsigned**.                                                       |
| [**short**](https://docs.microsoft.com/windows/desktop/Midl/short)           | A 16-bit integer that can be declared as either **signed** or **unsigned**.                                                                                         |
| [**small**](https://docs.microsoft.com/windows/desktop/Midl/small)           | A modifier for **int** that indicates an 8-bit integer. Can be declared as either **signed** or **unsigned**.                                                       |
| [**wchar\_t**](https://docs.microsoft.com/windows/desktop/Midl/wchar-t)      | Wide-character type that is supported as a Microsoft extension to IDL. Therefore, this type is not available if you compile using the [/**osf**](https://docs.microsoft.com/windows/desktop/Midl/-osf) switch. |



 

The header file Rpcndr.h provides definitions for most of these base data types. The keyword **int** is recognized and is transmittable on 32-bit platforms. On 16-bit platforms, the **int** data type requires a modifier, such as **short** or **long**, to specify its length.

Although **void \* \*** is recognized as a generic pointer type by the ANSI C standard, MIDL restricts its usage. Each pointer used in a remote or serializing operation must point to either base types or types constructed from base types. (There is an exception: context handles are defined as **void** types. For more information see [Context Handles](context-handles.md).)

 

 




