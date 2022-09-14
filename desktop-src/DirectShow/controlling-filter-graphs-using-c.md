---
description: Controlling Filter Graphs Using C
ms.assetid: 56e41f0a-2ea6-422c-8d3f-7849e91e3731
title: Controlling Filter Graphs Using C
ms.topic: article
ms.date: 05/31/2018
---

# Controlling Filter Graphs Using C

If you are writing a DirectShow application in C (rather than C++), you must use a vtable pointer to call methods. The following example illustrates how to call the **IUnknown::QueryInterface** method from an application written in C:


```C++
pGraph->lpVtbl->QueryInterface(pGraph, &IID_IMediaEvent, (void **)&pEvent);
```



The following shows the equivalent call in C++:


```C++
pGraph->QueryInterface(IID_IMediaEvent, (void **)&pEvent);
```



In C, COM interfaces are defined as structures. The **lpVtbl** member is a pointer to a table of interface methods (the vtable). All methods take an additional parameter, which is a pointer to the interface.

## Related topics

<dl> <dt>

[Appendixes](appendixes.md)
</dt> </dl>

 

 



