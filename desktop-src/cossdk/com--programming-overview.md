---
description: COM+ provides an enterprise development environment, based on the Microsoft Component Object Model (COM), for creating component-based, distributed applications.
ms.assetid: 141982d4-1e6c-4f01-8b0e-8b94f20dd82c
title: COM+ Programming Overview
ms.topic: article
ms.date: 05/31/2018
---

# COM+ Programming Overview

COM+ provides an enterprise development environment, based on the Microsoft Component Object Model (COM), for creating component-based, distributed applications. It also provides you with the tools to create transactional, multi-tier applications. COM+ combines enhancements to traditional COM-based development with many useful programming and administrative services. See [COM+ Services](com--services.md) for a complete list of these services.

The COM enhancements include improvements in both threading and security, along with the introduction of synchronization services. The services include the Component Services administrative tool.

For those familiar with COM programming, the COM+ improvements are significant, including the following:

-   COM+ implements a threading model called neutral apartment threading, which allows a component to have serialized access along with the ability to execute on any thread.
-   COM+ supports components with a special environment called a [context](com--contexts.md), which provides an extensible set of properties that define the execution environment for the component.
-   COM+ provides role-based security, asynchronous object execution, and a built-in moniker that represents a reference to an object instance running on an out-of-process server.

## Application and Component Administration

In COM+, a registration database, named RegDB, stores the metadata that describes components. This database is highly optimized for the type of information that COM+ needs for activation of components and is used instead of the system registry. In addition, COM+ exposes the *COM+ catalog*, which accesses information in the RegDB. The COM+ catalog is a system data store that contains configuration information for COM+ applications on a given server computer.

Finally, the Component Services administrative tool provides a fully scriptable user interface for developers and administrators to administer components as well as deploy both client-side and server-side multitier applications. For more information, see [Deploying COM+ Applications](deploying-com--applications.md).

## Automatic Transactions

COM+ supports all Microsoft Transaction Server (MTS) 2.0 semantics and adds the [auto-done](enabling-auto-done-for-a-method.md) capability, which you can set by using the Component Services administrative tool. This feature enables the system to abort a transaction automatically if an exception is triggered or to commit if not. For more information, see [COM+ Transactions](com--transactions.md), and [COM+ Just-in-Time Activation](com--just-in-time-activation.md).

 

 



