---
title: Procedure Header Descriptor
description: The header has been extended several times over the life of the NDR engine. The current compiler still generates different headers depending on the mode of the compiler. However, more recent headers are a superset of the older ones.
ms.assetid: 05b152b9-bd6d-49d1-8484-d104949c67b1
ms.topic: article
ms.date: 05/31/2018
---

# Procedure Header Descriptor

The header has been extended several times over the life of the NDR engine. The current compiler still generates different headers depending on the mode of the compiler. However, more recent headers are a superset of the older ones.

## The Old –Oi Header

The header has the following format:

``` syntax
handle_type<1> 
Oi_flags<1>
[rpc_flags<4>]
proc_num<2>  
stack_size<2>
[explicit_handle_description<>]
```

Where handle\_type<1> can be one of the values shown in the following table.



| Hex | Handle               |
|-----|----------------------|
| 31  | FC\_BIND\_GENERIC    |
| 32  | FC\_BIND\_PRIMITIVE  |
| 33  | FC\_AUTO\_HANDLE     |
| 34  | FC\_CALLBACK\_HANDLE |
| 0   | (explicit handle)    |



 

If the handle\_type<1> field is nonzero, then the procedure uses an implicit handle of the indicated kind. See the [Handles](handles.md) topic for a more information. If the handle\_type<1> field is zero, the handle used for binding is one of the procedure's parameters.

Explicit handles can be primitive, generic, and context; the last one has the following FC token.



| Hex | Handle            |
|-----|-------------------|
| 30  | FC\_BIND\_CONTEXT |



 

By convention, the handle type for DCOM interfaces is FC\_AUTO\_HANDLE.

The Oi\_flags<1> field is an 8-bit mask of the following flags.



| Hex | Flag                         | Meaning                                  |
|-----|------------------------------|------------------------------------------|
| 01  | Oi\_FULL\_PTR\_USED          | Uses the full pointer package.           |
| 02  | Oi\_RPCSS\_ALLOC\_USED       | Uses the RpcSs memory package.           |
| 04  | Oi\_OBJECT\_PROC             | A procedure in an object interface.      |
| 08  | Oi\_HAS\_RPCFLAGS            | The procedure has nonzero Rpc flags.     |
| 10  | Oi\_\*                       | Overloaded.                              |
| 20  | Oi\_\*                       | Overloaded.                              |
| 40  | Oi\_USE\_NEW\_INIT\_ROUTINES | Uses Windows NT3.5 Beta2+ init routines. |
| 80  |                              | Unused.                                  |



 

The following flags are overloaded.



| Hex | Flag                                    | Meaning                                             |
|-----|-----------------------------------------|-----------------------------------------------------|
| 10  | ENCODE\_IS\_USED                        | Used only in pickling.                              |
| 20  | DECODE\_IS\_USED                        | Used only in pickling.                              |
| 10  | Oi\_IGNORE\_OBJECT\_EXCEPTION\_HANDLING | Not used anymore (old OLE).                         |
| 20  | Oi\_HAS\_COMM\_OR\_FAULT                | In raw RPC only, \[comm \_, fault\_status\].        |
| 20  | Oi\_OBJ\_USE\_V2\_INTERPRETER           | In DCOM only, use [**–Oif**](/windows/desktop/Midl/-oi) interpreter. |



 

The rpc\_flags<4> field describes how to set the **RpcFlags** field of the [**RPC\_MESSAGE**](/windows/desktop/api/RpcdceP/ns-rpcdcep-rpc_message) structure. This field is only present if the Oi\_flags<1> field has Oi\_HAD\_RPCFLAGS set. If this field is not present, then the RPC flags for the remote procedure are zero.

> [!Note]  
> For performance, the async interpreters always have the rpc\_flags<4> field present.

 

The proc\_num<2> field provides the procedure's procedure number.

The stack\_size<2> provides the total size of all parameters on the stack, including any this pointer and/or return value.

The explicit\_handle\_description<> field is described later in this document. This field is not present if the procedure uses an implicit handle.

 

 