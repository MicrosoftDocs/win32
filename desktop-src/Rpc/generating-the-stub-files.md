---
title: Generating the Stub Files
description: After defining the client/server interface, you usually develop your client and server source files.
ms.assetid: e4d08bee-ab9a-4426-a1af-72a7d763797f
keywords:
- Remote Procedure Call RPC , tasks, generating stub files
ms.topic: article
ms.date: 05/31/2018
---

# Generating the Stub Files

After defining the client/server interface, you usually develop your client and server source files. Next use a single makefile to generate the stub and header files. Compile and link the client and server applications. However, if this is your first exposure to the distributed computing environment, you may want to invoke the MIDL compiler now to see what MIDL generates before you continue. The MIDL compiler (Midl.exe) is automatically installed when you install the Platform Software Development Kit (SDK).

When you compile these files, make sure that Hello.idl and Hello.acf are in the same directory. The following command will generate the header file Hello.h, and the client and server stubs, Hello\_c.c and Hello\_s.c.

**midl hello.idl**

Notice that Hello.h contains function prototypes for HelloProc and Shutdown, as well as forward declarations for two memory management functions, **midl\_user\_allocate** and **midl\_user\_free**. You will provide these two functions in the server application. If data were being transmitted from the server to the client (by means of an \[**out**\] parameter) you would also need to provide these two memory management functions in the client application.

Note the definitions for the global handle variable, hello\_IfHandle, and the client and server interface handle names, hello\_v1\_0\_c\_ifspec and hello\_v1\_0\_s\_ifspec. The client and server applications will use the interface handle names in run-time calls.

At this point, you don't need to do anything with the stub files Hello\_c.c and hello\_s.c.

``` syntax
/*file: hello.h */
/* this ALWAYS GENERATED file contains the definitions for the interfaces */
/* File created by MIDL compiler version 3.00.06 
/* at Tue Feb 20 11:33:32 1996 */
/* Compiler settings for hello.idl:
    Os, W1, Zp8, env=Win32, ms_ext, c_ext
    error checks: none */
//@@MIDL_FILE_HEADING(  )
#include "Rpc.h"
#include "rpcndr.h"
 
#ifndef __hello_h_
#define __hello_h_
 
#ifdef __cplusplus
extern "C"{
#endif 
 
/* Forward Declarations */ 
 
void __RPC_FAR * __RPC_USER MIDL_user_allocate(size_t);
void __RPC_USER MIDL_user_free( void __RPC_FAR * ); 
 
#ifndef __hello_INTERFACE_DEFINED__
#define __hello_INTERFACE_DEFINED__
 
/****************************************
 * Generated header for interface: hello
 * at Tue Feb 20 11:33:32 1996
 * using MIDL 3.00.06
 ****************************************/
/* [implicit_handle][version][uuid] */ 
 
            /* size is 0 */
void HelloProc( 
    /* [string][in] */ unsigned char __RPC_FAR *pszString);
    /* size is 0 */
void Shutdown( void);
extern handle_t hello_IfHandle;
 
extern RPC_IF_HANDLE hello_v1_0_c_ifspec;
extern RPC_IF_HANDLE hello_v1_0_s_ifspec;
#endif /* __hello_INTERFACE_DEFINED__ */
 
/* Additional Prototypes for ALL interfaces */
/* end of Additional Prototypes */
#ifdef __cplusplus
}
#endif
#endif
```

 

 




