---
title: wire_marshal attribute
description: The \ wire\_marshal\ attribute specifies a data type that will be used for transmission (the wire-type) instead of an application-specific data type (the userm-type).
ms.assetid: 51969f2c-7390-42c4-8aa6-ba12fdb22d23
keywords:
- wire_marshal attribute MIDL
topic_type:
- apiref
api_name:
- wire_marshal
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# wire\_marshal attribute

The **\[wire\_marshal\]** attribute specifies a data type that will be used for transmission (the *wire-type*) instead of an application-specific data type (the *userm-type*).

``` syntax
typedef [wire_marshal(wire_type)] type-specifier userm-type; 
unsigned long __RPC_USER  < userm-type >_UserSize(
    unsigned long __RPC_FAR *pFlags,
    unsigned long StartingSize,
    < userm-type > __RPC_FAR * pUser_typeObject );
unsigned char __RPC_FAR * __RPC_USER  < userm-type >_UserMarshal(
    unsigned long  __RPC_FAR * pFlags,
    unsigned char __RPC_FAR * Buffer,
    < userm-type >  __RPC_FAR * pUser_typeObject);
unsigned char __RPC_FAR * __RPC_USER  < userm-type >_UserUnmarshal(
    unsigned long  __RPC_FAR *  pFlags,
    unsigned char __RPC_FAR *  Buffer,
    < userm-type > __RPC_FAR * pUser_typeObject);
void __RPC_USER  < userm-type >_UserFree(
    unsigned long  __RPC_FAR * pFlags,
    < userm-type >  __RPC_FAR * pUser_typeObject);
```

## Parameters

<dl> <dt>

*wire-type* 
</dt> <dd>

Specifies the named transfer data type that is actually transferred between client and server. The *wire-type* must be a MIDL base type, predefined type, or a type identifier of a type that can be transmitted across the network.

</dd> <dt>

*type-specifier* 
</dt> <dd>

The type for which *userm-type* will become an alias.

</dd> <dt>

*userm-type* 
</dt> <dd>

Specifies the identifier of the user data type to be marshaled. It can be any type, as given by the *type-specifier*, as long as it has a well-defined size. The *userm-type* need not be transmittable but must be a type known to the MIDL compiler.

</dd> <dt>

*pFlags* 
</dt> <dd>

Specifies a pointer to a flag field ( [**unsigned**](unsigned.md) [**long**](long.md)). The high-order word specifies NDR data representation flags as defined by DCE for floating point, big- or little-endian, and character representation. The low-order word specifies a marshaling context flag. The exact layout of the flags is described in [The type\_UserSize Function](/windows/desktop/Rpc/the-type-usersize-function).

</dd> <dt>

*StartingSize* 
</dt> <dd>

Specifies the current buffer size (offset) before sizing the object.

</dd> <dt>

*pUser\_typeObject* 
</dt> <dd>

Specifies a pointer to an object of *userm\_type.*

</dd> <dt>

*Buffer* 
</dt> <dd>

Specifies the current buffer pointer.

</dd> </dl>

## Remarks

Each application-specific data type, *userm-type,* has a one-to-one correspondence with a *wire-type* that defines the wire representation of the type. You must supply routines to size the data for marshaling, to marshal and unmarshal the data, and to free memory. Note that if there are embedded types in your data that are also defined with **\[wire\_marshal\]** or **\[**[**user\_marshal**](user-marshal.md)**\]**, you need to manage the servicing of those embedded types also. For more information on these routines, see [The wire\_marshal Attribute](/windows/desktop/Rpc/the-wire-marshal-attribute).

Your implementation must follow the marshalling rules according to the OSF-DCE specification. Details about NDR transfer syntax can be found at [https://www.opengroup.org/onlinepubs/9629399/chap14.htm](https://pubs.opengroup.org/onlinepubs/9629399/chap14.htm). It is not recommended to use **\[wire\_marshal\]** if you are not familiar with the wire protocol.

The *wire-type* cannot be an interface pointer or a full pointer. The *wire-type* must have a well-defined memory size. See [Marshaling Rules for user\_marshal and wire\_marshal](/windows/desktop/Rpc/marshaling-rules-for-user-marshal-and-wire-marshal) for details on how to marshal a given *wire-type*.

The *userm-type* should not be an interface pointer because these can be marshaled directly. If the user type is a full pointer, you must manage the aliasing yourself.

You cannot use the **\[wire\_marshal\]** attribute with the **\[**[**allocate**](allocate.md)**\]** attribute, either directly or indirectly, because the NDR engine does not control memory allocation for the transmitted type.

## Examples

``` syntax
typedef unsigned long _FOUR_BYTE_DATA;

typedef struct _TWO_X_TWO_BYTE_DATA 
{
        unsigned short low;
        unsigned short high;
} TWO_X_TWO_BYTE_DATA;

typedef [wire_marshal(TWO_X_TWO_BYTE_DATA)] 
    _FOUR_BYTE_DATA FOUR_BYTE_DATA; 

//Marshaling functions:

// Calculate size that converted data will 
// require in the buffer
unsigned long __RPC_USER FOUR_BYTE_DATA_UserSize( 
    ULONG __RPC_FAR * pulFlags, 
    ULONG __RPC_FAR ulStartingSize,
    FOUR_BYTE_DATA __RPC_FAR * pul);

// Copy FOUR_BYTE_DATA into buffer as 
// TWO_X_TWO_BYTE_DATA
unsigned long __RPC_USER FOUR_BYTE_DATA_UserMarshal( 
    ULONG __RPC_FAR *pulFlags, 
    char __RPC_FAR * pBufferStart, 
    FOUR_BYTE_DATA __RPC_FAR * pul);

// Recreate FOUR_BYTE_DATA from TWO_X_TWO_BYTE_DATA in buffer
unsigned long __RPC_USER FOUR_BYTE_DATA_UserUnmarshal( 
    ULONG __RPC_FAR * pulFlags, 
    char __RPC_FAR * pBufferStart, 
    FOUR_BYTE_DATA __RPC_FAR * pul);

// Nothing to do here as the engine frees the top 
// node and FOUR_BYTE_DATA is a flat data type.
void __RPC_USER FOUR_BYTE_DATA_UserFree( 
    ULONG __RPC_FAR * pulFlags, 
    FOUR_BYTE_DATA __RPC_FAR * pul 
    );
```

## See also

<dl> <dt>

[**allocate**](allocate.md)
</dt> <dt>

[Data Representation](/windows/desktop/Rpc/data-representation)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**long**](long.md)
</dt> <dt>

[**NdrGetUserMarshalInfo**](/windows/desktop/api/rpcndr/nf-rpcndr-ndrgetusermarshalinfo)
</dt> <dt>

[The wire\_marshal Attribute](/windows/desktop/Rpc/the-wire-marshal-attribute)
</dt> <dt>

[**transmit\_as**](transmit-as.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> <dt>

[**user\_marshal**](user-marshal.md)
</dt> </dl>

 

 