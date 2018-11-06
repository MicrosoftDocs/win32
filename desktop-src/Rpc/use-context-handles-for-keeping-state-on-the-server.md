---
title: Use Context Handles for Keeping State on the Server
description: Use Context Handles for Keeping State on the Server
ms.assetid: ee511745-04cf-445d-a02b-41734aabc193
ms.topic: article
ms.date: 05/31/2018
---

# Use Context Handles for Keeping State on the Server

**Best practice:** Whenever state is kept on the server between calls, use context handles.

Context handles are often intimidating for new RPC programmers, and the overhead of learning context handles may not initially appear worth the effort. It is worth it because context handles have built-in solutions for many common pitfalls encountered in network programming that otherwise would have to be implemented from scratch. Understanding context handles pays dividends later.

 

 




