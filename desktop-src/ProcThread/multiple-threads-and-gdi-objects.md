---
description: To enhance performance, access to graphics device interface (GDI) objects (such as palettes, device contexts, regions, and the like) is not serialized.
ms.assetid: aefb6a0b-ca00-4951-a173-8d7806b5d4e7
title: Multiple Threads and GDI Objects
ms.topic: article
ms.date: 05/31/2018
---

# Multiple Threads and GDI Objects

To enhance performance, access to graphics device interface (GDI) objects (such as palettes, device contexts, regions, and the like) is not serialized. This creates a potential danger for processes that have multiple threads sharing these objects. For example, if one thread deletes a GDI object while another thread is using it, the results are unpredictable. This danger can be avoided simply by not sharing GDI objects. If sharing is unavoidable (or desirable), the application must provide its own mechanisms for synchronizing access. For more information about synchronizing access, see [Synchronizing Execution of Multiple Threads](synchronizing-execution-of-multiple-threads.md).

 

 



