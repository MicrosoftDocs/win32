---
title: Transaction Flags
description: An object can be opened in either direct or transacted mode.
ms.assetid: f3be52b9-957c-4ab9-8fc1-e765faae2489
ms.topic: article
ms.date: 05/31/2018
---

# Transaction Flags

An object can be opened in either direct or transacted mode. When an object is opened in direct mode, changes are made immediately and permanently. When an object is opened in transacted mode, changes are buffered so they can be explicitly committed or reverted once editing is complete. Committed changes are saved to the object while reverted changes are discarded. Direct mode is the default access mode.

Transacted mode is not required on a parent storage object in order to use it on a nested element. A transaction for a nested element, however, is nested within the transaction for its parent storage object. Therefore, changes made to a child object cannot be committed until those made to the parent are committed, and both remain uncommitted until the root storage object (the top-level parent) is actually written to disk. In other words, the changes move outward: inner objects publish changes to the transactions of their immediate containers.

 

 




