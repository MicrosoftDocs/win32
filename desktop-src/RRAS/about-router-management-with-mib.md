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
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# About Router Management with MIB

The Management Information Base (MIB) APIs for router management makes it possible to query and set the values of MIB variables exported by one of the router managers or any of the routing protocols that the router managers service. By using this API, the router supports the Simple Network Management Protocol (SNMP).

In the SNMP framework, each of the manageable objects in the router is represented by a variable that has a unique Object Identifier (OID). Corresponding to each OID is a value that represents the current state of the object. The collection of OIDs and values is referred to as a Management Information Base (MIB). The MprAdminMib calls allow a developer to specify an object by its OID and either query or write ("Set") the object's value.

To query and set MIB variables, the module that services the calls must define a set of data structures. These data structures include structures to use as Object Identifiers and structures that hold the values of the MIB variables being accessed. These data structures are opaque to all but the caller of the MIB function and the module servicing the call.

The module servicing the MIB call is a router manager or one of the routing protocols. The caller must specify a router manager even if the call is handled by one of the routing protocols. In such a case, the caller should specify the router manager that corresponds to the protocol family for that routing protocol. For example, if the Open Shortest Path First (OSPF) routing protocol were handling the MIB call, the caller would need to specify the IP Router Manager, since OSPF belongs to the IP protocol family. In each of the MIB functions, the *dwTransportId* parameter specifies a router manager, and the *RoutingPid* parameter specifies the routing protocol. The router manager also has a unique *RoutingPid*, since some of the MIB variables may be handled by the router manager itself.

The MprAdminMib functions can be called on a computer other than the one being administered. The MprAdminMIB functions that query or write values, take as a parameter a handle to the computer to administer. Use the [**MprAdminMIBServerConnect**](/windows/win32/Mprapi/nf-mprapi-mpradminmibserverconnect?branch=master) function to establish the connection to the remote computer and obtain this handle. After calling the necessary MprAdminMIB functions to accomplish a particular administrative task, call the [**MprAdminMIBServerDisconnect**](/windows/win32/Mprapi/nf-mprapi-mpradminmibserverdisconnect?branch=master) function to terminate the connection to the remote computer.

The [**MprAdminMIBEntryCreate**](/windows/win32/Mprapi/nf-mprapi-mpradminmibentrycreate?branch=master) and [**MprAdminMIBEntrySet**](/windows/win32/Mprapi/nf-mprapi-mpradminmibentryset?branch=master) functions take as parameters an OID and a buffer which contains the new value for the object.

The [**MprAdminMIBEntryGet**](/windows/win32/Mprapi/nf-mprapi-mpradminmibentryget?branch=master), [**MprAdminMIBEntryGetFirst**](/windows/win32/Mprapi/nf-mprapi-mpradminmibentrygetfirst?branch=master) and [**MprAdminMIBEntryGetNext**](/windows/win32/Mprapi/nf-mprapi-mpradminmibentrygetnext?branch=master) functions take as parameters an OID and the address of a pointer variable. On successful return, the pointer variable points to a buffer that contains the value for the object. The caller should free the memory for this buffer by calling the [**MprAdminMIBBufferFree**](/windows/win32/Mprapi/nf-mprapi-mpradminmibbufferfree?branch=master) function.

The [**MprAdminMIBEntryGetFirst**](/windows/win32/Mprapi/nf-mprapi-mpradminmibentrygetfirst?branch=master) and [**MprAdminMIBEntryGetNext**](/windows/win32/Mprapi/nf-mprapi-mpradminmibentrygetnext?branch=master) functions enable a developer to perform an *SNMP walk*. Because the OIDs are ordered, each OID and therefore each manageable object has a *next* OID. An SNMP walk refers to traversing a portion of the MIB by reading or writing a sequence of OIDs.

All MprAdminMib calls pass through the Dynamic Interface Manager (DIM). Depending on the OID, DIM passes the call to one of the router managers. (Both IP and IPX support SNMP). Again, depending on the OID, the router manager may handle the call itself, or pass the call to one of its clients. All router clients are required to implement and export the following functions which correspond to the similarly named MprAdminMIB functions:

-   [**MibCreate**](/windows/win32/Routprot/nc-routprot-pmib_create?branch=master)
-   [**MibDelete**](/windows/win32/Routprot/nc-routprot-pmib_delete?branch=master)
-   [**MibSet**](/windows/win32/Routprot/nc-routprot-pmib_set?branch=master)
-   [**MibGet**](/windows/win32/Routprot/nc-routprot-pmib_get?branch=master)
-   [**MibGetFirst**](/windows/win32/Routprot/nc-routprot-pmib_get_first?branch=master)
-   [**MibGetNext**](/windows/win32/Routprot/nc-routprot-pmib_get_next?branch=master)
-   [**MibGetTrapInfo**](/windows/win32/Routprot/nc-routprot-pmib_get_trap_info?branch=master)
-   [**MibSetTrapInfo**](/windows/win32/Routprot/nc-routprot-pmib_set_trap_info?branch=master)

 

 




