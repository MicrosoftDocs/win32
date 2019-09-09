---
title: Dynamic Data Exchange
description: This section provides guidelines for implementing dynamic data exchange for applications that cannot use the Dynamic Data Exchange Management Library (DDEML).
ms.assetid: 'vs|winui|~\winui\windowsuserinterface\dataexchange\dynamicdataexchange.htm'
keywords:
- Dynamic Data Exchange (DDE),about
- DDE (Dynamic Data Exchange),about
- data exchange,Dynamic Data Exchange (DDE)
ms.topic: article
ms.date: 05/31/2018
---

# Dynamic Data Exchange

This section provides guidelines for implementing dynamic data exchange for applications that cannot use the Dynamic Data Exchange Management Library (DDEML). For more information about the DDEML, see [Dynamic Data Exchange Management Library](dynamic-data-exchange-management-library.md).

### Overviews



| Name                                                           | Description                                                        |
|----------------------------------------------------------------|--------------------------------------------------------------------|
| [About Dynamic Data Exchange](about-dynamic-data-exchange.md) | Discusses transferring data between applications.<br/>       |
| [Using Dynamic Data Exchange](using-dynamic-data-exchange.md) | Provides code samples concerning dynamic data exchange.<br/> |
| [DDE Reference](dynamic-data-exchange-reference.md)           | The API reference.<br/>                                      |



 

### DDE Functions



| Name                                                             | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DdeSetQualityOfService**](/windows/desktop/api/Dde/nf-dde-ddesetqualityofservice)         | Specifies the quality of service (QOS) a raw Dynamic Data Exchange (DDE) application desires for future DDE conversations it initiates. The specified QOS applies to any conversations started while those settings are in place. A DDE conversation's quality of service lasts for the duration of the conversation; calls to the [**DdeSetQualityOfService**](/windows/desktop/api/Dde/nf-dde-ddesetqualityofservice) function during a conversation do not affect that conversation's QOS. <br/> |
| [**FreeDDElParam**](/windows/desktop/api/Dde/nf-dde-freeddelparam)                           | Frees the memory specified by the *lParam* parameter of a posted DDE message. An application receiving a posted DDE message should call this function after it has used the [**UnpackDDElParam**](/windows/desktop/api/Dde/nf-dde-unpackddelparam) function to unpack the *lParam* value. <br/>                                                                                                                                                                                                     |
| [**ImpersonateDdeClientWindow**](/windows/desktop/api/Dde/nf-dde-impersonateddeclientwindow) | Enables a DDE server application to impersonate a DDE client application's security context. This protects secure server data from unauthorized DDE clients. <br/>                                                                                                                                                                                                                                                                                                      |
| [**PackDDElParam**](/windows/desktop/api/Dde/nf-dde-packddelparam)                           | Packs a DDE *lParam* value into an internal structure used for sharing DDE data between processes.<br/>                                                                                                                                                                                                                                                                                                                                                                 |
| [**ReuseDDElParam**](/windows/desktop/api/Dde/nf-dde-reuseddelparam)                         | Enables an application to reuse a packed DDE *lParam* parameter, rather than allocating a new packed *lParam*. Using this function reduces reallocations for applications that pass packed DDE messages. <br/>                                                                                                                                                                                                                                                          |
| [**UnpackDDElParam**](/windows/desktop/api/Dde/nf-dde-unpackddelparam)                       | Unpacks a DDE *lParam* value received from a posted DDE message. <br/>                                                                                                                                                                                                                                                                                                                                                                                                  |



 

### DDE Messages



| Name                                         | Description                                                                                                                                                                                                                                                                                      |
|----------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_DDE\_INITIATE**](wm-dde-initiate.md) | Initiates a conversation with a server application responding to the specified application and topic names. Upon receiving this message, all server applications with names that match the specified application and that support the specified topic are expected to acknowledge it.<br/> |



 

### DDE Notifications



