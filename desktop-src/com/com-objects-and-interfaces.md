---
title: COM Objects and Interfaces
description: COM Objects and Interfaces
ms.assetid: a3b78086-0f02-4b3f-a856-46bfcf4457f4
ms.topic: article
ms.date: 05/31/2018
---

# COM Objects and Interfaces

COM is a technology that allows objects to interact across process and computer boundaries as easily as within a single process. COM enables this by specifying that the only way to manipulate the data associated with an object is through an *interface* on the object. When this term is used in this documentation, it refers to an implementation in code of a COM binary-compliant interface that is associated with an object.

COM uses the word *interface* in a sense different from that typically used in Visual C++ programming. A C++ interface refers to all of the functions that a class supports and that clients of an object can call to interact with it. A COM interface refers to a predefined group of related functions that a COM class implements, but a specific interface does not necessarily represent all the functions that the class supports.

Referring to an object *implementing* an interface means that the object uses code that implements each method of the interface and provides COM binary-compliant pointers to those functions to the COM library. COM then makes those functions available to any client who asks for a pointer to the interface, whether the client is inside or outside of the process that implements those functions.

For more information, see the following topics:

-   [Interfaces and Interface Implementations](interfaces-and-interface-implementations.md)
-   [Interface Pointers and Interfaces](interface-pointers-and-interfaces.md)
-   [IUnknown and Interface Inheritance](iunknown-and-interface-inheritance.md)

## Related topics

<dl> <dt>

[Interfaces](interfaces.md)
</dt> </dl>

 

 




