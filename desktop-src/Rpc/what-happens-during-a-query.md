---
title: What Happens During a Query
description: This section describes how the network handles the query when a 32-bit client searches for a name in its own domain.
ms.assetid: a8a88743-a245-4258-af05-9261c214ab50
ms.topic: article
ms.date: 05/31/2018
---

# What Happens During a Query

This section describes how the network handles the query when a 32-bit client searches for a name in its own domain.

When your client application calls [**RpcNsBindingImportBegin**](/windows/desktop/api/Rpcnsi/nf-rpcnsi-rpcnsbindingimportbegina), the locator residing on your client computer will try to satisfy this request. If there is nothing in the cache, it will forward the request by RPC to a master locator. If the master locator finds nothing in its cache, it sends the request to all the computers in the domain using a mail-slot broadcast. If there is a match, the locator on each computer will respond by a directed mail slot. (For example, if a process on that computer has exported the interface.) The responses are collated and the RPC is completed from the client's process locator, which will reply to the client process itself.

In a domain, the client locator searches for a master locator in the following places:

-   On the primary domain controller
-   On each backup domain controller

If a match is not found, the client locator declares itself to be the master locator. As such, it will broadcast queries if they cannot be satisfied locally.

In a workgroup, the client locator maintains a cache of the computers whose locators have broadcast. It uses the one that has been running the longest as the master locator. If that computer is unavailable, the next, longest-broadcasting computer is used, and so on. If the client needs a master locator and the cache is empty, it replenishes the cache by sending a special mail-slot broadcast that requests master locators to respond. If there are no responses, the client locator declares itself to be the master locator and will broadcast queries if they cannot be satisfied locally.

This changes if your client application is a 16-bit or MS-DOS-based program. In this case, there is no locator running on the client computer, and Rpcns1.dll or Rpcnslm.rpc contains the code to find a master locator. All requests are forwarded directly to the master locator.

These guidelines are valid for names in the client's domain, such as names for "/.:/entryname". If the client requests a name from another domain through the use of "/.../DOMAIN/entryname;" the client locator forwards the request to the specified domain which will broadcast it if it does not have the answer. If the domain is down or is actually a workgroup, the request will fail.

> [!Note]  
> Remember the following when working with entries in the name service:

 

-   A client cannot use the "/.../DOMAIN/entryname" syntax to find an entry in its own domain. Use the syntax "/.:/entryname". However, you can use "/.../DOMAIN/entryname" to find an entry in another domain.
-   The domain name in "/.../DOMAIN/entryname" must be uppercase. When looking for a match, the locator is case-sensitive.
-   Locator entry names are also case-sensitive, but need not be uppercase.
-   When the client uses the "/.:/entryname" syntax, the locator will not search for entries in other domains, even if they have a trust relationship with the logon domain.
-   Broadcasts do not cross LAN segments (for example, subnets). Thus, the usefulness of the locator is limited in an organization with multiple subnets.

 

 




