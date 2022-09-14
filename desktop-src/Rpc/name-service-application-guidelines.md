---
title: Name Service Application Guidelines
description: When you develop your distributed application, you need to provide the application users with a method for specifying the name under which they can register the application in the name service database.
ms.assetid: cda997b3-6031-4c0f-affc-c766ba4b7fd5
ms.topic: article
ms.date: 05/31/2018
---

# Name Service Application Guidelines

When you develop your distributed application, you need to provide the application users with a method for specifying the name under which they can register the application in the name service database. This method can consist of a data file, command-line input, or dialog box.

Although the RPC name service architecture supports various methods for organizing an application's server entries, it is optimized for lookups. As a result, frequent updates can hinder the performance of both the name service and the application. To avoid exporting information unnecessarily, choose a design that lets the server determine whether its information is in the name service database. In addition, each server instance should export to its own entry name. Otherwise, it will be difficult for an instance to change its supported object UUIDs or protocol sequences without disturbing another instance's information.

The following method avoids these pitfalls and provides good performance, no matter what name service your network uses.

To begin with, design your application so that the first time a given server instance starts, it picks a unique server-entry name and saves this name in the registry along with the application's other configuration information. Then, have it export its binding handles and object UUIDs, if any, to its name service entry.

Subsequent invocations of the server instance should check that the name service entry is present and contains the correct set of object UUIDs and binding handles. A missing entry may mean that an administrator removed it, or that a power outage caused the name service information to be lost. It is important to verify that the binding handles in the entry are correct; if an administrator adds TCP/IP support to a computer, for example, RPC servers will listen on that protocol sequence when they call [**RpcServerUseAllProtseqs**](/windows/desktop/api/Rpcdce/nf-rpcdce-rpcserveruseallprotseqs). However, if the server does not update the name service entry, clients will not be informed that TCP is supported.

When the client imports, it should specify **NULL** as the entry name. Specifying **NULL** causes the Microsoft RPC library functions to search for the interface in all name service entries in the client computer's domain or workgroup, thus finding the information for every instance.

If you use object UUIDs to represent well-known objects such as printers, you can use a variation of this method. Instead of exporting bindings to one entry, design your application so that each instance creates an entry for each supported object, such as "/.:/printers/Laser1" and "/.:/printers/Laser2." Then, have the server export its binding handles to each server entry, along with the object UUID relevant to that entry.

In this case, a client can look up a resource by name by importing from the relevant server entry; it does not require the object UUID of the resource. If it has the resource UUID but not the name, it can import from the **null** entry.

 

 




