---
title: About Router Management with MIB
description: The Management Information Base (MIB) APIs for router management makes it possible to query and set the values of MIB variables exported by one of the router managers or any of the routing protocols that the router managers service.
ms.assetid: d0fafd82-e7cb-4524-a499-d14830f02b21
keywords:
- Routing, Management Information Base
- Routing, Management Information Base, described
- Management Information Base RRAS
- MIB
- MIB, See Management Information Base
- Management Information Base RRAS
- Management Information Base RRAS , described
ms.topic: article
ms.date: 05/31/2018
---

# About Router Management with MIB

The Management Information Base (MIB) APIs for router management makes it possible to query and set the values of MIB variables exported by one of the router managers or any of the routing protocols that the router managers service. By using this API, the router supports the Simple Network Management Protocol (SNMP).

In the SNMP framework, each of the manageable objects in the router is represented by a variable that has a unique Object Identifier (OID). Corresponding to each OID is a value that represents the current state of the object. The collection of OIDs and values is referred to as a Management Information Base (MIB). The MprAdminMib calls allow a developer to specify an object by its OID and either query or write ("Set") the object's value.

To query and set MIB variables, the module that services the calls must define a set of data structures. These data structures include structures to use as Object Identifiers and structures that hold the values of the MIB variables being accessed. These data structures are opaque to all but the caller of the MIB function and the module servicing the call.

The module servicing the MIB call is a router manager or one of the routing protocols. The caller must specify a router manager even if the call is handled by one of the routing protocols. In such a case, the caller should specify the router manager that corresponds to the protocol family for that routing protocol. For example, if the Open Shortest Path First (OSPF) routing protocol were handling the MIB call, the caller would need to specify the IP Router Manager, since OSPF belongs to the IP protocol family. In each of the MIB functions, the *dwTransportId* parameter specifies a router manager, and the *RoutingPid* parameter specifies the routing protocol. The router manager also has a unique *RoutingPid*, since some of the MIB variables may be handled by the router manager itself.

The MprAdminMib functions can be called on a computer other than the one being administered. The MprAdminMIB functions that query or write values, take as a parameter a handle to the computer to administer. Use the [**MprAdminMIBServerConnect**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibserverconnect) function to establish the connection to the remote computer and obtain this handle. After calling the necessary MprAdminMIB functions to accomplish a particular administrative task, call the [**MprAdminMIBServerDisconnect**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibserverdisconnect) function to terminate the connection to the remote computer.

The [**MprAdminMIBEntryCreate**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentrycreate) and [**MprAdminMIBEntrySet**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentryset) functions take as parameters an OID and a buffer which contains the new value for the object.

The [**MprAdminMIBEntryGet**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentryget), [**MprAdminMIBEntryGetFirst**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentrygetfirst) and [**MprAdminMIBEntryGetNext**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentrygetnext) functions take as parameters an OID and the address of a pointer variable. On successful return, the pointer variable points to a buffer that contains the value for the object. The caller should free the memory for this buffer by calling the [**MprAdminMIBBufferFree**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibbufferfree) function.

The [**MprAdminMIBEntryGetFirst**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentrygetfirst) and [**MprAdminMIBEntryGetNext**](/windows/desktop/api/Mprapi/nf-mprapi-mpradminmibentrygetnext) functions enable a developer to perform an *SNMP walk*. Because the OIDs are ordered, each OID and therefore each manageable object has a *next* OID. An SNMP walk refers to traversing a portion of the MIB by reading or writing a sequence of OIDs.

All MprAdminMib calls pass through the Dynamic Interface Manager (DIM). Depending on the OID, DIM passes the call to one of the router managers. (Both IP and IPX support SNMP). Again, depending on the OID, the router manager may handle the call itself, or pass the call to one of its clients. All router clients are required to implement and export the following functions which correspond to the similarly named MprAdminMIB functions:

-   [**MibCreate**](/windows/desktop/api/Routprot/nc-routprot-pmib_create)
-   [**MibDelete**](/windows/desktop/api/Routprot/nc-routprot-pmib_delete)
-   [**MibSet**](/windows/desktop/api/Routprot/nc-routprot-pmib_set)
-   [**MibGet**](/windows/desktop/api/Routprot/nc-routprot-pmib_get)
-   [**MibGetFirst**](/windows/desktop/api/Routprot/nc-routprot-pmib_get_first)
-   [**MibGetNext**](/windows/desktop/api/Routprot/nc-routprot-pmib_get_next)
-   [**MibGetTrapInfo**](/windows/desktop/api/Routprot/nc-routprot-pmib_get_trap_info)
-   [**MibSetTrapInfo**](/windows/desktop/api/Routprot/nc-routprot-pmib_set_trap_info)

 

 




