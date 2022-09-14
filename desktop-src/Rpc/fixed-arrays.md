---
title: Fixed Arrays
description: If your interface specifies an array with a specific number of elements as a parameter, it is using a fixed array. When using MIDL, you define fixed arrays in the same way you define them in C. You specify the array's type, name, and size.
ms.assetid: b9a2fa0b-1386-43e1-ab55-0a57cd8d1f18
ms.topic: article
ms.date: 05/31/2018
---

# Fixed Arrays

If your interface specifies an array with a specific number of elements as a parameter, it is using a fixed array. When using MIDL, you define fixed arrays in the same way you define them in C. You specify the array's type, name, and size.

The following example demonstrates how to define a fixed array.

``` syntax
[
    /*Attributes are defined here. */
]
interface MyInterface
{
    const long ARRAY_SIZE = 1000;

    MyRemoteProc(char achArray[ARRAY_SIZE]);

    /* Other interface procedures are defined here. */
}
```

When a client program passes a fixed array to a server program, the client stub sends the entire array to the server stub. The server stub allocates memory for the array and stores the array data it receives across the network into the allocated memory. It then passes the array to the remote procedure on the server. The server may modify the data in the array.

When the remote procedure terminates, the server stub sends the contents of the array back to the client. The client stub copies the data it received from the server stub into the original array. The client program can then use the data as it would if it received the data from a local procedure call.

 

 




