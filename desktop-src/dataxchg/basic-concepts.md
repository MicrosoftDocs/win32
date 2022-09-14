---
title: Basic Concepts
description: This topic discusses key concepts concerning dynamic data exchange.
ms.assetid: 37826d83-4dcd-484f-b1aa-87bf309c5c09
keywords:
- Windows User Interface,Dynamic Data Exchange (DDE)
- Windows User Interface,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange (DDE),client server interaction
- DDE (Dynamic Data Exchange),client server interaction
- data exchange,Dynamic Data Exchange (DDE)
- data exchange,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange (DDE),client applications
- DDE (Dynamic Data Exchange),client applications
- Dynamic Data Exchange (DDE),server applications
- DDE (Dynamic Data Exchange),server applications
- Dynamic Data Exchange (DDE),callback functions
- DDE (Dynamic Data Exchange),callback functions
- Dynamic Data Exchange (DDE),transactions
- DDE (Dynamic Data Exchange),transactions
- Dynamic Data Exchange (DDE),service names
- DDE (Dynamic Data Exchange),service names
- Dynamic Data Exchange (DDE),item names
- DDE (Dynamic Data Exchange),item names
- Dynamic Data Exchange (DDE),topic names
- DDE (Dynamic Data Exchange),topic names
- Dynamic Data Exchange (DDE),System topic
- DDE (Dynamic Data Exchange),System topic
- Dynamic Data Exchange Management Library (DDEML),initialization
- DDEML (Dynamic Data Exchange Management Library),initialization
- Dynamic Data Exchange Management Library (DDEML),callback functions
- DDEML (Dynamic Data Exchange Management Library),callback functions
- Dynamic Data Exchange Management Library (DDEML),string management
- DDEML (Dynamic Data Exchange Management Library),string management
ms.topic: article
ms.date: 05/31/2018
---

# Basic Concepts (DDE)

These concepts are key to understanding Dynamic Data Exchange (DDE) and the Dynamic Data Exchange Management Library (DDEML).

