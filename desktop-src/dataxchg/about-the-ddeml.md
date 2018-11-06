---
title: About the DDEML
description: This topic discusses dynamic data exchange.
ms.assetid: 155b4cb0-dfbb-42f5-9fa3-8129349a0754
keywords:
- Windows User Interface,Dynamic Data Exchange (DDE)
- Dynamic Data Exchange (DDE),about
- DDE (Dynamic Data Exchange),about
- data exchange,Dynamic Data Exchange (DDE)
- Windows User Interface,Dynamic Data Exchange Management Library (DDEML)
- Dynamic Data Exchange Management Library (DDEML),about
- DDEML (Dynamic Data Exchange Management Library),about
- data exchange,Dynamic Data Exchange Management Library (DDEML)
ms.topic: article
ms.date: 05/31/2018
---

# About the DDEML

Dynamic Data Exchange (DDE) differs from the clipboard data-transfer mechanism. One difference is that the clipboard is almost always used as a one-time response to a specific action by the user — such as clicking **Paste** from a menu. Although DDE can also be initiated by a user, it typically continues without the user's further involvement.

The Dynamic Data Exchange Management Library (DDEML) provides an interface that simplifies the task of adding DDE capability to an application. Instead of sending, posting, and processing DDE messages directly, an application uses the functions provided by the DDEML to manage DDE conversations. A DDE conversation is the interaction between client and server applications. The DDEML also provides a means for managing the strings and data shared among DDE applications. Instead of using atoms and pointers to shared memory objects, DDE applications create and exchange string handles, which identify strings, and data handles, which identify DDE objects. The DDEML provides a function ([**DdeNameService**](/windows/desktop/api/Ddeml/nf-ddeml-ddenameservice)) that enables a server application to register the service names it supports. The service names are then broadcast to other applications in the system, which use the names to connect to the server. The DDEML also ensures compatibility among DDE applications by requiring them to implement the DDE protocol in a consistent manner.

Existing applications using the message-based DDE protocol are fully compatible with those that use the DDEML; that is, an application using message-based DDE can establish conversations and perform transactions with applications using the DDEML. Instead of using DDE messages in your new application, take advantage of the DDEML and the many improvements it offers.

To use the DDEML, you must include the DDEML.H header file in your source files, link with the USER32.LIB file, and ensure that the DDEML.DLL file resides in the system's path.

Whenever a DDEML function fails, an application can call the [**DdeGetLastError**](/windows/desktop/api/Ddeml/nf-ddeml-ddegetlasterror) function to determine the cause of the failure. **DdeGetLastError** returns an error value that specifies the cause of the most recent error.

 

 




