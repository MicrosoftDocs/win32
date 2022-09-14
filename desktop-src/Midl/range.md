---
title: range attribute
description: The \ range\ attribute lets you specify a range of allowable values for arguments or fields whose values are set at run time. When used with a pipe type, the attribute specifies the allowable range for the count of elements in the pipe chunks.
ms.assetid: 1609fea5-e82c-4389-b4f4-2cd8d0622cde
keywords:
- range attribute MIDL
topic_type:
- apiref
api_name:
- range
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# range attribute

The **\[range\]** attribute lets you specify a range of allowable values for arguments or fields whose values are set at run time. When used with a pipe type, the attribute specifies the allowable range for the count of elements in the pipe chunks.

``` syntax
[range(low-val,high-val)] type-specifier declarator
```

## Parameters

<dl> <dt>

*low-val* 
</dt> <dd>

The lowest allowable value that the parameter or field can hold.

</dd> <dt>

*high-val* 
</dt> <dd>

The highest allowable value that the parameter or field can hold.

</dd> <dt>

*type-specifier* 
</dt> <dd>

An integral type other than [**hyper**](hyper.md) or [**\_\_int64**](--int64.md), a type identifier to an integral type, an [**enum**](enum.md) type, or a pipe type name.

</dd> <dt>

*declarator* 
</dt> <dd>

A standard C declarator, such as an identifier.

</dd> </dl>

## Remarks

Use the **\[range\]** attribute to modify the meaning of sensitive parameters or fields, such as those used for size or length, with conformant or varying arrays; or whenever you want to check a parameter or field value against a range of valid values. The attribute is applicable to top-level parameters as well as lower-level parameters and fields. Adding the **\[range\]** attribute to a type does not change its wire format, thus does not affect backward compatibility.

The **\[range\]** attribute can also be used on conformant data such as buffers or arrays with a conformance attribute. The effect is to limit all conformance sizes for the conformant data to the specified range. If the conformant data is a multi-dimensional array, each array dimension is limited to the specified range.

Use of **\[range\]** on conformant data requires that the compilation target be â€“target NT60 or higher.

Note that you must use the [**/robust**](-robust.md) compiler option when you compile your IDL file in order to generate the stub code that will perform these checks. Without the **/robust** switch, the MIDL compiler ignores this attribute.

## Examples

``` syntax
HRESULT Method1(
    [in, range(0,100)] ULONG m,
    [in, range(0,100)] ULONG n,
    [size_is(m,n)] ULONG **pplong);

void InPipe(
    [in, range(0, MAX_CHUNK) LONG_PIPE pipe_date);
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[arrays](/windows/desktop/Rpc/arrays)
</dt> <dt>

[**first\_is**](first-is.md)
</dt> <dt>

[**last\_is**](last-is.md)
</dt> <dt>

[**length\_is**](length-is.md)
</dt> <dt>

[**max\_is**](max-is.md)
</dt> <dt>

[**/robust**](-robust.md)
</dt> <dt>

[**size\_is**](size-is.md)
</dt> <dt>

[**switch\_is**](switch-is.md)
</dt> </dl>

 

 