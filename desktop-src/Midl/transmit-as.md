---
title: transmit_as attribute
description: The \ transmit\_as\ attribute instructs the compiler to associate type-id, which is a presented type that client and server applications manipulate, with a transmitted type xmit-type.
ms.assetid: 3dd1a242-03ec-49b4-ac96-87ef186e41d2
keywords:
- transmit_as attribute MIDL
topic_type:
- apiref
api_name:
- transmit_as
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# transmit\_as attribute

The **\[transmit\_as\]** attribute instructs the compiler to associate **type-id***,* which is a presented type that client and server applications manipulate, with a transmitted type **xmit-type.**

``` syntax
typedef [transmit_as(xmit-type) [[ , type-attribute-list ]] ] type-specifier declarator-list; 

void __RPC_USER type-id_to_xmit (
  type-id __RPC_FAR *,
  xmit-type __RPC_FAR * __RPC_FAR *);
void __RPC_USER type-id_from_xmit (
  xmit-type __RPC_FAR *,
  type-id __RPC_FAR *);
void __RPC_USER type-id_free_inst (
  type-id __RPC_FAR *);
void __RPC_USER type-id_free_xmit (
  xmit-type__RPC_FAR *);
```

## Parameters

<dl> <dt>

*xmit-type* 
</dt> <dd>

Specifies the data type that is transmitted between client and server.

</dd> <dt>

*type-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the type. Valid type attributes include **\[**[**handle**](handle.md)**\]**, **\[**[**switch\_type**](switch-type.md)**\]**; the pointer attribute **\[**[**ref**](ref.md)**\]**, **\[**[**unique**](unique.md)**\]**, or **\[**[**ptr**](ptr.md)**\]**; and the usage attributes **\[**[**string**](string.md)**\]** and **\[**[**ignore**](ignore.md)**\]**. Separate multiple attributes with commas.

</dd> <dt>

*type-specifier* 
</dt> <dd>

Specifies a [base type](midl-base-types.md), [**struct**](struct.md), [**union**](union.md), [**enum**](enum.md) type, or type identifier. An optional storage specification can precede *type-specifier*.

</dd> <dt>

*declarator-list* 
</dt> <dd>

Specifies standard C declarators, such as identifiers, pointer declarators, and array declarators. For more information, see [Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md), [**arrays**](arrays-1.md), and [Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers). The *declarator-list* consists of one or more declarators separated by commas. The parameter declarator in the function declarator, such as the parameter name, is optional.

</dd> <dt>

*type-id* 
</dt> <dd>

Specifies the name of the data type that is presented to the client and server applications.

</dd> </dl>

## Remarks

To use the **\[transmit\_as\]** attribute, the user must supply routines that convert data between the presented and the transmitted types; these routines must also free memory used to hold the converted data. The **\[transmit\_as\]** attribute instructs the stubs to call the user-supplied conversion routines.

The transmitted type *xmit-type* must resolve to a MIDL base type, predefined type, or a type identifier. For more information, see [MIDL Base Types](midl-base-types.md).

The user must supply the following routines.



| Routine name              | Description                                                                                                                                                                                                       |
|---------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| *type-id***\_to\_xmit**   | Converts data from the presented type to the transmitted type. This routine allocates memory for the transmitted type and for any data referenced by pointers in the transmitted type.                            |
| *type-id***\_from\_xmit** | Converts data from the transmitted type to the presented type. This routine is responsible for allocating memory for data referenced by pointers in the presented type. RPC allocates memory for the type itself. |
| *type-id***\_free\_inst** | Frees memory allocated for data referenced by pointers in the presented type. RPC frees memory for the type itself.                                                                                               |
| *type-id***\_free\_xmit** | Frees storage used by the caller for the transmitted type and for data referenced by pointers in the transmitted type.                                                                                            |



 

 

The client stub calls *type-id***\_to\_xmit** to allocate space for the transmitted type and to translate the data into objects of type *xmit-type.* The server stub allocates space for the original data type and calls *type-id***\_from\_xmit** to translate the data from its transmitted type to the presented type.

Upon return from the application code, the server stub calls *type-id***\_free\_inst** to deallocate the storage for *type-id* on the server side. The client stub calls *type-id***\_free\_xmit** to deallocate the *xmit-type* storage on the client side.

The following types cannot have a **\[transmit\_as\]** attribute:

-   Context handles (types with the **\[**[**context\_handle**](context-handle.md)**\]** type attribute and types that are used as parameters with the **\[context\_handle\]** attribute)
-   Types that are pipes or derived from pipes
-   Data types that are used as the base type of a pipe definition
-   Parameters that are pointers or resolve to pointers
-   Parameters that are conformant, varying, or open arrays
-   Structures that contain conformant arrays
-   The predefined type [**handle\_t**](handle-t.md), [**void**](void.md)

Types that are transmitted must conform to the following restrictions:

-   They must not be pointers or contain pointers.
-   They must not be pipes or contain pipes.

## Examples

``` syntax
typedef struct _TREE_NODE_TYPE 
{ 
    unsigned short data; 
    struct _TREE_NODE_TYPE * left; 
    struct _TREE_NODE_TYPE * right; 
} TREE_NODE_TYPE; 
 
typedef [transmit_as(TREE_XMIT_TYPE)] TREE_NODE_TYPE * TREE_TYPE; 
 
void __RPC_USER TREE_TYPE_to_xmit( 
    TREE_TYPE __RPC_FAR * , 
    TREE_XMIT_TYPE __RPC_FAR * __RPC_FAR *); 
 
void __RPC_USER TREE_TYPE_from_xmit ( 
    TREE_XMIT_TYPE __RPC_FAR *, 
    TREE_TYPE __RPC_FAR *); 
 
void __RPC_USER TREE_TYPE_free_inst( 
    TREE_TYPE __RPC_FAR *); 
 
void __RPC_USER TREE_TYPE_free_xmit( 
    TREE_XMIT_TYPE __RPC_FAR *);
```

## See also

<dl> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[**enum**](enum.md)
</dt> <dt>

[**handle**](handle.md)
</dt> <dt>

[**handle\_t**](handle-t.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**ignore**](ignore.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**string**](string.md)
</dt> <dt>

[**struct**](struct.md)
</dt> <dt>

[**switch\_type**](switch-type.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> <dt>

[**union**](union.md)
</dt> <dt>

[**unique**](unique.md)
</dt> <dt>

[**void**](void.md)
</dt> </dl>

 

 