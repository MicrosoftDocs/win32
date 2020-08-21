---
title: About Dynamic Data Exchange
description: This topic discusses transferring data between applications.
ms.assetid: 0bcd8de4-a6f0-4f2a-8b9d-0b1b638925fb
keywords:
- Dynamic Data Exchange (DDE),about
- DDE (Dynamic Data Exchange),about
- data exchange,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),linking to real-time data
- DDE (Dynamic Data Exchange),linking to real-time data
- Dynamic Data Exchange (DDE),creating compound documents
- DDE (Dynamic Data Exchange),creating compound documents
- Dynamic Data Exchange (DDE),data queries
- DDE (Dynamic Data Exchange),data queries
- Dynamic Data Exchange (DDE),examples
- DDE (Dynamic Data Exchange),examples
- Dynamic Data Exchange (DDE),impersonation
- DDE (Dynamic Data Exchange),impersonation
- Dynamic Data Exchange (DDE),messages
- DDE (Dynamic Data Exchange),messages
- Dynamic Data Exchange (DDE),atoms
- DDE (Dynamic Data Exchange),atoms
- Dynamic Data Exchange (DDE),shared memory objects
- DDE (Dynamic Data Exchange),shared memory objects
- Dynamic Data Exchange (DDE),parameter packing functions
- DDE (Dynamic Data Exchange),parameter packing functions
ms.topic: article
ms.date: 05/31/2018
---

# About Dynamic Data Exchange

Windows provides several methods for transferring data between applications. One method is to use the Dynamic Data Exchange (DDE) protocol. The DDE protocol is a set of messages and guidelines. It sends messages between applications that share data and uses shared memory to exchange data between applications. Applications can use the DDE protocol for one-time data transfers and for continuous exchanges in which applications send updates to one another as new data becomes available.

Windows also supports the Dynamic Data Exchange Management Library (DDEML). The DDEML is a dynamic-link library (DLL) that applications can use to share data. The DDEML provides functions and messages that simplify the task of adding DDE capability to an application. Instead of sending, posting, and processing DDE messages directly, an application uses the DDEML functions to manage DDE conversations. (A DDE conversation is the interaction between client and server applications.)

The DDEML also provides a facility for managing the strings and data that DDE applications share. Instead of using atoms and pointers to shared memory objects, DDE applications create and exchange string handles, which identify strings, and data handles, which identify memory objects. The DDEML also makes it possible for a server application to register the service names it supports. The names are broadcast to other applications in the system, which can use the names to connect to the server. Moreover, the DDEML ensures compatibility among DDE applications by forcing them to implement the DDE protocol in a consistent manner.

Existing applications that use the message-based DDE protocol are fully compatible with those that use the DDEML. That is, an application that uses message-based DDE can establish conversations and perform transactions with applications that use the DDEML. Because of the many advantages of the DDEML, new applications should use it rather than the DDE messages. To use the API elements of the DDEML, you must include the DDEML header file in your source files, link with the DDEML library, and ensure that the DDEML dynamic-link library is in the system's search path.

The following topics are discussed in this section.

