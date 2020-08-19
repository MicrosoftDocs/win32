---
title: The  size_is Attribute
description: The \ size\_is\ attribute is associated with an integer constant, expression, or variable that specifies the allocation size of the array.
ms.assetid: 5252c1a2-8e07-4e28-8280-6a9563d1b291
keywords:
- size_is
ms.topic: article
ms.date: 05/31/2018
---

# The \[size\_is\] Attribute

The \[ [size\_is](/windows/desktop/Midl/size-is)\] attribute is associated with an integer constant, expression, or variable that specifies the allocation size of the array. Consider a character array whose length is determined by user input:

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(2.0)
]
interface arraytest
{
  void fArray2([in] short sSize,
               [in, out, size_is(sSize)] char achArray[*]);
}
```

> [!Note]  
> The asterisk (\*) that marks the placeholder for the variable-array dimension is optional.

 

The server stub must allocate memory on the server that corresponds to the memory on the client for that parameter. The variable that specifies the size must always be at least an \[ [in](/windows/desktop/Midl/in)\] parameter. The **\[in\]** directional attribute is required so that the size value is defined on entry to the server stub. This size value provides information that the server stub requires to allocate the memory.

The size parameter can also be \[in, [out](/windows/desktop/Midl/out-idl)\]. This is useful if, for instance, the array the client sends is not large enough for the data that the server needs to store in it. You can use an **\[in, out\]** size parameter to send the required size back to the client program.

## Related topics

<dl> <dt>

[Multiple Levels of Pointers](multiple-levels-of-pointers.md)
</dt> </dl>

 

 