---
description: Receiving a Response
ms.assetid: 48919608-a102-43e2-9ca0-80b17344b5eb
title: Receiving a Response
ms.topic: article
ms.date: 05/31/2018
---

# Receiving a Response

Because queued components are designed to work asynchronously, client applications should not block while waiting for a response from a queued request. Nevertheless, it is often useful for the client application or a related application on the client machine to receive a response eventually. For example, a client may want to be notified when a requested transaction has been completed successfully.

There are a variety of ways for a queued component to send a response back to its caller asynchronously. For example, it could send an email. Alternatively, the server could publish loosely coupled events to which the client could subscribe.

Another way for a client to obtain a response from a queued component that runs on a server is for the client to pass the called method a notification object. A notification object is an instance of a queued component that runs on the client. Such a notification object might be quite simple, containing only an integer that is used to represent an error value, or it might be quite complex, containing all the information necessary to roll back a transaction on the client. In either case, the calling client passes a notification object as an input parameter whenever it desires a response from a queued component that runs on a server. Because the notification object is queued, the server can call on its methods to alter its state, which can subsequently be read out by the client. In this scenario, the COM+ queued components service is used on both the client and the server to allow asynchronous communication in both directions.

 

 



