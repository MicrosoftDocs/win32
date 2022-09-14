---
title: The named_type_free_local Function
description: The stubs call the type\_free\_local function to free the memory allocated by a call to the named\_type\_to\_local routine.
ms.assetid: 8e8c6a46-20c1-483b-b804-0772391e9918
keywords:
- named_type_free_local
ms.topic: article
ms.date: 05/31/2018
---

# The named\_type\_free\_local Function

The stubs call the **type\_free\_local** function to free the memory allocated by a call to the [named\_type\_to\_local](the-named-type-to-local-function.md) routine. It does not free the memory allocated by the stub. The function prototype is defined as:

``` syntax
void __RPC_USER <local_type>_free_local(<named_type> __RPC_FAR *);
```

The parameter is a pointer to the memory allocated by **named\_type\_to\_local**.

 

 




