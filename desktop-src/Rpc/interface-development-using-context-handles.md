---
title: Interface Development Using Context Handles
description: Typically, you create a context handle by specifying the \ context\_handle\ attribute on a type definition in the IDL file.
ms.assetid: e4caf91f-f92d-4aef-a20f-0a3073230640
ms.topic: article
ms.date: 05/31/2018
---

# Interface Development Using Context Handles

Typically, you create a context handle by specifying the \[[**context\_handle**](/windows/desktop/Midl/context-handle)\] attribute on a type definition in the IDL file. The type definition also implicitly specifies a context run-down routine, which you must provide. If communication between the client and server breaks down, the server run time invokes this routine to perform any needed cleanup. For more information on context run-down routines, see [Server Context Run-down Routine](server-context-run-down-routine.md).

An interface that uses a context handle must have a binding handle for the initial binding, which has to take place before the server can return a context handle. You can use an automatic, implicit, or explicit binding handle to create the binding and establish the context.

A context handle must be of the [**void \***](/windows/desktop/Midl/void) type, or a type that resolves to [**void \***](/windows/desktop/Midl/void). The server program casts it to the required type.

> [!Note]  
> The use of \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] for context handle parameters is discouraged except for routines that close context handles. If context handles parameters marked \[[**in**](/windows/desktop/Midl/in), [**out**](/windows/desktop/Midl/out-idl)\] are used, do not pass a **NULL** or uninitialized context handle from the client to the server. A **NULL** pointer to a context handle should be passed instead. Please note, context handle parameters marked \[[**in**](/windows/desktop/Midl/in)\] do not accept **NULL** pointers.

 

The following fragment of a sample interface definition shows how a distributed application can use a context handle to have a server open and update a data file for each client.

The interface must contain a remote procedure call to initialize the handle and set it to a non-**null** value. In this example, the RemoteOpen function performs this operation. It specifies the context handle with an \[[**out**](/windows/desktop/Midl/out-idl)\] directional attribute. Alternatively, you could return the context handle as the procedure's return value. However in this example, we'll pass the context handle out through the parameter list.

In this example, the context information is a file handle. It keeps track of the current location in the file. The interface packages the file handle as a context handle and passes it as a parameter to remote procedure calls. A structure contains the file name and the file handle.

``` syntax
/* file: cxhndl.idl (fragment of interface definition file) */
typedef [context_handle] void * PCONTEXT_HANDLE_TYPE;
typedef [ref] PCONTEXT_HANDLE_TYPE * PPCONTEXT_HANDLE_TYPE;
 
short RemoteOpen([out] PPCONTEXT_HANDLE_TYPE pphContext,
    [in, string] unsigned char * pszFile);
 
void RemoteRead(
    [in] PCONTEXT_HANDLE_TYPE phContext,
    [out, size_is(cbBuf)] unsigned char achBuf[],
    [in, out] short *pcbBuf);
 
short RemoteClose([in, out] PPCONTEXT_HANDLE_TYPE pphContext);
```

The RemoteOpen function creates a valid, non-**null** context handle. It passes the context handle to the client. Subsequent remote procedure calls, such as RemoteRead, use the context handle as an in pointer.

In addition to the remote procedure that initializes the context handle, the interface must contain a procedure that frees the server context and sets context handle to **NULL**. In the preceding example, the RemoteClose function performs this operation.

 

 