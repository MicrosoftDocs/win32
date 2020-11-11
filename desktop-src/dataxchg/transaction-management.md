---
title: Transaction Management (Data Exchange)
description: This topic discusses how a client can send transactions to obtain data and services from the server.
ms.assetid: 2d08ffa3-cbd7-4806-b94f-979938322c38
keywords:
- Windows User Interface,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),transactions
- DDE (Dynamic Data Exchange),transactions
- data exchange,Dynamic Data Exchange (DDE)
- Windows User Interface,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange Management Library (DDEML),transactions
- DDEML (Dynamic Data Exchange Management Library),transactions
- data exchange,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange (DDE),request transactions
- DDE (Dynamic Data Exchange),request transactions
- Dynamic Data Exchange Management Library (DDEML),request transactions
- DDEML (Dynamic Data Exchange Management Library),request transactions
- Dynamic Data Exchange (DDE),poke transactions
- DDE (Dynamic Data Exchange),poke transactions
- Dynamic Data Exchange Management Library (DDEML),poke transactions
- DDEML (Dynamic Data Exchange Management Library),poke transactions
- Dynamic Data Exchange (DDE),advise transactions
- DDE (Dynamic Data Exchange),advise transactions
- Dynamic Data Exchange Management Library (DDEML),advise transactions
- DDEML (Dynamic Data Exchange Management Library),advise transactions
- Dynamic Data Exchange (DDE),execute transactions
- DDE (Dynamic Data Exchange),execute transactions
- Dynamic Data Exchange Management Library (DDEML),execute transactions
- DDEML (Dynamic Data Exchange Management Library),execute transactions
- Dynamic Data Exchange (DDE),synchronous transactions
- DDE (Dynamic Data Exchange),synchronous transactions
- Dynamic Data Exchange Management Library (DDEML),synchronous transactions
- DDEML (Dynamic Data Exchange Management Library),synchronous transactions
- Dynamic Data Exchange (DDE),asynchronous transactions
- DDE (Dynamic Data Exchange),asynchronous transactions
- Dynamic Data Exchange Management Library (DDEML),asynchronous transactions
- DDEML (Dynamic Data Exchange Management Library),asynchronous transactions
ms.topic: article
ms.date: 05/31/2018
---

# Transaction Management (Data Exchange)

After establishing a conversation with a server, a client can send transactions to obtain data and services from the server.

The following topics describe the types of transactions that clients can use to interact with a server.

