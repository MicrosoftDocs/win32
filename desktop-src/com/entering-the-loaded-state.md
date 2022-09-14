---
title: Entering the Loaded State
description: Entering the Loaded State
ms.assetid: 841b6f1a-cf9d-4a7e-9732-0701777a9617
ms.topic: article
ms.date: 05/31/2018
---

# Entering the Loaded State

When an object enters the loaded state, the in-memory structures representing the object are created so that operations can be invoked on it. The object's handler or in-process server is loaded. This process, referred to as *instantiation*, occurs when an object is loaded from persistent storage (a transition from the passive to the loaded state) or when an object is being created for the first time.

Internally, instantiation is a two-phase process. An object of the appropriate class is created, after which a method on that object is called to perform initialization and give access to the object's data. The initialization method is defined in one of the object's supported interfaces. The particular initialization method called depends on the context in which the object is being instantiated and the location of the initialization data.

 

 




