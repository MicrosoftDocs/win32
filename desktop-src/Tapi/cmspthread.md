---
description: The CMSPThread class implements the MSPs worker thread.
ms.assetid: 9dc2373a-cdcf-4e60-95fa-56cb68bda15b
title: CMSPThread
ms.topic: article
ms.date: 05/31/2018
---

# CMSPThread

The **CMSPThread** class implements the MSP's worker thread. The base classes use this worker thread for a number of purposes. A generic and lightweight work item mechanism is provided to allow the derived MSP to use this thread for its own synchronous or asynchronous work items, whatever they may be. The thread also pumps messages and supports handling of APCs (although APCs are not used in the base classes).

When multiple like addresses are present (that is, when the same MSP implementation from the same DLL is instantiated multiple times), the thread class ensures scalability by automatically using a single thread for all the addresses. The interface to the thread class is such that the MSP implementation can think of the thread class as a private thread and need not care about the other addresses that may be sharing it.

Defined in MSPthrd.h.

 

 



