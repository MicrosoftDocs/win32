---
title: call_as attribute
description: The \ call\_as\ attribute enables you to map a function that cannot be called remotely to a remote function.
ms.assetid: 4078f37a-9bd7-4316-b228-afbffc4caeab
keywords:
- call_as attribute MIDL
topic_type:
- apiref
api_name:
- call_as
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# call\_as attribute

The **\[call\_as\]** attribute enables you to map a function that cannot be called remotely to a remote function.

``` syntax
[call_as (local-proc), [ , operation-attribute-list ] ] operation-name ;
```

## Parameters

<dl> <dt>

*local-proc* 
</dt> <dd>

Specifies an operation-defined routine.

</dd> <dt>

*operation-attribute-list* 
</dt> <dd>

Specifies one or more attributes that apply to the operation. Separate multiple attributes with commas.

</dd> <dt>

*operation-name* 
</dt> <dd>

Specifies the named operation presented to the application.

</dd> </dl>

## Remarks

The ability to map a function that cannot be called remotely to a remote function is particularly helpful in interfaces that have numerous parameter types that cannot be transmitted across the network. Rather than using many **\[**[**represent\_as**](represent-as.md)**\]** and **\[**[**transmit\_as**](transmit-as.md)**\]** types, you can combine all the conversions using **\[call\_as\]** routines. You supply the two **\[call\_as\]** routines (client side and server side) to bind the routine between the application calls and the remote calls.

The **\[call\_as\]** attribute can be used for object interfaces. In this case, the interface definition can be used for local calls as well as remote calls because **\[call\_as\]** allows an interface that can't be accessed remotely to be transparently mapped to a remote interface. The **\[call\_as\]** attribute cannot be used with [**/osf**](-osf.md) mode.

For example, assume that the routine **f1** in object interface **IFace** requires numerous conversions between the user calls and what is actually transmitted. The following examples describe the IDL and ACF files for interface **IFace**:

In the IDL file for interface **IFace**:

``` syntax
[local] HRESULT f1 ( <users parameter list> ) 
[call_as( f1 )] long Remf1( <remote parameter list> );
```

In the ACF for interface **IFace**:

``` syntax
[call_as( f1 )] Remf1();
```

This causes the generated header file to define the interface using the definition of **f1**, yet it also provides stubs for **Remf1**.

The MIDL compiler will generate the following Vtable in the header file for interface **IFace**:

``` syntax
struct IFace_vtable
{ 
    HRESULT ( * f1) ( <users parameter list> ); 
    /* Other vtable functions. */
};
```

The client-side proxy would then have a typical MIDL-generated proxy for **Remf1**, while the server side stub for **Remf1** would be the same as the typical MIDL-generated stub:

``` syntax
HRESULT IFace_Remf1_Stub ( <parameter list> ) 
{ 
    // Other function code.

    /* instead of IFace_f1 */
    invoke IFace_f1_Stub ( <remote parameter list> ); 

    // Other function code.
}
```

Then, the two **\[call\_as\]** bond routines (client side and server side) must be manually coded:

``` syntax
HRESULT f1_Proxy ( <users parameter list> ) 
{ 
    // Other function code.

    Remf1_Proxy ( <remote parameter list> ); 

    // Other function code.
} 
 
long IFace_f1_Stub ( <remote parameter list> ) 
{ 
    // Other function code.

    IFace_f1 ( <users parameter list> ); 

    // Other function code.
    }
```

For object interfaces, these are the prototypes for the bond routines.

For client side:

``` syntax
<local_return_type>  <interface>_<local_routine>_proxy( 
    <local_parameter_list> );
```

For server side:

``` syntax
<remote_return_type>  <interface>_<local_routine>_stub(
    <remote_parameter_list> );
```

For nonobject interfaces, these are the prototypes for the bond routines.

For client side:

``` syntax
<local_return_type>  <local_routine> ( <local_parameter_list> );
```

For server side:

``` syntax
<local_return_type>  <interface>_v<maj>_<min>_<local_routine> ( 
    <remote_parameter_list> );
```

## See also

<dl> <dt>

[**/osf**](-osf.md)
</dt> <dt>

[**represent\_as**](represent-as.md)
</dt> <dt>

[**transmit\_as**](transmit-as.md)
</dt> </dl>

 

 




