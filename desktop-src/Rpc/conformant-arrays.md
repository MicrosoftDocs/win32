---
title: Conformant Arrays
description: The size of a conformant array can vary or conform each time the client passes it to a remote procedure on the server.
ms.assetid: b4aaec77-b7ae-495d-8666-4702017e675f
ms.topic: article
ms.date: 05/31/2018
---

# Conformant Arrays

The size of a conformant array can vary or conform each time the client passes it to a remote procedure on the server. The interface definition in the application's MIDL file enables the client to specify the size of the array each time it invokes the remote procedure. Use empty square brackets (\[ \]) or an asterisk in the square brackets (\[\*\]) in the array definition to indicate a conformant array.

The following sample contains the definition of a remote procedure in an interface in a MIDL file. The client specifies the size of the array that it passes to the server by the parameter *arraySize*.

``` syntax
[
    /*Attributes are defined here. */
]
interface MyInterface
{
    MyRemoteProc(
         long lArraySize,
         [size_is(lArraySize)] char achArray[*]
    );

    /* Other interface procedures are defined here. */
}
```

The interface definition uses the MIDL attribute \[[**size\_is**](/windows/desktop/Midl/size-is)\] to specify the size of the array that the client passes to the server. If you would rather indicate the maximum value of the array's index numbers, use the \[[**max\_is**](/windows/desktop/Midl/max-is)\] attribute instead. For more information on these MIDL attributes, see [Array Attributes](array-attributes.md).

The following code fragment illustrates how a client might invoke the remote procedure defined in the preceding MIDL file.


```C++
long lArrayLength = 20;
char achCharArray[20], achAnotherCharArray[200];

// Code to store 20 chars in achCharArray goes here.

MyRemoteProc(
    lArrayLength ,
    achCharArray);

lArrayLength = 200;

// Code to store 200 chars in achAnotherCharArray goes here.

MyRemoteProc(
    lArrayLength ,
    achAnotherCharArray);
```



This fragment calls the remote procedure MyRemoteProc twice. On the first invocation it passes an array of 20 elements. On the second call, the client passes an array of 200 elements.

 

 