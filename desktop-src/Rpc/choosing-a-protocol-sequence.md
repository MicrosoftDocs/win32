---
title: Choosing a Protocol Sequence
description: Best practices for choosing a protocol sequence involve using ncacn\_ip\_tcp and ncalrpc, not ncacn\_np, ncacn\_spx, and ncadg\_\ .
ms.assetid: 4b81b534-f001-4522-bf63-044bf5f414f2
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Choosing a Protocol Sequence

**Best practice:** Use [**ncacn\_ip\_tcp**](https://msdn.microsoft.com/library/windows/desktop/aa367104) when making a remote call. Use [**ncalrpc**](https://msdn.microsoft.com/library/windows/desktop/aa367115) for local calls. Do not use [**ncacn\_np**](https://msdn.microsoft.com/library/windows/desktop/aa367108), [**ncacn\_spx**](https://msdn.microsoft.com/library/windows/desktop/aa367109), or any of the **ncadg\_\*** protocol sequences; they are less efficient and have inferior capabilities.

 

 