| Name                                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                   |
|------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_DDE\_ACK**](wm-dde-ack.md)             | Nnotifies a DDE application of the receipt and processing of the following messages: [**WM\_DDE\_POKE**](wm-dde-poke.md), [**WM\_DDE\_EXECUTE**](wm-dde-execute.md), [**WM\_DDE\_DATA**](wm-dde-data.md), [**WM\_DDE\_ADVISE**](wm-dde-advise.md), [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md), [**WM\_DDE\_INITIATE**](wm-dde-initiate.md), or [**WM\_DDE\_REQUEST**](wm-dde-request.md) (in some cases). <br/> |
| [**WM\_DDE\_ADVISE**](wm-dde-advise.md)       | A DDE client application posts the [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message to a DDE server application to request the server to supply an update for a data item whenever the item changes. <br/>                                                                                                                                                                                                              |
| [**WM\_DDE\_DATA**](wm-dde-data.md)           | A DDE server application posts a [**WM\_DDE\_DATA**](wm-dde-data.md) message to a DDE client application to pass a data item to the client or to notify the client of the availability of a data item. <br/>                                                                                                                                                                                                           |
| [**WM\_DDE\_EXECUTE**](wm-dde-execute.md)     | A DDE client application posts a [**WM\_DDE\_EXECUTE**](wm-dde-execute.md) message to a DDE server application to send a string to the server to be processed as a series of commands. The server application is expected to post a [**WM\_DDE\_ACK**](wm-dde-ack.md) message in response. <br/>                                                                                                                      |
| [**WM\_DDE\_POKE**](wm-dde-poke.md)           | A DDE client application posts a [**WM\_DDE\_POKE**](wm-dde-poke.md) message to a DDE server application. A client uses this message to request the server to accept an unsolicited data item. The server is expected to reply with a [**WM\_DDE\_ACK**](wm-dde-ack.md) message indicating whether it accepted the data item. <br/>                                                                                   |
| [**WM\_DDE\_REQUEST**](wm-dde-request.md)     | A DDE client application posts a [**WM\_DDE\_REQUEST**](wm-dde-request.md) message to a DDE server application to request the value of a data item. <br/>                                                                                                                                                                                                                                                              |
| [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) | A DDE application (client or server) posts a [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) message to terminate a conversation. <br/>                                                                                                                                                                                                                                                                                  |
| [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md)   | A DDE client application posts a [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md) message to inform a DDE server application that the specified item or a particular clipboard format for the item should no longer be updated. This terminates the warm or hot data link for the specified item. <br/>                                                                                                                     |



 

### DDE Structures



| Name                           | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|--------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**DDEACK**](/windows/desktop/api/Dde/ns-dde-ddeack)       | Contains status flags that a DDE application passes to its partner as part of the [**WM\_DDE\_ACK**](wm-dde-ack.md) message. The flags provide details about the application's response to the messages [**WM\_DDE\_DATA**](wm-dde-data.md), [**WM\_DDE\_POKE**](wm-dde-poke.md), [**WM\_DDE\_EXECUTE**](wm-dde-execute.md), [**WM\_DDE\_ADVISE**](wm-dde-advise.md), [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md), and [**WM\_DDE\_REQUEST**](wm-dde-request.md). <br/> |
| [**DDEADVISE**](/windows/desktop/api/Dde/ns-dde-ddeadvise) | Contains flags that specify how a DDE server application should send data to a client application during an advise loop. A client passes a handle to a [**DDEADVISE**](/windows/desktop/api/Dde/ns-dde-ddeadvise) structure to a server as part of a [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message. <br/>                                                                                                                                                                                               |
| [**DDEDATA**](/windows/desktop/api/Dde/ns-dde-ddedata)     | Contains the data, and information about the data, sent as part of a [**WM\_DDE\_DATA**](wm-dde-data.md) message. <br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**DDEPOKE**](/windows/desktop/api/Dde/ns-dde-ddepoke)     | Contains the data, and information about the data, sent as part of a [**WM\_DDE\_POKE**](wm-dde-poke.md) message. <br/>                                                                                                                                                                                                                                                                                                                                                       |
| [**HSZPAIR**](/windows/win32/api/ddeml/ns-ddeml-hszpair)     | Contains a DDE service name and topic name. A DDE server application can use this structure during an [**XTYP\_WILDCONNECT**](xtyp-wildconnect.md) transaction to enumerate the service-topic pairs that it supports. <br/>                                                                                                                                                                                                                                                   |



 

 

 





