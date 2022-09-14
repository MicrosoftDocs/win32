---
title: ' in, out, size_is Prototype'
description: '\ in, out, size\_is\ prototype uses a single-counted character array that is passed from client to server and from server to client.'
ms.assetid: bce9a36f-9f7c-4438-9b5a-15b8877f74c0
ms.topic: article
ms.date: 05/31/2018
---

# \[in, out, size\_is\] Prototype

The following function prototype uses a single-counted character array that is passed both ways: from client to server and from server to client:

``` syntax
#define STRSIZE 500 //maximum string length

void Analyze(
    [in, out, length_is(*pcbSize), size_is(STRSIZE)] char  achInOut[],
    [in, out]  long *pcbSize);
```

As an \[[**in**](/windows/desktop/Midl/in)\] parameter, *achInOut* must point to valid storage on the client side. The developer allocates memory associated with the array on the client side before making the remote procedure call.

The stubs use the \[[**size\_is**](/windows/desktop/Midl/size-is)\] parameter *strsize* to allocate memory on the server and then use the \[[**length\_is**](/windows/desktop/Midl/length-is)\] parameter *pcbSize* to transmit the array elements into this memory. The developer must make sure the client code sets the **\[length\_is\]** variable before calling the remote procedure.

In some situations, using separate parameters instead of a single string for the input and output is more efficient and provides flexibility. This is demonstrated in the next example:

``` syntax
/* client */ 
char achInOut[STRSIZE];
long cbSize;
...
gets_s(achInOut, STRSIZE);       // get patient input
cbSize = strlen(achInOut) + 1;   // transmit '\0' too
Analyze(achInOut, &cbSize);
```

In the previous example, the character array achInOut is also used as an \[[**out**](/windows/desktop/Midl/out-idl)\] parameter. In C, the name of the array is equivalent to the use of a pointer. By default, all top-level pointers are reference pointers — they do not change in value and they point to the same area of memory on the client before and after the call. All memory that the remote procedure accesses must fit the size that the client specifies before the call, or the stubs will generate an exception.

Before returning, the Analyze function on the server must reset the *pcbSize* parameter to indicate the number of elements that the server will transmit to the client as shown:

``` syntax
/* server */ 
Analyze(char * str, long * pcbSize)
{
   ...
   *pcbSize = strlen(str) + 1; // transmit '\0' too
   return;
}
```

 

 