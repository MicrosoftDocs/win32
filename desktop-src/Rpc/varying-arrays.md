---
title: Varying Arrays
description: In MIDL, varying arrays are fixed in size. They allow clients to pass different portions of arrays from clients to servers. The size of the array portion can vary from invocation to invocation. However, the size of the overall array is fixed.
ms.assetid: 31c4bc63-de55-4937-832e-8dde9bcc47b9
ms.topic: article
ms.date: 05/31/2018
---

# Varying Arrays

In MIDL, varying arrays are fixed in size. They allow clients to pass different portions of arrays from clients to servers. The size of the array portion can vary from invocation to invocation. However, the size of the overall array is fixed.

For instance, the following example shows the definition of a remote procedure in an interface in a MIDL file. The size of the array that the client passes to the server is fixed by the constant ARRAY\_SIZE. The interface specifies the portion of the array that the client passes to the server in the parameters firstElement and chunkSize.

``` syntax
[
    /*Attributes are defined here. */
]
interface MyInterface
{
    const long ARRAY_SIZE = 1000;

    MyRemoteProc(
        [in] long lFirstElement,
        [in] long lChunkSize,
        [in, first_is(lFirstElement), 
          length_is(lChunkSize)] char achArray[ARRAY_SIZE]
    );

    /* Other interface procedures are defined here. */
}
```

The interface definition uses the MIDL attribute \[[**first\_is**](/windows/desktop/Midl/first-is)\] to specify the index number of the first element in the portion of the array that the client passes to the server. The \[[**length\_is**](/windows/desktop/Midl/length-is)\] attribute specifies the total number of array elements that the client passes. For more information on these MIDL attributes, see [Array Attributes](array-attributes.md).

The following code fragment illustrates how a client might invoke the remote procedure defined in the preceding MIDL file.


```C++
long lFirstArrayElementNumber = 20;
long lTotalElementsPassed = 100;
char achCharArray[ARRAY_SIZE];

// Code to store chars in the array goes here.

MyRemoteProc(
    lFirstArrayElementNumber ,
    lTotalElementsPassed , 
    achCharArray);

firstArrayElementNumber = 120;
totalElementsPassed = 200;

MyRemoteProc(
    lFirstArrayElementNumber ,
    lTotalElementsPassed , 
    achCharArray);
```



This fragment calls the remote procedure MyRemoteProc twice. On the first invocation it passes the array elements numbered 20 through 119, as indicated by the values in the variables firstArrayElementNumber and totalElementsPassed. On the second call, the client passes the array elements numbered 120 through 319.

 

 