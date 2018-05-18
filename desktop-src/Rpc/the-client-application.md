---
title: The Client Application
description: The example below is from the 'Hello World' application in the RPC\\Hello directory of the Platform Software Development Kit (SDK).
ms.assetid: '8c33801a-341a-4674-bd41-5bdca7e244fb'
---

# The Client Application

The example below is from the 'Hello World' application in the RPC\\Hello directory of the Platform Software Development Kit (SDK). The Helloc.c source file contains a directive to include the MIDL-generated header file, Hello.h. Within Hello.h are directives to include Rpc.h and rpcndr.h, which contain the definitions for the RPC run-time routines, **HelloProc** and **Shutdown**, and data types that the client and server applications use. The MIDL compiler must be used with the example below.

Because the client is managing its connection to the server, the client application calls run-time functions to establish a handle to the server and to release this handle after the remote procedure calls are complete. The function [**RpcStringBindingCompose**](rpcstringbindingcompose.md) combines the components of the binding handle into a string representation of that handle and allocates memory for the string binding. The function [**RpcBindingFromStringBinding**](rpcbindingfromstringbinding.md) creates a server binding handle, **hello\_ClientIfHandle**, for the client application from that string representation.

In the call to [**RpcStringBindingCompose**](rpcstringbindingcompose.md), the parameters do not specify the UUID because this tutorial assumes there is just one implementation of the interface "hello." In addition, the call does not specify a network address because the application will use the default, which is the local host machine. The protocol sequence is a character string that represents the underlying network transport. The endpoint is a name which is specific to the protocol sequence. This example uses named pipes for its network transport, so the protocol sequence is "ncacn\_np". The endpoint name is "\\pipe\\hello".

The actual remote procedure calls, **HelloProc** and **Shutdown**, take place within the RPC exception handler—a set of macros that let you control exceptions that occur outside the application code. If the RPC run-time module reports an exception, control passes to the [**RpcExcept**](rpcexcept.md) block. This is where you would insert code to do any needed cleanup and then exit gracefully. This example program simply informs the user that an exception occurred. If you do not want to use exceptions, you can use the ACF attributes [comm\_status](https://msdn.microsoft.com/library/windows/desktop/aa366754) and [fault\_status](https://msdn.microsoft.com/library/windows/desktop/aa366827) to report errors.

After the remote procedure calls are completed, the client first calls [**RpcStringFree**](rpcstringfree.md) to free the memory that was allocated for the string binding. Note that once the binding handle has been created, a client program can free a string binding at any time. The client next calls [**RpcBindingFree**](rpcbindingfree.md) to release the handle.


```C++
/* file: helloc.c */
#include <stdlib.h>
#include <stdio.h>
#include <ctype.h>
#include "hello.h" 
#include <windows.h>

void main()
{
    RPC_STATUS status;
    unsigned char * pszUuid             = NULL;
    unsigned char * pszProtocolSequence = "ncacn_np";
    unsigned char * pszNetworkAddress   = NULL;
    unsigned char * pszEndpoint         = "\\pipe\\hello";
    unsigned char * pszOptions          = NULL;
    unsigned char * pszStringBinding    = NULL;
    unsigned char * pszString           = "hello, world";
    unsigned long ulCode;
 
    status = RpcStringBindingCompose(pszUuid,
                                     pszProtocolSequence,
                                     pszNetworkAddress,
                                     pszEndpoint,
                                     pszOptions,
                                     &amp;pszStringBinding);
    if (status) exit(status);

    status = RpcBindingFromStringBinding(pszStringBinding, &amp;hello_ClientIfHandle);
 
    if (status) exit(status);
 
    RpcTryExcept  
    {
        HelloProc(pszString);
        Shutdown();
    }
    RpcExcept(1) 
    {
        ulCode = RpcExceptionCode();
        printf("Runtime reported exception 0x%lx = %ld\n", ulCode, ulCode);
    }
    RpcEndExcept
 
    status = RpcStringFree(&amp;pszStringBinding); 
 
    if (status) exit(status);
 
    status = RpcBindingFree(&amp;hello_IfHandle);
 
    if (status) exit(status);

    exit(0);
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



 

 




