---
title: Name Service
description: This topic discusses how the Dynamic Data Exchange Management Library makes it possible for a server application to register the service names that it supports.
ms.assetid: 4b7e7f43-18aa-4c2e-aa2b-5ce7bb18048f
keywords:
- Windows User Interface,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),name service
- DDE (Dynamic Data Exchange),name service
- data exchange,Dynamic Data Exchange (DDE)
- Windows User Interface,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange Management Library (DDEML),name service
- DDEML (Dynamic Data Exchange Management Library),name service
- data exchange,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange (DDE),service name registration
- DDE (Dynamic Data Exchange),service name registration
- Dynamic Data Exchange Management Library (DDEML),service name registration
- DDEML (Dynamic Data Exchange Management Library),service name registration
- Dynamic Data Exchange (DDE),service name filter
- DDE (Dynamic Data Exchange),service name filter
- Dynamic Data Exchange Management Library (DDEML),service name filter
- DDEML (Dynamic Data Exchange Management Library),service name filter
ms.topic: article
ms.date: 05/31/2018
---

# Name Service

The Dynamic Data Exchange Management Library (DDEML) makes it possible for a server application to register the service names that it supports and to prevent the DDEML from sending [**XTYP\_CONNECT**](xtyp-connect.md) transactions for unsupported service names to the server's Dynamic Data Exchange (DDE) callback function.

The following topics describe the name service.

-   [Service Name Registration](#service-name-registration)
-   [Service Name Filter](#service-name-filter)

## Service Name Registration

By registering its service names with the DDEML, a server informs other DDE applications in the system that a new server is available. A server registers a service name by calling the [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice) function and specifying a string handle that identifies the name. In response, the DDEML sends an [**XTYP\_REGISTER**](xtyp-register.md) transaction to the callback function of each DDEML application in the system (except those that specified the CBF\_SKIP\_REGISTRATIONS filter flag in the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function). The **XTYP\_REGISTER** transaction passes two string handles to a callback function: the first identifies the string specifying the base service name, and the second identifies the string specifying the instance-specific service. A client typically uses the base service name in a list of available servers, so the user can select a server from the list. The client uses the instance-specific service name to establish a conversation with a specific instance of a server application, if more than one instance is running.

A server can use [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice) to unregister a service name. This function causes the DDEML to send [**XTYP\_UNREGISTER**](xtyp-unregister.md) transactions to the other DDE applications in the system, informing them that they can no longer use the name to establish conversations.

A server must call [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice) to register its service names soon after calling [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea). A server must unregister its service names by using **DdeNameService** just before calling the [**DdeUninitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeuninitialize) function.

## Service Name Filter

In addition to registering service names, [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice) enables a server to turn its service name filter on or off. When a server turns off its service name filter, the DDEML sends the [**XTYP\_CONNECT**](xtyp-connect.md) transaction to the server's DDE callback function whenever any client calls the [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) function, regardless of the service name specified in the function. When a server turns on its service name filter, the DDEML sends the **XTYP\_CONNECT** transaction to the server only when **DdeConnect** specifies a service name the server has specified in a call to **DdeNameService**.

By default, the service name filter is on when an application calls [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea). This default prevents the DDEML from sending the [**XTYP\_CONNECT**](xtyp-connect.md) transaction to a server before the server has created the string handles it needs. A server can turn off its service name filter by specifying the DNS\_FILTEROFF flag in a call to [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice). The DNS\_FILTERON flag turns on the filter.

 

 




