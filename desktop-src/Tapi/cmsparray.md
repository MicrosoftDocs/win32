---
description: The CMSPArray template implements a smart array that will grow on demand.
ms.assetid: 9b30885c-01a4-4aea-a1c3-5d7966e4697f
title: CMSPArray
ms.topic: article
ms.date: 05/31/2018
---

# CMSPArray

The CMSPArray template implements a smart array that will grow on demand. It is designed to hold small arrays with simple data types. It doesn't have a critical section. Its only dependencies are **realloc** and **memmove**. It is used internally to keep lists of object pointers. It is similar to ATL's **CSimpleArray** implementation, but it is more efficient for initial allocations.

This template is defined in MSPutils.h.

 

 



