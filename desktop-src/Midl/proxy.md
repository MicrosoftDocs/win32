---
title: proxy attribute
description: The \ proxy\ attribute prevents Automation from registering as a proxy/stub handler for a dual interface.
ms.assetid: 88e59938-83c9-436a-931c-f4396fdcf653
keywords:
- proxy attribute MIDL
topic_type:
- apiref
api_name:
- proxy
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# proxy attribute

The **\[proxy\]** attribute prevents Automation from registering as a proxy/stub handler for a dual interface.

``` syntax
[ 
    proxy, 
    uuid(string-uuid <>)
    [ , interface-attribute-list <>] 
] 
interface interface-name <> : base-interface <>
{
    ...
}
```

## Parameters

<dl> <dt>

*string-uuid* 
</dt> <dd>

Specifies a string consisting of 8 hexadecimal digits followed by a hyphen, then three groups of 4 hexadecimal digits each followed by a hyphen, then 12 hexadecimal digits. You can enclose the UUID string in quotes, except when you use the MIDL compiler switch [**/osf**](-osf.md).

</dd> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies a list of zero or more IDL attributes that apply to the interface as a whole. When two or more interface attributes are present, they must be separated by commas.

</dd> <dt>

*interface-name* 
</dt> <dd>

Name of the interface.

</dd> <dt>

*base-interface* 
</dt> <dd>

Specifies the name of an interface from which this derived interface inherits member functions, status codes, and interface attributes. The derived interface does not inherit type definitions. To do this, use the [**import**](import.md) keyword to import the IDL file of the base interface.

</dd> </dl>

## Remarks

Using the \[ **proxy**\] attribute for a dual interface prevents the TLB from taking over generated stubs. If this attribute is specified, the typelib proxy should not be unregistered when the typelib is unregistered.

### Flags

<dl> <dt>

<span id="TYPEFLAG_PROXY"></span><span id="typeflag_proxy"></span>TYPEFLAG\_PROXY
</dt> <dd>

Interfaces can be marked with the TYPEFLAG\_PROXY flag to indicate they will be using a proxy/stub dynamic link library. This flag specifies the typelib proxy should not be unregistered when the typelib is unregistered.

</dd> </dl>

## See also

<dl> <dt>

[**Generating a Type Library with MIDL**](generating-a-type-library-with-midl-2.md)
</dt> <dt>

[**dual**](dual.md)
</dt> <dt>

[**TYPEFLAGS**](/windows/win32/api/oaidl/ne-oaidl-typeflags)
</dt> </dl>

 

 