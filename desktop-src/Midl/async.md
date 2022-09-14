---
title: async attribute
description: The \ async\ ACF attribute defines a remote procedure call as an asynchronous operation.
ms.assetid: 8002980a-94be-4d45-99d7-dfa4eae7f102
keywords:
- async attribute MIDL
topic_type:
- apiref
api_name:
- async
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# async attribute

The \[**async**\] ACF attribute defines a remote procedure call as an asynchronous operation.

``` syntax
[async, opt-acf-attributes] function-name (param-list)
```

## Parameters

<dl> <dt>

*opt-acf-attributes* 
</dt> <dd>

Specifies optional application configuration attributes.

</dd> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the function in the IDL file.

</dd> <dt>

*param-list* 
</dt> <dd>

Specifies an optional parameter list.

</dd> </dl>

## Remarks

This attribute is not applicable in COM interfaces.

To declare an RPC function as asynchronous, first declare the function as part of an interface definition in an IDL file. Then modify that function declaration, within the application configuration file (ACF), by applying the \[**async**\] attribute. Note that the function declaration makes no mention of the asynchronous handle and that the binding handle is the first parameter. Applying the \[**async**\] attribute in the ACF file generates the appropriate code so that when this function is called, the asynchronous server expects to receive an asynchronous handle before the other parameters.

> [!Note]  
> The async attribute cannot be used with the [**/osf**](-osf.md) command line switch.

 

## Examples

``` syntax
//file:Xasync.idl
interface AsyncIface 
{
    HRESULT MyAsyncFunc (
        handle_t hBinding,
        [in] int a,
        [in] int b,
        [out] int *c) ;
//other interface definitions
}
//end XAsync.idl

// file: Xasync.acf
interface AsyncIface
{
    [async] MyAsyncFunc () ;
    //any other ACF definitions
}
//end Xasync.acf
```

## See also

<dl> <dt>

[Application Configuration File (ACF)](application-configuration-file-acf-.md)
</dt> <dt>

[Asynchronous RPC](/windows/desktop/Rpc/asynchronous-rpc)
</dt> </dl>

 

 