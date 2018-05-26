---
title: Multi-Threaded Issues
description: Multi-Threaded Issues
ms.assetid: 17e74d2a-af4f-4188-89fa-b4f50abc424f
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Multi-Threaded Issues

OLE provides support for multithreaded applications, allowing applications to make OLE calls from multiple threads. This multithreaded support is called the apartment model, it is important that all OLE components using multiple threads follow this model. The apartment model requires that interface pointers are marshaled (using [**CoMarshalInterface**](/windows/win32/combaseapi/nf-combaseapi-comarshalinterface?branch=master), and [**CoUnmarshalInterface**](/windows/win32/combaseapi/nf-combaseapi-counmarshalinterface?branch=master)) when passed between threads.

## Related topics

<dl> <dt>

[Processes, Threads, and Apartments](processes--threads--and-apartments.md)
</dt> </dl>

 

 




