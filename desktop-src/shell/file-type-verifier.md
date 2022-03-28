---
description: The File Type Verifier is a tool that enables independent software vendors (ISVs) to verify that their unique file types are implemented correctly.
ms.assetid: 1BD7452B-2DF5-44e9-9B09-C29ABFFA5F93
title: File Type Verifier
ms.topic: article
ms.date: 05/31/2018
---

# File Type Verifier

The File Type Verifier is a tool that enables independent software vendors (ISVs) to verify that their unique file types are implemented correctly. High quality implementations of your file type handlers are crucial for a good user experience because users interact with your file format in many ways in Windows Explorer. Users can do full-text searches, sort by custom metadata, or view rich thumbnails and previews of your file format.

For instructions on using the File Type Verifier, see [How To Use the File Type Verifier](how-to-use-the-file-type-verifier.md).

## About the File Type Verifier Tool

File Type Verifier is a program that is available as part of the [Windows 7 SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx). It is designed to help developers who create custom Windows [File Types](fa-file-types.md) to detect potential issues with their file types. Although the File Type Verifier runs only on Windows 7 and later, the rules that the File Type Verifier enforces apply to all versions of Windows where the features it checks are available.

The File Type Verifier runs several tests on the file type to verify that it is properly registered, and that it provides the appropriate [File Type Handlers](fa-file-extensions.md) to display the file type properly in Windows Explorer, and when appropriate, that it supports indexing the file content.

The File Type Verifier tests the following things:

- [Preview Handlers](building-preview-handlers.md)
- [Thumbnail Handlers](building-thumbnail-providers.md)
- [Property Handlers](../search/-search-3x-wds-extidx-propertyhandlers.md)
- [Verb Handlers](fa-verbs.md)
- [Filters (IFilter)](../search/-search-3x-wds-extidx-filters.md)
- [Kind Associations](../properties/building-property-handlers-user-friendly-kind-names.md)
- [Perceived Types](fa-perceivedtypes.md)
- [Important Properties](../search/-shell-systemdefinedpropertiesforfileformats.md)

## Related topics

<dl> <dt>

[How To Use the File Type Verifier](how-to-use-the-file-type-verifier.md)
</dt> <dt>

[Application Registration](app-registration.md)
</dt> <dt>

[File Types](fa-file-types.md)
</dt> <dt>

[How File Associations Work](fa-how-work.md)
</dt> <dt>

[Content View By File Type or Kind](prophand-content-view.md)
</dt> <dt>

[File Type Handlers](fa-file-extensions.md)
</dt> <dt>

[Programmatic Identifiers](fa-progids.md)
</dt> <dt>

[Perceived Types](fa-perceivedtypes.md)
</dt> <dt>

[Association Arrays](fa-associationarray.md)
</dt> </dl>

 

 