-   [Client and Server Interaction](#client-and-server-interaction)
-   [Transactions and the DDE Callback Function](#transactions-and-the-dde-callback-function)
-   [Service Names, Topic Names, and Item Names](#service-names-topic-names-and-item-names)
-   [System Topic](#system-topic)
-   [Initialization](#initialization)
-   [Callback Function](#callback-function)
-   [String Management](#string-management)
-   [DDEML and Threads](#ddeml-and-threads)

## Client and Server Interaction

DDE always occurs between a client application and a server application. The *DDE client application* initiates the exchange by establishing a conversation with the server to send transactions to the server. A transaction is a request for data or services. The *DDE server application* responds to transactions by providing data or services to the client. For example, a graphics application might contain a bar graph representing a corporation's quarterly profits, but the data for the bar graph might be contained in a spreadsheet application. To obtain the latest profit figures, the graphics application (the client) could establish a conversation with the spreadsheet application (the server). The graphics application could then send a transaction to the spreadsheet application, requesting the latest profit figures.

A server can have many clients at the same time, and a client can request data from multiple servers. An application can also be both a client and a server. Either the client or the server can terminate the conversation at any time.

## Transactions and the DDE Callback Function

The DDEML notifies an application about DDE activity that affects the application by sending transactions to the application's DDE callback function. A *DDE transaction* is similar to a message   it is a named constant accompanied by other parameters that contain additional information about the transaction.

The DDEML passes a transaction to an application-defined DDE callback function that carries out an action appropriate to the type of transaction. For example, when a client application attempts to establish a conversation with a server application, the client calls the [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) function. This function causes the DDEML to send an [**XTYP\_CONNECT**](xtyp-connect.md) transaction to the server's DDE callback function. The callback function can allow the conversation by returning **TRUE** to the DDEML, or it can deny the conversation by returning **FALSE**. For a detailed discussion of transactions, see [Transaction Management](transaction-management.md).

## Service Names, Topic Names, and Item Names

A DDE server uses a three-level hierarchy   service name (called "application name" in previous DDE documentation), topic name, and item name   to uniquely identify a unit of data the server can exchange during a conversation.

A *service name* is a string a server application responds to when a client attempts to establish a conversation with the server. A client must specify this service name to establish a conversation with the server. Although a server can respond to many service names, most servers respond to only one name.

A *topic name* is a string that identifies a logical data context. For servers that operate on file-based documents, topic names are typically filenames; for other servers, they are other application-specific strings. A client must specify a topic name along with a server's service name when it attempts to establish a conversation with a server.

An *item name* is a string that identifies a unit of data a server can pass to a client during a transaction. For example, an item name might identify an integer, a string, several paragraphs of text, or a bitmap.

The service, topic, and item names enable the client to establish a conversation with a server and to receive data from the server.

## System Topic

The System topic provides a context for information of general interest to any DDE client. It is recommended that server applications support the System topic at all times. The System topic is defined in the DDEML.H header file as SZDDESYS\_TOPIC.

To determine which servers are present and the kinds of information they can provide, a client application can request a conversation on the System topic upon starting, setting the device name to **NULL**. Such wildcard conversations are costly in terms of system performance, so they should be kept to a minimum. For more information about initiating DDE conversations, see [Conversation Management](conversation-management.md).

A server must support the following item names within the System topic and any other item names that are useful to a client.



| Item                     | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|--------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SZDDE\_ITEM\_ITEMLIST    | A list of the items supported under a non-System topic. (This list can vary from moment to moment and from topic to topic.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| SZDDESYS\_ITEM\_FORMATS  | A tab-delimited list of strings representing all clipboard formats potentially supported by the service application. Strings that represent predefined clipboard formats are equivalent to the CF\_ values with the "CF\_" prefix removed. For example, the CF\_TEXT format is represented by the string "TEXT". These strings must be uppercase to further identify them as predefined formats. The list of formats must appear in the order of most rich in content to least rich in content. For more information about clipboard formats and rendering data, see [Clipboard](clipboard.md).<br/> |
| SZDDESYS\_ITEM\_HELP     | User-readable information of general interest. This item must contain, at a minimum, information on how to use the server application's DDE features. This information can include, but is not limited to, how to specify items within topics, what execute strings the server can perform, what poke transactions are allowed, and how to find help on other System topic items.                                                                                                                                                                                                                           |
| SZDDESYS\_ITEM\_RTNMSG   | Supporting detail for the most recently used [**WM\_DDE\_ACK**](wm-dde-ack.md) message. This item is useful when more than 8 bits of application-specific return data are required.                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SZDDESYS\_ITEM\_STATUS   | An indication of the current status of the server. Typically, this item supports only the CF\_TEXT format and contains the Ready or Busy string.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SZDDESYS\_ITEM\_SYSITEMS | A list of the items supported under the System topic by this server.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SZDDESYS\_ITEM\_TOPICS   | A list of the topics supported by the server at the current time. (This list can vary from moment to moment.)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |



 

These item names are values defined in the DDEML.H header file. To obtain string handles to these strings, an application must use the DDEML string-management functions, just as it would for any other string in a DDEML application. For more information about managing strings, see [String Management](#string-management).

## Initialization

Before calling any other DDEML function, an application must call the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function. **DdeInitialize** obtains an instance identifier for the application, registers the application's DDE callback function with the DDE, and specifies the transaction filter flags for the callback function.

Each instance of an application or a DLL must pass its instance identifier as the *idInst* parameter to any other DDEML function that requires it. The purpose of multiple DDEML instances is to support DLLs that must use the DDEML at the same time an application is using it. An application must not use more than one instance of the DDEML.

*Transaction filters* optimize system performance by preventing the DDEML from passing unwanted transactions to the application's DDE callback function. An application sets the transaction filters in the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) *ufCmd* parameter. An application must specify a transaction filter flag for each type of transaction that it does not process in its callback function. An application can change its transaction filters with a subsequent call to **DdeInitialize**. For more information about transactions, see [Transaction Management](transaction-management.md).

The following example shows how to initialize an application to use the DDEML.


```
DWORD idInst = 0; 
HINSTANCE hinst; 
 
DdeInitialize(&idInst,         // receives instance identifier 
    (PFNCALLBACK) DdeCallback, // pointer to callback function 
    CBF_FAIL_EXECUTES |        // filter XTYPE_EXECUTE 
    CBF_SKIP_ALLNOTIFICATIONS, // filter notifications 
    0); 
```



An application must call the [**DdeUninitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeuninitialize) function when it is no longer going to use the DDEML. This function terminates any conversations currently open for the application and frees the DDEML resources the system allocated for the application.

## Callback Function

An application that uses the DDEML must provide a callback function that processes the DDE events affecting the application. The DDEML notifies an application of such events by sending transactions to the application's DDE callback function. The transactions a callback function receives depend on which callback filter flags the application specified in [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) and whether the application is a client, a server, or both. For more information, please see [**DdeCallback**](/windows/win32/api/ddeml/nc-ddeml-pfncallback).

The following example shows the general structure of a callback function for a typical client application.


```
HDDEDATA CALLBACK DdeCallback(uType, uFmt, hconv, hsz1, 
    hsz2, hdata, dwData1, dwData2) 
UINT uType;       // transaction type 
UINT uFmt;        // clipboard data format 
HCONV hconv;      // handle to conversation 
HSZ hsz1;         // handle to string 
HSZ hsz2;         // handle to string 
HDDEDATA hdata;   // handle to global memory object 
DWORD dwData1;    // transaction-specific data 
DWORD dwData2;    // transaction-specific data 
{ 
    switch (uType) 
    { 
        case XTYP_REGISTER: 
        case XTYP_UNREGISTER: 
            . 
            . 
            . 
            return (HDDEDATA) NULL; 
 
        case XTYP_ADVDATA: 
            . 
            . 
            . 
            return (HDDEDATA) DDE_FACK; 
 
        case XTYP_XACT_COMPLETE: 
            
            // 
            
            return (HDDEDATA) NULL; 
 
        case XTYP_DISCONNECT: 
            
            // 
            
            return (HDDEDATA) NULL; 
 
        default: 
            return (HDDEDATA) NULL; 
    } 
} 
```



The *uType* parameter specifies the transaction type sent to the callback function by the DDEML. The values of the remaining parameters depend on the transaction type. The transaction types and the events that generate them are described in the following topics. For detailed information about each transaction type, see [Transaction Management](transaction-management.md).

## String Management

To carry out a DDE task, many DDEML functions require access to strings. For example, a client must specify a service name and a topic name when it calls the [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) function to request a conversation with a server. An application specifies a string by passing a string handle (HSZ) rather than a pointer in a DDEML function. A *string handle* is a **DWORD** value, assigned by the system, that identifies a string.

An application can obtain a string handle to a particular string by calling the [**DdeCreateStringHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatestringhandlea) function. This function registers the string with the system and returns a string handle to the application. The application can pass the handle to DDEML functions that must access the string. The following example obtains string handles to the System topic string and the service name string.


```
HSZ hszServName; 
HSZ hszSysTopic; 
hszServName = DdeCreateStringHandle( 
    idInst,         // instance identifier 
    "MyServer",     // string to register 
    CP_WINANSI);    // Windows ANSI code page 
 
hszSysTopic = DdeCreateStringHandle( 
    idInst,         // instance identifier 
    SZDDESYS_TOPIC, // System topic 
    CP_WINANSI);    // Windows ANSI code page 
    
```



The *idInst* parameter in the preceding example specifies the instance identifier obtained by the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function.

An application's DDE callback function receives one or more string handles during most DDE transactions. For example, a server receives two string handles during the [**XTYP\_REQUEST**](xtyp-request.md) transaction: one identifies a string specifying a topic name, and the other identifies a string specifying an item name. An application can obtain the length of the string that corresponds to a string handle and copy the string to an application-defined buffer by calling the [**DdeQueryString**](/windows/desktop/api/Ddeml/nf-ddeml-ddequerystringa) function, as shown in the following example.


```
DWORD idInst; 
DWORD cb; 
HSZ hszServ; 
PSTR pszServName; 
cb = DdeQueryString(idInst, hszServ, (LPSTR) NULL, 0, 
    CP_WINANSI) + 1; 
pszServName = (PSTR) LocalAlloc(LPTR, (UINT) cb); 
DdeQueryString(idInst, hszServ, pszServName, cb, CP_WINANSI); 
```



An instance-specific string handle cannot be mapped from string handle to string and back to string handle. For instance, although [**DdeQueryString**](/windows/desktop/api/Ddeml/nf-ddeml-ddequerystringa) creates a string from a string handle and then [**DdeCreateStringHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatestringhandlea) creates a string handle from that string, the two handles are not the same, as shown in the following example.


```
DWORD idInst; 
DWORD cb; 
HSZ hszInst, hszNew; 
PSZ pszInst; 
DdeQueryString(idInst, hszInst, pszInst, cb, CP_WINANSI); 
hszNew = DdeCreateStringHandle(idInst, pszInst, CP_WINANSI); 
// hszNew != hszInst ! 
```



To compare the values of two string handles, use the [**DdeCmpStringHandles**](/windows/desktop/api/Ddeml/nf-ddeml-ddecmpstringhandles) function.

A string handle passed to an application's DDE callback function becomes invalid when the callback function returns. An application can save a string handle for use after the callback function returns by using the [**DdeKeepStringHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddekeepstringhandle) function.

When an application calls [**DdeCreateStringHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatestringhandlea), the system enters the specified string into a string table and generates a handle that it uses to access the string. The system also maintains a usage count for each string in the string table.

When an application calls [**DdeCreateStringHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatestringhandlea) and specifies a string that already exists in the table, the system increments the usage count rather than adding another occurrence of the string. (An application can also increment the usage count by using [**DdeKeepStringHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddekeepstringhandle).) When an application calls the [**DdeFreeStringHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddefreestringhandle) function, the system decrements the usage count.

A string is removed from the table when its usage count equals zero. Because more than one application can obtain the handle to a particular string, an application must not free a string handle more times than it has created or retained the handle. Otherwise, the application can cause the string to be removed from the table, denying other applications access to the string.

The DDEML string-management functions are based on the atom manager and are subject to the same size restrictions as are atoms.

## DDEML and Threads

The [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function registers an application with the DDEML, creating a DDEML instance. A DDEML instance is thread-based, associated with the thread that called **DdeInitialize**.

All DDEML function calls for objects belonging to a DDEML instance must be made from the same thread that called [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) to create the instance. If you call a DDEML function from a different thread, the function will fail. You cannot access a DDEML conversation from a thread other than the one that allocated the conversation.

 

