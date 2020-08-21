---
title: Correlation Descriptors
description: A correlation descriptor is a format string that describes an expression based on one argument related to another argument.
ms.assetid: 9f5f5077-d6a9-4253-bddf-b8cd0c868973
ms.topic: article
ms.date: 05/31/2018
---

# Correlation Descriptors

A correlation descriptor is a format string that describes an expression based on one argument related to another argument. A correlation descriptor is needed for handling semantics related to attributes like \[**size\_is()**\], \[**length\_is()**\], \[**switch\_is()**\] and \[**iid\_is()**\]. Correlation descriptors are used with arrays, sized pointers, unions, and interface pointers. The eventual expression value can be a size, a length, a union discriminant, or a pointer to an IID, respectively. In terms of format strings, correlation descriptors are used with arrays, unions, and interface pointers. A sized pointer is described in format strings as a pointer to an array.

There are two routines performing basic expression calculations: NdrpComputeConformance is used for sizes, switches and IID\* while NdrpComputeVariance is used for lengths. There is also a single routine to perform a correlation value validation for denial-of-attack functionality.

Correlation descriptors have been designed to support only very limited expressions. For complicated situations, the compiler generates an expression evaluation routine to be called by the engine when needed.

A correlation descriptor has the following format:

``` syntax
correlation_type<1>
correlation_operator<1>
offset<2>
[robust_flags<2>]
```

The correlation descriptor correlation\_type<1> consists of two nibbles: the upper 4 bits describe where the expression can be found and the lower 4 bits describe the type of the expression value.

The upper nibble can have one of these five values:

``` syntax
00  FC_NORMAL_CONFORMANCE
10  FC_POINTER_CONFORMANCE
20  FC_TOP_LEVEL_CONFORMANCE
80  FC_TOP_LEVEL_MULTID_CONFORMANCE
40  FC_CONSTANT_CONFORMANCE
```

<dl> <dt>

<span id="FC_NORMAL_CONFORMANCE"></span><span id="fc_normal_conformance"></span>FC\_NORMAL\_CONFORMANCE
</dt> <dd>

A normal case of conformance, such as that described in a field of a structure.

</dd> <dt>

<span id="FC_POINTER_CONFORMANCE"></span><span id="fc_pointer_conformance"></span>FC\_POINTER\_CONFORMANCE
</dt> <dd>

For attributed pointers (**size\_is()**, **length\_is()**) which are fields in a structure. This affects the way the base memory pointer is set.

</dd> <dt>

<span id="FC_TOP_LEVEL_CONFORMANCE"></span><span id="fc_top_level_conformance"></span>FC\_TOP\_LEVEL\_CONFORMANCE
</dt> <dd>

For top-level conformance described by another parameter.

</dd> <dt>

<span id="FC_TOP_LEVEL_MULTID_CONFORMANCE"></span><span id="fc_top_level_multid_conformance"></span>FC\_TOP\_LEVEL\_MULTID\_CONFORMANCE
</dt> <dd>

For top-level conformance of a multidimensional array described by another parameter.

> [!Note]  
> Multidimensional sized arrays and pointers trigger a switch to [**–Oicf**](/windows/desktop/Midl/-oi).

 

</dd> <dt>

<span id="FC_CONSTANT_CONFORMANCE"></span><span id="fc_constant_conformance"></span>FC\_CONSTANT\_CONFORMANCE
</dt> <dd>

For a constant value. The compiler precalculates the value from a constant expression supplied by the user. When this is the case, the subsequent 3 bytes in the conformance description contain the lower 3 bytes of a long describing the conformance size. No further computation is required.

</dd> </dl>

The lower nibble gives the type of the value that needs to be extracted from memory:

``` syntax
FC_LONG | FC_ULONG | 
FC_SHORT | FC_USHORT | 
FC_SMALL | FC_USMALL | 
FC_HYPER
```

> [!Note]
> 64-bit expressions are not supported. FC\_HYPER is used only for **iid\_is()** on 64-bit platforms to extract the pointer value for IID\*.
>
> The compiler sets the type nibble to zero for the following cases: constant expression mentioned above and when evaluation expression routine needs to be called, for example, when FC\_CONSTANT\_CONFORMANCE and FC\_CALLBACK are used.

 

The size\_is\_op<1> field allows for one of the following operations to be applied to the conformance variable:

``` syntax
FC_DEREFERENCE | 
FC_DIV_2 | FC_MULT_2 | FC_SUB_1 | FC_ADD_1 | 
FC_CALLBACK
```

The FC\_DEREFERENCE constant is used for correlation being a pointee, like for **\[size\_is(\*pL)\]**. Arithmetic operators just use the indicated constant. The FC\_CALLBACK constant indicates that an expression evaluation routine needs to be called.

The offset<2> field is typically a relative memory offset to the expression argument variable. It can also be an expression evaluation–routine index. As mentioned previously in this document, for constant expressions it is a part of actual, final expression value.

The interpretation of the offset<2> field as memory offset depends on the complexity of the expression, the location of the expression variable, and in the case of an array, whether the array is actually an attributed pointer.

If the array is an attributed pointer and the conformance variable is a field in a structure, the offset field contains the offset from the beginning of the structure to the conformance-describing field. If the array is not an attributed pointer and the conformance variable is a field in a structure, the offset field contains the offset from the end of the nonconformant part of the structure to the conformance-describing field. Typically, the conformant array is at the end of the structure.

For top-level conformance, the offset field contains the offset from the stub's first parameter's location on the stack to the parameter that describes the conformance. This is not used in **–Os** mode. There are other exceptions to the interpretation of the offset field; such exceptions are described in the description of those types.

When offset<2> is used with FC\_CALLBACK, it contains an index in the expression evaluation routine table generated by the compiler. The stub message is passed to the evaluation routine, which then computes the conformance value and assigns it to the MaxCount field of the stub message.

The robust\_flags<2> field has been added for Windows 2000 to support [**/robust**](/windows/desktop/Midl/-robust), such as the denial-of-attacks feature. The following flags are defined on the first byte:

``` syntax
typedef  struct  _NDR_CORRELATION_FLAGS
  {
  unsigned char   Early     : 1;
  unsigned char   Split     : 1;
  unsigned char   IsIidIs   : 1;
  unsigned char   DontCheck : 1;
  unsigned char   Unused    : 4;
  } NDR_CORRELATION_FLAGS;
```

The Early flag indicates early versus late correlation. An early correlation is when the expression argument precedes the described argument, for example a size argument is before a sized pointer argument. A late correlation is when the expression argument comes after the related argument. The engine performs validation of early correlation values right away, the late correlation values are stored for checking after unmarshaling is done.

The Split flag indicates an async split among \[in\] and \[out\] arguments. For example, a size argument may be \[in\] while the sized pointer may be \[out\]. In the DCOM async context, these arguments happen to be on different stacks, so the engine must be aware of this.

The IsIidIs flag indicates an **iid\_is()** correlation. The NdrComputeConformance routine is tricked to obtain a pointer to IID as an expression value, but the validation routine cannot compare such values (they would be pointers) and so the flag indicates that actual IIDs need to be compared.

### Variance Description and Other Array Attributes

The variance description field format is identical to the conformance description field. The difference is that a different stub message field is used by the NDR engine as a temporary variable. In the case of variance description, it is the length that is evaluated and the corresponding field is called ActualLength.

With variance, the starting offset is typically zero and the engine is tuned accordingly. If the **first\_is()** attribute is applied to a conformant varying array, a callback to an expression evaluation routine is forced.

 

 