---
title: Sorting (ADSI)
description: A client can request a server to sort the result set.
ms.assetid: 795d27f0-0bfa-417e-aa1f-f2471f92dc45
ms.tgt_platform: multiple
ms.topic: article
ms.date: 05/31/2018
---

# Sorting (ADSI)

A client can request a server to sort the result set. You can specify:

-   Sort order: Either ascending or descending sort order can be specified.
-   Sort attributes: Multiple attributes can be specified in a sort string. For example, sort by Last Name, then First Name.

When you specify sort order, you should try to use one of the indexed attributes. Otherwise, the server must calculate a complete result set before sending it to the client. This is true even if you have requested a paged search and specified a page size.

> [!Note]  
> Not all directory servers support multiple attribute sorts or sort order.

 

 

 




