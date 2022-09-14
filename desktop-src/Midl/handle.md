---
title: handle attribute
description: The \ handle\ attribute specifies a user-defined or \ 0034;customized \ 0034; handle type.
ms.assetid: db5c6ea6-6081-4cea-9265-5e2f67fd8c14
keywords:
- handle attribute MIDL
topic_type:
- apiref
api_name:
- handle
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# handle attribute

The \[**handle**\] attribute specifies a user-defined or "customized" handle type.

``` syntax
typedef [handle] typename;  
handle_t __RPC_USER typename_bind (typename);
void __RPC_USER typename_unbind (typename, handle_t);
```

## Parameters

<dl> <dt>

*typename* 
</dt> <dd>

Specifies the name of the user-defined binding-handle type.

</dd> </dl>

## Remarks

User-defined handles permit developers to design handles that are meaningful to the application. A user-defined handle can only be defined in a type declaration, not in a function declarator.

A parameter of a type defined by the \[**handle**\] attribute is used to determine the binding for the call and is transmitted to the called procedure.

The user must provide binding and unbinding routines to convert between primitive and user-defined handle types. Given a user-defined handle of type *typename*, the user must supply the routines *typename*\_**bind** and *typename*\_**unbind**. For example, if the user-defined handle type is named MYHANDLE, the routines are named MYHANDLE\_**bind** and MYHANDLE\_**unbind**.

If successful, the *typename*\_**bind** routine should return a valid primitive binding handle. If unsuccessful, the routine should return a **NULL**. If the routine returns **NULL**, the *typename*\_**unbind** routine will not be called. If the binding routine returns an invalid binding handle different from **NULL**, the stub behavior is undefined.

When the remote procedure has a user-defined handle as a parameter or as an implicit handle, the client stubs call the binding routine before calling the remote procedure. The client stubs call the unbinding routine after the remote call.

In DCE IDL, a parameter with the \[**handle**\] attribute must appear as the first parameter in the remote procedure argument list. Subsequent parameters, including other \[**handle**\] attributes, are treated as ordinary parameters. Microsoft supports an extension to DCE IDL that allows the user-defined \[**handle**\] parameter to appear in positions other than the first parameter.

## Examples

``` syntax
typedef [handle] struct 
{ 
    char machine[8]; 
    char nmpipe[256]; 
} h_service; 
 
handle_t __RPC_USER h_service_bind(h_service); 
void __RPC_USER h_service_unbind(h_service, handle_t);
```

## See also

<dl> <dt>

[Binding and Handles](/windows/desktop/Rpc/binding-and-handles)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> <dt>

[**implicit\_handle**](implicit-handle.md)
</dt> <dt>

[**typedef**](typedef.md)
</dt> </dl>

 

 