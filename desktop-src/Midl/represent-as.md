---
title: represent_as attribute
description: The \ represent\_as\ ACF attribute associates a named local type in the target language repr-type with a transfer type named-type that is transferred between client and server.
ms.assetid: ae44d220-e8f3-47a3-8f5e-a2668ac75411
keywords:
- represent_as attribute MIDL
topic_type:
- apiref
api_name:
- represent_as
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# represent\_as attribute

The **\[represent\_as\]** ACF attribute associates a named local type in the target language *repr-type* with a transfer type *named-type* that is transferred between client and server.

``` syntax
typedef [represent_as(repr-type) [[ , type-attribute-list ]] ] named-type; 
void __RPC_USER named-type_from_local (
  repr-type __RPC_FAR * ,
  named-type __RPC_FAR * __RPC_FAR * );
void __RPC_USER named-type_to_local (
  named-type __RPC_FAR * ,
  repr-type __RPC_FAR * ); void __RPC_USER named-type _free_inst ( named-type __RPC_FAR * ); void __RPC_USER named-type _free_local ( repr-type __RPC_FAR * );
```

## Parameters

<dl> <dt>

*named-type* 
</dt> <dd>

Specifies the named transfer data type that is transferred between client and server.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type. Separate multiple attributes with commas.

</dd> <dt>

*repr-type* 
</dt> <dd>

Specifies the represented local type in the target language that is presented to the client and server applications.

</dd> </dl>

## Remarks

When using **\[represent\_as\]**, you must supply routines that convert between the local and the transfer types and that free memory used to hold the converted data. The **\[represent\_as\]** attribute instructs the stubs to call the user-supplied conversion routines.

The transferred type *named-type* must resolve to a MIDL base type, predefined type, or to a type identifier. For more information, see [MIDL Base Types](midl-base-types.md).

You must supply the following routines:



| Routine name                   | Description                                                                                                                                                                                                |
|--------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *named\_type***\_from\_local** | Converts data from the local type to the network type. The routine allocates memory for the network data type, including memory for any data referenced by pointers in the network data type.              |
| *named\_type***\_to\_local**   | Converts data from the network type to the local type. The routine is responsible for allocating memory for data referenced by pointers in the local type. RPC allocates memory for the local type itself. |
| *named\_type***\_free\_local** | Frees memory allocated for data referenced by pointers in the local type. RPC frees memory for the type itself                                                                                             |
| *named\_type***\_free\_inst**  | Frees memory allocated for the data referenced by pointers in the network type and for the network type itself.                                                                                            |



 

The client stub calls *named-type***\_from\_local** to allocate space for the transmitted type and to translate the data from the local type to the network type. The server stub allocates space for the original data type and calls *named-type***\_to\_local** to translate the data from the network type to the local type.

Upon return from the application code, the client and server stubs call *named-type***\_free\_inst** to deallocate the storage for network type. The client stub calls *named-type***\_free\_local** to deallocate storage returned by the routine.

The following types cannot have a **\[represent\_as\]** attribute:

-   Conformant, varying, or conformant-varying arrays
-   Structures in which the last member is a conformant array (a conformant structure)
-   Pointers or types that contain a pointer
-   Pipes or types that contain pipes
-   Types that are used as the base type for a pipe
-   Predefined types [**handle\_t**](handle-t.md), [**void**](void.md)
-   Types that have the [**\[handle\]**](handle.md) attribute

## Examples

``` syntax
//these data types defined in .IDL or elsewhere
typedef struct  _lbox 
{ 
    long         data; 
    struct _lbox *next; 
} lbox; 
typedef [ref] lbox *PBOX_LOC; 
typedef long LONG4[4]; 
 
//in .ACF file :
interface iface
{
    typedef  [ represent_as(PBOX_LOC) ]  LONG4; 
}
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**handle\_t**](handle-t.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**void**](void.md)
</dt> </dl>

 

 




