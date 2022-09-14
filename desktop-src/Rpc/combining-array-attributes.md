---
title: Combining Array Attributes
description: Field attributes can be supplied in various combinations as long as the stub can use the information to determine the size of the array and the number of bytes to transmit to the server.
ms.assetid: ff4f971f-9e46-4454-9d57-d8ebdf70b261
ms.topic: article
ms.date: 05/31/2018
---

# Combining Array Attributes

Field attributes can be supplied in various combinations as long as the stub can use the information to determine the size of the array and the number of bytes to transmit to the server. The relationships between the attributes are defined using the following formulas:

``` syntax
size_is = max_is + 1;
length_is = last_is - first_is + 1;
```

The values associated with the attributes must obey several common-sense rules based on those formulas. These rules are:

-   Do not specify a \[[**first\_is**](/windows/desktop/Midl/first-is)\] index value smaller than zero or a \[[**last\_is**](/windows/desktop/Midl/last-is)\] value greater than \[[**max\_is**](/windows/desktop/Midl/max-is)\].
-   Do not specify a negative size for an array. Define the first and last elements so that they result in a length value of zero or greater. Define the \[[**max\_is**](/windows/desktop/Midl/max-is)\] value so that the size is zero or greater. If MIDL was invoked with the [**/error**](/windows/desktop/Midl/-error) bounds\_check option, then the stub raises an exception when the size is less than zero, or the transmitted length is less than zero.
-   Do not use the \[[**length\_is**](/windows/desktop/Midl/length-is)\] and \[[**last\_is**](/windows/desktop/Midl/last-is)\] attributes at the same time, nor the \[**size\_is**\] and \[**last\_is**\] attributes at the same time.

Because of the close relationship in C between arrays and pointers, MIDL also lets you declare arrays in parameter lists using pointer notation. MIDL treats a parameter that is a pointer to a type as an array of that type if the parameter has any of the attributes commonly associated with arrays.

``` syntax
/* IDL file */
[ 
  uuid(ba209999-0c6c-11d2-97cf-00c04f8eea45)
  version(6.0) 
]
interface arraytest
{
  void fArray6([in] short sSize, 
               [in, out, size_is(sSize)] char * p1);
  void fArray7([in] short sSize, 
               [in, out, size_is(sSize)] char achArray[]);
}
```

In the preceding example, the array and pointer parameters in the functions fArray6 and fArray7 are equivalent.

 

 