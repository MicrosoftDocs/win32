---
description: The Synchronization Manager includes user interface components, such as the tabbed dialog boxes in the SyncMgr service, error dialogs, and progress dialogs.
title: Synchronization Manager Architecture
ms.topic: article
ms.date: 05/31/2018
ms.assetid: db338835-ca8d-4e9f-973a-8eb081feda2b
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Synchronization Manager Architecture

The Synchronization Manager includes user interface components, such as the tabbed dialog boxes in the SyncMgr service, error dialogs, and progress dialogs. With the user interface components the end user can schedule applications for synchronization and set up automatic synchronization to occur in conjunction with specified system events. For example, the SyncMgr can be invoked at user logon or system shutdown. The user can also invoke a manual synchronization.

The user selects an application and specifies the items within the application to be synchronized and sets a trigger event. For example, within an email application, the Inbox, the Outbox, or some other folder containing messages can be a separate item for the application.

SyncMgr also includes a programming interface so that applications can register to use synchronization features, can process errors, and can receive progress information and notifications during the synchronization process.

 

 



