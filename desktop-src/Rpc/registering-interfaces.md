---
title: Registering Interfaces
description: Registering a Remote Procedure Call (RPC) interface.
ms.assetid: c22e3fa8-98be-461a-b06d-292d3f655ffc
ms.topic: article
ms.date: 05/31/2018
---

# Registering Interfaces

This section presents a detailed discussion of the process of registering an RPC interface.

The information in this section is presented in the following topics:

-   [Interface Registration Functions](#interface-registration-functions)
-   [Entry-Point Vectors](#entry-point-vectors)
-   [Manager EPVs](#manager-epvs)
-   [Registering a Single Implementation of an Interface](#registering-a-single-implementation-of-an-interface)
-   [Registering Multiple Implementations of an Interface](#registering-multiple-implementations-of-an-interface)
-   [Rules for Invoking Manager Routines](#rules-for-invoking-manager-routines)
-   [Dispatching a Remote Procedure Call to a Server-Manager Routine](#dispatching-a-remote-procedure-call-to-a-server-manager-routine)
-   [Supplying Your Own Object-Inquiry Function](#supplying-your-own-object-inquiry-function)

## Interface Registration Functions

Servers register their interfaces by calling the [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif) function. Complex server programs often support more than one interface. Server applications must call this function once for each interface they support.

Also, servers can support multiple versions of the same interface, each with its own implementation of the interface's functions. If your server program does this, it must provide a set of entry points. An entry point is a manager routine that dispatches calls for a version of an interface. There must be one entry point for each version of the interface. The group of entry points is called an entry point vector. For details, see [Entry-Point Vectors](#entry-point-vectors).

In addition to the standard function [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), RPC also supports other interface registration functions. The [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) function extends the capabilities of **RpcServerRegisterIf** by enabling you to specify a set of registration flags (see [Interface Registration Flags](interface-registration-flags.md)), the maximum number of concurrent remote procedure call requests the server can accept, and the maximum size in bytes of incoming data blocks.

The RPC library also contains a function called [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex). Like the [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif) function, this function registers an interface. Your server program can also use this function to specify a set of registration flags (see [Interface Registration Flags](interface-registration-flags.md)), the maximum number of concurrent remote procedure call requests the server can accept, and a security callback function.

The [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), and [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) functions set values in the internal interface registry table. This table is used to map the interface UUID and object UUIDs to a manager EPV. The manager EPV is an array of function pointers that contains exactly one function pointer for each function prototype in the interface specified in the IDL file.

For information on supplying multiple EPVs to provide multiple implementations of the interface, see [Multiple Interface Implementations](#registering-multiple-implementations-of-an-interface).

The run-time library uses the interface registry table (set by calls to the function [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2)) and the object registry table (set by calls to the function [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype)) to map interface and object UUIDs to the function pointer.

When you want your server program to remove an interface from the RPC run-time library registry, call the [**RpcServerUnregisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterif) function. After the interface is removed from the registry, the RPC run-time library will no longer accept new calls for that interface.

## Entry-point Vectors

The manager entry-point vector (EPV) is an array of function pointers that point to implementations of the functions specified in the IDL file. The number of elements in the array corresponds to the number of functions specified in the IDL file. RPC supports multiple entry-point vectors representing multiple implementations of the functions specified in the interface.

The MIDL compiler automatically generates a manager EPV data type for use in constructing manager EPVs. The data type is named *if-name***\_SERVER\_EPV**, where *if-name* specifies the interface identifier in the IDL file.

The MIDL compiler automatically creates and initializes a default manager EPV on the assumption that a manager routine of the same name exists for each procedure in the interface and is specified in the IDL file.

When a server offers multiple implementations of the same interface, the server must create one additional manager EPV for each implementation. Each EPV must contain exactly one entry point (address of a function) for each procedure defined in the IDL file. The server application declares and initializes one manager EPV variable of type *if-name***\_SERVER\_EPV** for each additional implementation of the interface. To register the EPVs it calls [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) once for each object type it supports.

When the client makes a remote procedure call to the server, the EPV containing the function pointer is selected based on the interface UUID and the object type. The object type is derived from the object UUID by the object-inquiry function or the table-driven mapping controlled by [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype).

## Manager EPVs

By default, the MIDL compiler uses the procedure names from an interface's IDL file to generate a manager EPV, which the compiler places directly into the server stub. This default EPV is statically initialized using the procedure names declared in the interface definition.

To register a manager using the default EPV, specify **NULL** as the value of the *MgrEpv* parameter in a call to either the [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) function. If the routine names used by a manager correspond to those of the interface definition, you can register this manager using the default EPV of the interface generated by the MIDL compiler. You can also register a manager using an EPV that the server application supplies.

A server can (and sometimes must) create and register a non-**null** manager EPV for an interface. To select a server application–supplied EPV, pass the address of an EPV whose value has been declared by the server as the value of the *MgrEpv* a parameter. A non-**null** value for the *MgrEpv* a parameter always overrides a default EPV in the server stub.

The MIDL compiler automatically generates a manager EPV data type (RPC\_MGR\_EPV) for a server application to use in constructing manager EPVs. A manager EPV must contain exactly one entry point (function address) for each procedure defined in the IDL file.

A server must supply a non-**null** EPV in the following cases:

-   When the names of manager routines differ from the procedure names declared in the interface definition
-   When the server uses the default EPV for registering another implementation of the interface

A server declares a manager EPV by initializing a variable of type *if-name***\_SERVER\_EPV** for each implementation of the interface.

## Registering a Single Implementation of an Interface

When a server offers only one implementation of an interface, the server calls [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) only once. In the standard case, the server uses the default manager EPV. (The exception is when the manager uses routine names that differ from those declared in the interface.)

For the standard case, you supply the following values for calls to [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2):

-   Manager EPVs

    To use the default EPV, specify a **null** value for the *MgrEpv* a parameter.

-   Manager type UUID

    When using the default EPV, register the interface with a nil manager type UUID by supplying either a **null** value or a nil UUID for the *MgrTypeUuid* a parameter. In this case, all remote procedure calls, regardless of the object UUID in their binding handle, are dispatched to the default EPV, assuming no [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) calls have been made.

    You can also provide a non-nil manager type UUID. In this case, you must also call the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine.

## Registering Multiple Implementations of an Interface

You can supply more than one implementation of the remote procedure(s) specified in the IDL file. The server application calls [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) to map object UUIDs to type UUIDs and calls [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) to associate manager EPVs with a type UUID. When a remote procedure call arrives with its object UUID, the RPC server run-time library maps the object UUID to a type UUID. The server application then uses the type UUID and the interface UUID to select the manager EPV.

You can also specify your own function to resolve the mapping from object UUID to manager type UUID. You specify the mapping function when you call [**RpcObjectSetInqFn**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsetinqfn).

To offer multiple implementations of an interface, a server must register each implementation by calling [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex) or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) separately. For each implementation a server registers, it supplies the same *IfSpec* a parameter, but a different pair of *MgrTypeUuid* and *MgrEpv* a parameters.

In the case of multiple managers, use [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex) or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) as follows:

-   Manager EPVs

    To offer multiple implementations of an interface, a server must:

    -   Create a non-**null** manager EPV for each additional implementation.
    -   Specify a non-**null** value for the *MgrEpv* a parameter in [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2).

    Please note that the server can also register with the default manager EPV.

-   Manager type UUID

    Provide a manager type UUID for each EPV of the interface. The nil type UUID (or **null** value) for the *MgrTypeUuid* a parameter can be specified for one of the manager EPVs. Each type UUID must be different.

## Rules for Invoking Manager Routines

The RPC run-time library dispatches an incoming remote procedure call to a manager that offers the requested RPC interface. When multiple managers are registered for an interface, the RPC run-time library must select one of them. To select a manager, the RPC run-time library uses the object UUID specified by the call's binding handle.

The run-time library applies the following rules when interpreting the object UUID of a remote procedure call:

-   Nil object UUIDs

    A nil object UUID is automatically assigned the nil type UUID (it is illegal to specify a nil object UUID in the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine). Therefore, a remote procedure call whose binding handle contains a nil object UUID is automatically dispatched to the manager registered with the nil type UUID, if any.

-   Non-nil object UUIDs

    In principle, a remote procedure call whose binding handle contains a non-nil object UUID should be processed by a manager whose type UUID matches the type of the object UUID. However, identifying the correct manager requires that the server has specified the type of that object UUID by calling the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine.

    If a server fails to call the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine for a non-nil object UUID, a remote procedure call for that object UUID goes to the manager EPV that services remote procedure calls with a nil object UUID (that is, the nil type UUID).

    Remote procedure calls with a non-nil object UUID in the binding handle cannot be executed if the server assigned that non-nil object UUID a type UUID by calling the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine, but did not also register a manager EPV for that type UUID by calling [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex) or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2).

The following table summarizes the actions that the run-time library uses to select the manager routine.



| Object UUID of call | Server set type for object UUID? | Server registered EPV type? | Dispatching action                                                                                                                                 |
|---------------------|----------------------------------|-----------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|
| Nil                 | Not applicable                   | Yes                         | Uses the manager with the nil type UUID.                                                                                                           |
| Nil                 | Not applicable                   | No                          | Error (RPC\_S\_UNSUPPORTED\_TYPE); rejects the remote procedure call.                                                                              |
| Non-nil             | Yes                              | Yes                         | Uses the manager with the same type UUID.                                                                                                          |
| Non-nil             | No                               | Ignored                     | Uses the manager with the nil type UUID. If no manager with the nil type UUID, error (RPC\_S\_UNSUPPORTEDTYPE); rejects the remote procedure call. |
| Non-nil             | Yes                              | No                          | Error (RPC\_S\_UNSUPPORTEDTYPE); rejects the remote procedure call.                                                                                |



 

The object UUID of the call is the object UUID found in a binding handle for a remote procedure call.

The server sets the type of the object UUID by calling [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) to specify the type UUID for an object.

The server registers the type for the manager EPV by calling [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex) or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) using the same type UUID.

> [!Note]  
> The nil object UUID is always automatically assigned the nil type UUID. It is illegal to specify a nil object UUID in the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine.

 

## Dispatching a Remote Procedure Call to a Server-manager Routine

The following tables show the steps that the RPC run-time library takes to dispatch a remote procedure call to a server-manager routine.

A simple case where the server registers the default manager EPV, is described in the following tables.

**Interface Registry Table**



| Interface UUID | Manager type UUID | Entry-point vector |
|----------------|-------------------|--------------------|
| *uuid1*        | Nil               | Default EPV        |



 

**Object Registry Table**



| Object UUID             | Object type |
|-------------------------|-------------|
| Nil                     | Nil         |
| (Any other object UUID) | Nil         |



 

**Mapping the Binding Handle to an Entry-point Vector (EPV)**



| Interface UUID (from client binding handle) | Object UUID (from client binding handle) | Object type (from object registry table) | Manager EPV (from interface registry table) |
|---------------------------------------------|------------------------------------------|------------------------------------------|---------------------------------------------|
| *uuid1*                                     | Nil                                      | Nil                                      | Default EPV                                 |
| Same as above                               | *uuidA*                                  | Nil                                      | Default EPV                                 |



 

The following steps describe the actions that the RPC server's run-time library take, as shown in the preceding tables, when a client with interface UUID *uuid1* calls it.

1.  The server calls [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) to associate an interface it offers with the nil manager type UUID and with the MIDL-generated default manager EPV. This call adds an entry in the interface registry table. The interface UUID is contained in the *IfSpec* a parameter.
2.  By default, the object registry table associates all object UUIDs with the nil type UUID. In this example, the server does not call [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype).
3.  The server run-time library receives a remote procedure code containing the interface UUID that the call belongs to and the object UUID from the call's binding handle.

    See the following function reference entries for discussions of how an object UUID is set into a binding handle:

    -   [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina)
    -   [**RpcNsBindingLookupBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindinglookupbegina)
    -   [**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding)
    -   [**RpcBindingSetObject**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetobject)

4.  Using the interface UUID from the remote procedure call, the server's run-time library locates that interface UUID in the interface registry table.

    If the server did not register the interface using [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2), then the remote procedure call returns to the caller with an RPC\_S\_UNKNOWN\_IF status code.

5.  Using the object UUID from the binding handle, the server's run-time library locates that object UUID in the object registry table. In this example, all object UUIDs map to the nil object type.
6.  The server's run-time library locates the nil manager type in the interface registry table.
7.  Combining the interface UUID and nil type in the interface registry table resolves to the default EPV, which contains the server-manager routines to be executed for the interface UUID found in the remote procedure call.

Assume that the server offers multiple interfaces and multiple implementations of each interface, as described in the following tables.

**Interface Registry Table**



| Interface UUID | Manager-type UUID | Entry-point vector |
|----------------|-------------------|--------------------|
| *uuid1*        | Nil               | *epv1*             |
| *uuid1*        | *uuid3*           | *epv4*             |
| *uuid2*        | *uuid4*           | *epv2*             |
| *uuid2*        | *uuid7*           | *epv3*             |



 

**Object Registry Table**



| Object UUID      | Object type |
|------------------|-------------|
| *uuidA*          | *uuid3*     |
| *uuidB*          | *uuid7*     |
| *uuidC*          | *uuid7*     |
| *uuidD*          | *uuid3*     |
| *uuidE*          | *uuid3*     |
| *uuidF*          | *uuid8*     |
| Nil              | Nil         |
| (Any other UUID) | Nil         |



 

**Mapping the Binding Handle to an Entry-point Vector**



| Interface UUID (from client binding handle) | Object UUID (from client binding handle) | Object type (from object registry table) | Manager EPV (from interface registry table) |
|---------------------------------------------|------------------------------------------|------------------------------------------|---------------------------------------------|
| *uuid1*                                     | Nil                                      | Nil                                      | *epv1*                                      |
| *uuid1*                                     | *uuidA*                                  | *uuid3*                                  | *epv4*                                      |
| *uuid1*                                     | *uuidD*                                  | *uuid3*                                  | *epv4*                                      |
| *uuid1*                                     | *uuidE*                                  | *uuid3*                                  | *epv4*                                      |
| *uuid2*                                     | *uuidB*                                  | *uuid7*                                  | *epv3*                                      |
| *uuid2*                                     | *uuidC*                                  | *uuid7*                                  | *epv3*                                      |



 

The following steps describe the actions that the server's run-time library take, as shown in the preceding tables when a client with interface UUID *uuid2* and object UUID *uuidC* calls it.

1.  The server calls [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) to associate the interfaces it offers with the different manager EPVs. The entries in the interface registry table reflect four calls of [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) to offer two interfaces, with two implementations (EPVs) for each interface.
2.  The server calls [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) to establish the type of each object it offers. In addition to the default association of the nil object to a nil type, all other object UUIDs not explicitly found in the object registry table also map to the nil type UUID.

    In this example, the server calls the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine six times.

3.  The server run-time library receives a remote procedure call containing the interface UUID that the call belongs to and an object UUID from the call's binding handle.
4.  Using the interface UUID from the remote procedure call, the server's run-time library locates the interface UUID in the interface registry table.
5.  Using the *uuidC* object UUID from the binding handle, the server's run-time library locates the object UUID in the object registry table and finds that it maps to type *uuid7*.
6.  To locate the manager type, the server's run-time library combines the interface UUID, *uuid2*, and type *uuid7* in the interface registry table. This resolves to *epv3*, which contains the server manager routine to be executed for the remote procedure call.

The routines in *epv2* will never be executed because the server has not called the [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) routine to add any objects with a type UUID of *uuid4* to the object registry table.

A remote procedure call with interface UUID *uuid2* and object UUID *uuidF* returns to the caller with an RPC\_S\_UNKNOWN\_MGR\_TYPE status code because the server did not call [**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif), [**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex), or [**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2) to register the interface with a manager type of *uuid8*.

## Return Values

This function returns one of the following values.



| Value                             | Meaning                      |
|-----------------------------------|------------------------------|
| RPC\_S\_OK                        | Success                      |
| RPC\_S\_TYPE\_ALREADY\_REGISTERED | Type UUID already registered |



 

## Supplying Your Own Object-inquiry Function

Consider a server that manages thousands of objects of many different types. Whenever the server started, the server application would have to call the function [**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype) for every one of the objects, even though clients might refer to only a few of them (or take a long time to refer to them). These thousands of objects are likely to be on disk, so retrieving their types would be time consuming. Also, the internal table that is mapping the object UUID to the manager type UUID would essentially duplicate the mapping maintained with the objects themselves.

For convenience, the RPC function set includes the function [**RpcObjectSetInqFn**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsetinqfn). With this function, you provide your own object-inquiry function.

As an example, you can supply your own object-inquiry function when you map objects 100–199 to type number 1, 200–299 to type number 2, and so on. The object inquiry function can also be extended to a distributed file system, where the server application does not have a list of all the files (object UUIDs) available, or when object UUIDs name files in the file system and you do not want to preload all of the mappings between object UUIDs and type UUIDs.

## Related topics

<dl> <dt>

[**RpcBindingFromStringBinding**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingfromstringbinding)
</dt> <dt>

[**RpcBindingSetObject**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcbindingsetobject)
</dt> <dt>

[**RpcNsBindingExport**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingexporta)
</dt> <dt>

[**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina)
</dt> <dt>

[**RpcNsBindingLookupBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindinglookupbegina)
</dt> <dt>

[**RpcObjectSetType**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcobjectsettype)
</dt> <dt>

[**RpcServerRegisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif)
</dt> <dt>

[**RpcServerRegisterIf2**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterif2)
</dt> <dt>

[**RpcServerRegisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverregisterifex)
</dt> <dt>

[**RpcServerUnregisterIf**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterif)
</dt> <dt>

[**RpcServerUnregisterIfEx**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserverunregisterifex)
</dt> </dl>

 

 




