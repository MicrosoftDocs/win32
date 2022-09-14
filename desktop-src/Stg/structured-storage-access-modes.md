---
title: Structured Storage Access Modes
description: Mechanisms for controlling simultaneous access to an object, by multiple processes and users, are essential.
ms.assetid: 2d524c2b-f2b4-49f2-9be8-2037846eb9e9
keywords:
- Structured Storage Strctd Stg , fundamentals, API functions, flags for access
ms.topic: article
ms.date: 05/31/2018
---

# Structured Storage Access Modes

Mechanisms for controlling simultaneous access to an object, by multiple processes and users, are essential. COM provides these mechanisms by defining access modes for both storage and stream objects. The access mode specified for a parent storage object is inherited by its children, though you can place additional restrictions on the child storage or stream. A nested storage or stream object can be opened in the same mode or in a more restricted mode than that of its parent, but it cannot be opened in a less restricted mode than that of its parent.

You specify access modes by using the values listed in [**STGM Constants**](stgm-constants.md). These values serve as flags to be passed as arguments to methods in the [**IStorage**](/windows/desktop/api/Objidl/nn-objidl-istorage) interface and associated API functions. Typically, several flags are combined in the parameter *grfMode*, using a Boolean **OR** operation.

The flags fall into six groups. Only one flag from each group can be specified at a time:

-   [Transaction Flags](transaction-flags.md)
-   [Storage Creation Flags](storage-creation-flags.md)
-   [Temporary Creation Flags](temporary-creation-flags.md)
-   [Priority Flags](priority-flags.md)
-   [Access Permission Flags](access-permission-flags.md)
-   [Shared Access Flags](shared-access-flags.md)

 

 




