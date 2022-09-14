---
title: The type_to_xmit Function
description: The stubs call the type\_to\_xmit function to convert the type that is presented by the application into the transmitted type.
ms.assetid: fb5b3760-d660-4e4e-b5c5-768e8e598e23
keywords:
- type_to_xmit
ms.topic: article
ms.date: 05/31/2018
---

# The type\_to\_xmit Function

The stubs call the **type\_to\_xmit** function to convert the type that is presented by the application into the transmitted type. The function is defined as:

``` syntax
void __RPC_USER <type>_to_xmit ( 
     <type> __RPC_FAR *, <xmit_type> __RPC_FAR *     __RPC_FAR *);
```

The first parameter is a pointer to the application data. The second parameter is set by the function to point to the transmitted data. The function must allocate memory for the transmitted type.

In the following example, the client calls the remote procedure that has an **\[in, out\]** parameter of type DOUBLE\_LINK\_TYPE. The client stub calls the **type\_to\_xmit** function, here named DOUBLE\_LINK\_TYPE\_to\_xmit, to convert double-linked list data into a sized array.

The function determines the number of elements in the list, allocates an array large enough to hold those elements, then copies the list elements into the array. Before the function returns, the second parameter, *ppArray*, is set to point to the newly allocated data structure.


```C++
void __RPC_USER DOUBLE_LINK_TYPE_to_xmit ( 
    DOUBLE_LINK_TYPE __RPC_FAR * pList, 
    DOUBLE_XMIT_TYPE __RPC_FAR * __RPC_FAR * ppArray)
{
    short cCount = 0;
    DOUBLE_LINK_TYPE * pHead = pList;  // save pointer to start 
    DOUBLE_XMIT_TYPE * pArray;
 
    /* count the number of elements to allocate memory */
    for (; pList != NULL; pList = pList->pNext)
        cCount++;
 
    /* allocate the memory for the array */
    pArray = (DOUBLE_XMIT_TYPE *) MIDL_user_allocate 
         (sizeof(DOUBLE_XMIT_TYPE) + (cCount * sizeof(short)));
    pArray->sSize = cCount;
 
    /* copy the linked list contents into the array */
    cCount = 0;
    for (i = 0, pList = pHead; pList != NULL; pList = pList->pNext)
        pArray->asNumber[cCount++] = pList->sNumber;
 
    /* return the address of the pointer to the array */
    *ppArray = pArray;
}
```



 

 




