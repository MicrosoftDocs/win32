---
title: Changing Interfaces in a Backward Compatible Manner
description: The methods explained in The Versioning Theory for RPC and COM may be unacceptable for many reasons.
ms.assetid: 7dec4b67-3d50-453f-b0ef-290d091186fd
ms.topic: article
ms.date: 05/31/2018
---

# Changing Interfaces in a Backward Compatible Manner

The methods explained in [The Versioning Theory for RPC and COM](the-versioning-theory-for-rpc-and-com.md) may be unacceptable for many reasons. Changing an interface version according to the rules essentially requires that new clients not communicate with old servers. This is frequently impossible with commercial software deployed in the field. Sometimes, Windows has introduced interface changes absent of changed GUIDs or versions. This was a result of new clients needing to communicate with legacy servers, and because the solution that a new client would support both the old and new interfaces was deemed undesirable.

## Best practice

These are the reasonable methods of working around the wire incompatibility issue when the interface GUID and version cannot be changed.

1.  Have the application be aware of the other side's capabilities.

    The client and server have a protocol that enables each (or at least the new client) to establish the identity of the partner. Typically it is sufficient to have the new client be aware of features supported by old and new servers. This may easily be done when an application holds on to a connection context, and be supported through an *XxxGetInfo* type of function call executed by the client before performing any RPC operations. When an application manages the features on a per-server release basis, a call with an incompatibility to the old server/client can never occur, since the application controls which calls are issued to which server. The bottom line is that the application is proactive in preventing a mismatch from happening. This may be performed in conjunction with the second practice.

2.  Introduce a new remote API.

    A new remote method does not collide with existing methods if it is added at the very end of the interface. Old clients can call new servers as they always have. The new client can call the new method without knowing the server's identity, provided it watches for the errors coming from the server being called. The RPC run time always checks the method number for each interface before a dispatch to ensure the method is within an appropriate v-table. For a method that is unknown to a server, the RPC run time raises the exception RPC\_S\_PROCNUM\_OUT\_OF\_RANGE. This exception is raised only in this particular situation. Therefore, a new client can watch for the exception as a sign that the call went to an old server and can modify its behavior gracefully.

3.  Introduce new parameters or new data types only in the new methods.

    One reason to introduce a new method is to avoid data incompatibility. If a new data type is introduced or simply modified, in principle it should be used only in a new method (or methods). See [Examples of Incompatible Changes](examples-of-incompatible-changes.md) for examples of incompatible data type changes. The only notable exception to this rule is described in item four.

4.  Map new parameters or new data types through a wrapper.

    This solution applies when a new parameter or data type must be exposed to a user, but actually does not have to be remoted separately or can be mapped to the old data types or parameters. For example, many system APIs turn around and execute a remote call. They may or may not be doing some kind of mapping from the user known data types to the data types actually used in the underlying RPC call. It is therefore always worth examining if the change in the user interface needs to propagate as a change to a remote interface.

    A similar situation may happen when the user calls a remote API directly, but a wrapper could be introduced to do a new type mapping or some other additional actions that have become necessary. Interface Definition Language (IDL) has several ways of facilitating such remapping, namely \[[**call\_as**](/windows/desktop/Midl/call-as)\], \[[**transmit\_as**](/windows/desktop/Midl/transmit-as)\], and \[[**wire\_marshal**](/windows/desktop/Midl/wire-marshal)\]. The \[**call\_as**\] attribute introduces a function wrapper on the client and server. Both are placed between the user code and the marshaler. The other attributes deal with direct type mapping. For extension problems, \[**call\_as**\] is the most frequently used, and is easiest to understand and manipulate without pitfalls.

5.  Modify data types through a defaultless union.

    Changing an attribute or data type typically leads to wire incompatibility. See [Examples of Incompatible Changes](examples-of-incompatible-changes.md) for examples. However, in the case of a union without a default clause, the incompatibility may be managed in a way similar to the case of a procedure out of range, as described previously. This scheme is readily applicable to the popular *XxxINFO* types that use unions.

    For example, a call like this

    ```C++
    XxxGetInfo( [in] level, [out] XxxINFO  * pInfo );
    ```

    

    could return information at level 1, 2 or 3, with *XxxINFO* being a union with three branches: 1, 2 and 3.

6.  Use the \[[**range**](/windows/desktop/Midl/range)\] attribute to specify range.

    You can specify the \[[**range**](/windows/desktop/Midl/range)\] attribute on a simple scale type without breaking backward compatibility. This attribute does not affect wire format, but during unmarshalling RPC checks the value on wire to confirm that it is within the range specified in the .idl file. If not, a RPC\_X\_INVALID\_BOUND exception is thrown. This is especially useful if the server knows the maximum size of a sized array.

    For example:

    ```C++
    HRESULT Method1( [in, range(0,100)] ULONG m, [size_is(m)] ULONG *plong); 
    ```

    

The RPC behavior when the indicated level is 4 and the arm is missing, depends on the definition of the union. For a union with the default clause defined, RPC transmits a type indicated in the default clause for anything different than the known arm labels (in this case, anything other than 1, 2 or 3). For a defaultless union, the unmarshaler raises an exception because by definition there is no default to fall back to. The exception is RPC\_S\_INVALID\_TAG.

Again, a new client can adjust its behavior upon discovering that it called an old server.

What follows from these recommended practices is that if a remotable data type must be designed that can be extended in future, use a defaultless union in the IDL file. Given a choice, an encapsulated union is slightly cleaner.

Due to quirks of internal representation of the NDR64 wire protocol, the recommendation for adding arms provided earlier in this section needs to be qualified as follows: The new arm being added cannot change the alignment of the union, and in particular, the biggest alignment of the arms should not change. This is typically not an issue, as a pointer in an arm forces alignment to 8. A design where each arm is a pointer to an arm type is one clean way of satisfying the requirement.

 

 