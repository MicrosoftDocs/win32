---
title: Asynchronous Monikers
description: Asynchronous Monikers
ms.assetid: 24c50f7b-f085-4086-aa44-81e5cab011cb
ms.topic: article
ms.date: 05/31/2018
---

# Asynchronous Monikers

The OLE moniker architecture provides a consistent, extensible programming model for working with Internet objects, providing methods for parsing names, representing Universal Resource Locators (URLs) as printable names, and locating and binding to the objects represented by URL strings. (Also see [URL Monikers](url-monikers.md).) Standard OLE monikers (notably, item, file, and pointer monikers), however, are inappropriate for the Internet because they are synchronous, returning a pointer to an object or its storage only at such time as all data is available. Depending on the amount of data to be downloaded, binding synchronously can tie up the client's user interface for prolonged periods.

The Internet requires new approaches to application design. Applications should be able to perform all expensive network operations asynchronously to avoid stalling the user interface. An application should be able to trigger an operation and receive notification on full or partial completion. At that point, the application should have the choice either of proceeding with the next step of the operation or providing additional information as needed. As a download proceeds, an application should also be able to provide users with progress information and the opportunity to cancel the operation at any time.

Asynchronous monikers provide these capabilities, as well as various levels of asynchronous binding behavior, while providing backward compatibility for applications that are either unaware of or do not require asynchronous behavior. Another OLE technology, asynchronous storage, works with asynchronous monikers to provide asynchronous downloading of an Internet object's persistent state. The asynchronous moniker triggers the bind operation and sets up the necessary components, including storage and stream objects, byte-array objects, and notification sinks. Once the components are connected, the moniker gets out of the way and the rest of the bind is executed mainly between the components implementing the asynchronous storage components and the object.

For more information, see the following topics:

-   [Asynchronous and Synchronous Monikers](./asynchronous-vs.-synchronous-monikers.md)
-   [Asynchronous and Synchronous Binding](./asynchronous-vs.-synchronous-binding.md)
-   [Asynchronous and Synchronous Storage](./asynchronous-vs.-synchronous-storage.md)
-   [Data-Pull Model and Data-Push Model](./data-pull-model-vs.-data-push-model.md)

## Related topics

<dl> <dt>

[URL Monikers](url-monikers.md)
</dt> </dl>

 

 