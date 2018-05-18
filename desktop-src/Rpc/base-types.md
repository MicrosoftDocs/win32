---
title: Base Types
description: To prevent the problems that implementation-dependent data types can cause on different computer architectures, MIDL defines its own base data types.
ms.assetid: '0b2778c7-8cee-415f-bb5e-01f6c9eedc70'
---

# Base Types

To prevent the problems that implementation-dependent data types can cause on different computer architectures, MIDL defines its own base data types.



| Base type                         | Description                                                                                                                                                         |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**boolean**](https://msdn.microsoft.com/library/windows/desktop/aa366740)       | A data item that can have the value **TRUE** or **FALSE**.                                                                                                          |
| [**byte**](https://msdn.microsoft.com/library/windows/desktop/aa366743)             | An 8-bit data item guaranteed to be transmitted without any change.                                                                                                 |
| [**char**](https://msdn.microsoft.com/library/windows/desktop/aa366749)         | An 8-bit unsigned character data item.                                                                                                                              |
| [**double**](https://msdn.microsoft.com/library/windows/desktop/aa366806)         | A 64-bit floating-point number.                                                                                                                                     |
| [**float**](https://msdn.microsoft.com/library/windows/desktop/aa366833)           | A 32-bit floating-point number.                                                                                                                                     |
| [**handle\_t**](https://msdn.microsoft.com/library/windows/desktop/aa366849)    | A primitive handle that can be used for RPC binding or data serializing.                                                                                            |
| [**hyper**](https://msdn.microsoft.com/library/windows/desktop/aa367039)           | A 64-bit integer that can be declared as either [**signed**](https://msdn.microsoft.com/library/windows/desktop/aa367162) or [**unsigned**](https://msdn.microsoft.com/library/windows/desktop/aa367295) Can also be referred to as **\_int64**.                  |
| [**int**](https://msdn.microsoft.com/library/windows/desktop/aa367053)               | A 32-bit integer that can be declared as either **signed** or **unsigned**.                                                                                         |
| [**\_\_int3264**](https://msdn.microsoft.com/library/windows/desktop/aa367390) | A keyword that specifies an integral type that has either 32-bit or 64-bit properties.                                                                              |
| [**long**](https://msdn.microsoft.com/library/windows/desktop/aa367072)             | A modifier for **int** that indicates a 32-bit integer. Can be declared as either **signed** or **unsigned**.                                                       |
| [**short**](https://msdn.microsoft.com/library/windows/desktop/aa367161)           | A 16-bit integer that can be declared as either **signed** or **unsigned**.                                                                                         |
| [**small**](https://msdn.microsoft.com/library/windows/desktop/aa367165)           | A modifier for **int** that indicates an 8-bit integer. Can be declared as either **signed** or **unsigned**.                                                       |
| [**wchar\_t**](https://msdn.microsoft.com/library/windows/desktop/aa367308)      | Wide-character type that is supported as a Microsoft extension to IDL. Therefore, this type is not available if you compile using the [/**osf**](https://msdn.microsoft.com/library/windows/desktop/aa367357) switch. |



 

The header file Rpcndr.h provides definitions for most of these base data types. The keyword **int** is recognized and is transmittable on 32-bit platforms. On 16-bit platforms, the **int** data type requires a modifier, such as **short** or **long**, to specify its length.

Although **void \* \*** is recognized as a generic pointer type by the ANSI C standard, MIDL restricts its usage. Each pointer used in a remote or serializing operation must point to either base types or types constructed from base types. (There is an exception: context handles are defined as **void** types. For more information see [Context Handles](context-handles.md).)

 

 




