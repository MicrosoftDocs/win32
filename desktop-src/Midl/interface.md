---
title: interface attribute
description: The interface keyword specifies the name of the interface. The interface name must be provided in both the IDL file and the ACF.
ms.assetid: 239b782e-57de-493c-b2f4-310d1859a9ae
keywords:
- interface attribute MIDL
topic_type:
- apiref
api_name:
- interface
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# interface attribute

The **interface** keyword specifies the name of the interface. The interface name must be provided in both the IDL file and the ACF.

``` syntax
[ 
    interface-attribute-list 
] 
interface interface-name [ : base-interface ]
{
}

typedef interface interface-name declarator-list
```

## Parameters

<dl> <dt>

*interface-attribute-list* 
</dt> <dd>

Specifies attributes that apply to the interface as a whole. Valid interface attributes for an IDL file include **\[**[**endpoint**](endpoint.md)**\]**, **\[**[**local**](local.md)**\]**, **\[**[**object**](object.md)**\]**, **\[**[**pointer\_default**](pointer-default.md)**\]**, **\[**[**uuid**](uuid.md)**\]**, and **\[**[**version**](version.md)**\]**. Valid interface attributes for an ACF include **\[**[**encode**](encode.md)**\]**, **\[**[**decode**](decode.md)**\]**, either **\[**[**auto\_handle**](auto-handle.md)**\]** or **\[**[**implicit\_handle**](implicit-handle.md)**\]**, and either **\[**[**code**](code.md)**\]** or **\[**[**nocode**](nocode.md)**\]**.

</dd> <dt>

*interface-name* 
</dt> <dd>

Specifies the name of the interface. The interface name must be a unique name and must start with an alphabetic or underscore character.

</dd> <dt>

*base-interface* 
</dt> <dd>

Specifies the name of an interface from which this derived interface inherits member functions, status codes, and interface attributes. The derived interface does not inherit type definitions. To do this, use the [**import**](import.md) keyword to import the IDL file of the base interface.

</dd> <dt>

*declarator-list* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md)., and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators, separated by commas.

</dd> </dl>

## Remarks

The interface names in the IDL file and ACF must be the same, except when you use the MIDL compiler switch [**/acf**](-acf.md).

The interface name forms the first part of the name of interface-handle data structures that are parameters to the RPC run-time functions. For more information, see [**RPC\_IF\_HANDLE**](/windows/desktop/Rpc/rpc-if-handle).

If the interface header includes the **\[**[**object**](object.md)**\]** attribute to indicate a COM interface, it must also include the **\[**[**uuid**](uuid.md)**\]** attribute and must specify the base COM interface from which it is derived. For more information about COM interfaces, see **\[**[**object**](object.md)**\]**.

You can also use the **interface** keyword with the [**typedef**](typedef.md) keyword to define an interface data type.

## Examples

``` syntax
/* use of interface keyword in IDL file for an RPC interface */ 
[ 
    uuid (00000000-0000-0000-0000-000000000000), 
    version (1.0) 
] 
interface remote_if_2 
{  
    // Interface definition statements.
} 
 
/* use of interface keyword in ACF for an RPC interface */ 
[
    implicit_handle( handle_t xa_bhandle ) 
] 
interface remote_if_2 
{ 
    // Attribute configuration statements.
} 
 
/* use of interface keyword in IDL file for a COM interface */ 
[ 
    object, uuid (00000000-0000-0000-0000-000000000000) 
] 
interface IDerivedInterface : IBaseInterface 
{  
    import "base.idl" 
    Save(); 
} 
 
/* use of interface keyword to define an interface pointer type */ 
typedef interface IStorage *LPSTORAGE;
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**endpoint**](endpoint.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**local**](local.md)
</dt> <dt>

[**object**](object.md)
</dt> <dt>

[**pointer\_default**](pointer-default.md)
</dt> <dt>

[**RPC\_IF\_HANDLE**](/windows/desktop/Rpc/rpc-if-handle)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**uuid**](uuid.md)
</dt> <dt>

[**version**](version.md)
</dt> </dl>

 

 