-   [Dynamic Data Exchange Protocol](#dynamic-data-exchange-protocol)
-   [Uses for Windows Dynamic Data Exchange](#uses-for-windows-dynamic-data-exchange)
-   [Dynamic Data Exchange from the User's Point of View](#dynamic-data-exchange-from-the-users-point-of-view)
-   [Dynamic Data Exchange Concepts](#dynamic-data-exchange-concepts)
    -   [Client, Server, and Conversation](#client-server-and-conversation)
    -   [Application, Topic, and Item Names](#application-topic-and-item-names)
    -   [The System Topic](#the-system-topic)
    -   [Permanent Data Links](#permanent-data-links)
    -   [Atoms and Shared Memory Objects](#atoms-and-shared-memory-objects)
-   [Dynamic Data Exchange Messages Overview](#dynamic-data-exchange-messages-overview)
-   [Dynamic Data Exchange Message Flow](#dynamic-data-exchange-message-flow)
-   [Parameter Packing Functions](#parameter-packing-functions)
-   [Dynamic Data Exchange and Impersonation](#dynamic-data-exchange-and-impersonation)

## Dynamic Data Exchange Protocol

Because Windows has a message-based architecture, passing messages is the most appropriate method for automatically transferring information between applications. However, messages contain only two parameters (*wParam* and *lParam*) for passing data. As a result, these parameters must refer indirectly to other pieces of data when more than a few words of information pass between applications. The DDE protocol defines exactly how applications should use the *wParam* and *lParam* parameters to pass larger pieces of data by means of global atoms and shared memory handles. The DDE protocol has specific rules for allocating and deleting global atoms and shared memory objects.

A global atom is a reference to a character string. In the DDE protocol, atoms identify the applications exchanging data, the nature of the data being exchanged, and the data items themselves. For more information about atoms, see [About Atoms](about-atom-tables.md).

## Uses for Windows Dynamic Data Exchange

DDE is most appropriate for data exchanges that do not require ongoing user interaction. Usually, an application provides a method for the user to establish the link between the applications exchanging data. Once that link is established, however, the applications exchange data without further user involvement.

DDE can be used to implement a broad range of application features — for example:

-   Linking to real-time data, such as to stock market updates, scientific instruments, or process control.
-   Creating compound documents, such as a word processing document that includes a chart produced by a graphics application. Using DDE, the chart will change when the source data is changed, while the rest of the document remains the same.
-   Performing data queries between applications, such as a spreadsheet querying a database for accounts past due.

## Dynamic Data Exchange from the User's Point of View

The following example illustrates how two DDE applications can cooperate, as seen from the user's point of view.

A spreadsheet user wants to use Microsoft Excel to track the price of a particular stock on the New York Stock Exchange. The user has an application called Quote that in turn has access to NYSE data. The DDE conversation between Excel and Quote takes place as follows:

-   The user initiates the conversation by supplying the name of the application (Quote) that will supply the data and the particular topic of interest (NYSE). The resulting DDE conversation is used to request quotes on specific stocks.
-   Excel broadcasts the application and topic names to all DDE applications currently running in the system. Quote responds, establishing a conversation with Excel about the NYSE topic.
-   The user can then create a spreadsheet formula in a cell that requests that the spreadsheet be automatically updated whenever a particular stock quotation changes. For example, the user could request an automatic update whenever a change occurs in the selling price of ZAXX stock by specifying the following Excel formula: ='Quote'\|'NYSE'!ZAXX
-   The user can terminate the automatic updating of the ZAXX stock quotation at any time. Other data links that were established separately (such as for quotations for other stocks) still will remain active under the same NYSE conversation.
-   The user can also terminate the entire conversation between Excel and Quote on the NYSE topic, so that no specific data links on that topic can be established without initiating a new conversation.

## Dynamic Data Exchange Concepts

The following sections explain the important concepts and terminology that are key to understanding dynamic data exchange.

-   [Client, Server, and Conversation](#client-server-and-conversation)
-   [Application, Topic, and Item Names](#application-topic-and-item-names)
-   [The System Topic](#the-system-topic)
-   [Permanent Data Links](#permanent-data-links)
-   [Atoms and Shared Memory Objects](#atoms-and-shared-memory-objects)

### Client, Server, and Conversation

Two applications participating in DDE are said to be engaged in a DDE conversation. The application that initiates the conversation is the DDE client application; the application that responds to the client is the DDE server application. An application can engage in several conversations at the same time, acting as the client in some and as the server in others.

A DDE conversation takes place between two windows, one for each of the participating applications. A window may be the main window of the application; a window associated with a specific document, as in a multiple-document interface (MDI) application; or a hidden (invisible) window whose only purpose is to process DDE messages.

Since a DDE conversation is identified by the pair of handles to the windows engaged in the conversation, no window should be engaged in more than one conversation with another window. Either the client application or the server application must provide a different window for each of its conversations with a particular server or client application.

An application can ensure a pair of client and server windows is never involved in more than one conversation by creating a hidden window for each conversation. The sole purpose of this window is to process DDE messages.

### Application, Topic, and Item Names

The DDE protocol identifies the units of data passed between the client and server with a three-level hierarchy of application, topic, and item names.

Each DDE conversation is uniquely defined by the application name and topic. At the beginning of a DDE conversation, the client and server determine the application name and topic. The application name is usually the name of the server application. For example, when Excel acts as the server in a conversation, the application name is Excel.

The DDE topic is a general classification of data within which multiple data items may be "discussed" (exchanged) during the conversation. For applications that operate on file-based documents, the topic is usually a filename. For other applications, the topic is an application-specific name.

Because the client and server window handles together identify a DDE conversation, the application name and topic that define a conversation cannot be changed during the course of the conversation.

A DDE data item is information related to the conversation topic exchanged between the applications. Values for the data item can be passed from the server to the client, or from the client to the server. Data can be passed with any of the standard clipboard formats or with a registered clipboard format. A special, registered format named Link identifies an item in a DDE conversation. For more information about clipboard formats, see [Clipboard](clipboard.md).

### The System Topic

Applications should support the system topic at all times. This topic provides a context for information that may be of general interest to another application.

Data-item values must be rendered in the [**CF\_TEXT**](standard-clipboard-formats.md) clipboard format. Individual elements of item values for a system topic must be delimited by tab characters. The following table suggests some items for the system topic.



| Item          | Description                                                                                                                                                                                                                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Formats       | Tab-delimited list of clipboard formats the application can render. Typically, **CF\_** formats are listed with the "**CF\_**" portion of the names removed (for example, **CF\_TEXT** is listed as "**TEXT**").                                                                                        |
| Help          | Text that briefly explains how to use the DDE server.                                                                                                                                                                                                                                                   |
| ReturnMessage | Supporting detail for the most recently used [**WM\_DDE\_ACK**](wm-dde-ack.md) message. This item is useful when more than eight bits of application-specific return data are required.                                                                                                                |
| Status        | Indication of the current status of the application. When a server receives a [**WM\_DDE\_REQUEST**](wm-dde-request.md) message for this system-topic item, it should respond by posting a [**WM\_DDE\_DATA**](wm-dde-data.md) message with a string containing either Busy or Ready, as appropriate. |
| SysItems      | List of system-topic items the application supports.                                                                                                                                                                                                                                                    |
| TopicItemList | Similar to the SysItems item, except that TopicItemList should be supported for each topic other than the system topic. This allows browsing of the items supported under any topic. If the items cannot be enumerated, this item should contain only "TopicItemList".                                  |
| Topics        | List of topics the application supports at the current time; this list can vary from moment to moment.                                                                                                                                                                                                  |



 

### Permanent Data Links

Once a DDE conversation has begun, the client can establish one or more permanent data links with the server. A data link is a communications mechanism by which the server notifies the client whenever the value of a specified data item changes. The data link is permanent in the sense that this notification process continues until the data link or the DDE conversation itself is terminated.

There are two kinds of permanent DDE data links: warm and hot. In a warm data link, the server notifies the client that the value of the data item has changed, but the server does not send the data value to the client until the client requests it. In a hot data link, the server immediately sends the changed data value to the client.

Applications that support warm or hot data links typically provide a **Copy** or **Paste Link** command in their **Edit** menu to enable the user to establish links between applications.

### Atoms and Shared Memory Objects

Certain arguments of DDE messages are global atoms or shared memory objects. Applications using these arguments must follow explicit rules about when to allocate and delete them. In all cases, the message sender must delete any atom or shared memory object that the intended receiver will not receive because of an error condition, such as failure of the [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea) function.

DDE uses shared memory objects for three purposes:

-   To carry a data-item value to be exchanged. This is an item referenced by the *hData* parameter in the [**WM\_DDE\_DATA**](wm-dde-data.md) and [**WM\_DDE\_POKE**](wm-dde-poke.md) messages.
-   To carry options in a message. This is an item referenced by the *hOptions* parameter in a [**WM\_DDE\_ADVISE**](wm-dde-advise.md) message.
-   To carry a command execution string. This is an item referenced by the *hCommands* parameter in the [**WM\_DDE\_EXECUTE**](wm-dde-execute.md) message and its corresponding [**WM\_DDE\_ACK**](wm-dde-ack.md) message.

An application that receives a DDE shared memory object must treat it as read only. The application must not use the object as a mutual read-write area for the free exchange of data.

As it does with a DDE atom, an application should free a shared memory object to manage memory effectively. The application should also lock and unlock memory objects.

## Dynamic Data Exchange Messages Overview

Because DDE is a message-based protocol, it employs no functions or libraries. All DDE transactions are conducted by passing certain defined DDE messages between the client and server windows.

There are nine DDE messages; the symbolic constants for these messages are defined in the DDE header file. Certain structures for the various DDE messages are also defined in this header file.

The following table summarizes the DDE messages.



| Message                                        | Description                                                                                                                                      |
|------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| [**WM\_DDE\_ACK**](wm-dde-ack.md)             | Acknowledges receiving or not receiving a message.                                                                                               |
| [**WM\_DDE\_ADVISE**](wm-dde-advise.md)       | Requests the server application to supply an update or notification for a data item whenever it changes. This establishes a permanent data link. |
| [**WM\_DDE\_DATA**](wm-dde-data.md)           | Sends a data-item value to the client application.                                                                                               |
| [**WM\_DDE\_EXECUTE**](wm-dde-execute.md)     | Sends a string to the server application, which is expected to process the string as a series of commands.                                       |
| [**WM\_DDE\_INITIATE**](wm-dde-initiate.md)   | Initiates a conversation between the client and server applications.                                                                             |
| [**WM\_DDE\_POKE**](wm-dde-poke.md)           | Sends a data-item value to the server application.                                                                                               |
| [**WM\_DDE\_REQUEST**](wm-dde-request.md)     | Requests the server application to provide the value of a data item.                                                                             |
| [**WM\_DDE\_TERMINATE**](wm-dde-terminate.md) | Terminates a conversation.                                                                                                                       |
| [**WM\_DDE\_UNADVISE**](wm-dde-unadvise.md)   | Terminates a permanent data link.                                                                                                                |



 

An application calls [**SendMessage**](/windows/desktop/api/winuser/nf-winuser-sendmessage) to issue the [**WM\_DDE\_INITIATE**](wm-dde-initiate.md) message or a [**WM\_DDE\_ACK**](wm-dde-ack.md) message sent in response to **WM\_DDE\_INITIATE**. All other messages are sent by [**PostMessage**](/windows/desktop/api/winuser/nf-winuser-postmessagea). The first parameter of these calls is a handle to the receiving window; the second parameter contains the message to be sent; the third parameter identifies the sending window; and the fourth parameter contains the message-specific arguments.

## Dynamic Data Exchange Message Flow

A typical DDE conversation consists of the following events:

1.  The client application initiates the conversation, and the server application responds.
2.  The applications exchange data by any or all of the following methods:
    -   -   The server application sends data to the client at the client's request.
        -   The client application sends unsolicited data to the server application.
        -   The client application requests the server application to notify the client whenever a data item changes (warm data link).
        -   The client application requests the server application to send data whenever the data changes (hot data link).
        -   The server application carries out a command at the client's request.

3.  Either the client or server application terminates the conversation.

An application window that processes requests from a client or server must process them strictly in the order they are received.

A client can establish conversations with more than one server; a server can have conversations with more than one client. When handling messages from more than one source, a client or server must process the messages of a conversation synchronously, but need not process all messages synchronously. In other words, it can shift from one conversation to another as needed.

If an application is unable to process an incoming request because it is waiting for a DDE response, it must prevent deadlock by posting a [**WM\_DDE\_ACK**](wm-dde-ack.md) message with the **fBusy** member of the [**DDEACK**](/windows/desktop/api/Dde/ns-dde-ddeack) structure set to 1. An application can also send a busy **WM\_DDE\_ACK** message if, for any reason, it cannot process an incoming request within a reasonable amount of time.

An application should be able to handle the failure of a client or server to respond to a message within a certain time. Since the time-out interval may vary depending on the nature of the application and the configuration of the user's system (including whether it is connected to a network), the application should provide a way for the user to specify the interval.

## Parameter Packing Functions

The *lParam* parameter of many DDE messages contains two pieces of data. For example, the *lParam* of the [**WM\_DDE\_DATA**](wm-dde-data.md) message contains a data handle and an atom. Applications must use the [**PackDDElParam**](/windows/desktop/api/Dde/nf-dde-packddelparam) function to pack the handle and atom into an *lParam* parameter, and the [**UnpackDDElParam**](/windows/desktop/api/Dde/nf-dde-unpackddelparam) function to remove the values. DDE applications must use **PackDDElParam** and **UnpackDDElParam** for all messages posted during a DDE conversation.

Applications can also use the [**ReuseDDElParam**](/windows/desktop/api/Dde/nf-dde-reuseddelparam) and [**FreeDDElParam**](/windows/desktop/api/Dde/nf-dde-freeddelparam) functions. **ReuseDDElParam** allows a DDE application to reuse a packed *lParam* parameter, helping reduce the number of memory reallocations the application must perform during a conversation. An application can use **FreeDDElParam** to free the memory associated with a data handle received during a DDE conversation.

## Dynamic Data Exchange and Impersonation

To allow a server to impersonate a client, the client calls the [**DdeSetQualityOfService**](/windows/desktop/api/Dde/nf-dde-ddesetqualityofservice) function. The [**SECURITY\_IMPERSONATION\_LEVEL**](/windows/win32/api/winnt/ne-winnt-security_impersonation_level) structure is used to control the level of impersonation the server may perform.

A DDE server can impersonate a DDE client by calling the [**ImpersonateDdeClientWindow**](/windows/desktop/api/Dde/nf-dde-impersonateddeclientwindow) function. A DDEML server should use the [**DdeImpersonateClient**](/windows/desktop/api/Ddeml/nf-ddeml-ddeimpersonateclient) function.

 

 