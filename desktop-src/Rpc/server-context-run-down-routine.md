---
title: Server Context Run-down Routine
description: If communication breaks down while the server is maintaining context on behalf of the client, a cleanup routine may be needed to clean up the state maintained by the server on behalf of a given client.
ms.assetid: b39654e4-6f03-43a0-8a5d-6f24bd0a529c
ms.topic: article
ms.date: 05/31/2018
---

# Server Context Run-down Routine

If communication breaks down while the server is maintaining context on behalf of the client, a cleanup routine may be needed to clean up the state maintained by the server on behalf of a given client. This cleanup routine is called a *context run-down routine*. When a connection breaks, the server stub and the run-time library will call this routine on every context handle opened by the client.

The context run-down routine is required, and is implicitly declared and named, when you apply the \[**context\_handle**\] attribute to a type definition. The server will not call the context run-down routine if the \[**context\_handle**\] attribute was applied directly to a parameter.

The context run-down routine syntax is:

``` syntax
void __RPC_USER type-id_rundown (type-id);
```

Note that the type name determines the name of the context run-down routine.

The code fragment that follows presents a sample context run-down routine. that calls the RemoteClose procedure used in the example in [Interface Development Using Context Handles](interface-development-using-context-handles.md), [Server Development Using Context Handles](server-development-using-context-handles.md), and [Client Development Using Context Handles](client-development-using-context-handles.md). This procedure closes the file handle, frees the memory associated with the file, and assigns **NULL** to the context handle. Assigning **NULL** is a result of calling the RemoteClose function, and is not necessary in a run-down scenario. The RPC run time cleans up its state regardless of whether the context handle is set to **NULL**.

``` syntax
//file: cxhndp.c (fragment of file containing remote procedures)
//The rundown routine is associated with the context handle type.  
void __RPC_USER PCONTEXT_HANDLE_TYPE_rundown(
    PCONTEXT_HANDLE_TYPE phContext)
{
    printf("Client died with an open file, closing it..\n");
    RemoteClose(&phContext);
    assert(phContext == 0);
}
```

 

 




