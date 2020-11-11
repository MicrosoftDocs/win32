---
title: length_is attribute
description: The \ length\_is\ attribute specifies the number of array elements to be transmitted. You must specify a non-negative value.
ms.assetid: 060dbd4a-3078-4050-abfe-c1b633c06861
keywords:
- length_is attribute MIDL
topic_type:
- apiref
api_name:
- length_is
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# length\_is attribute

The **\[length\_is\]** attribute specifies the number of array elements to be transmitted. You must specify a non-negative value.

``` syntax
[length_is( limited-expression-list )]
```

## Parameters

<dl> <dt>

*limited-expression-list* 
</dt> <dd>

Specifies one or more C-language expressions. Each expression evaluates to an integer that represents the number of array elements to be transmitted. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow increment and decrement operators. Separate multiple expressions with commas.

</dd> </dl>

## Remarks

The **\[length\_is\]** attribute determines the value of the array indexes corresponding to the **\[**[**last\_is**](last-is.md)**\]** attribute when **\[last\_is\]** is not specified. The relationship between these array indexes is as follows: length = last - first + 1.

The **\[length\_is\]** attribute cannot be used at the same time as the **\[**[**last\_is**](last-is.md)**\]** attribute or the **\[**[**string**](string.md)**\]** attribute.

To define a counted string with a **\[length\_is\]** or **\[**[**last\_is**](last-is.md)**\]** attribute, use a character array or pointer without the **\[**[**string**](string.md)**\]** attribute.

Using a constant expression with the **\[length\_is\]** attribute is an inappropriate use of the attribute. It is legal, but inefficient, and will result in slower marshaling code.

You can use the **\[**[**size\_is**](size-is.md)**\]** and **\[length\_is\]** attributes together. When you do, the **\[size\_is\]** attribute controls the amount of memory allocated for the data. The **\[length\_is\]** attribute specifies how many elements are transmitted. The amount of memory specified by the **\[size\_is\]** and **\[length\_is\]** attributes need not be the same. For instance, your client may pass an **\[in**, **out\]** parameter to a server and specify a large memory allocation with **\[size\_is\]**, even though it specifies a small number of data elements to be passed with **\[length\_is\]**. This enables the server to fill the array with more data than it received, which it can then send back to the client.

In general, it isn't useful to specify both **\[**[**size\_is**](size-is.md)**\]** and **\[length\_is\]** on **\[**[**in**](in.md)**\]** or **\[**[**out**](out-idl.md)**\]** parameters. In both cases, **\[size\_is\]** controls memory allocation. Your application could use **\[size\_is\]** to allocate more array elements than it transmits (as specified by **\[length\_is\]**). However, this would be inefficient. It would also be inefficient to specify identical values for **\[size\_is\]** and **\[length\_is\]**. Because it would create extra overhead during parameter marshaling. When the values of **\[size\_is\]** and **\[length\_is\]** are always the same, omit the **\[length\_is\]** attribute.

## Examples

``` syntax
/* counted string holding at most "size" characters */ 
typedef struct 
{ 
    unsigned short size; 
    unsigned short length; 
    [size_is(size), length_is(length)] char string[*]; 
 } COUNTED_STRING_TYPE; 
 
/* counted string holding at most 80 characters */ 
typedef struct 
{ 
    unsigned short length; 
    [length_is(length)] char string[80]; 
} STATIC_COUNTED_STRING_TYPE; 
 
HRESULT Proc1(
    [in] short iLength; 
    [in, length_is(iLength)] short asNumbers[10]);
```

## See also

<dl> <dt>

[Field Attributes](/windows/desktop/Rpc/field-attributes)
</dt> <dt>

[**first\_is**](first-is.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**last\_is**](last-is.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**min\_is**](min-is.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> <dt>

[**string**](string.md)
</dt> </dl>

 

 