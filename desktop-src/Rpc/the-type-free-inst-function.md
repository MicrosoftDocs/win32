---
title: The type_free_inst Function
description: The stubs call the type\_free\_inst function to free memory associated with the presented type.
ms.assetid: 4ee2e6a6-b506-445f-adaf-3705228defa7
keywords:
- type_free_inst
ms.topic: article
ms.date: 05/31/2018
---

# The type\_free\_inst Function

The stubs call the **type\_free\_inst** function to free memory associated with the presented type. The function is defined as:

``` syntax
void __RPC_USER <type>_free_inst(<type> __RPC_FAR *)
```

The parameter points to the presented type instance. This object should not be freed. For a discussion on when to call the function, see [The transmit\_as Attribute](the-transmit-as-attribute.md).

In the following example, the double-linked list is freed by walking the list to its end, then backing up and freeing each element of the list.


```C++
void __RPC_USER DOUBLE_LINK_TYPE_free_inst(
     DOUBLE_LINK_TYPE __RPC_FAR * pList)
{
    while (pList->pNext != NULL)  // go to end of the list
        pList = pList->pNext;

    pList = pList->pPrevious;
    while (pList != NULL) 
    {  
        // back through the list
        midl_user_free(pList->pNext);
        pList = pList->pPrevious;
    }
} 
```



 

 




