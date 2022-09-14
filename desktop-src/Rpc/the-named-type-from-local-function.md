---
title: The named_type_from_local Function
description: The stubs call the named\_type\_from\_local function.
ms.assetid: ba35e2fb-957e-4e62-b0d4-ae76e30fa343
keywords:
- named_type_from_local
ms.topic: article
ms.date: 05/31/2018
---

# The named\_type\_from\_local Function

The stubs call the named\_type\_from\_local function. It converts the type that the application uses into the type the stubs transmit across the network. The function is defined as:

``` syntax
void __RPC_USER <named_type>_from_local ( 
    <local_type> __RPC_FAR *, <named_type> __RPC_FAR * __RPC_FAR *);
```

The first parameter is a pointer to the application data. The second parameter is a pointer to a pointer. The function points it to the transmitted data. The function must allocate memory for the transmitted type.

 

 




