---
title: The named_type_free_inst Function
description: The stubs call the named\_type\_free\_inst function to free memory associated with the transmitted type.
ms.assetid: 4b9e10cb-25bb-4f00-86a0-5436e5ac71d9
keywords:
- named_type_free_inst
ms.topic: article
ms.date: 05/31/2018
---

# The named\_type\_free\_inst Function

The stubs call the **named\_type\_free\_inst** function to free memory associated with the transmitted type. The function is defined as:

``` syntax
void __RPC_USER <named_type>_free_inst(<type> __RPC_FAR *)
```

The parameter points to the instance of the transmitted type. This object should not be freed. For a discussion on when to call the function, see [The represent\_as Attribute](the-represent-as-attribute.md).

 

 




