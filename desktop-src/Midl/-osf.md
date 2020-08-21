---
title: /osf switch
description: The /osf switch forces strict compatibility with OSF DCE.
ms.assetid: d94228fa-24af-43d7-9596-cf3a14690e0b
keywords:
- /osf switch MIDL
topic_type:
- apiref
api_name:
- /osf
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /osf switch

The **/osf** switch forces strict compatibility with OSF DCE.

``` syntax
midl /osf
```

## Switch Options

This switch has no parameters.

## Remarks

Use this switch if your application requires strict compatibility with OSF DCE for portability reasons.

In **/osf** mode, the RpcSs package is automatically enabled when you use full pointers, the arguments require memory allocation, or when you use the [**enable\_allocate**](enable-allocate.md) attribute. This means that you do not have to supply the [**midl\_user\_allocate**](/windows/desktop/Rpc/the-midl-user-allocate-function) and [**midl\_user\_free**](/windows/desktop/Rpc/the-midl-user-free-function) functions in your client and server application.

The following Microsoft-extended features are not available when you compile with the **/osf** switch:

-   Abstract declarators (unnamed parameters) in the IDL file.
-   Interface definitions for COM objects.
-   Interface names with more than 17 characters.
-   MIDL-only attributes, such as [**wire\_marshal**](wire-marshal.md), [**user\_marshal**](user-marshal.md), and the typelib (ODL)extensions.
-   Using ACF keywords in an IDL file (the MIDL **/app\_config** option).
-   Static callback functions on the client.
-   The [**async**](async.md) attribute.
-   [**cpp\_quote**](cpp-quote.md) and **\#pragma midl\_echo**.
-   [**wchar\_t**](wchar-t.md) wide-character types, constants, and strings.
-   [**enum**](enum.md) initialization (sparse enumerators).
-   [**out**](out-idl.md)-only size specification.
-   Mixed sized-pointers and sized arrays.
-   Expressions used for size and discriminator specifiers.
-   Explicit handle parameters in any position in the argument list. In **/osf** mode, the MIDL compiler looks for an explicit binding handle as the first parameter. When the first parameter is not a binding handle and one or more context handles are specified, the leftmost context handle is used as the binding handle. When the first parameter is not a handle and there are no context handles, the procedure uses implicit binding using the ACF attribute [**implicit\_handle**](implicit-handle.md) or [**auto\_handle**](auto-handle.md).
-   Pointer-attribute type inheritance. OSF DCE does not allow unattributed pointers. Therefore, in **/osf** mode each IDL file must define attributes for its pointers. If any pointer does not have an explicit attribute, the IDL file must have a [**pointer\_default**](pointer-default.md) specification to set the pointer type.
-   Multiple interfaces in an IDL file.
-   Definitions outside of the interface block.
-   Type qualifiers such as **far** and **stdcall**.
-   Omitting directional attributes.

The following C/C++ language extensions are not available when you compile with the **/osf** switch:

-   Bit fields in structures and unions.
-   Single line comments delimited with two slash characters (//).
-   External declarations.
-   Procedures with ellipses in the parameter list.
-   Type [**int**](int.md).
-   Type **void \*** (except with the [**context\_handle**](context-handle.md) attribute).
-   Type qualifiers, including the form with the ANSI-conformant prefix, contain two underscore characters: **\_\_cdecl**, **cdecl**, [**const**](const.md), **const**, **\_\_export**, **export**, **\_\_far**, **far**, **\_\_loadds**, **loadds**, **\_\_near**, **near**, **\_\_pascal**, **pascal**, **\_\_stdcall**, **stdcall**, **\_\_volatile**, and **volatile**.
-   Any \# [**pragma**](pragma.md) warning or **\#pragma** comment.
-   Type serialization.
-   The [**\_\_int3264**](--int3264.md) data type.
-   The [**/protocol**](-protocol.md) switch, and ndr64 transfer syntax.

## Examples

**midl /osf filename.idl**

**midl /osf /app\_config filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/app\_config**](-app-config.md)
</dt> <dt>

[**/ms\_ext**](-ms-ext.md)
</dt> <dt>

[Rpcss Memory Management Package](/windows/desktop/Rpc/rpcss-memory-management-package)
</dt> </dl>

 

 