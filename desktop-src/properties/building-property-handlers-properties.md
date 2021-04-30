---
description: Properties are represented by IDs known as property identifiers (PIDs).
ms.assetid: a773c7b3-a1a2-4cce-ae5f-b54217ea06f4
title: Understanding Property Handlers
ms.topic: article
ms.date: 05/31/2018
---

# Understanding Property Handlers

Properties are represented by IDs known as property identifiers (PIDs). Each property MUST have a globally unique identifier (GUID). This identifier consists of a GUID, representing a collection of properties called a property set plus either a string or a 32-bit integer to identify the property within the set. If the integer form of ID is used, the values 0x00000000, 0xFFFFFFFF, and 0xFFFFFFFE are considered invalid. Vendors can guarantee that their properties are uniquely defined by placing them in a property set defined by their own GUIDs.

> [!IMPORTANT]
> It is critical that you define properties carefully and strategically for the first release of the schema. Any changes to custom properties (such as column width or property type) will not be reflected in the database after a schema has been registered. The only way to have these changes recognized after the schema has been registered once on a system would be either to rebuild the index and then register the new schema, or to register the schema and then create a new property (which consists of a canonical name and a PKEY) for each subequent release; for example `PKEY_GroupName_PropertyNameV2`, `PKEY_GroupName_PropertyNameV3`, and so forth). We do not recommend creating new properties in this manner, because multiple extraneous columns may impact system performance.

 

This topic is organized as follows:

-   [Metadata](#metadata)
    -   [Open Metadata](#open-metadata)
-   [About Property Handlers](#about-property-handlers)
-   [Legacy Technology](#legacy-technology)
-   [Related topics](#related-topics)

## Metadata

In Windows Vista and later, a new property system based on metadata is central to organizing items such as files, e-mail, and contacts. In this new property system, items can be searched based on their metadata, and users can read or write that metadata. Metadata in this system is represented by an extensible set of *properties* implemented as name/value pairs.

In Windows Vista and later, an extensive set of properties covers the specifics of items such as photos, music, documents, messages, contacts, and files. Independent software vendors (ISVs) can introduce their own properties to the platform if no existing property meets their needs.

### Open Metadata

The property system in Windows Vista and later is an open metadata system. A file format stores any property assigned to it and exposes that value when queried, regardless of relevance or meaning. This enables third-party developers to attach extra properties to the file without requiring a change in the property handler associated with it. Open metadata is a powerful concept. For more information about how to support open metadata for an XML-based file format, see "Supporting Open Metadata" in [Initializing Property Handlers](./building-property-handlers-property-handlers.md).

> [!Note]  
> Property handlers are always associated with specific file types; thus, if your file format contains properties that require a custom property handler, you should always register a unique file name extension for each file format.

 

## About Property Handlers

In Windows Vista and later, Windows has an extensible property system for storing and retrieving metadata in the files and data items that you access. Windows Explorer and the Windows Search system, along with other applications, use property handlers to read and modify this metadata. If you are a developer who owns a specific file type, you should register a property handler to give the property system access to the metadata in your files. In some cases, you might be able to use an existing property handler that can read and understand your file format and its properties; in other cases, you might need to develop a new property handler for your file type.

The first step in writing a property handler is to consider what properties your file type supports. Property values are stored in the file stream, primarily to enable transportability. When the property values are stored in the file itself, as they are in this system, a user can copy a file to another computer, a USB flash drive, or another file system, or sends the file as an e-mail attachment, the properties travel with the file and never get out of sync or lost. Therefore, if the file format supports storing extra information, it is best to store the properties in the file itself.

The next step is to determine which properties the file should provide. You might initially think that a limited set of properties is adequate. An audio file could support only audio-related properties and end there. However, that audio file could be a recording of a session of a court of law, archived by a law firm. In that case, the law firm would certainly want to associate other non-audio properties with this file, such as the case number. The provider of the audio file format cannot possibly determine all of the scenarios in which their format will ever be used. They should therefore consider enabling blanket storage of any arbitrary property supported by the property system.

## Legacy Technology

Microsoft Windows NT File System (NTFS) secondary stream technology was developed to support the persistence of extra information with the file through an alternate stream set at the file system layer. One might wonder why those secondary streams are not used as the main method to store properties, especially with open metadata support. The primary reason is the transportability of this extra information. Unfortunately, these alternate streams are removed in many scenarios including client-side caching support (CSC), sending files as attachments, and copying files to a non-NTFS store.

Secondary streams do not provide a robust solution in which properties are guaranteed to travel with the file, and hence, the Windows Vista property system does not provide a built-in mechanism that exploits the secondary NTFS streams for property storage. ISVs are also highly discouraged from building property handlers that use secondary streams for the storage of properties. Of course there are scenarios where NTFS secondary streams are appropriate, particularly when applications can guarantee that the file they are dealing with is always stored in an NTFS volume and will not travel as a result of end user interaction.

## Related topics

<dl> <dt>

[Using Kind Names](./building-property-handlers-user-friendly-kind-names.md)
</dt> <dt>

[Using Property Lists](./building-property-handlers-property-lists.md)
</dt> <dt>

[Initializing Property Handlers](./building-property-handlers-property-handlers.md)
</dt> <dt>

[Registering and Distributing Property Handlers](./prophand-reg-dist.md)
</dt> <dt>

[Property Handler Best Practices and FAQ](./prophand-bestprac-faq.md)
</dt> </dl>

 

 
