---
title: Choosing a Protocol Sequence
description: Best practices for choosing a protocol sequence involve using ncacn\_ip\_tcp and ncalrpc, not ncacn\_np, ncacn\_spx, and ncadg\_\ .
ms.assetid: 4b81b534-f001-4522-bf63-044bf5f414f2
ms.topic: article
ms.date: 05/31/2018
---

# Choosing a Protocol Sequence

**Best practice:** Use [**ncacn\_ip\_tcp**](/windows/desktop/Midl/ncacn-ip-tcp) when making a remote call. Use [**ncalrpc**](/windows/desktop/Midl/ncalrpc) for local calls. Do not use [**ncacn\_np**](/windows/desktop/Midl/ncacn-np), [**ncacn\_spx**](/windows/desktop/Midl/ncacn-spx), or any of the **ncadg\_\*** protocol sequences; they are less efficient and have inferior capabilities.

 

 