-   [Request Transaction](#request-transaction)
-   [Poke Transaction](#poke-transaction)
-   [Advise Transaction](#advise-transaction)
-   [Execute Transaction](#execute-transaction)
-   [Synchronous and Asynchronous Transactions](#synchronous-and-asynchronous-transactions)
-   [Transaction Control](#transaction-control)
-   [Transaction Classes](#transaction-classes)
-   [Transaction Types](#transaction-types)

## Request Transaction

A client application can use the [**XTYP\_REQUEST**](xtyp-request.md) transaction to request a data item from a server application. The client calls the [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) function, specifying **XTYP\_REQUEST** as the transaction type and specifying the data item the application needs.

The Dynamic Data Exchange Management Library (DDEML) passes the [**XTYP\_REQUEST**](xtyp-request.md) transaction to the server, specifying the topic name, item name, and data format requested by the client. If the server supports the requested topic, item, and format, the server should return a data handle that identifies the current value of the item. The DDEML passes this handle to the client as the return value from [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction). The server should return **NULL** if it does not support the topic, item, or format requested.

[**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) uses the *lpdwResult* parameter to return a transaction-status flag to the client. If the server does not process the [**XTYP\_REQUEST**](xtyp-request.md) transaction, **DdeClientTransaction** returns **NULL**, and *lpdwResult* points to the DDE\_FNOTPROCESSED or DDE\_FBUSY flag. If the DDE\_FNOTPROCESSED flag is returned, the client cannot determine why the server did not process the transaction.

If a server does not support the [**XTYP\_REQUEST**](xtyp-request.md) transaction, it should specify the CBF\_FAIL\_REQUESTS filter flag in the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function. This flag prevents the DDEML from sending the transaction to the server.

## Poke Transaction

A client can send unsolicited data to a server by using [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) to send an [**XTYP\_POKE**](xtyp-poke.md) transaction to a server's callback function.

The client application first creates a buffer that contains the data to send to the server and then passes a pointer to the buffer as a parameter to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction). Alternatively, the client can use the [**DdeCreateDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatedatahandle) function to obtain a data handle that identifies the data and then pass the handle to **DdeClientTransaction**. In either case, the client also specifies the topic name, item name, and data format when it calls **DdeClientTransaction**.

The DDEML passes the [**XTYP\_POKE**](xtyp-poke.md) transaction to the server, specifying the topic name, item name, and data format that the client requested. To accept the data item and format, the server should return DDE\_FACK. To reject the data, the server should return DDE\_FNOTPROCESSED. If the server is too busy to accept the data, the server should return DDE\_FBUSY.

When [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) returns, the client can use the *lpdwResult* parameter to access the transaction-status flag. If the flag is DDE\_FBUSY, the client should send the transaction again later.

If a server does not support the [**XTYP\_POKE**](xtyp-poke.md) transaction, it should specify the CBF\_FAIL\_POKES filter flag in [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea). This flag prevents the DDEML from sending this transaction to the server.

## Advise Transaction

A client application can use the DDEML to establish one or more links to items in a server application. When such a link has been established, the server sends periodic updates about the linked item to the client (typically, whenever the value of the item associated with the server application changes). Linking establishes an advise loop between the two applications that remains in place until the client ends it.

There are two kinds of advise loops: "hot" and "warm." In a hot advise loop, the server immediately sends a data handle that identifies the changed value. In a warm advise loop, the server notifies the client that the value of the item has changed but does not send the data handle until the client requests it.

A client can request a hot advise loop with a server by specifying the [**XTYP\_ADVSTART**](xtyp-advstart.md) transaction type in a call to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction). To request a warm advise loop, the client must combine the XTYPF\_NODATA flag with the **XTYP\_ADVSTART** transaction type. In either event, the DDEML passes the **XTYP\_ADVSTART** transaction to the server's Dynamic Data Exchange (DDE) callback function. The server's DDE callback function should examine the parameters that accompany the **XTYP\_ADVSTART** transaction (including the requested format, topic name, and item name) and then return **TRUE** to allow the advise loop or **FALSE** to deny it.

After an advise loop has been established, the server application should call the [**DdePostAdvise**](/windows/desktop/api/Ddeml/nf-ddeml-ddepostadvise) function whenever the value of the item associated with the requested item name changes. This call results in an [**XTYP\_ADVREQ**](xtyp-advreq.md) transaction being sent to the server's own DDE callback function. The server's DDE callback function should return a data handle that identifies the new value of the data item. The DDEML then notifies the client that the specified item has changed by sending the [**XTYP\_ADVDATA**](xtyp-advdata.md) transaction to the client's DDE callback function.

If the client requested a hot advise loop, the DDEML passes the data handle to the changed item to the client during the [**XTYP\_ADVDATA**](xtyp-advdata.md) transaction. Otherwise, the client can send an [**XTYP\_REQUEST**](xtyp-request.md) transaction to obtain the data handle.

It is possible for a server to send updates faster than a client can process the new data. The speed of updates can be a problem for a client that must perform lengthy processing operations on the data. In this case, the client should specify the XTYPF\_ACKREQ flag when it requests an advise loop. This flag causes the server to wait for the client to acknowledge that it has received and processed a data item before the server sends the next data item. Advise loops that are established with the XTYPF\_ACKREQ flag are more robust with fast servers but can occasionally miss updates. Advise loops established without the XTYPF\_ACKREQ flag are guaranteed not to miss updates as long as the client keeps up with the server.

A client can end an advise loop by specifying the [**XTYP\_ADVSTOP**](xtyp-advstop.md) transaction type in a call to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction).

If a server does not support advise loops, it should specify the CBF\_FAIL\_ADVISES filter flag in the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function. This flag prevents the DDEML from sending the [**XTYP\_ADVSTART**](xtyp-advstart.md) and [**XTYP\_ADVSTOP**](xtyp-advstop.md) transactions to the server.

## Execute Transaction

A client can use the [**XTYP\_EXECUTE**](xtyp-execute.md) transaction to cause a server to execute a command or a series of commands.

To execute a server command, the client first creates a buffer that contains a command string for the server to execute and then passes either a pointer to the buffer or a data handle identifying the buffer when it calls [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction). Other required parameters include the conversation handle, the item name string handle, the format specification, and the [**XTYP\_EXECUTE**](xtyp-execute.md) transaction type. An application that creates a data handle to passing execute data must specify **NULL** for the *hszItem* parameter of the [**DdeCreateDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddecreatedatahandle) function and zero for the *uFmt* parameter.

The DDEML passes the [**XTYP\_EXECUTE**](xtyp-execute.md) transaction to the server's DDE callback function and specifies the format name, conversation handle, topic name, and data handle identifying the command string. If the server supports the command, it should use the [**DdeAccessData**](/windows/desktop/api/Ddeml/nf-ddeml-ddeaccessdata) function to obtain a pointer to the command string, execute the command, and then return DDE\_FACK. If the server does not support the command or cannot complete the transaction, it should return DDE\_FNOTPROCESSED. The server should return DDE\_FBUSY if it is too busy to complete the transaction.

In general, a server's callback function should process the [**XTYP\_EXECUTE**](xtyp-execute.md) transaction before returning with the following exceptions:

1.  When the command passed with the [**XTYP\_EXECUTE**](xtyp-execute.md) transaction requests the server to terminate, the server should not terminate until its callback function returns from processing **XTYP\_EXECUTE**.
2.  If the server must perform an operation, such as processing a dialog box or a DDE transaction that might cause DDEML recursion problems, the server should return the CBR\_BLOCK return code to block the execute transaction, perform the operation, and then resume processing the execute transaction.

When [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) returns, the client can use the *lpdwResult* parameter to access the transaction status flag. If the flag is DDE\_FBUSY, the client should send the transaction again later.

If a server does not support the [**XTYP\_EXECUTE**](xtyp-execute.md) transaction, it should specify the CBF\_FAIL\_EXECUTES filter flag in the [**DdeInitialize**](/windows/desktop/api/Ddeml/nf-ddeml-ddeinitializea) function. Doing so prevents the DDEML from sending the transaction to the server.

## Synchronous and Asynchronous Transactions

A client can send either synchronous or asynchronous transactions. In a synchronous transaction, the client specifies a time-out value that indicates the maximum amount of time it will wait for the server to process the transaction. [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) does not return until the server processes the transaction, the transaction fails, or the time-out value expires. The client specifies the time-out value when it calls **DdeClientTransaction**.

During a synchronous transaction, the client enters a modal loop while waiting for the transaction to be processed. The client can still process user input but cannot send another synchronous transaction until [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) returns.

A client sends an asynchronous transaction by specifying the TIMEOUT\_ASYNC flag in [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction). The function returns after the transaction has begun, passing a transaction identifier to the client. When the server finishes processing the asynchronous transaction, the DDEML sends an [**XTYP\_XACT\_COMPLETE**](xtyp-xact-complete.md) transaction to the client. One of the parameters that the DDEML passes to the client during the **XTYP\_XACT\_COMPLETE** transaction is the transaction identifier. By comparing this transaction identifier with the identifier returned by **DdeClientTransaction**, the client identifies which asynchronous transaction the server has finished processing.

A client can use the [**DdeSetUserHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddesetuserhandle) function as an aid in processing an asynchronous transaction. This function makes it possible for a client to associate an application-defined value with a conversation handle and a transaction identifier. The client can use the [**DdeQueryConvInfo**](/windows/desktop/api/Ddeml/nf-ddeml-ddequeryconvinfo) function during the [**XTYP\_XACT\_COMPLETE**](xtyp-xact-complete.md) transaction to obtain the application-defined value. Because of this function, an application need not maintain a list of active transaction identifiers.

When a client successfully completes a request for data using a synchronous transaction, the DDEML has no way to tell when the client has finished using the data received. The client application must pass the data handle received to the [**DdeFreeDataHandle**](/windows/desktop/api/Ddeml/nf-ddeml-ddefreedatahandle) function, notifying the DDEML that the handle will no longer be used. Data handles returned by synchronous transactions are effectively owned by the client.

If a server does not process an asynchronous transaction in a timely manner, the client can abandon the transaction by calling the [**DdeAbandonTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeabandontransaction) function. The DDEML releases all resources associated with the transaction and discards the results of the transaction when the server finishes processing it. A time-out during a synchronous transaction effectively cancels the transaction.

The asynchronous transaction method is provided for applications that must send a high volume of DDE transactions while simultaneously performing a substantial amount of processing, such as performing calculations. The asynchronous method is also useful in applications that must stop processing DDE transactions temporarily so they can complete other tasks without interruption. In most other situations, an application should use the synchronous method.

Synchronous transactions are simpler to maintain and are faster than asynchronous transactions. However, only one synchronous transaction can be performed at a time, whereas many asynchronous transactions can be performed simultaneously. With synchronous transactions, a slow server can cause a client to remain idle while it is waiting for a response. Also, synchronous transactions cause the client to enter a modal loop that could bypass message filtering in the application's own message loop.

If the client has installed a hook procedure to filter messages (that is, specified the WH\_MSGFILTER hook type in a call to the [**SetWindowsHookEx**](/windows/desktop/api/winuser/nf-winuser-setwindowshookexa) function), a synchronous transaction will not cause the system to bypass the hook procedure. When an input event occurs while the client is waiting for a synchronous transaction to end, the hook procedure receives an MSGF\_DDEMGR hook code. The main danger of using a synchronous transaction modal loop is that a modal loop created by a dialog box can interfere with its operation. Asynchronous transactions should always be used when the DDEML is being used by a DLL.

## Transaction Control

An application can suspend transactions to its DDE callback function   either those transactions associated with a specific conversation handle or all transactions regardless of the conversation handle. This capability is useful when an application receives a transaction that requires lengthy processing. In such a case, the application can return the CBR\_BLOCK return code to suspend future transactions associated with the transaction's conversation handle, so that the application is free to process other conversations.

When processing has been completed, the application calls the [**DdeEnableCallback**](/windows/desktop/api/Ddeml/nf-ddeml-ddeenablecallback) function to resume transactions associated with the suspended conversation. Calling **DdeEnableCallback** causes the DDEML to resend the transaction that resulted in the application suspending the conversation. Therefore, the application should store the result of the transaction in such a way that it can obtain and return the result without reprocessing the transaction.

An application can suspend all transactions associated with a specific conversation handle by specifying the handle and the EC\_DISABLE flag in a call to [**DdeEnableCallback**](/windows/desktop/api/Ddeml/nf-ddeml-ddeenablecallback). By specifying a **NULL** handle, an application can suspend all transactions for all conversations.

When a conversation has been suspended, the DDEML saves transactions for the conversation in a transaction queue. When the application reenables the conversation, the DDEML removes the saved transactions from the queue and passes each transaction to the appropriate callback function. The capacity of the transaction queue is large, but an application should reenable a suspended conversation as soon as possible to avoid losing transactions.

An application can resume usual transaction processing by specifying the EC\_ENABLEALL flag in [**DdeEnableCallback**](/windows/desktop/api/Ddeml/nf-ddeml-ddeenablecallback). For a more controlled resumption of transaction processing, the application can specify the EC\_ENABLEONE flag. This flag removes one transaction from the transaction queue and passes it to the appropriate callback function; after that transaction has been processed, any conversations are again disabled.

If the EC\_ENABLEONE flag and a conversation handle are specified in the call to [**DdeEnableCallback**](/windows/desktop/api/Ddeml/nf-ddeml-ddeenablecallback), only that conversation is blocked after the transaction has been processed. If a **NULL** conversation handle is specified, all conversations are blocked after a transaction has been processed in any conversation.

## Transaction Classes

The DDEML has four classes of transactions. Each class is identified by a constant that begins with the XCLASS\_ prefix. The classes are defined in the DDEML header file. The class value is combined with the transaction-type value and is passed to the DDE callback function of the receiving application.

A transaction's class determines the return value that a callback function is expected to return if it processes the transaction. The following return values and transaction types are associated with each of the four transaction classes.



| Class                | Return value                                                     | Transaction                                                                                                                                                                                                                                                                                                                                                                                    |
|----------------------|------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XCLASS\_BOOL         | **TRUE** or **FALSE**                                            | [**XTYP\_ADVSTART**](xtyp-advstart.md)<br/> [**XTYP\_CONNECT**](xtyp-connect.md)<br/>                                                                                                                                                                                                                                                                                            |
| XCLASS\_DATA         | A data handle, the CBR\_BLOCK return code, or **NULL**           | [**XTYP\_ADVREQ**](xtyp-advreq.md)<br/> [**XTYP\_REQUEST**](xtyp-request.md)<br/> [**XTYP\_WILDCONNECT**](xtyp-wildconnect.md)<br/>                                                                                                                                                                                                                                       |
| XCLASS\_FLAGS        | A transaction flag: DDE\_FACK, DDE\_FBUSY, or DDE\_FNOTPROCESSED | [**XTYP\_ADVDATA**](xtyp-advdata.md)<br/> [**XTYP\_EXECUTE**](xtyp-execute.md)<br/> [**XTYP\_POKE**](xtyp-poke.md)<br/>                                                                                                                                                                                                                                                   |
| XCLASS\_NOTIFICATION | None                                                             | [**XTYP\_ADVSTOP**](xtyp-advstop.md)<br/> [**XTYP\_CONNECT\_CONFIRM**](xtyp-connect-confirm.md)<br/> [**XTYP\_DISCONNECT**](xtyp-disconnect.md)<br/> [**XTYP\_ERROR**](xtyp-error.md)<br/> [**XTYP\_REGISTER**](xtyp-register.md)<br/> [**XTYP\_UNREGISTER**](xtyp-unregister.md)<br/> [**XTYP\_XACT\_COMPLETE**](xtyp-xact-complete.md)<br/> |



 

## Transaction Types

Each DDE transaction type has a receiver and an associated activity that causes the DDEML to generate each type.



| Transaction type                                       | Receiver                   | Cause                                                                                                                                                                         |
|--------------------------------------------------------|----------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**XTYP\_ADVDATA**](xtyp-advdata.md)                  | Client                     | A server responded to an [**XTYP\_ADVREQ**](xtyp-advreq.md) transaction by returning a data handle.                                                                          |
| [**XTYP\_ADVREQ**](xtyp-advreq.md)                    | Server                     | A server called the [**DdePostAdvise**](/windows/desktop/api/Ddeml/nf-ddeml-ddepostadvise) function, indicating that the value of a data item in an advise loop had changed.                                  |
| [**XTYP\_ADVSTART**](xtyp-advstart.md)                | Server                     | A client specified the [**XTYP\_ADVSTART**](xtyp-advstart.md) transaction type in a call to the [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction) function.               |
| [**XTYP\_ADVSTOP**](xtyp-advstop.md)                  | Server                     | A client specified the [**XTYP\_ADVSTOP**](xtyp-advstop.md) transaction type in a call to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction).                              |
| [**XTYP\_CONNECT**](xtyp-connect.md)                  | Server                     | A client called the [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) function and specified a service name and topic name supported by the server.                                            |
| [**XTYP\_CONNECT\_CONFIRM**](xtyp-connect-confirm.md) | Server                     | The server returned **TRUE** in response to an [**XTYP\_CONNECT**](xtyp-connect.md) or [**XTYP\_WILDCONNECT**](xtyp-wildconnect.md) transaction.                            |
| [**XTYP\_DISCONNECT**](xtyp-disconnect.md)            | Client/Server              | A partner in a conversation called the [**DdeDisconnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddedisconnect) function, causing both partners to receive this transaction.                                    |
| [**XTYP\_ERROR**](xtyp-error.md)                      | Client/Server              | A critical error has occurred. The DDEML may not have sufficient resources to continue.                                                                                       |
| [**XTYP\_EXECUTE**](xtyp-execute.md)                  | Server                     | A client specified the [**XTYP\_EXECUTE**](xtyp-execute.md) transaction type in a call to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction).                              |
| [**XTYP\_MONITOR**](xtyp-monitor.md)                  | DDE monitoring application | A DDE event occurred in the system. For more information about DDE monitoring applications, see [Monitoring Applications](monitoring-applications.md).                       |
| [**XTYP\_POKE**](xtyp-poke.md)                        | Server                     | A client specified the [**XTYP\_POKE**](xtyp-poke.md) transaction type in a call to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction).                                    |
| [**XTYP\_REGISTER**](xtyp-register.md)                | Client/Server              | A server application used the [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice) function to register a service name.                                                                   |
| [**XTYP\_REQUEST**](xtyp-request.md)                  | Server                     | A client specified the [**XTYP\_REQUEST**](xtyp-request.md) transaction type in a call to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction).                              |
| [**XTYP\_UNREGISTER**](xtyp-unregister.md)            | Client/Server              | A server application used [**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice) to unregister a service name.                                                                              |
| [**XTYP\_WILDCONNECT**](xtyp-wildconnect.md)          | Server                     | A client called the [**DdeConnect**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnect) or [**DdeConnectList**](/windows/desktop/api/Ddeml/nf-ddeml-ddeconnectlist) function, specifying **NULL** for the service name, the topic name, or both. |
| [**XTYP\_XACT\_COMPLETE**](xtyp-xact-complete.md)     | Client                     | An asynchronous transaction, sent when the client specified the TIMEOUT\_ASYNC flag in a call to [**DdeClientTransaction**](/windows/desktop/api/Ddeml/nf-ddeml-ddeclienttransaction), has concluded.         |



 

 

