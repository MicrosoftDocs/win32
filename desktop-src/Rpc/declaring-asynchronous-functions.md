---
title: Declaring Asynchronous Functions
description: To declare an RPC function as asynchronous, first declare the function as part of an interface definition in an Interface Definition Language (IDL) file.
ms.assetid: 8fc627ce-ccf1-40d9-a540-14461c7fc5e1
keywords:
- Remote Procedure Call RPC , tasks, declaring asynchronous functions
ms.topic: article
ms.date: 05/31/2018
---

# Declaring Asynchronous Functions

To declare an RPC function as asynchronous, first declare the function as part of an interface definition in an Interface Definition Language (IDL) file. The use of asynchronous RPC functions does not require any special alterations to your IDL file. The following example shows an IDL file for an application that uses one asynchronous function.

``` syntax
[ 
    uuid (7f6c4340-eb67-11d1-b9d7-00c04fad9a3b),
    version(1.0),
    pointer_default(unique)
]
interface AsyncRPC
{
    const long DEFAULT_ASYNC_DELAY        = 10000;
    const short APP_ERROR                 = -1;
    const char* DEFAULT_PROTOCOL_SEQUENCE = "ncacn_ip_tcp";
    const char* DEFAULT_ENDPOINT          = "8765";
 
    void NonAsyncFunc(handle_t hBinding,
                      [in, string] unsigned char * pszMessage);
 
    void AsyncFunc(handle_t hBinding,
                   [in] unsigned long nAsychDelay);
 
    void Shutdown(handle_t hBinding);
}
```

For all asynchronous RPC functions that your application uses, you will need to modify the declaration of the asynchronous functions within your application's ACF file. Apply the [**\[async\]**](../midl/async.md) attribute to each asynchronous function name, as shown in the following example:

``` syntax
interface AsyncRPC
{
    [async] AsyncFunc();
}
```

When you apply the **\[async\]** attribute in the ACF file, the MIDL compiler automatically generates an additional asynchronous handle parameter in the stub code.

 

 