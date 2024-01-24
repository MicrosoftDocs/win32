---
description: If data is coherent, data on the server and all the clients is synchronized. One type of software system that provides data coherency is a revision control system (RCS).
ms.assetid: cd33d20e-bf25-4a50-9b20-344495554434
title: Data Coherency
ms.topic: article
ms.date: 05/31/2018
---

# Data Coherency

Data that is *coherent* is data that is the same across the network. In other words, if data is coherent, data on the server and all the clients is synchronized. One type of software system that provides data coherency is a revision control system (RCS). Such a system is usually fairly simple, with only one user allowed to modify a specified file at a time. Others can read the file but cannot change it.

The user who can change a file is said to have checked it out. The user then checks in the modified file so that others may see the changes. Only after the user has checked a file back in can another user check it out.

An RCS requires the active intervention of users to operate in a useful manner. A file system that operates across a network should handle the problem automatically.

Providing local caching of coherent data is fairly simple when you have one thread on one client accessing a file across the network at a time. However, in most situations many different threads on one or more computers may be reading the same file. This situation is still fairly straightforward. Because the data in the file is static, each client computer can have its own local copy with no implications for data coherency.

A more common situation is one thread modifying the file, and a lot of other threads reading it. The moment a write operation occurs, all of the local caches of that file are obsolete. The server must notify each client to abandon its cache. Any subsequent read operations for the file must be performed across the network.

In another common situation, multiple threads on one or more network clients might try to write to the same file. This situation is similar to a one in which several RCS users all want to make changes to the same file. Each user in sequence must check out the file, make changes, and then check the file back in. Similarly, in a local caching scheme the server must hand off the privilege of writing to a file to one client thread at a time.

 

 



