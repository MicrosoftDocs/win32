---
title: size_is attribute
description: Use the \ size\_is\ attribute to specify the size of memory, in elements, allocated for sized pointers, sized pointers to sized pointers, and single- or multidimensional arrays.
ms.assetid: 1f3f3629-f668-460d-86fd-16ef22449973
keywords:
- size_is attribute MIDL
topic_type:
- apiref
api_name:
- size_is
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# size\_is attribute

Use the \[**size\_is**\] attribute to specify the size of memory, in elements, allocated for sized pointers, sized pointers to sized pointers, and single- or multidimensional arrays.

``` syntax
[ size_is(limited-expression-list) ]
```

## Parameters

<dl> <dt>

*limited-expression-list* 
</dt> <dd>

Specifies one or more C-language expressions. Each expression evaluates to a non-negative integer that represents the amount of memory allocated to a sized pointer or an array. In the case of an array, specifies a single expression that represents the allocation size, in elements, of the first dimension of that array. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow increment and decrement operators. Use commas as placeholders for implicit parameters, or to separate multiple expressions.

</dd> </dl>

## Remarks

If you are using the \[**size\_is**\] attribute to allocate memory for a multidimensional array and you are using array \[ \] notation, keep in mind that only the first dimension of a multidimensional array can be dynamically determined at run time. The other dimensions must be statically specified. For more information on using the \[**size\_is**\] attribute with multiple levels of pointers to enable a server to return a dynamically-sized array of data to a client, as shown in the example Proc7, see [Multiple Levels of Pointers](/windows/desktop/Rpc/multiple-levels-of-pointers).

You can use either \[**size\_is**\] or [**max\_is**](max-is.md) (but not both in the same attribute list) to specify the size of an array whose upper bounds are determined at run time. Note, however, that the \[**size\_is**\] attribute cannot be used on array dimensions that are fixed. The \[**max\_is**\] attribute specifies the maximum valid array index. As a result, specifying \[size\_is(n)\] is equivalent to specifying \[max\_is(n-1)\].

An \[ [**in**](in.md)\] or \[in, [**out**](out-idl.md)\] conformant-array parameter with the \[ [**string**](string.md)\] attribute need not have the \[**size\_is**\] or \[[**max\_is**](max-is.md)\] attribute. In this case, the size of the allocation is determined from the NULL terminator of the input string. All other conformant arrays with the \[string\] attribute must have a \[**size\_is**\] or \[**max\_is**\] attribute.

While it is legal to use the \[**size\_is**\] attribute with a constant, doing so is inefficient and unnecessary. For example, use a fixed size array:

``` syntax
HRESULT Proc3([in] short Arr[MAX_SIZE]);
```

instead of:

``` syntax
// legal but marshaling code is much slower
HRESULT Proc3([in size_is(MAX_SIZE)] short Arr[] );
```

You can use the \[**size\_is**\] and \[[**length\_is**](length-is.md)\] attributes together. When you do, the \[**size\_is**\] attribute controls the amount of memory allocated for the data. The \[**length\_is**\] attribute specifies how many elements are transmitted. The amount of memory specified by the \[**size\_is**\] and \[**length\_is**\] attributes need not be the same. For instance, your client may pass an \[in,out\] parameter to a server and specify a large memory allocation with \[**size\_is**\], even though it specifies a small number of data elements to be passed with \[**length\_is**\]. This enables the server to fill the array with more data than it received, which it can then send back to the client.

In general, it isn't useful to specify both \[**size\_is**\] and \[[**length\_is**](length-is.md)\] on \[in\] or \[out\] parameters. In both cases, \[**size\_is**\] controls memory allocation. Your application could use \[**size\_is**\] to allocate more array elements than it transmits (as specified by \[**length\_is**\]). However, this would be inefficient. It would also be inefficient to specify identical values for \[**size\_is**\] and \[**length\_is**\]. It would create extra overhead during parameter marshaling. If the values of \[**size\_is**\] and \[**length\_is**\] are always the same, omit the \[**length\_is**\] attribute.

## Examples

``` syntax
HRESULT Proc1(
    [in] short m;
    [in, size_is(m)] short a[]);  // If m = 10, a[10]
HRESULT Proc2(
    [in] short m;
    [in, size_is(m)] short b[][20]);  // If m = 10, b[10][20]
HRESULT Proc3(
    [in] short m;
    [size_is(m)] short * pshort); /* Specifies a pointer
                                  to an m-sized block of shorts */
HRESULT Proc4(
    [in] short m;
    [size_is( , m)] short ** ppshort); /* Specifies a pointer 
                                       to a pointer to an m-sized 
                                       block of shorts */
HRESULT Proc5(
    [in] short m;
    [size_is(m ,)] short ** ppshort); /* Specifies an
                                      m-sized block of pointers 
                                      to shorts */
HRESULT Proc6(
    [in] short m;
    [in] short n;
    [size_is(m,n)] short ** ppshort); /* Specifies a pointer to an 
                                      m-sized block of pointers, each 
                                      of which points to an n-sized 
                                      block of shorts. m associates with
                                      the pointer closeest to the identifer
                                      it decorates. n associates with rest.*/
 HRESULT Proc7(
     [out] long  * pSize,
     [out, size_is( , *pSize)] my_type ** ppMyType); /* Specifies a pointer 
                                              to a sized pointer, 
                                              which points to a block 
                                              of my_types, whose size is
                                              unknown when the stub 
                                              calls the server. */
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[Field Attributes](/windows/desktop/Rpc/field-attributes)
</dt> <dt>

[**first\_is**](first-is.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**last\_is**](last-is.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**min\_is**](min-is.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**string**](string.md)
</dt> </dl>

 

 