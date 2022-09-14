---
title: Performance Attributes
description: Use the following attributes in an IDL file to reduce the size of the stub code or otherwise improve performance.
ms.assetid: 0f23265e-7f3e-4a15-ac3b-1d852a8110eb
keywords:
- IDL MIDL , attributes, performance
ms.topic: article
ms.date: 05/31/2018
---

# Performance Attributes

Use the following attributes in an IDL file to reduce the size of the stub code or otherwise improve performance.



| Attribute                             | Usage                                                                                                                                                |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**ignore**](ignore.md)              | Designates that a pointer contained in a structure or union and the object indicated by the pointer is not to be transmitted.                        |
| [**local**](local.md)                | Designates a function that is local to the application for which MIDL does not need to generate stub code.                                           |
| [**wire\_marshal**](wire-marshal.md) | Defines a data type as a simpler type for transmission over a network and allows you to implement marshaling and unmarshaling routines for the type. |



 

## Related topics

<dl> <dt>

[Memory Management ACF Attributes](memory-management-acf-attributes.md)
</dt> <dt>

[Stub Optimization ACF Attributes](stub-optimization-acf-attributes.md)
</dt> </dl>

 

 




