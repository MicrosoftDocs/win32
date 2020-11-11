---
title: ignore attribute
description: The \ ignore\ attribute designates that a pointer contained in a structure or union and the object indicated by the pointer is not transmitted. The \ ignore\ attribute is restricted to pointer members of structures or unions.
ms.assetid: 9c2fc71a-4fac-4a59-95f5-2121067b326f
keywords:
- ignore attribute MIDL
topic_type:
- apiref
api_name:
- ignore
api_type:
- NA
ms.topic: reference
ms.date: 05/31/2018
---

# ignore attribute

The **\[ignore\]** attribute designates that a pointer contained in a structure or union and the object indicated by the pointer is not transmitted. The **\[ignore\]** attribute is restricted to pointer members of structures or unions.

``` syntax
[ignore] pointer-member-type pointer-name;
```

## Parameters

<dl> <dt>

*pointer-member-type* 
</dt> <dd>

Specifies the type of the pointer member of the structure or union.

</dd> <dt>

*pointer-name* 
</dt> <dd>

Specifies the name of the pointer member that is to be ignored during marshaling.

</dd> </dl>

## Remarks

The value of a structure member with the **\[ignore\]** attribute is undefined at the destination. An **\[**[**in**](in.md)**\]** parameter is not defined at the remote computer. An **\[**[**out**](out-idl.md)**\]** parameter is not defined at the local computer.

The **\[ignore\]** attribute allows you to prevent transmission of data. This is useful in situations such as a double-linked list. The following example includes a double-linked list that introduces data aliasing:

``` syntax
/* IDL file */ 
typedef struct _DBL_LINK_NODE_TYPE 
{ 
    long value; 
    struct _DBL_LINK_NODE_TYPE * next; 
    struct _DBL_LINK_NODE_TYPE * previous; 
} DBL_LINK_NODE_TYPE; 
 
HRESULT remote_op([in] DBL_LINK_NODE_TYPE * list_head); 
 
/* application */ 
DBL_LINK_NODE_TYPE * p, * q 
 
p = (DBL_LINK_NODE_TYPE *) midl_user_allocate(
        sizeof(DBL_LINK_NODE_TYPE)); 
q = (DBL_LINK_NODE_TYPE *) midl_user_allocate(
        sizeof(DBL_LINK_NODE_TYPE)); 
 
p->next = q;  
q->previous = p; 
p->previous = q->next = NULL; 
.. 
remote_op(p);
```

Aliasing occurs in the preceding example because the same memory area is available from two different pointers in the function **p** and **p->next->previous**.

Note that **\[ignore\]** cannot be used as a type attribute.

## Examples

``` syntax
typedef struct _DBL_LINK_NODE_TYPE 
{ 
    long value; 
    struct _DBL_LINK_NODE_TYPE * next; 
    [ignore] struct _DBL_LINK_NODE_TYPE * previous; 
} DBL_LINK_NODE_TYPE;
```

## See also

<dl> <dt>

[Array and Sized-Pointer Attributes](array-and-sized-pointer-attributes.md)
</dt> <dt>

[**arrays**](arrays-1.md)
</dt> <dt>

[Arrays and Pointers](/windows/desktop/Rpc/arrays-and-pointers)
</dt> <dt>

[**in**](in.md)
</dt> <dt>

[**out**](out-idl.md)
</dt> <dt>

[**ptr**](ptr.md)
</dt> <dt>

[**ref**](ref.md)
</dt> <dt>

[**unique**](unique.md)
</dt> </dl>

 

 