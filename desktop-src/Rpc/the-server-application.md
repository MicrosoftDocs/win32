---
title: The Server Application
description: View the server application part of a remote procedure call (RPC) example. The example is from the 'Hello World' application in the Platform SDK.
ms.assetid: '82ccfd67-6626-49c4-8974-86ebc5841444'
ms.topic: article
ms.date: 05/31/2018
---

# The Server Application

The example below is from the 'Hello World' application in the RPC\\Hello directory of the Platform Software Development Kit (SDK). The server side of the distributed application informs the system that its services are available. It then waits for client requests. The MIDL compiler must be used with the example below.

Depending on the size of your application and your coding preferences, you can choose to implement remote procedures in one or more separate files. In this tutorial program, the source file Hellos.c contains the main server routine. The file Hellop.c contains the remote procedure.

The benefit of organizing the remote procedures in separate files is that the procedures can be linked with a standalone program to debug the code before it is converted to a distributed application. After the procedures work in the standalone program, you can compile and link the source files containing the remote procedures with the server application. As with the client-application source file, the server-application source file must include the Hello.h header file.

The server calls the RPC run-time functions [**RpcServerUseProtseqEp**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseprotseqep) and [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif) to make binding information available to the client. This example program passes the interface handle name to **RpcServerRegisterIf**. The other parameters are set to **NULL**. The server then calls the [**RpcServerListen**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverlisten) function to indicate that it is waiting for client requests.

The server application must also include the two memory management functions that the server stub calls: [**midl\_user\_allocate**](the-midl-user-allocate-function.md) and [**midl\_user\_free**](the-midl-user-free-function.md). These functions allocate and free memory on the server when a remote procedure passes parameters to the server. In this example program, **midl\_user\_allocate** and **midl\_user\_free** are simply wrappers for the C-library functions [**malloc**](pointers-and-memory-allocation.md) and **free**. (Note that, in the MIDL compiler- generated forward declarations, "MIDL" is uppercase. The header file Rpcndr.h defines midl\_user\_free and midl\_user\_allocate to be MIDL\_user\_free and MIDL\_user\_allocate, respectively.)


```C++
/* file: hellos.c */
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include "hello.h"
#include <windows.h>

void main()
{
    RPC_STATUS status;
    unsigned char * pszProtocolSequence = "ncacn_np";
    unsigned char * pszSecurity         = NULL; 
    unsigned char * pszEndpoint         = "\\pipe\\hello";
    unsigned int    cMinCalls = 1;
    unsigned int    fDontWait = FALSE;
 
    status = RpcServerUseProtseqEp(pszProtocolSequence,
                                   RPC_C_LISTEN_MAX_CALLS_DEFAULT,
                                   pszEndpoint,
                                   pszSecurity); 
 
    if (status) exit(status);
 
    status = RpcServerRegisterIf(hello_ServerIfHandle,  
                                 NULL,   
                                 NULL); 
 
    if (status) exit(status);
 
    status = RpcServerListen(cMinCalls,
                             RPC_C_LISTEN_MAX_CALLS_DEFAULT,
                             fDontWait);
 
    if (status) exit(status);
 }

/******************************************************/
/*         MIDL allocate and free                     */
/******************************************************/
 
void __RPC_FAR * __RPC_USER midl_user_allocate(size_t len)
{
    return(malloc(len));
}
 
void __RPC_USER midl_user_free(void __RPC_FAR * ptr)
{
    free(ptr);
}
```



 

 




