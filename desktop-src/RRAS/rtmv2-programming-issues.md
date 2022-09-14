---
title: RTMv2 Programming Issues
description: RTMv2 functions are written with the following assumptions.
ms.assetid: c8c6f553-57cc-4eec-bbc0-b6b50897cc75
keywords:
- Programming issues, RTMv2
ms.topic: article
ms.date: 05/31/2018
---

# RTMv2 Programming Issues

RTMv2 functions are written with the following assumptions.

-   RTMv2 functions do not allocate memory for the client. The client must always allocate memory.
-   When a client is unregistering, it must perform clean-up operations itself, such as releasing all memory allocated.
-   Clients must release handles correctly; memory leaks can occur if a client does not observe this practice.

 

 




