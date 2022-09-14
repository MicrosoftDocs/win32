---
title: max_is attribute
description: The \ max\_is\ attribute designates the maximum value for a valid array index.
ms.assetid: 8d09f610-cae6-45f6-815c-5ba916d8a5e7
keywords:
- max_is attribute MIDL
topic_type:
- apiref
api_name:
- max_is
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# max\_is attribute

The **\[max\_is\]** attribute designates the maximum value for a valid array index.

``` syntax
[max_is(limited-expression-list )]
```

## Parameters

<dl> <dt>

*limited-expression-list* 
</dt> <dd>

Specifies one or more C-language expressions. Each expression evaluates to an integer that represents the highest valid array index. The MIDL compiler supports conditional expressions, logical expressions, relational expressions, and arithmetic expressions. MIDL does not allow function invocations in expressions and does not allow increment and decrement operators. Separate multiple expressions with commas.

</dd> </dl>

## Remarks

The **\[max\_is\]** attribute does not necessarily correspond to the number of elements in the array. For an array of size *n* in C, where the first array element is element number zero, the maximum value for a valid array index is *n*–1.

The **\[max\_is\]** attribute cannot be used as a field attribute at the same time as the **\[**[**size\_is**](size-is.md)**\]** attribute.

While it is legal to use the **\[max\_is\]** attribute with a constant expression, doing so is inefficient and unnecessary. For example, use a fixed size array:

``` syntax
/* transmits values of a[0]... a[MAX_SIZE-1] */ 
HRESULT Proc3([in] short Arr[MAX_SIZE]); 
```

instead of:

``` syntax
/* legal but marshaling code is much slower */ 
HRESULT Proc3([in max_is(MAX_SIZE-1)] short Arr[] );
```

## Examples

``` syntax
/* if m = 10, there are 11 transmitted elements (a[0]...a[10])*/ 
HRESULT Proc1( 
    [in] short m, 
    [in, max_is(m)] short a[]);  
 
/* if m = 10, the valid range for b is b[0...10][20] */ 
HRESULT Proc2( 
    [in] short m, 
    [in, max_is(m)] short b[][20];
```

## See also

<dl> <dt>

[Field Attributes](/windows/desktop/Rpc/field-attributes)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**min\_is**](min-is.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> </dl>

 

 