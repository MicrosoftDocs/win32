---
title: Linked Objects
description: Linked Objects
ms.assetid: 105b3060-b6c0-4186-9855-c742109d9c5a
ms.topic: article
ms.date: 05/31/2018
---

# Linked Objects

When a link to an object is inserted in a compound document, the source data, or *link source*, continues to reside wherever it was initially created, usually in another document. The compound document contains only a reference, or *link*, to the actual data stored at the link source, along with information about how to present that data to the user.

Activating a link runs the link source's server application, which the user requires in order to edit or otherwise manipulate the link data. Linking keeps the size of a compound document small. It is also useful when the data source is maintained by someone else and must be shared among many users. If the person maintaining the link source changes the data, the change is automatically updated in all documents containing a link to that data. In addition to creating simple links, users can nest links and combine linked and embedded objects to create complex documents.

## Related topics

<dl> <dt>

[Creating Linked and Embedded Objects from Existing Data](creating-linked-and-embedded-objects-from-existing-data.md)
</dt> <dt>

[Distributed Link Tracking and Object Identifiers](/windows/desktop/FileIO/distributed-link-tracking-and-object-identifiers)
</dt> <dt>

[Linked Objects and Monikers](linked-objects-and-monikers.md)
</dt> </dl>

 

 