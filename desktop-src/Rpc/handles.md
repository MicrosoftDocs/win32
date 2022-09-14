---
title: Handles
description: As many as two parts in the format string description of a procedure address handles.
ms.assetid: '11c6742c-b2f5-4201-8b1c-7e31ae52e0da'
ms.topic: article
ms.date: 05/31/2018
---

# Handles

As many as two parts in the format string description of a procedure address handles. The first part is the handle\_type<1> field of a procedure's description, used to indicate implicit handles. This part is always present. The second part is a parameter description of any explicit handle in the procedure. Both are explained in the following sections, along with a discussion of the additional MIDL compiler support of the Stub Descriptor structure for binding handle issues.

## Implicit Handles

If a procedure uses an implicit handle for binding, the handle\_type<1> field of the procedure's description contains one of three valid nonzero values. MIDL compiler support for implicit handles is found in the IMPLICIT\_HANDLE\_INFO field of the Stub Descriptor structure:

``` syntax
typedef  (__RPC_FAR * GENERIC_BINDING_ROUTINE)();

typedef struct 
  {
  GENERIC_BINDING_ROUTINE  pfnBind;
  GENERIC_BINDING_ROUTINE  pfnUnbind;
  } GENERIC_BINDING_ROUTINE_PAIR;
  
typedef struct __GENERIC_BINDING_INFO 
  {
  void __RPC_FAR*          pObj;
  unsigned char            Size;
  GENERIC_BINDING_ROUTINE  pfnBind;
  GENERIC_BINDING_ROUTINE    pfnUnbind;
  } GENERIC_BINDING_INFO,  *PGENERIC_BINDING_INFO;

union 
  {
  handle_t*                pAutoHandle;
  handle_t*                pPrimitiveHandle;
  PGENERIC_BINDING_INFO    pGenericBindingInfo;
  } IMPLICIT_HANDLE_INFO;
```

If the procedure uses an auto handle, the **pAutoHandle** member contains the address of the stub defined–auto handle variable.

If the procedure uses an implicit primitive handle, the **pPrimitiveHandle** member contains the address of the stub defined–primitive handle variable.

Finally, if the procedure uses an implicit generic handle, the **pGenericBindingInfo** member holds the address of the pointer to the corresponding **GENERIC\_BINDING\_INFO** structure. The data structure **MIDL\_STUB\_DESC** contains a pointer to a collection of **GENERIC\_BINDING\_PAIR** structures. The entry in the zero position of this collection is reserved for the **bind** and **unbind** routines corresponding to the generic binding handle referenced by **pGenericBindingInfo** in **IMPLICIT\_HANDLE\_INFO**. The type of implicit binding handle is indicated in the format string.

## Explicit Handles

There are three possible explicit handle types: context, generic, and primitive. In the case of an explicit handle (or an \[**out**\] only context handle, which is handled in the same way), the binding handle information appears as one of the procedure's parameters. The three possible descriptions are as follows.

Primitive

``` syntax
FC_BIND_PRIMITIVE, flag<1>, offset<2>.
```

The flag<1> indicates whether the handle is passed by a pointer.

The offset<2> provides the offset from the beginning of the stack to the primitive handle.

> [!Note]  
> A primitive handle description in the type format string is reduced to a single FC\_IGNORE.

 

Generic

``` syntax
FC_BIND_GENERIC, flag_and_size<1>, offset<2>, binding_routine_pair_index<1>, FC_PAD
```

The flag\_and \_size<1> has the upper flag nibble and the lower size nibble. The flag indicates whether the handle is passed by a pointer. The size field provides the size of the user defined–generic handle type. This size is limited to be 1, 2 or 4 bytes on 32-bit systems and 1, 2, 4 or 8 bytes on 64-bit systems.

The offset<2> field provides the offset from the beginning of the stack of the pointer to the data of the size given.

The binding\_routine\_pair\_index<1> field gives the index into the aGenericBindingRoutinePairs field of the Stub Descriptor to the **bind** and **unbind** routine function pointers for the generic handle.

> [!Note]  
> A generic handle description in the type format is the description of the related data type only.

 

Context

