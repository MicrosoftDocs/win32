---
title: Summary of Memory Allocation Rules
description: The following table summarizes key rules regarding memory allocation.
ms.assetid: 0c1f8398-75e6-45ec-a9f9-9dcdbe21c24d
ms.topic: article
ms.date: 05/31/2018
---

# Summary of Memory Allocation Rules

The following table summarizes key rules regarding memory allocation.



| MIDL element                                                                                                                                           | Description                                                                                                                                                           |
|--------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Top-level \[ [ref](/windows/desktop/Midl/ref)\] pointers                                                                                                                | Must be non-null pointers.                                                                                                                                            |
| Function return value                                                                                                                                  | New memory is always allocated for pointer return values.                                                                                                             |
| \[ [unique](/windows/desktop/Midl/unique), [out](/windows/desktop/Midl/out-idl)\] or \[ [ptr](/windows/desktop/Midl/ptr), out\] pointer                                                                   | Not allowed by MIDL.                                                                                                                                                  |
| Non-top-level \[[unique](/windows/desktop/Midl/unique), [in](/windows/desktop/Midl/in), [out](/windows/desktop/Midl/out-idl)\] or \[[ptr](/windows/desktop/Midl/ptr), in, out\] pointer that changes from null to non-null | Client stubs allocate new memory on client on return.                                                                                                                 |
| Non-top-level \[[unique](/windows/desktop/Midl/unique), [in](/windows/desktop/Midl/in), [out](/windows/desktop/Midl/out-idl)\] pointer that changes from non-null to null                                 | Memory is orphaned on client; client application is responsible for freeing memory and preventing leaks.                                                              |
| Non-top-level \[[ptr](/windows/desktop/Midl/ptr), [in](/windows/desktop/Midl/in), [out](/windows/desktop/Midl/out-idl)\] pointer that changes from non-null to null                                       | Memory will be orphaned on client if not aliased; client application is responsible for freeing and preventing memory leaks in this case.                             |
| \[[ref](/windows/desktop/Midl/ref)\] pointers                                                                                                                           | Client-application layer usually allocates.                                                                                                                           |
| Non-null \[[in](/windows/desktop/Midl/in), [out](/windows/desktop/Midl/out-idl)\] pointer                                                                                                | Stubs attempt to write into existing storage on client. If **\[string\]** and size increases beyond size allocated on the client, it will cause a GP-fault on return. |



 

The following table summarizes the effects of key IDL and ACF attributes on memory management.



| MIDL feature                                                                   | Client issues                                                                                                                                  | Server issues                                                                                                                 |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| \[ [allocate](/windows/desktop/Midl/allocate)(single\_node)\], \[allocate(all\_nodes)\]         | Determines whether one or many calls are made to the memory functions.                                                                         | Same as client, except private memory can often be used for allocate (single\_node) \[in\] and \[in,out\] data.               |
| \[allocate(free)\] or \[allocate(dont\_free)\]                                 | (None; affects server.)                                                                                                                        | Determines whether memory on the server is freed after each remote procedure call.                                            |
| array attributes \[ [max\_is](/windows/desktop/Midl/max-is)\] and \[ [size\_is](/windows/desktop/Midl/size-is)\] | (None; affects server.)                                                                                                                        | Determines size of memory to be allocated.                                                                                    |
| \[ [byte\_count](/windows/desktop/Midl/byte-count)\]                                            | Client must allocate buffer; not allocated or freed by client stubs.                                                                           | ACF parameter attribute determines size of buffer allocated on server.                                                        |
| \[ [enable\_allocate](/windows/desktop/Midl/enable-allocate)\]                                  | Usually, none. However, the client may be using a different memory management environment.                                                     | Server uses a different memory management environment. [**RpcSmAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmallocate) should be used for allocations. |
| \[ [in](/windows/desktop/Midl/in)\]attribute                                                    | Client application responsible for allocating memory for data.                                                                                 | Allocated on server by stubs.                                                                                                 |
| \[ [out](/windows/desktop/Midl/out-idl)\] attribute                                             | Allocated on client by stubs.                                                                                                                  | \[[out](/windows/desktop/Midl/out-idl)\]-only pointer must be \[[ref](/windows/desktop/Midl/ref)\] pointer; allocated on server by stubs.                       |
| \[ [ref](/windows/desktop/Midl/ref)\] attribute                                                 | Memory referenced by pointer must be allocated by client application.                                                                          | Top-level and first-level reference pointers managed by stubs.                                                                |
| \[ [unique](/windows/desktop/Midl/unique)\] attribute                                           | Non-null to null can result in orphaned memory; null to non-null causes client stub to call [midl\_user\_allocate](/windows/desktop/Midl/midl-user-allocate-1). | (Affects client.)                                                                                                             |
| \[ [ptr](/windows/desktop/Midl/ptr)\] attribute                                                 | (See \[ [unique](/windows/desktop/Midl/unique)\].)                                                                                                              | (See \[ [unique](/windows/desktop/Midl/unique)\].)                                                                                             |



 

 

 