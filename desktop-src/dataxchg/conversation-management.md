---
title: Conversation Management
description: This topic discusses conversations between a client and a server.
ms.assetid: 4e5ff1a1-d46a-4e2a-a37c-8df951f2a1ee
keywords:
- Windows User Interface,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),conversations
- DDE (Dynamic Data Exchange),conversations
- data exchange,Dynamic Data Exchange (DDE)
- Windows User Interface,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange Management Library (DDEML),conversations
- DDEML (Dynamic Data Exchange Management Library),conversations
- data exchange,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange (DDE),multiple conversations
- DDE (Dynamic Data Exchange),multiple conversations
- Dynamic Data Exchange Management Library (DDEML),multiple conversations
- DDEML (Dynamic Data Exchange Management Library),multiple conversations
ms.topic: article
ms.date: 05/31/2018
---

# Conversation Management

A conversation between a client and a server is always established at the request of the client. When a conversation is established, each partner receives a handle that identifies the conversation. The partners use this handle in other Dynamic Data Exchange Management Library (DDEML) functions to send transactions and manage the conversation. A client can request a conversation with a single server, or it can request multiple conversations with one or more servers.

The following topics describe how an application establishes new conversations and gets information about existing conversations.

-   [Single Conversations](#single-conversations)
-   [Multiple Conversations](#multiple-conversations)

## Single Conversations

A client application requests a single conversation with a server by calling the [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) function and specifying string handles that identify the strings containing the service name of the server application and the topic name for the conversation. The DDEML responds by sending the [**XTYP\_CONNECT**](xtyp-connect.md) transaction to the Dynamic Data Exchange (DDE) callback function of each server application that either has registered a service name that matches the one specified in **DdeConnect** or has turned service name filtering off by calling [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice). A server can also filter **XTYP\_CONNECT** transactions by specifying the CBF\_FAIL\_CONNECTIONS filter flag in the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function. During the **XTYP\_CONNECT** transaction, the DDEML passes the service name and the topic name to the server. The server must examine the names and return **TRUE** if it supports the service name and topic name pair or **FALSE** if it does not.

If no server responds positively to the client's request to connect, the client receives **NULL** from [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) and no conversation is established. If a server returns **TRUE**, a conversation is established and the client receives a conversation handle — a **DWORD** value that identifies the conversation. The client uses the handle in subsequent DDEML calls to obtain data from the server. The server receives the [**XTYP\_CONNECT\_CONFIRM**](xtyp-connect-confirm.md) transaction (unless the server specified the CBF\_SKIP\_CONNECT\_CONFIRMS filter flag). This transaction passes the conversation handle to the server.

The following example requests a conversation on the System topic with a server that recognizes the service name MyServer. The *hszServName* and *hszSysTopic* parameters are previously created string handles.


```
HCONV hConv;         // conversation handle 
HWND hwndParent;     // parent window handle 
HSZ hszServName;     // service name string handle 
HSZ hszSysTopic;     // System topic string handle 
 
hConv = DdeConnect( 
    idInst,               // instance identifier 
    hszServName,          // service name string handle 
    hszSysTopic,          // System topic string handle 
    (PCONVCONTEXT) NULL); // use default context 
 
if (hConv == NULL) 
{ 
    MessageBox(hwndParent, "MyServer is unavailable.", 
        (LPSTR) NULL, MB_OK); 
    return FALSE; 
} 
```



In the preceding example, [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) causes the DDE callback function of the MyServer application to receive an [**XTYP\_CONNECT**](xtyp-connect.md) transaction.

In the following example, the server responds to the [**XTYP\_CONNECT**](xtyp-connect.md) transaction by comparing the topic name string handle the DDEML passed to the server with each element in the array of topic name string handles the server supports. If the server finds a match, it establishes the conversation.


```
#define CTOPICS 5 
 
HSZ hsz1;                  // string handle passed by DDEML 
HSZ ahszTopics[CTOPICS];   // array of supported topics 
int i;                     // loop counter 
 
// Use a switch statement to examine transaction types. 
// Here is the connect case.
 
    case XTYP_CONNECT: 
        for (i = 0; i < CTOPICS; i++) 
        { 
            if (hsz1 == ahszTopics[i]) 
                return TRUE;   // establish a conversation 
        } 
 
        return FALSE; // Topic not supported; deny conversation.  
 
// Process other transaction types. 
```



If the server returns **TRUE** in response to the [**XTYP\_CONNECT**](xtyp-connect.md) transaction, the DDEML sends an [**XTYP\_CONNECT\_CONFIRM**](xtyp-connect-confirm.md) transaction to the server's DDE callback function. The server can obtain the handle to the conversation by processing this transaction.

A client can establish a wildcard conversation by specifying **NULL** for the service name string handle, the topic name string handle, or both in a call to [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect). If at least one of the string handles is **NULL**, the DDEML sends the [**XTYP\_WILDCONNECT**](xtyp-wildconnect.md) transaction to the callback functions of all DDE applications (except those that filter the **XTYP\_WILDCONNECT** transaction). Each server application should respond by returning a data handle that identifies a null-terminated array of [**HSZPAIR**](/windows/win32/api/ddeml/ns-ddeml-hszpair) structures. If the server application has not called [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice) to register its service names and if filtering is on, the server does not receive **XTYP\_WILDCONNECT** transactions. For more information about data handles, see [Data Management](data-management.md).

The array must contain one structure for each service name and topic name pair that matches the pair specified by the client. The DDEML selects one of the pairs to establish a conversation and returns to the client a handle that identifies the conversation. The DDEML sends the [**XTYP\_CONNECT\_CONFIRM**](xtyp-connect-confirm.md) transaction to the server (unless the server filters this transaction). The following example shows a typical server response to the [**XTYP\_WILDCONNECT**](xtyp-wildconnect.md) transaction.


```
#define CTOPICS 2 
 
UINT uType; 
HSZPAIR ahszp[(CTOPICS + 1)]; 
HSZ ahszTopicList[CTOPICS]; 
HSZ hszServ, hszTopic; 
WORD i, j; 
 
if (uType == XTYP_WILDCONNECT) 
{ 
    // Scan the topic list and create an array of HSZPAIR structures. 
 
    j = 0; 
    for (i = 0; i < CTOPICS; i++) 
    { 
        if (hszTopic == (HSZ) NULL || 
                hszTopic == ahszTopicList[i]) 
        { 
            ahszp[j].hszSvc = hszServ; 
            ahszp[j++].hszTopic = ahszTopicList[i]; 
        } 
    } 
 
    // End the list with an HSZPAIR structure that contains NULL 
    // string handles as its members. 
 
    ahszp[j].hszSvc = NULL; 
    ahszp[j++].hszTopic = NULL; 
 
    // Return a handle to a global memory object containing the 
    // HSZPAIR structures. 
 
    return DdeCreateDataHandle( 
        idInst,          // instance identifier 
        (LPBYTE) &ahszp, // pointer to HSZPAIR array 
        sizeof(HSZ) * j, // length of the array 
        0,               // start at the beginning 
        (HSZ) NULL,      // no item name string 
        0,               // return the same format 
        0);              // let the system own it 
} 
```



Either the client or the server can terminate a conversation at any time by calling the [**DdeDisconnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddedisconnect) function. This function causes the callback function of the partner in the conversation to receive the [**XTYP\_DISCONNECT**](xtyp-disconnect.md) transaction (unless the partner specified the CBF\_SKIP\_DISCONNECTS filter flag). Typically, an application responds to the **XTYP\_DISCONNECT** transaction by using the [**DdeQueryConvInfo**](/windows/desktop/api/Ddeml/nf-ddeml-ddequeryconvinfo) function to obtain information about the conversation that terminated. After the callback function returns from processing the **XTYP\_DISCONNECT** transaction, the conversation handle is no longer valid.

A client application that receives an [**XTYP\_DISCONNECT**](xtyp-disconnect.md) transaction in its DDE callback function can attempt to reestablish the conversation by calling the [**DdeReconnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddereconnect) function. The client must call **DdeReconnect** from within its DDE callback function.

## Multiple Conversations

A client application can use the [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist) function to determine whether any servers of interest are available in the system. A client specifies a service name and topic name when it calls **DdeConnectList**, causing the DDEML to broadcast the [**XTYP\_WILDCONNECT**](xtyp-wildconnect.md) transaction to the DDE callback functions of all servers that match the service name (except those that filter the transaction). A server's callback function should return a data handle that identifies a null-terminated array of [**HSZPAIR**](/windows/win32/api/ddeml/ns-ddeml-hszpair) structures. The array should contain one structure for each service name and topic name pair that matches the pair specified by the client. The DDEML establishes a conversation for each **HSZPAIR** structure filled by the server and returns a conversation list handle to the client. The server receives the conversation handle by way of the [**XTYP\_CONNECT**](xtyp-connect.md) transaction (unless the server filters this transaction).

A client can specify **NULL** for the service name, topic name, or both when it calls [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist). If the service name is **NULL**, all servers in the system that support the specified topic name respond. A conversation is established with each responding server, including multiple instances of the same server. If the topic name is **NULL**, a conversation is established on each topic recognized by each server that matches the service name.

A client can use the [**DdeQueryNextServer**](/windows/desktop/api/Ddeml/nf-ddeml-ddequerynextserver) and [**DdeQueryConvInfo**](/windows/desktop/api/Ddeml/nf-ddeml-ddequeryconvinfo) functions to identify the servers that respond to [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist). **DdeQueryNextServer** returns the next conversation handle in a conversation list, and **DdeQueryConvInfo** fills a [**CONVINFO**](/windows/win32/api/ddeml/ns-ddeml-convinfo) structure with information about the conversation. The client can keep the conversation handles that it needs and discard the rest from the conversation list.

The following example uses [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist) to establish conversations with all servers that support the System topic and then uses the [**DdeQueryNextServer**](/windows/desktop/api/Ddeml/nf-ddeml-ddequerynextserver) and [**DdeQueryConvInfo**](/windows/desktop/api/Ddeml/nf-ddeml-ddequeryconvinfo) functions to obtain the servers' service name string handles and store them in a buffer.


```
HCONVLIST hconvList; // conversation list 
DWORD idInst;        // instance identifier 
HSZ hszSystem;       // System topic 
HCONV hconv = NULL;  // conversation handle 
CONVINFO ci;         // holds conversation data 
UINT cConv = 0;      // count of conv. handles 
HSZ *pHsz, *aHsz;    // point to string handles 
 
// Connect to all servers that support the System topic. 
 
hconvList = DdeConnectList(idInst, NULL, hszSystem, NULL, NULL); 
 
// Count the number of handles in the conversation list. 
 
while ((hconv = DdeQueryNextServer(hconvList, hconv)) != NULL) 
    cConv++; 
 
// Allocate a buffer for the string handles. 
 
hconv = NULL; 
aHsz = (HSZ *) LocalAlloc(LMEM_FIXED, cConv * sizeof(HSZ)); 
 
// Copy the string handles to the buffer. 
 
pHsz = aHsz; 
while ((hconv = DdeQueryNextServer(hconvList, hconv)) != NULL) 
{ 
    DdeQueryConvInfo(hconv, QID_SYNC, (PCONVINFO) &ci); 
    DdeKeepStringHandle(idInst, ci.hszSvcPartner); 
    *pHsz++ = ci.hszSvcPartner; 
} 
 
// Use the handles; converse with the servers. 
 
// Free the memory and terminate the conversations. 
 
LocalFree((HANDLE) aHsz); 
DdeDisconnectList(hconvList); 
```



An application can terminate an individual conversation in a conversation list by calling the [**DdeDisconnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddedisconnect) function. An application can terminate all conversations in a conversation list by calling the [**DdeDisconnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddedisconnectlist) function. Both functions cause the DDEML to send [**XTYP\_DISCONNECT**](xtyp-disconnect.md) transactions to each partner's DDE callback function. **DdeDisconnectList** sends an **XTYP\_DISCONNECT** transaction for each conversation handle in the list.

A client can retrieve a list of the conversation handles in a conversation list by passing an existing conversation list handle to [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist). The enumeration process removes the handles of terminated conversations from the list, and nonduplicate conversations that fit the specified service name and topic name are added.

If [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist) specifies an existing conversation list handle, the function creates a new conversation list that contains the handles of any new conversations and the handles from the existing list.

If duplicate conversations exist, [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist) attempts to prevent duplicate conversation handles in the conversation list. A duplicate conversation is a second conversation with the same server on the same service name and topic name. Two such conversations would have different handles, yet they would identify the same conversation.

 

 




