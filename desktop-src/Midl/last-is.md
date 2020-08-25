---
title: last_is attribute
description: The field attribute \ last\_is\ specifies the index of the last array element to be transmitted. When the specified index is zero or negative, no array elements are transmitted.
ms.assetid: 42a5cb0d-0887-4aa7-b34f-2fbad0f4c8ab
keywords:
- last_is attribute MIDL
topic_type:
- apiref
api_name:
- last_is
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# last\_is attribute

The field attribute **\[last\_is\]** specifies the index of the last array element to be transmitted. When the specified index is zero or negative, no array elements are transmitted.

``` syntax
[last_is( limited-expression-list )]
```

## Parameters

<dl> <dt>

*limited-expression-list* 
</dt> <dd>

Specifies one or more C-language expressions. Each expression evaluates to an integer that represents the array index of the last array element to be transmitted. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow increment and decrement operators. Separate multiple expressions with commas.

</dd> </dl>

## Remarks

The **\[last\_is\]** attribute determines the value of the array index corresponding to the **\[**[**length\_is**](length-is.md)**\]** attribute when **\[length\_is\]** is not specified. The relationship between these array indexes is as follows: length = last - first + 1.

If the value of the array index specified by **\[**[**first\_is**](first-is.md)**\]** is larger than the value specified by **\[last\_is\]**, zero elements are transmitted.

The **\[last\_is\]** attribute cannot be used as a field attribute at the same time as the **\[**[**length\_is**](length-is.md)**\]** attribute or the **\[**[**string**](string.md)**\]** attribute.

Using a constant expression with the **\[last\_is\]** attribute is an inappropriate use of the attribute. It is legal, but inefficient, and will result in slower marshaling code.

When the value specified by **\[**[**max\_is**](max-is.md)**\]** is equal to or greater than zero, the following relationship must be true: 0 <= last\_is <= max\_is.

## Examples

``` syntax
proc1(
    [in] short Last,
    [in, last_is(Last)] short asNumbers[MAXSIZE]);
```

## See also

<dl> <dt>

[Field Attributes](/windows/desktop/Rpc/field-attributes)
</dt> <dt>

[**first\_is**](first-is.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> </dl>

 

 