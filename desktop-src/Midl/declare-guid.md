---
title: declare_guid attribute
description: The declare\_guid attribute instructs MIDL to express a GUID variable into the generated header file.
keywords:
- declare_guid attribute MIDL
topic_type:
- apiref
api_name:
- declare_guid
api_type:
- NA
ms.topic: reference
ms.date: 02/05/2021
---

# declare\_guid attribute

The **declare\_guid** attribute instructs MIDL to express a GUID variable into the generated header file.

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

## Remarks

This attribute is effectively a short-hand on using the `EXTERN_GUID` macro in the form:

```C
cpp_quote("EXTERN_GUID(SID_Widget, 0x5144c348, 0x169e, 0x4359, 0xa7, 0x9d, 0x54, 0x82, 0x46, 0x1d, 0x99, 0x29);")
```

It provides no functional advantage over the alternative format. It is a convenience feature that can make it easier to locate multiple defined instances of the same *GUID* within a codebase as the condensed format matches the declaration style of the [`uuid` attribute](uuid.md).

## Examples

``` syntax
declare_guid(SID_Widget, 5144C348-169E-4359-A79D-5482461D9929)  
```

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
