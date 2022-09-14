---
title: The  length_is Attribute
description: The \ size\_is\ attribute lets you specify the maximum size of the array.
ms.assetid: 577a1efd-2d16-40d6-99bb-998d81ee2f8c
keywords:
- length_is
ms.topic: article
ms.date: 05/31/2018
---

# The \[length\_is\] Attribute

The \[[**size\_is**](/windows/desktop/Midl/size-is)\] attribute lets you specify the maximum size of the array. When this is the only attribute, all elements of the array are transmitted. Instead of sending all elements of the array, you can specify the transmitted elements using the \[[**length\_is**](/windows/desktop/Midl/length-is)\] attribute, as follows:

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(3.0)
]
interface arraytest
{
  void fArray3([in] short sSize,
               [in] short sLength
               [in, out, size_is(sSize), 
                 length_is(sLength)] char achArray[*]);
}
```

Size describes allocation while length describes transmission. The number of elements transmitted must always be less than or equal to the number of elements allocated. The value associated with **length\_is** is always less than or equal to **size\_is**.

 

 