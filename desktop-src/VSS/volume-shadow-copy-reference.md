---
description: The Volume Shadow Copy Service (VSS) is a set of COM and C++ APIs that enable volume backups to be performed while applications on the system (called writers) continue to write to the volumes.
ms.assetid: 94d9504b-2838-4516-8031-daa7bd9d2fec
title: Volume Shadow Copy API Reference
ms.topic: article
ms.date: 05/31/2018
---

# Volume Shadow Copy API Reference

The Volume Shadow Copy Service (VSS) is a set of COM and C++ APIs that enable volume backups to be performed while applications on the system (called writers) continue to write to the volumes.

VSS supports these backups through the creation of shadow copies, a duplicate of the original volume at a given point in time.

Third-party developers can use the VSS API to create requesters (such as a backup application) to create and manage shadow copies.

The actual work of creating and representing shadow copies is conducted by system-level applications known as providers.

Developers can also use the API to construct writers: VSS-aware applications that are able to coordinate I/O operations with the creation and manipulation of shadow copies.

-   [Volume Shadow Copy API Classes](volume-shadow-copy-api-classes.md)
-   [Volume Shadow Copy API Data Types](volume-shadow-copy-api-data-types.md)
-   [Volume Shadow Copy API Enumerations](volume-shadow-copy-api-enumeration-types.md)
-   [Volume Shadow Copy API Functions](volume-shadow-copy-api-functions.md)
-   [Volume Shadow Copy API Interfaces](volume-shadow-copy-api-interfaces.md)
-   [Volume Shadow Copy API Structures](volume-shadow-copy-api-structures.md)
-   [Volume Shadow Copy Glossary](volume-shadow-copy-glossary.md)

For more information on writing requesters and writers, see [Using the Volume Shadow Copy Service](using-the-volume-shadow-copy-service.md).

 

 



