---
title: uuid attribute
description: The \ uuid\ interface attribute designates a universally unique identifier (UUID) that is assigned to the interface and that distinguishes it from other interfaces.
ms.assetid: 72cf12f5-49cd-440d-9665-73211509d050
keywords:
- uuid attribute MIDL
topic_type:
- apiref
api_name:
- uuid
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# uuid attribute

The **\[uuid\]** interface attribute designates a universally unique identifier (UUID) that is assigned to the interface and that distinguishes it from other interfaces.

``` syntax
uuid (string-uuid) 
uuid ("string-uuid")
```

## Parameters

<dl> <dt>

*string-uuid* 
</dt> <dd>

Specifies a string consisting of 8 hexadecimal digits followed by a hyphen, then three groups of 4 hexadecimal digits each followed by a hyphen, then 12 hexadecimal digits. You can enclose the UUID string in quotes, except when you use the MIDL compiler switch [**/osf**](-osf.md).

</dd> </dl>

## Remarks

The run-time library uses the interface UUID that the **\[uuid\]** attribute designates to help establish communication between the client and server applications. The **\[uuid\]** attribute can appear in the interface attribute list for either an RPC interface or a COM interface.

For an RPC interface, the interface attribute list must include either the **\[uuid\]** attribute or the **\[**[**local**](local.md)**\]** attribute, and the one you choose must occur exactly once. If the list includes the **\[uuid\]** attribute, it can also include the **\[**[**version**](version.md)**\]** attribute.

For a COM interface (identified by the **\[**[**object**](object.md)**\]** interface attribute), the interface attribute list must include the **\[uuid\]** attribute, but it cannot include the **\[version\]** attribute. The list for a COM interface can include the **\[local\]** attribute even though the **\[uuid\]** attribute is present.

Microsoft RPC supports an extension to DCE IDL that allows the UUID to be enclosed in double quotation marks ("" ""). The quoted form is needed for C-compiler preprocessors that interpret UUID numbers as floating-point numbers.

All UUID values should be computer-generated to guarantee uniqueness. Use the Uuidgen utility to generate unique UUID values.

The UUID and version numbers of the interface are used to determine whether the client can bind to the server. For the client to bind to the server, the UUID specified in the client and server interfaces must be the same.

Note that an interface without attributes can be imported into a base IDL file. However, the interface must contain only datatypes with no procedures. If even one procedure is contained in the interface, a local or UUID attribute must be specified.

## Examples

``` syntax
uuid(6B29FC40-CA47-1067-B31D-00DD010662DA) 
 
uuid("6B29FC40-CA47-1067-B31D-00DD010662DA")
```

## See also

<dl> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**interface**](interface.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[**object**](object.md)
</dt> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**version**](version.md)
</dt> </dl>

 

 




