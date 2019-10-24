---
title: void attribute
description: The base type void indicates a procedure with no arguments or a procedure that does not return a result value.
ms.assetid: a3eebfe7-bf43-4bab-b87b-9188a54ab9bf
keywords:
- void attribute MIDL
topic_type:
- apiref
api_name:
- void
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# void attribute

The base type **void** indicates a procedure with no arguments or a procedure that does not return a result value.

``` syntax
void function-name(parameter-list);

return-type function-name(void);

typedef [context_handle] void * context-handle-type;

return-type function-name(
    [context_handle] void * * context-handle-type
    , ...);
```

## Parameters

<dl> <dt>

*function-name* 
</dt> <dd>

Specifies the name of the remote procedure.

</dd> <dt>

*parameter-list* 
</dt> <dd>

Specifies the list of parameters passed to the function along with the associated parameter types and parameter attributes.

</dd> <dt>

*return-type* 
</dt> <dd>

Specifies the name of the type returned by the function.

</dd> <dt>

*context-handle-type* 
</dt> <dd>

Specifies the name of the type that takes the **\[**[**context\_handle**](context-handle.md)**\]** attribute.

</dd> </dl>

## Remarks

The pointer type **void \***, which in C describes a generic pointer that can be cast to represent any pointer type, is limited in MIDL to its use with the **\[context\_handle\]** keyword.

## Examples

``` syntax
void VoidFunc1(void); 
HRESULT VoidFunc2([in, out] short s1); 
typedef [context_handle] void * MY_CX_HNDL_TYPE; 
HRESULT InitHandle([out] MY_CX_HNDL_TYPE * ppCxHndl);
```

## See also

<dl> <dt>

[MIDL Base Types](midl-base-types.md)
</dt> <dt>

[**context\_handle**](context-handle.md)
</dt> <dt>

[Interface Definition (IDL) File](interface-definition-idl-file.md)
</dt> </dl>

 

 




