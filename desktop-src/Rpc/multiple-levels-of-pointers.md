---
title: Multiple Levels of Pointers
description: Using multiple levels of pointers in Remote Procedure Call (RPC).
ms.assetid: d45b9b20-3b21-4d46-9097-8aacb4e4e921
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Levels of Pointers

When there are multiple levels of pointers, the attributes are associated with the pointer closest to the variable name. The client is still responsible for allocating any memory associated with the response.

The following example allows the stub to call the server without knowing in advance how much data will be returned:

``` syntax
[
    uuid( ...),
    version(3.3),
]
interface AnInterface
{
    HRESULT GetBars([out] long * pSize,
             [out, size_is( , *pSize)]
             BAR ** ppBar);//BAR type defined elsewhere
}
```

In this example, the stub passes the server a unique pointer, which the server initializes to **NULL**. The server then allocates a block of BARs, sets the pointer, sets the size argument and returns. Note that in order for the server to have an effect on the caller you must pass a \[ref\] pointer to a \[[**unique**](/windows/desktop/Midl/unique)\] pointer to your data. Also note the comma in \[[**size\_is**](/windows/desktop/Midl/size-is)( , \*pSize )\], which indicates that the top-level pointer is not a sized pointer, but that the lower-level pointer is.

On the client side, the stub sets \*ppBar to **NULL** before calling the remote procedure. The stub then allocates and unmarshals the arry of BAR objects. The size argument indicates the size of the block (and the number of unmarshaled BARs). The client must free the returned array of BAR objects when it is no longer required.

## Related topics

<dl> <dt>

[**size\_is**](/windows/desktop/Midl/size-is)
</dt> </dl>

 

 