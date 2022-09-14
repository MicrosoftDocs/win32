---
title: Common Resource Attributes
description: The resource-definition statements supported on 16-bit Windows include a load-mem option that specifies the loading and memory characteristics of the resource.
ms.assetid: 53740997-854b-447c-9ab1-de8e17c0de1e
ms.topic: article
ms.date: 05/31/2018
---

# Common Resource Attributes

The resource-definition statements supported on 16-bit Windows include a *load-mem* option that specifies the loading and memory characteristics of the resource. These attributes are permitted in resource scripts for backward compatibility, but they are ignored. Windows resources are loaded when the corresponding module is loaded, and are freed when the module is unloaded.

## Load Attributes

The load attributes specify when the resource is to be loaded. The load parameter must be one of the following attributes.



| Attribute      | Description                                                                  |
|----------------|------------------------------------------------------------------------------|
| **PRELOAD**    | Ignored. In 16-bit Windows, the resource is loaded with the executable file. |
| **LOADONCALL** | Ignored. In 16-bit Windows, the resource is loaded when called.              |



 

## Memory Attributes

The memory attributes specify whether the resource is fixed or movable, whether it is discardable, and whether it is pure. The memory parameter can be one or more of the following attributes.



| Attribute       | Description                                                                                                                               |
|-----------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **FIXED**       | Ignored. In 16-bit Windows, the resource remains at a fixed memory location.                                                              |
| **MOVEABLE**    | Ignored. In 16-bit Windows, the resource can be moved if necessary to compact memory.                                                     |
| **DISCARDABLE** | Ignored. In 16-bit Windows, the resource can be discarded if no longer needed.                                                            |
| **PURE**        | Ignored. Accepted for compatibility with existing resource scripts.                                                                       |
| **IMPURE**      | Ignored. Accepted for compatibility with existing resource scripts.                                                                       |
| **SHARED**      | Ignored. In 16-bit Windows, SHARED is ignored for regular modules. For a resource from a ROM Windows module, the memory is shared.        |
| **NONSHARED**   | Ignored. In 16-bit Windows, NONSHARED is ignored for regular modules. For a resource from a ROM Windows module, the memory is not shared. |



 

 

 




