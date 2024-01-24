---
title: declare_guid keyword
description: The declare\_guid keyword instructs MIDL to emit a GUID variable into the generated header file.
keywords:
- declare_guid keyword MIDL
topic_type:
- apiref
api_name:
- declare_guid
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# declare\_guid keyword

The **declare\_guid** keyword instructs MIDL to emit a GUID variable into the generated header file.

``` syntax
declare_guid(variable-name, guid)
```

## Parameters

<dl> <dt>

*variable-name* 
</dt> <dd>

Specifies a variable name for the identifier in the generated header file.

</dd> <dt>

*guid*
</dt> <dd>

Specifies the [GUID](/windows/win32/api/guiddef/ns-guiddef-guid) that will apply to the variable name in the generated header file.

</dd> </dl>

## Examples

``` syntax
declare_guid(SID_Widget, 5144C348-169E-4359-A79D-5482461D9929)  
```

## Remarks

Using `declare_guid` is equivalent to using `cpp_quote` to generate an invocation of the `EXTERN_GUID` macro.

The above example results in the following output:

```C
cpp_quote("EXTERN_GUID(SID_Widget, 0x5144c348, 0x169e, 0x4359, 0xa7, 0x9d, 0x54, 0x82, 0x46, 0x1d, 0x99, 0x29);")
```

The `declare_guid` statement is provided as a convenience. It has the advantage of using the same GUID syntax as the [`uuid` attribute](uuid.md).

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**cpp_quote**](cpp-quote.md)
</dt> <dt>

[**uuid attribute**](uuid.md)
</dt> <dt>

[**GUID structure**](/windows/win32/api/guiddef/ns-guiddef-guid)
</dt> </dl>
