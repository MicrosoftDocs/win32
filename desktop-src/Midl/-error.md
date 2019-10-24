---
title: /error switch
description: The /error switch determines the types of error checking that the generated stubs will perform at run time.
ms.assetid: abd3616a-2d2c-4a7d-bf3a-c84a43387894
keywords:
- /error switch MIDL
topic_type:
- apiref
api_name:
- /error
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# /error switch

The **/error** switch determines the types of error checking that the generated stubs will perform at run time.

> [!Note]  
> This feature is obsolete and no longer supported. The use of the [**/robust**](-robust.md) switch is recommended.

 

``` syntax
midl /error { allocation | stub_data | ref | bounds_check | none | all }
```

## Switch Options

<dl> <dt>

 
</dt> <dd>

<dt>

<span id="allocation"></span><span id="ALLOCATION"></span>

<span id="allocation"></span><span id="ALLOCATION"></span>****allocation****


</dt> <dd>

Checks whether [**midl\_user\_allocate**](midl-user-allocate-1.md) returns a **NULL** value, indicating an out-of-memory error.

</dd> <dt>

<span id="stub_data"></span><span id="STUB_DATA"></span>

<span id="stub_data"></span><span id="STUB_DATA"></span>****stub\_data****


</dt> <dd>

Generates a stub that catches unmarshaling exceptions on the server side and propagates them back to the client.

</dd> <dt>

<span id="ref"></span><span id="REF"></span>

<span id="ref"></span><span id="REF"></span>****ref****


</dt> <dd>

Generates code that runs a check at run time to ensure that no **NULL** reference pointers are being passed to the client stubs and raises an RPC\_X\_NULL\_REF\_POINTER exception if it finds any.

</dd> <dt>

<span id="bounds_check"></span><span id="BOUNDS_CHECK"></span>

<span id="bounds_check"></span><span id="BOUNDS_CHECK"></span>****bounds\_check****


</dt> <dd>

Checks size of conformant-varying and varying arrays against transmission length specification.

</dd> <dt>

<span id="none"></span><span id="NONE"></span>

<span id="none"></span><span id="NONE"></span>****none****


</dt> <dd>

Performs no error checking.

</dd> <dt>

<span id="all"></span><span id="ALL"></span>

<span id="all"></span><span id="ALL"></span>****all****


</dt> <dd>

Performs all error checking. Effective with MIDL version 5.0, this is a default compiler switch.

</dd> </dl> </dd> </dl>

## Remarks

The **/error** switch selects the number of error checks that the generated stub files will perform. Effective with MIDL version 5.0, the default setting is **/error all**.

The enum errors that are checked (by default in all versions of MIDL) are truncation errors caused when converting between **long enum** types (32-bit integers) and **short enum** types (the network-data representation of [**enum**](enum.md)), and the number of identifiers in an enumeration exceeding 32,767.

The memory-access error checking (also by default in all versions of MIDL) is for pointers that exceed the end of the buffer in marshaling code and for conformant arrays whose size is less than zero. Use the **/error bounds\_check** flag to check for other invalid array bounds.

When you specify **/error allocation**, the stubs include code that raises an exception when [**midl\_user\_allocate**](midl-user-allocate-1.md) returns 0.

The **/error stub\_data** option prevents client data from crashing the server during unmarshaling, effectively providing a more robust method of handling the unmarshaling operation.

Effective with WindowsÂ 2000, the underlying run-time NDR marshaling engine performs most of these checks. This means that if you are using one of the fully-interpreted modes ([**/Oi**](-oi.md), **/Oif**) of stub generation, choosing different error checking options will not have a marked effect on performance.

## Examples

**midl /error allocation filename.idl**

**midl /error none filename.idl**

## See also

<dl> <dt>

[General MIDL Command-line Syntax](general-midl-command-line-syntax.md)
</dt> <dt>

[**/robust**](-robust.md)
</dt> </dl>

 

 




