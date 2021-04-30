---
description: COM+ introduces neutral apartments to simplify programming in multithreaded environments. The neutral apartment is the preferred model for COM+ for components with no user interface.
ms.assetid: 679742af-7c04-4b0e-822a-a43e1aafa936
title: Neutral Apartments
ms.topic: article
ms.date: 05/31/2018
---

# Neutral Apartments

COM+ introduces neutral apartments to simplify programming in multithreaded environments. The neutral apartment is the preferred model for COM+ for components with no user interface.

In the past, to prevent bottlenecks, COM+ developers requiring server scalability had to implement free-threaded components; however, free-threading models are complicated to implement because they must deal with interlocking access. In neutral apartments, objects follow the guidelines for multithreaded apartments but can execute on any kind of thread. When a thread is running in a neutral apartment, the object's context is received without causing a thread switch.

Each process can have only one neutral apartment. To select a neutral apartment, use the following registry setting:

```
HKEY_LOCAL_MACHINE\SOFTWARE\Classes\CLSID
   {CLSID}
      InprocServer32
         ThreadingModel = Neutral
```

Components that have user interfaces should continue to use single-threaded apartments as the preferred model. To select a single-threaded apartment, use the following registry setting:

**ThreadingModel** = Apartment

 

 



