---
title: The  string Attribute in Arrays
description: You can use the \ string\ attribute for one-dimensional character arrays, wide-character arrays, and byte arrays that represent text strings.
ms.assetid: 96cebb84-6123-4bf8-b70b-a4f6d48cce52
keywords:
- string
ms.topic: article
ms.date: 05/31/2018
---

# The \[string\] Attribute in Arrays

You can use the \[ [string](/windows/desktop/Midl/string)\] attribute for one-dimensional character arrays, wide-character arrays, and byte arrays that represent text strings. If you use the **\[string\]** attribute, the client stub uses the C-library functions **strlen** or **wstrlen** to count the number of characters in the string. To avoid possible inconsistencies, MIDL does not let you use the **\[string\]** attribute at the same time as the \[ [first\_is](/windows/desktop/Midl/first-is)\], \[ [last\_is](/windows/desktop/Midl/last-is)\], and \[ [size\_is](/windows/desktop/Midl/size-is)\] attributes.

With null-terminated strings in C, you must allow space for the null character at the end of the string. For example, when declaring a string that will hold up to 80 characters, allocate 81 characters. The following sample IDL file demonstrates how to declare arrays with the **\[string\]** attribute.

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45),
  version(8.0)
]
interface arraytest
{
  void fArray8([in, out, string] char achArray[]);
}
```

 

 