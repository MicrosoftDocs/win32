---
title: Multiple Directory Services
description: One challenge of working within a distributed computing environment is identifying and locating resources such as users, groups, print queues, and documents.
ms.assetid: 66929290-b830-4768-a2ae-604d1a9de5c4
ms.tgt_platform: multiple
keywords:
- Multiple Directory Services ADSI
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Directory Services

One challenge of working within a distributed computing environment is identifying and locating resources such as users, groups, print queues, and documents. A directory service is the part of a distributed computing environment that provides a way to locate and identify the users and resources available in the system. A directory service is like a phone directory. Given a name for a person or a resource, it provides the data necessary to access that person or resource. You do not have to start with binding data to access a resource on the network.

Most enterprises already have many different directories in place. For example, network operating systems, electronic mail systems, and "groupware" products all have their own directories. Many issues arise when a single enterprise deploys multiple directories. These issues include usability, data consistency, development cost, and support cost, among others.

These issues are addressed in ADSI, in that there is provided a single, consistent, open set of interfaces that can be used for managing and using any directory service that has an ADSI provider.

 

 




