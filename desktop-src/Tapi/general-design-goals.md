---
description: The following list contains the TAPI MSP design goals.
ms.assetid: 286b96c1-047b-4cb9-a189-af2818cfec58
title: General Design Goals
ms.topic: article
ms.date: 05/31/2018
---

# General Design Goals

The following list contains the TAPI MSP design goals.

-   Base classes have been kept simple, with members and methods introduced only when absolutely necessary.
-   Simple inheritance. No multiple inheritance among classes, although multiple inheritance is used for the interfaces.
-   Locking happens only in one direction to prevent deadlock. Methods on the call object that require the lock on the call might call methods on the stream that require the lock on the stream. However, methods on the stream that require the lock on the stream will never call a method on the call that requires a lock on the call.
-   Refcounts are used to protect access. All callbacks posted to the thread pool hold refcounts. The refcount is canceled when the wait is canceled. The Address object has refcounts on Terminals. Call objects have refcounts on the Address and on Streams. Stream objects have refcounts on Calls and Terminals. The Terminals have refcounts on Streams. The circular refcounts break when the shutdown method on the Address and Call objects is called.

 

 



