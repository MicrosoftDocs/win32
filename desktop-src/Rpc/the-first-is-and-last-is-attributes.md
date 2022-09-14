---
title: The  first_is and  last_is Attributes
description: You can determine the number of transmitted elements by specifying the first and last elements.
ms.assetid: bd4dcf42-64a7-4b05-ac55-be77c381eb2e
keywords:
- first_is
- last_is
ms.topic: article
ms.date: 05/31/2018
---

# The \[first\_is\] and \[last\_is\] Attributes

You can determine the number of transmitted elements by specifying the first and last elements. Use the \[[**first\_is**](/windows/desktop/Midl/first-is)\] and \[[**last\_is**](/windows/desktop/Midl/last-is)\] attributes as shown:

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(4.0)
]
interface arraytest
{

  void fArray4([in]               short sSize,
               [in]               short sLast,
               [in]               short sFirst,
               [in, 
                out,
                size_is(sSize),
                first_is(sFirst),
                last_is(sLast)]   char achArray[]) ;
}
```

 

 