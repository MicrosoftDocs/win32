---
title: first_is attribute
description: The \ first\_is\ attribute specifies the index of the first array element to be transmitted.
ms.assetid: 1de7821c-19e7-4b2c-98fc-2fae3563831c
keywords:
- first_is attribute MIDL
topic_type:
- apiref
api_name:
- first_is
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# first\_is attribute

The \[**first\_is**\] attribute specifies the index of the first array element to be transmitted.

``` syntax
first_is(limited-expression-list)
```

## Parameters

<dl> <dt>

*limited-expression-list* 
</dt> <dd>

Specifies one or more C-language expressions. Each expression evaluates to an integer that represents the array index of the first array element to be transmitted. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow increment and decrement operators. Separate multiple expressions with commas.

</dd> </dl>

## Remarks

If the **\[first\_is\]** attribute is not present, or if the specified index is a negative number, array element zero is the first element transmitted.

The **\[first\_is\]** attribute can also help determine the values of the array indexes corresponding to the **\[**[**last\_is**](last-is.md)**\]** or **\[**[**length\_is**](length-is.md)**\]** attribute when these attributes are not specified. The relationship between these array indexes is:

``` syntax
length = last - first + 1
```

The following relationship must also hold:

``` syntax
0 <= first_is <= max_is
```

The following relationship must hold when **\[**[**max\_is**](max-is.md)**\] <= 0:**

``` syntax
first_is == 0
```

The **\[first\_is\]** attribute cannot be used at the same time as the **\[**[**string**](string.md)**\]** attribute.

Using a constant expression with the **\[first\_is\]** attribute is an inappropriate use of the attribute. It is legal, but inefficient, and will result in slower marshaling code.

## Examples

``` syntax
HRESULT Proc1(
    [in] short First,
    [first_is(First)] Arr[10]);
```

## See also

<dl> <dt>

[field\_attributes](/windows/desktop/Rpc/field-attributes)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**last\_is**](last-is.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**min\_is**](min-is.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> <dt>

[**string**](string.md)
</dt> </dl>

 

 