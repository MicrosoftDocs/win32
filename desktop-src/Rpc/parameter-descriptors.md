---
title: Parameter Descriptors
description: As mentioned previously, \ 8211;Oi and \ 8211;Oif style parameter descriptors exist.
ms.assetid: c2dad284-abe5-4b38-b3a6-3c7373fc5b84
ms.topic: article
ms.date: 05/31/2018
---

# Parameter Descriptors

As mentioned previously, [**–Oi**](/windows/desktop/Midl/-oi) and **–Oif** style parameter descriptors exist.

## The –Oi Parameter Descriptors

Fully interpreted stubs require additional information for each of the parameters in an RPC call. The parameter descriptions of a procedure follow immediately after the description of the procedure.

[**Simple –Oi**](/windows/desktop/Midl/-oi)

**Parameter Descriptors**

The format for the description of an \[**in**\] or return simple type parameter is:

``` syntax
FC_IN_PARAM_BASETYPE 
simple_type<1>
```

–or–

``` syntax
FC_RETURN_PARAM_BASETYPE 
simple_type<1>
```

Where simple\_type<1> is the FC token indicating the simple type. The codes are as follows:

``` syntax
4e  FC_IN_PARAM_BASETYPE 
53  FC_RETURN_PARAM_BASETYPE
```

**Other –Oi**

**Parameter Descriptors**

The format for the description for all other parameter types is:

``` syntax
param_direction<1> 
stack_size<1> 
type_offset<2>
```

Where the param\_direction<1> field for each of these descriptions must be one of those shown in the following table.



| Hex | Flag                          | Meaning                                                     |
|-----|-------------------------------|-------------------------------------------------------------|
| 4d  | FC\_IN\_PARAM                 | An in parameter.                                            |
| 50  | FC\_IN\_OUT\_PARAM            | An in/out parameter.                                        |
| 51  | FC\_OUT\_PARAM                | An out parameter.                                           |
| 52  | FC\_RETURN\_PARAM             | A procedure return value.                                   |
| 4f  | FC\_IN\_PARAM\_NO\_FREE\_INST | An in xmit/rep as a parameter for which no freeing is made. |



 

The stack\_size<1> is the size of the parameter on the stack, expressed as the number of integers the parameter occupies on the stack.

> [!Note]  
> The [**–Oi**](/windows/desktop/Midl/-oi) mode is not supported on 64-bit platforms.

 

The type\_offset<2> field is the offset in the type format string table, indicating the type descriptor for the argument.

## The –Oif Parameter Descriptors

There are two possible formats for a parameter description, one for base types, another for all other types.

Base types:

``` syntax
PARAM_ATTRIBUTES<2> 
stack_offset<2> 
type_format_char<1> 
unused<1>
```

Other:

``` syntax
PARAM_ATTRIBUTES<2> 
stack_offset<2> 
type_offset<2>
```

In both stack\_offset<2> indicates the offset on the virtual argument stack, in bytes. For base types, the argument type is given directly by the format character corresponding to the type. For other types, the type\_offset<2> field gives the offset in the type format string table where the type descriptor for the argument is located.

The parameter attribute field is defined as follows:

``` syntax
typedef struct
  {
  unsigned short  MustSize            : 1;    // 0x0001
  unsigned short  MustFree            : 1;    // 0x0002
  unsigned short  IsPipe              : 1;    // 0x0004
  unsigned short  IsIn                : 1;    // 0x0008
  unsigned short  IsOut               : 1;    // 0x0010
  unsigned short  IsReturn            : 1;    // 0x0020
  unsigned short  IsBasetype          : 1;    // 0x0040
  unsigned short  IsByValue           : 1;    // 0x0080
  unsigned short  IsSimpleRef         : 1;    // 0x0100
  unsigned short  IsDontCallFreeInst  : 1;    // 0x0200
  unsigned short  SaveForAsyncFinish  : 1;    // 0x0400
  unsigned short  Unused              : 2;
  unsigned short  ServerAllocSize     : 3;    // 0xe000
  } PARAM_ATTRIBUTES, *PPARAM_ATTRIBUTES;
```

-   The **MustSize** bit is set only if the parameter must be sized.
-   The **MustFree** bit is set if the server must call the parameter's NdrFree\* routine.
-   The **IsSimpleRef** bit is set for a parameter that is a reference pointer to anything other than another pointer, and which has no allocate attributes. For such a type, the parameter description's type\_offset<> field, except for a reference pointer to a base type, provides the offset to the referent's type; the reference pointer is simply skipped.
-   The **IsDontCallFreeInst** bit is set for certain represent\_as parameters whose free instance routines should not be called.
-   The **ServerAllocSize** bits are nonzero if the parameter is \[**out**\], \[**in**\], or \[**in,out**\] pointer to pointer, or pointer to enum16, and will be initialized on the server interpreter's stack, rather than using a call to **I\_RpcAllocate**. If nonzero, this value is multiplied by 8 to get the number of bytes for the parameter. Note that doing so means at least 8 bytes are always allocated for a pointer.
-   The **IsBasetype** bit is set for simple types that are being marshaled by the main [**–Oif**](/windows/desktop/Midl/-oi) interpreter loop. In particular, a simple type with a range attribute on it is not flagged as a base type in order to force the range routine marshaling through dispatching using an FC\_RANGE token.
-   The **IsByValue** bit is set for compound types being sent by value, but is not set for simple types, regardless of whether the argument is a pointer. The compound types for which it is set are structures, unions, [**transmit\_as**](/windows/desktop/Midl/transmit-as), [**represent\_as**](/windows/desktop/Midl/represent-as), [**wire\_marshal**](/windows/desktop/Midl/wire-marshal) and SAFEARRAY. In general, the bit was introduced for the benefit of the main interpreter loop in the [**–Oicf**](/windows/desktop/Midl/-oi) interpreter, to ensure the nonsimple arguments (referred to as compound type arguments) are properly dereferenced. This bit was never used in previous versions of the interpreter.

 

 