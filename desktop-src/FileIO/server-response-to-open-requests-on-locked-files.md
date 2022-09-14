---
description: You can minimize the impact your application has on other clients and the impact they have on your application by granting as much sharing as possible, requesting the minimum access level necessary, and using the least intrusive opportunistic lock suitable for your application.
ms.assetid: c28b0ae0-0d35-4b59-9f54-87c55ca72716
title: Server Response to Open Requests on Locked Files
ms.topic: article
ms.date: 05/31/2018
---

# Server Response to Open Requests on Locked Files

The life of an opportunistic lock includes three distinct time spans. During each, the server determines by different means its reaction to a request from a client to open a file locked by another client. In general, you can minimize the impact your application has on other clients and the impact they have on your application by granting as much sharing as possible, requesting the minimum access level necessary, and using the least intrusive opportunistic lock suitable for your application.

First is the period after the server opens a file for a client but before it grants a lock. During this time, no lock exists on the file, and the server depends on sharing, access modes, and the type of opportunistic lock you request to determine its reaction to another request to open the same file. For example, if you open the file in question for write access, you may inhibit granting opportunistic locks that allow read caching access to other clients. The time span before the server grants a lock is typically in the millisecond range but may be longer.

After the opportunistic lock is granted, the server examines the lock to determine server reaction to an open request on a locked file. Again, how your application opened the file and the type of lock it holds affects how the server responds. For more information on how the server responds in each case, see [Types of Opportunistic Locks](types-of-opportunistic-locks.md).

Finally, there is the span after the server determines that your lock should be broken (ended) but before your application completes its reaction to the break. Depending on the type of lock, your application can downgrade the lock to a lower level or to none at all. Your application can also close the file and the lock. During this time, the server holds in abeyance any requests from other clients to open the formerly locked file. This time span may range from milliseconds to tens of seconds. For more information, see [Breaking Opportunistic Locks](breaking-opportunistic-locks.md).

 

 



