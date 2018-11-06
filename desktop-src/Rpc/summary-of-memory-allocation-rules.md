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
| Top-level \[ [ref](https://msdn.microsoft.com/library/windows/desktop/aa367153)\] pointers                                                                                                                | Must be non-null pointers.                                                                                                                                            |
| Function return value                                                                                                                                  | New memory is always allocated for pointer return values.                                                                                                             |
| \[ [unique](https://msdn.microsoft.com/library/windows/desktop/aa367294), [out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\] or \[ [ptr](https://msdn.microsoft.com/library/windows/desktop/aa367149), out\] pointer                                                                   | Not allowed by MIDL.                                                                                                                                                  |
| Non-top-level \[[unique](https://msdn.microsoft.com/library/windows/desktop/aa367294), [in](https://msdn.microsoft.com/library/windows/desktop/aa367051), [out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\] or \[[ptr](https://msdn.microsoft.com/library/windows/desktop/aa367149), in, out\] pointer that changes from null to non-null | Client stubs allocate new memory on client on return.                                                                                                                 |
| Non-top-level \[[unique](https://msdn.microsoft.com/library/windows/desktop/aa367294), [in](https://msdn.microsoft.com/library/windows/desktop/aa367051), [out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\] pointer that changes from non-null to null                                 | Memory is orphaned on client; client application is responsible for freeing memory and preventing leaks.                                                              |
| Non-top-level \[[ptr](https://msdn.microsoft.com/library/windows/desktop/aa367149), [in](https://msdn.microsoft.com/library/windows/desktop/aa367051), [out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\] pointer that changes from non-null to null                                       | Memory will be orphaned on client if not aliased; client application is responsible for freeing and preventing memory leaks in this case.                             |
| \[[ref](https://msdn.microsoft.com/library/windows/desktop/aa367153)\] pointers                                                                                                                           | Client-application layer usually allocates.                                                                                                                           |
| Non-null \[[in](https://msdn.microsoft.com/library/windows/desktop/aa367051), [out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\] pointer                                                                                                | Stubs attempt to write into existing storage on client. If **\[string\]** and size increases beyond size allocated on the client, it will cause a GP-fault on return. |



 

The following table summarizes the effects of key IDL and ACF attributes on memory management.



| MIDL feature                                                                   | Client issues                                                                                                                                  | Server issues                                                                                                                 |
|--------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------|
| \[ [allocate](https://msdn.microsoft.com/library/windows/desktop/aa366724)(single\_node)\], \[allocate(all\_nodes)\]         | Determines whether one or many calls are made to the memory functions.                                                                         | Same as client, except private memory can often be used for allocate (single\_node) \[in\] and \[in,out\] data.               |
| \[allocate(free)\] or \[allocate(dont\_free)\]                                 | (None; affects server.)                                                                                                                        | Determines whether memory on the server is freed after each remote procedure call.                                            |
| array attributes \[ [max\_is](https://msdn.microsoft.com/library/windows/desktop/aa367074)\] and \[ [size\_is](https://msdn.microsoft.com/library/windows/desktop/aa367164)\] | (None; affects server.)                                                                                                                        | Determines size of memory to be allocated.                                                                                    |
| \[ [byte\_count](https://msdn.microsoft.com/library/windows/desktop/aa366744)\]                                            | Client must allocate buffer; not allocated or freed by client stubs.                                                                           | ACF parameter attribute determines size of buffer allocated on server.                                                        |
| \[ [enable\_allocate](https://msdn.microsoft.com/library/windows/desktop/aa366808)\]                                  | Usually, none. However, the client may be using a different memory management environment.                                                     | Server uses a different memory management environment. [**RpcSmAllocate**](/windows/desktop/api/Rpcndr/nf-rpcndr-rpcsmallocate) should be used for allocations. |
| \[ [in](https://msdn.microsoft.com/library/windows/desktop/aa367051)\]attribute                                                    | Client application responsible for allocating memory for data.                                                                                 | Allocated on server by stubs.                                                                                                 |
| \[ [out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\] attribute                                             | Allocated on client by stubs.                                                                                                                  | \[[out](https://msdn.microsoft.com/library/windows/desktop/aa367136)\]-only pointer must be \[[ref](https://msdn.microsoft.com/library/windows/desktop/aa367153)\] pointer; allocated on server by stubs.                       |
| \[ [ref](https://msdn.microsoft.com/library/windows/desktop/aa367153)\] attribute                                                 | Memory referenced by pointer must be allocated by client application.                                                                          | Top-level and first-level reference pointers managed by stubs.                                                                |
| \[ [unique](https://msdn.microsoft.com/library/windows/desktop/aa367294)\] attribute                                           | Non-null to null can result in orphaned memory; null to non-null causes client stub to call [midl\_user\_allocate](https://msdn.microsoft.com/library/windows/desktop/aa367095). | (Affects client.)                                                                                                             |
| \[ [ptr](https://msdn.microsoft.com/library/windows/desktop/aa367149)\] attribute                                                 | (See \[ [unique](https://msdn.microsoft.com/library/windows/desktop/aa367294)\].)                                                                                                              | (See \[ [unique](https://msdn.microsoft.com/library/windows/desktop/aa367294)\].)                                                                                             |



 

 

 




