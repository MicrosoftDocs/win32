---
title: Procedure Serialization
description: When you use procedure serialization, a procedure is labeled with the \ encode\ or \ decode\ attribute. Instead of generating the usual remote stub, the compiler generates a serialization stub for the routine.
ms.assetid: 98367b00-696b-44c4-a747-92ecac34ba1e
ms.topic: article
ms.date: 05/31/2018
---

# Procedure Serialization

When you use procedure serialization, a procedure is labeled with the \[[**encode**](/windows/desktop/Midl/encode)\] or \[[**decode**](/windows/desktop/Midl/decode)\] attribute. Instead of generating the usual remote stub, the compiler generates a serialization stub for the routine.

Just as a remote procedure must use a binding handle to make a remote call, a serialization procedure must use a serialization handle to use serialization services. If a serialization handle is not specified, a default implicit handle is used to direct the call. On the other hand, if the serialization handle is specified, either as an explicit [**handle\_t**](/windows/desktop/Midl/handle-t) argument of the routine or by using the \[[**explicit\_handle**](/windows/desktop/Midl/explicit-handle)\] attribute, you must pass a valid handle as an argument of the call. For additional information on how to create a valid serialization handle, see [Serialization Handles](serialization-handles.md), [Examples of Fixed Buffer Encoding](fixed-buffer-serialization.md), and [Examples of Incremental Encoding](examples-of-incremental-encoding.md).

> [!Note]
> Microsoft RPC allows remote and serialization procedures to be mixed in one interface. However, use caution when doing so.
> 
> For remote procedures with implicit binding handles, the MIDL compiler generates a global handle variable of type [**handle\_t**](/windows/desktop/Midl/handle-t). Procedures and types with implicit serialization handles use this same global handle variable.
> 
> For implicit handles, the global implicit handle must be set to a valid binding handle before a remote call. The implicit handle must be set to a valid serialization handle before a serialization call. Therefore, a procedure cannot be both remote and serialized. It must be one or the other.

 

 

 