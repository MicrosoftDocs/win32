---
title: user_marshal attribute
description: The user\_marshal ACF attribute associates a named local type in the target language (userm-type) with a transfer type (wire-type) that is transferred between client and server.
ms.assetid: a2407aa3-574d-4690-8cdf-cb1c01ca8c49
keywords:
- user_marshal attribute MIDL
topic_type:
- apiref
api_name:
- user_marshal
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# user\_marshal attribute

The **user\_marshal** ACF attribute associates a named local type in the target language (*userm-type*) with a transfer type (*wire-type*) that is transferred between client and server.

``` syntax
typedef [user_marshal(userm_type)] wire-type; 
unsigned long __RPC_USER  < userm_type >_UserSize(
    unsigned long __RPC_FAR *pFlags,
    unsigned long StartingSize,
    < userm_type >  __RPC_FAR * pUser_typeObject );
unsigned char __RPC_FAR * __RPC_USER  < userm-type >_UserMarshal(
    unsigned long __RPC_FAR *pFlags,
    unsigned char __RPC_FAR * Buffer,
    < userm_type >  __RPC_FAR * pUser_typeObject);
unsigned char __RPC_FAR * __RPC_USER  < userm_type >_UserUnmarshal(
    unsigned long  __RPC_FAR *  pFlags,
    unsigned char __RPC_FAR *  Buffer,
    < userm_type >  __RPC_FAR * pUser_typeObject);
void __RPC_USER  < userm_type >_UserFree(
    unsigned long  __RPC_FAR * pFlags,
    < userm_type >  __RPC_FAR * pUser_typeObject);
```

## Parameters

<dl> <dt>

*userm-type* 
</dt> <dd>

Specifies the identifier of the user data type to be marshaled. The *userm-type* need not be transmittable and need not be a type known to the MIDL compiler.

</dd> <dt>

*wire-type* 
</dt> <dd>

Specifies the named transfer data type that is actually transferred between client and server. The wire type must be a MIDL base type, predefined type, or a type identifier of a type that can be transmitted across the network.

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

Specifies a pointer to an object of *userm\_type*.

</dd> <dt>

*Buffer* 
</dt> <dd>

Specifies the current buffer pointer.

</dd> </dl>

## Remarks

Each named local type, *userm-type*, has a one-to-one correspondence with a *wire-type* that defines the wire representation of the type. You must supply routines to size the data for marshaling, to marshal and unmarshal the data, and to free memory. For more information on these routines, see [The user\_marshal Attribute](/windows/desktop/Rpc/the-user-marshal-attribute). Note that if there are embedded types in your data that are also defined with **user\_marshal** or \[ [**\[wire\_marshal\]**](wire-marshal.md), you need to manage the servicing of those embedded types also.

The *wire-type* cannot be an interface pointer or a full pointer. The *wire-type* must have a well-defined memory size. See [Marshaling Rules for user\_marshal and wire\_marshal](/windows/desktop/Rpc/marshaling-rules-for-user-marshal-and-wire-marshal) for details on how to marshal a given *wire-type*.

The *userm-type* should not be an interface pointer as these can be marshaled directly. If the user type is a full pointer, you must manage the aliasing yourself.

## Examples

``` syntax
// Marshal a long as a structure containing two shorts.

typedef unsigned long FOUR_BYTE_DATA;
typedef struct _TWO_X_TWO_BYTE_DATA 
{ 
    unsigned short low; 
    unsigned short high; 
} TWO_X_TWO_BYTE_DATA;
```

``` syntax
// ACFL file

typedef [user_marshal(FOUR_BYTE_DATA)] TWO_X_TWO_BYTE_DATA;

// Marshaling functions:

// Calculate size that converted data will require in the buffer
unsigned long __RPC_USER FOUR_BYTE_DATA_UserSize( 
    ULONG __RPC_FAR * pulFlags, 
    ULONG __RPC_FAR ulStartingSize,
    FOUR_BYTE_DATA __RPC_FAR * pul);

// Copy FOUR_BYTE_DATA into buffer as TWO_X_TWO_BYTE_DATA
unsigned long __RPC_USER FOUR_BYTE_DATA_UserMarshal( 
    ULONG __RPC_FAR *pulFlags, 
    char __RPC_FAR * pBufferStart, 
    FOUR_BYTE_DATA __RPC_FAR * pul);

// Recreate FOUR_BYTE_DATA from TWO_X_TWO_BYTE_DATA in buffer
unsigned long __RPC_USER FOUR_BYTE_DATA_UserUnmarshal( 
    ULONG __RPC_FAR * pulFlags, 
    char __RPC_FAR * pBufferStart, 
    FOUR_BYTE_DATA __RPC_FAR * pul);

// Nothing to do here as the engine frees the top node and FOUR_BYTE_DATA is a flat data type.
void __RPC_USER FOUR_BYTE_DATA_UserFree( 
    ULONG __RPC_FAR * pulFlags, 
    FOUR_BYTE_DATA __RPC_FAR * pul);
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**long**](long.md)
</dt> <dt>

[**represent\_as**](represent-as.md)
</dt> <dt>

[**unsigned**](unsigned.md)
</dt> <dt>

[The user\_marshal Attribute](/windows/desktop/Rpc/the-user-marshal-attribute)
</dt> <dt>

[**wire\_marshal**](wire-marshal.md)
</dt> <dt>

[**NdrGetUserMarshalInfo**](/windows/desktop/api/rpcndr/nf-rpcndr-ndrgetusermarshalinfo)
</dt> </dl>

 

 