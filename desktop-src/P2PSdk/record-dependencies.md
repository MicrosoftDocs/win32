---
description: The Peer Infrastructure does not guarantee the order for receiving and processing records.
ms.assetid: 840aa931-c54c-463d-b37b-7d01c8a44409
title: Record Dependencies
ms.topic: article
ms.date: 05/31/2018
---

# Record Dependencies

The Peer Infrastructure does not guarantee the order for receiving and processing records. If your application has record dependencies, which means that the processing or validation of one record relies on another record, then your application must be able to handle situations when records might be received in an arbitrary and unpredictable order. For example, a chat application may have two types of records: a record that contains information about a specific user, and a record that contains a chat message that refers to the user record.

An application must be able to handle the situation when a chat message record is received before the user record for the chat message. One way to handle the situation is to wait for the user record by using a **stand-by list**, or a cache and timer. The application can periodically examine each record in the list or cache, and then handle the situation when the required user record is received.

To handle record dependencies, a well-designed application consists of the following:

-   Always checks for record dependencies before performing an action.
-   Anticipates conditions that might occur when records are received in an unexpected order, and then handles the situation.

 

 



