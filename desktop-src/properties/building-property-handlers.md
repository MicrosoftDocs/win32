---
description: Learn how to create a property handler that reads and writes properties to and from a file stream. Each handlers is associated with a given file type.
ms.assetid: 9dacd399-2cf3-40dd-9501-f26f0281500d
title: Implementing Property Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Implementing Property Handlers

In Windows Vista and later, metadata became central as a method of organizing items such as files, e-mail, or contacts. To enable a system where items can be searched based on their metadata and where users can read or write that metadata, Windows Vista introduced a new property system. Metadata in this system is represented by an extensible set of properties. In this set of topics we describe how you can create a handler that reads and writes properties to and from a file stream. These handlers are called property handlers and each is associated with a given file types, identified by the file name extension.

The following topics discuss the requirements and strategies involved in defining your properties and property handlers.

-   [Understanding Property Handlers](./building-property-handlers-properties.md)
-   [Using Kind Names](./building-property-handlers-user-friendly-kind-names.md)
-   [Using Property Lists](./building-property-handlers-property-lists.md)
-   [Initializing Property Handlers](./building-property-handlers-property-handlers.md)
-   [Registering and Distributing Property Handlers](./prophand-reg-dist.md)
-   [Property Handler Best Practices and FAQ](./prophand-bestprac-faq.md)

## Related topics

<dl> <dt>

[Creating Custom Properties](./building-property-handlers-property-schemas.md)
</dt> <dt>

[Property Description Schema](./propdesc-schema-entry.md)
</dt> </dl>

 

 
