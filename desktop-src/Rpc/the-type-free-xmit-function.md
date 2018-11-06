---
title: The type_free_xmit Function
description: The stubs call the type\_free\_xmit function to free memory associated with the transmitted data.
ms.assetid: f15ce25b-d36c-4ee5-b796-f0aba1997047
keywords:
- type_free_xmit
ms.topic: article
ms.date: 05/31/2018
---

# The type\_free\_xmit Function

The stubs call the **type\_free\_xmit** function to free memory associated with the transmitted data. After the [type\_from\_xmit](the-type-from-xmit-function.md) function converts the transmitted data to its presented type, the memory is no longer needed. The function is defined as:

``` syntax
void __RPC_USER <type>_free_xmit(<xmit_type> __RPC_FAR *);
```

The parameter is a pointer to the memory that contains the transmitted type.

In this example, the memory contains an array that is in a single structure. The function DOUBLE\_LINK\_TYPE\_free\_xmit uses the user-supplied function midl\_user\_free to free the memory:

``` syntax
void __RPC_USER DOUBLE_LINK_TYPE_free_xmit( 
     DOUBLE_XMIT_TYPE __RPC_FAR * pArray)
{
     midl_user_free(pArray);
}
```

 

 




