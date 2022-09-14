---
title: Client Development Using Context Handles
description: The only use a client program has for a context handle is to pass it to the server each time the client makes a remote procedure call.
ms.assetid: fcbdfb1e-4f1e-4d22-9a3e-cf5a29d300d0
ms.topic: article
ms.date: 05/31/2018
---

# Client Development Using Context Handles

The only use a client program has for a context handle is to pass it to the server each time the client makes a remote procedure call. The client application does not need to access the contents of the handle. It should not try to change the context handle data in any way. The remote procedures that the client invokes perform all necessary operations on the server's context.

Prior to requesting a context handle from a server, clients must establish a binding with the server. The client may use an automatic, implicit, or explicit binding handle. With a valid binding handle, the client can call a remote procedure on the server that either returns an opened (non-**NULL**) context handle or passes one through an **\[out\]** parameter in the remote procedure's parameter list.

Clients may use opened context handles in any way they require. They should, however, invalidate the handle when they no longer need it. There are two way to do this:

-   To invoke a remote procedure offered by the server program that frees the context and closes the context handle (sets it to **NULL**).
-   When the server is unreachable, call the [**RpcSsDestroyClientContext**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcssdestroyclientcontext) function.

The second approach only cleans up the client side state, and does not clean up the server-side state, so it should be used only when network partition is suspected, and the client and the server will do an independent cleanup. The server performs independent cleanup through the run-down routine, the client does so using the [**RpcSsDestroyClientContext**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcssdestroyclientcontext) function.

The following code fragment presents an example of how a client might use a context handle. To view the definition of the interface that this example uses, see [Interface Development Using Context Handles](interface-development-using-context-handles.md). For the server implementation, see [Server Development Using Context Handles](server-development-using-context-handles.md).

In this example, the client calls RemoteOpen to obtain a context handle that contains valid data. The client can then use the context handle in remote procedure calls. Because it no longer needs the binding handle, the client can free the explicit handle it used to create the context handle:


```C++
// cxhndlc.c  (fragment of client side application)
printf("Calling the remote procedure RemoteOpen\n");
if (RemoteOpen(&phContext, pszFileName) < 0) 
{
    printf("Unable to open %s\n", pszFileName);
    Shutdown();
    exit(2);
}
 
// Now the context handle also manages the binding.
// The variable hBindingHandle is a valid binding handle.
status = RpcBindingFree(&hBindingHandle);
printf("RpcBindingFree returned 0x%x\n", status);
if (status) 
    exit(status);
```



The client application in this example uses a procedure called RemoteRead to read a data file on the server until it encounters an end of file. It then closes the file by calling RemoteClose. The context handle appears as a parameter in the RemoteRead and RemoteClose functions as:


```C++
printf("Calling the remote procedure RemoteRead\n");
do 
{
    cbRead = 1024; // Using a 1K buffer
    RemoteRead(phContext, pbBuf, &cbRead);
    // cbRead contains the number of bytes actually read.
    for (int i = 0; i < cbRead; i++)
        putchar(*(pbBuf+i));
} while(cbRead);
 
printf("Calling the remote procedure RemoteClose\n");
if (RemoteClose(&phContext) < 0 ) 
{
    printf("Close failed on %s\n", pszFileName);
    exit(2);
}
```



 

 




