---
title: Persistent Storage on the Server
description: You can optimize your application so the server stub does not free memory on the server at the conclusion of a remote procedure call.
ms.assetid: 340334e2-94ac-4be2-a16d-38bc4c64e7db
ms.topic: article
ms.date: 05/31/2018
---

# Persistent Storage on the Server

You can optimize your application so the server stub does not free memory on the server at the conclusion of a remote procedure call. For example, when a context handle will be manipulated by several remote procedures, you can use the ACF attribute **\[allocate(dont\_free)\]** to retain the allocated memory on the server.

The **\[allocate(dont\_free)\]** attribute is added to the ACF **typedef** declaration in the ACF. For example:

``` syntax
/* ACF file fragment */
typedef [allocate(all_nodes, dont_free)] P_TREE_TYPE;
```

When the **\[allocate(dont\_free)\]** attribute is specified, the tree data structure is allocated, but not freed, by the server stub. When you make the pointers to such persistent data areas available to other routines—for example, by copying the pointers to global variables—the retained data is accessible to other server functions. The **\[allocate(dont\_free)\]** attribute is particularly useful for maintaining persistent pointer structures as part of the server state information associated with a context-handle type.

 

 




