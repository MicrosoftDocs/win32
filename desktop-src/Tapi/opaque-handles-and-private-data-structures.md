---
description: Opaque handles are used in TSPI to refer to the data structures representing lines, phones, and call appearances.
ms.assetid: aa1742aa-6cd4-461a-ad92-972eefcf637f
title: Opaque Handles and Private Data Structures
ms.topic: article
ms.date: 05/31/2018
---

# Opaque Handles and Private Data Structures

Opaque handles are used in TSPI to refer to the data structures representing lines, phones, and call appearances. These appear as parameters to most of the functions and callbacks. There are few functions that refer to the device using a device identifier instead of an opaque handle. In such a case, the reference is to the device itself rather than to a data structure. Functions that work in this fashion are typically those called at early initialization times before data structures are created and opaque handles are exchanged.

The service provider must decide how to interpret these handles. A service provider typically uses the pointer to its data structure or to the index into an array of data structures as its opaque handle. The only restriction is that the service provider cannot use the value 0 as an [HDRVLINE](hdrvline.md), HDRVCALL, or [HDRVPHONE](hdrvphone.md). The value 0 or **NULL** for a handle has a special meaning in some operations.

 

 



