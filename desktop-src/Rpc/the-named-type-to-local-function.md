---
title: The named_type_to_local Function
description: The stubs call the named\_type\_to\_local function to convert data from a transmitted type to the type that they present to the application.
ms.assetid: c272cc1f-e47b-4d5a-a4e2-cefeaeb8c175
keywords:
- named_type_to_local
ms.topic: article
ms.date: 05/31/2018
---

# The named\_type\_to\_local Function

The stubs call the **named\_type\_to\_local** function to convert data from a transmitted type to the type that they present to the application. The function is defined as:

``` syntax
void __RPC_USER <named_type>_to_local( 
    <named_type> __RPC_FAR * _RPC_FAR * , 
    <local_type> __RPC_FAR * );
```

The first parameter points to the transmitted data. The function sets the second parameter to point to the presented data.

The **named\_type\_to\_local** function must manage memory for the presented type. The function must allocate memory for the entire data structure that starts at the address indicated by the second parameter, except for the parameter itself (the stub allocates memory for the root node and passes it to the function). The value of the second parameter cannot change during the call. The function can change the contents at that address.

 

 




