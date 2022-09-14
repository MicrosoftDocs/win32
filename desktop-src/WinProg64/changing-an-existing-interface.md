---
title: Changing an Existing Interface
description: Whenever possible, implement a new interface for your application, rather than making changes to an existing one.
ms.assetid: 29845cf5-445c-403d-b298-d4e07c3536b7
keywords:
- changing existing interfaces 64-bit Windows Programming
ms.topic: article
ms.date: 05/31/2018
---

# Changing an Existing Interface

Whenever possible, implement a new interface for your application, rather than making changes to an existing one. If you cannot avoid changing an existing interface, use new data types in new methods only. Introducing a new data type or modifying an existing type is the most common source of incompatibility problems. The RPC run-time model assumes that the receiving application knows about the types of data that it receives, so data is put onto the wire without a generic data description. When the recipient expects a different data type than what the sender has put on the wire, the stub raises an exception (or transmission fails in some other less graceful manner).

An RPC interface is defined by its UUID and its major and minor version numbers. When you change an existing interface, you should add the new methods at the end of the interface and change the minor version number. If you add methods anywhere else or make any other changes to the interface, you will also need to change the major version number.

Realistically, there are times when you cannot change even the minor version number, because a new client will not be able to communicate with an old server and you cannot update the server. The RPC run time raises an exception, RPC\_S\_PROCNUM\_OUT\_OF\_RANGE, when a client calls a method beyond the ones specified for its interface with the server. The workaround is to leave the version numbers unchanged and write your client code to handle this exception gracefully—by the client degrading its performance, for example, or by whatever means are appropriate for your application.

There is a similar workaround for one special case of changing a data type in an existing method. If you have a [**union**](/windows/desktop/Midl/union) whose branches are pointers and that does not have a default branch for unrecognized types, you can add a new branch that uses the new data type. This will not change the size of the data structure. When your client talks to a new server, it can use the new data type. However, when your client talks to an old server, the run time will raise the exception RPC\_S\_INVALID\_TAG. Again, you will need to write your client code to handle this exception appropriately.

A DCOM interface is identified by its GUID. In DCOM, interfaces are considered immutable and you can make changes only by creating a new interface that inherits from the old one. These rules ensure that clients and servers remain compatible.

 

 