``` syntax
FC_BIND_CONTEXT flags<1> offset<2> context_rundown_routine_index<1> param_num<1>
```

The flags<1> indicate how the handle is passed and what type it is. Valid flags are shown in the following table.



| Hex | Flag                                   |
|-----|----------------------------------------|
| 80  | HANDLE\_PARAM\_IS\_VIA\_PTR            |
| 40  | HANDLE\_PARAM\_IS\_IN                  |
| 20  | HANDLE\_PARAM\_IS\_OUT                 |
| 21  | HANDLE\_PARAM\_IS\_RETURN              |
| 08  | NDR\_STRICT\_CONTEXT\_HANDLE           |
| 04  | NDR\_CONTEXT\_HANDLE\_NO\_SERIALIZE    |
| 02  | NDR\_CONTEXT\_HANDLE\_SERIALIZE        |
| 01  | NDR\_CONTEXT\_HANDLE\_CANNOT\_BE\_NULL |



 

The first four flags have always been present, the last four were added in Windows 2000.

The offset<2> field provides the offset from the start of the stack to the context handle.

The context\_rundown\_routine\_index<1> provides an index into the **apfnNdrRundownRoutines** field of the Stub Descriptor to the rundown routine used for this context handle. The compiler always generates an index. For routines that do not have a rundown routine, this is an index to a table position that holds null.

For stubs built in **–Oi2**, the param\_num<1> provides the ordinal count, starting at zero, specifying which context handle it is in the given procedure.

For previous versions of the interpreter, the param\_num<1> provides the context handle's parameter number, starting at zero, in its procedure.

> [!Note]  
> A context handle description in the type format string will not have the offset<2> in the description.

 

## The New –Oif Header

As mentioned previously, the [**–Oif**](/windows/desktop/Midl/-oi) header expands on the **–Oi** header. For convenience, all fields are shown here:

(The old header)

``` syntax
handle_type<1> 
Oi_flags<1>
[rpc_flags<4>]
proc_num<2>  
stack_size<2>
[explicit_handle_description<>]
```

(The [**–Oif**](/windows/desktop/Midl/-oi) extensions)

``` syntax
constant_client_buffer_size<2>
constant_server_buffer_size<2>
INTERPRETER_OPT_FLAGS<1>
number_of_params<1>
```

The constant\_client\_buffer\_size<2> provides the size of the marshaling buffer that could have been pre-computed by the compiler. This may be only a partial size, as the ClientMustSize flag triggers the sizing.

The constant\_server\_buffer\_size<2> provides the size of the marshaling buffer as precomputed by the compiler. This may be only a partial size, as the ServerMustSize flag triggers the sizing.

The INTERPRETER\_OPT\_FLAGS are defined in Ndrtypes.h:

``` syntax
typedef struct
  {
  unsigned char   ServerMustSize      : 1;    // 0x01
  unsigned char   ClientMustSize      : 1;    // 0x02
  unsigned char   HasReturn           : 1;    // 0x04
  unsigned char   HasPipes            : 1;    // 0x08
  unsigned char   Unused              : 1;
  unsigned char   HasAsyncUuid        : 1;    // 0x20
  unsigned char   HasExtensions       : 1;    // 0x40
  unsigned char   HasAsyncHandle      : 1;    // 0x80
  } INTERPRETER_OPT_FLAGS, *PINTERPRETER_OPT_FLAGS;
```

-   The ServerMustSize bit is set if the server needs to perform a buffer sizing pass.
-   The ClientMustSize bit is set if the client needs to perform a buffer sizing pass.
-   The HasReturn bit is set if the procedure has a return value.
-   The HasPipes bit is set if the pipe package needs to be used to support a pipe argument.
-   The HasAsyncUuid bit is set if the procedure is an asynchronous DCOM procedure.
-   The HasExtensions bit indicates that Windows 2000 and later extensions are used.
-   The HasAsyncHandle bit indicates an asynchronous RPC procedure.

The HasAsyncHandle bit has been initially used for a different DCOM implementation of async support, and hence could not be used for the current style async support in DCOM. The HasAsyncUuid bit currently indicates this.

 

 