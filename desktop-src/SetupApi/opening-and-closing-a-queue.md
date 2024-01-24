---
description: Before you can queue file operations, you must open a file queue. Calling the SetupOpenFileQueue function returns a handle to a queue file. This handle is used by subsequent queue functions to reference the open queue and add operations to it or scan it.
ms.assetid: 3eeb4f34-c89e-4733-8a8c-54e470a1fd30
title: Opening and Closing a Queue
ms.topic: article
ms.date: 05/31/2018
---

# Opening and Closing a Queue

Before you can queue file operations, you must open a file queue. Calling the [**SetupOpenFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenfilequeue) function returns a handle to a queue file. This handle is used by subsequent queue functions to reference the open queue and add operations to it or scan it.

After all the specified file operations have been queued and committed, you must call the [**SetupCloseFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupclosefilequeue) function to release resources allocated during the call to [**SetupOpenFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupopenfilequeue).

> [!Note]  
> The [**SetupCloseFileQueue**](/windows/desktop/api/Setupapi/nf-setupapi-setupclosefilequeue) function does not commit the file queue. Any operations that are uncommitted when **SetupCloseFileQueue** is called will not be performed.

 

 

 



