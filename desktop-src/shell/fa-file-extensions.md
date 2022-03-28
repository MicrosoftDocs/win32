---
description: Registering a file type is the first step in creating a file association, which makes that file type &\#0034;known&\#0034; to the Shell. However, without file type handlers, the Shell is unable to expose information to the user from and about the file.
ms.assetid: c0c5c3ef-35ff-4ab6-bb8a-1f0640109d50
title: File Type Handlers
ms.topic: article
ms.date: 05/31/2018
---

# File Type Handlers

[Registering a file type](fa-how-work.md) is the first step in creating a file association, which makes that file type "known" to the Shell. However, without file type handlers, the Shell is unable to expose information to the user from and about the file.

This topic is organized as follows:

- [Make a File Type Known to Shell](#make-a-file-type-known-to-shell)
- [File Type Handler Descriptions](#file-type-handler-descriptions)
- [Related topics](#related-topics)

## Make a File Type Known to Shell

In the following screen shot of Windows Explorer, the image file Desert.known appears in the Shell **Pictures** library, and is associated only with the Paint application.

![screen shot showing explorer opening an image with no file type](images/file-assoc/fileassoc-filetypehandler.png)

The Desert.known file in the preceding screen shot lacks the following functionality that is enabled by a file type handler:

-   Thumbnail or preview
-   Image-specific verbs in the shortcut menu, such as:
    -   Rotate Preview
    -   Set as Desktop Background
    -   Print
-   Image-specific properties in the **Details** pane, such as:
    -   Date Taken
    -   Tags
    -   Rating
-   Indexing of file text

In the following screen shot, the same file (Desert.known) has the .jpg extension, which is a registered file type that has associated file type handlers, so a thumbnail image and more properties are shown.

![image with a registered file type and associated file type handlers](images/file-assoc/fileassoc-filetypehandler-2ndex.png)

## File Type Handler Descriptions

The functionality provided by each file type handler is listed in the following table:



| Handler                                                      | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|--------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [Shortcut menu](context-menu-handlers.md)                   | A shortcut menu handler, sometimes referred to as a context menu handler, is a file type handler that adds commands to an existing context menu. These handlers are associated with a particular file type and are called any time a context menu is displayed for a member of the file type.                                                                                                                                                                                                                                                                           |
| [Thumbnail](thumbnail-providers.md)                         | A handler that provides an image to represent a Shell item.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [Property](../properties/building-property-handlers-properties.md) | A property handler that provides access to item properties for Windows Search, the Windows Explorer and other applications that need to access properties.                                                                                                                                                                                                                                                                                                                                                                                                              |
| [Preview](preview-handlers.md)                              | A handler that quickly produces a read-only, simplified view of the item to be displayed in the Windows Explorer preview pane.                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| [Filters](../search/-search-3x-wds-extidx-filters.md)              | A filter, an implementation of the [**IFilter**](/windows/win32/api/filter/nn-filter-ifilter) interface, that scans documents for text and properties (also called attributes). It extracts chunks of text from these documents, filtering out embedded formatting and retaining information about the position of the text. It also extracts chunks of values, which are properties of an entire document or of well defined parts of a document. **IFilter** provides the foundation for building higher-level applications such as document indexers and application-independent viewers. |



 

## Related topics

<dl> <dt>

[Application Registration](app-registration.md)
</dt> <dt>

[File Types](fa-file-types.md)
</dt> <dt>

[How File Associations Work](fa-how-work.md)
</dt> <dt>

[Content View By File Type or Kind](prophand-content-view.md)
</dt> <dt>

[File Type Verifier](file-type-verifier.md)
</dt> <dt>

[Programmatic Identifiers](fa-progids.md)
</dt> <dt>

[Perceived Types](fa-perceivedtypes.md)
</dt> <dt>

[Association Arrays](fa-associationarray.md)
</dt> </dl>

 

 
