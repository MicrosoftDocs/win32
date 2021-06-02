---
description: Some applications are designed in a way that prevents multiple instances of the application from being installed on a computer.
ms.assetid: 951d20c8-7908-40d8-a9d5-d321340c97f3
title: Application Design Restrictions
ms.topic: article
ms.date: 05/31/2018
---

# Application Design Restrictions

Some applications are designed in a way that prevents multiple instances of the application from being installed on a computer. With such a limitation, an application cannot make use of the partitions feature. The following application design features might need to be modified before partitions can be used for that application.

## Tables and Arrays

Some applications create database tables, in-memory tables, or arrays that use a CLSID as a unique registry key. On a computer without partitions, this registry key is typically computer/CLSID (one CLSID per computer).

Conversely, on a computer with partitions, this registry key is computer/partition ID/application ID/CLSID (multiple instances of a CLSID per computer). Because the partitions feature allows multiple instances of a CLSID to exist on a computer, applications that contain design elements that require a unique CLSID per computer might be adversely affected.

## Global Resources

Some applications use global resources such as shared memory, data files, and registry entries. This could cause problems if multiple instances of such an application are executing simultaneously.

For example, if a component uses shared memory for interacting with other components, the component will need to be modified so that each instance of the component allocates its own shared memory.

## Type Libraries

Type libraries provide information about a component's interfaces and methods. This information is used for several purposes, including the following:

-   Marshaling data between components when function calls are made
-   Helping the COM+ Queued Components and COM+ Events services
-   Providing the correct information within a Microsoft Visual Basic editor

References to a type library are installed in the registry of a computer. When developing applications that will be invoked from within partitions, it is important that the latest version of a type library is installed in the registry. This ensures that the Visual Basic editor being used will get accurate information about the methods available for that component.

## Related topics

<dl> <dt>

[COM+ Queued Components and Partitions](com--queued-components-and-partitions.md)
</dt> <dt>

[Partition Implementation](partition-implementation.md)
</dt> <dt>

[Registering and Activating Components in Partitions](registering-and-activating-components-in-partitions.md)
</dt> <dt>

[What Are COM+ Partitions?](what-are-com--partitions-.md)
</dt> </dl>

 

 



