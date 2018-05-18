---
title: The \ max\_is\ Attribute
description: You can specify the valid bounds of the index numbers of an array using the \ max\_is\ attribute.
ms.assetid: 'b629e3cf-544d-47ee-8f8f-b049f693897c'
keywords: ["max_is"]
---

# The \[max\_is\] Attribute

You can specify the valid bounds of the index numbers of an array using the \[[**max\_is**](https://msdn.microsoft.com/library/windows/desktop/aa367074)\] attribute.

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(5.0)
]
interface arraytest
{
  void fArray5([in] short sMax,
               [in, out, max_is(sMax)]  char achArray[]);
}
```

 

 




