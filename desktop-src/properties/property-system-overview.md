---
description: The Windows Property System is an extensible read/write system of data definitions that provides a uniform way of expressing metadata about Shell items.
ms.assetid: eb2dc2be-fc53-40aa-81f6-f353ab1d3a57
title: Property System Overview
ms.topic: article
ms.date: 05/31/2018
---

# Property System Overview

The Windows Property System is an extensible read/write system of data definitions that provides a uniform way of expressing metadata about Shell items. The Windows Property system in Windows Vista and later enables you to store and retrieve metadata for Shell items. A Shell item is any single piece of content, such as a file, folder, email, or contact. A property is an individual piece of metadata associated with a Shell item. Property values are expressed as a [**PROPVARIANT**](/windows/win32/api/propidlbase/ns-propidlbase-propvariant) structure.

This topic is organized as follows:

-   [Introduction](#introduction)
-   [Development Scenarios](#development-scenarios)
-   [Properties and Windows Search](#properties-and-windows-search)
-   [Note to Implementers](#note-to-implementers)
-   [Windows Property System Documentation](#windows-property-system-documentation)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## Introduction

Properties are uniquely identified by their canonical name (such as `System.Document.LastAuthor`) and property key (such as `PKEY_Document_LastAuthor`). A property key (PKEY) is the name portion of a name-value pair that consists of a PKEY/PROPVARIANT or a string/PROPVARIANT, where the string is the canonical name of the PKEY (such as `System.Document.LastAuthor`). A PKEY is a definition that tells the property system everything it needs to know about the property, whereas the value is an actual instance of the property. A PKEY internally contains a formatID and propID.

An individual property consists of the following three pieces:

-   A canonical name, such as `System.Music.Artist`.
-   A schema description, which is specified in the .propdesc XML file format and expressed programmatically through [**IPropertyDescription**](/windows/desktop/api/Propsys/nn-propsys-ipropertydescription).
-   A value, such as the name of a singer.

The schema description consists of information about the property, such as the property name, data type, constraints, information on how the property interacts with views and the search system, and so forth. The name and schema description are defined globally, and are the same for all items and types. A value is specific to an individual item. That is, the `System.Music.Artist` property is always defined as a multi-value string, but may have a different value (or no value at all) for each item.

A property handler translates data stored in a file into a structured schema that is recognized by and can be accessed by Windows Explorer, Windows Search, and other applications. These systems can then interact with the property handler to write and read properties to and from the file. The translated data is exposed programmatically and shown to the user through Windows Explorer in a variety of contexts including details view, infotips, details pane, property pages, and so forth. Each property handler is associated with a particular file type, which is identified by the file name extension. Developers should implement a property handler that produces and consumes their file type's native format, such as .jpg or .png, or use the In-Memory Property Store, which produces and consumes the MS-PROPSTORE binary format.

The Windows Property System creates an abstract data model that provides a level of abstraction from individual file formats. The abstract data model provided by the Windows Property System is a method for reading and writing an extensible set of named values that are associated with a Shell item. The value expression is flexible, supporting many data types, and is extensible, enabling arbitrary data (**VT\_BLOB**) and objects to be expressed as a value.

Due to the abstraction, you can query the attributes or metadata of any item. Examples of items that can be abstracted include Microsoft Office documents, ID3 tags, and AutoCAD and other third-party proprietary software. Similarly, if you have a .jpeg file, you can use the .jpeg and EXIF codecs to read the bytes of the file to discover what the dimensions of the image are. If you have a .png file instead, you need a different codec and different code to do so. Using the Windows Property System avoids this sort of problem. If you implement a new file type, you have the option to plug into the uniform abstraction offered by the Windows Property System and specify how to make your metadata consumable. For these reasons, it is always preferable to use the common platform provided by the Windows Property System.

## Development Scenarios

Properties are expressed by producers and by consumers. In this context, producers are the inventors of properties in the Windows Property System and consumers are applications (and their developers) that consume property information from this system. Uses of and participants in the Windows Property System are identified in the following table.



| Use of the Windows Property System                                                                                                                                                                                            | Participant |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| A building block that provides an extensible registry of property descriptions, an in-memory property store implementation, and services for binding to property handlers, converting types, and serializing property stores. | Consumer    |
| Applications that want to read and write properties in an abstract way.                                                                                                                                                       | Consumer    |
| Property inventors who define new properties for the property system by defining custom property schemas and developing their own property handlers.                                                                          | Producer    |
| File format owners who want to enable access to the properties stored in their custom file formats.                                                                                                                           | Producer    |



 

Consumers consume existing properties, schemas, and property handlers. Properties available for consumption include read/write properties from property handlers for supported file types and may also include some custom properties. Available schemas include at least the system schema, and sometimes others, too. A consumer can create an application to consume metadata and build a view based on artist, regardless of what folders the items are stored in. The file folder hierarchy is irrelevant. For example, you can specify all song items by a particular singer without being concerned about the location of such items. This complex, end-to-end scenario is not limited to the Windows Property System, but involves several different components, such as the indexing and search folders.

Property inventors, or third-party developers, are producers in the Windows Property System. When preparing to define a new property, first inspect the set of properties that Windows defines. If you find one that meets your needs, of the type and semantics that match your required use, use that property and do not invent a new one. If you are defining a new custom property, try to obtain agreement with other developers that might want to use it and publish the result of that agreement so that they can join the community of users of that property.

Producers can take advantage of Windows Explorer functionality. For example, if you are writing a new image format, and implement a property handler, your new file format becomes available in Windows Explorer. Users can then tag their photographs and pivot their collection of photographs based on any property in the Windows Property System. In fact, anything that Shell does with properties, third-party developers can do in their own applications. This includes grouping, sorting, querying, and displaying full properties. The user experience that Windows Explorer provides can be largely implemented by third parties with publically available APIs. Windows Explorer can be replaced or extended using these APIs.

From the point of view of an application that uses the Shell data model, there are a huge variety of scenarios that involve the use of the Windows property system. Media management applications are a prominent example. Core property system scenarios include scenarios such as reading the keyword property of a photograph or setting the datetaken property. Examples of end-to-end integration scenarios that the Windows Property System enables, but that require several other components to function, include showing all pictures, or finding a document that contains a keyword.

## Properties and Windows Search

Properties serve both producers and consumers when they interface with Windows Search and indexing. Windows Search has a cache of property values that are used in the implementation of the Windows Search Service (WSS). These property values can be programmatically queried by using the Windows Search OLE DB provider, or through [**ISearchFolderItemFactory**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory), which represents items in search results and query-based views. Windows Search then collects and stores properties emitted by filter handlers or property handlers when an item such as a Word document is indexed. This store is discarded and rebuilt when the index is rebuilt.

> [!Note]  
> Remember that when you reregister a schema, changes made to attributes of previously defined properties may not be respected by the indexer. The solution is either to rebuild the index, or introduce new properties that reflect the changes instead of updating old ones (not recommended). For more information, see [Note to Implementers](#note-to-implementers) later in this topic.

 

For example, a developer creating a media application wants to show users of the application all available music by a particular artist. The application would provide the user with a list of available artists, and then generate a list of all available music by the artist that the user selects. Or an end user might want to do a query for ?artist:Beethoven?, and be exposed to the full list of available properties in the course of their searche. This example involves the use of the Shell namespace, property handlers, and/or querying the index through one of the following:

-   A Shell data source.
-   An OLE DB provider.
-   A Saved Search file (.search-ms) that is used to initiate a query by navigating to the search file in Windows Explorer or binding to [**IShellFolder**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-ishellfolder) programmatically.

> [!Note]  
> Although the `System.Kind` property does not participate in this media application scenario, it could be used to build a query that would return all of the .search-ms files in a particular scope.

 

The preferred way to access the Search APIs and create Windows Search applications is through a Shell data source. [**ISearchFolderItemFactory**](/windows/win32/api/shobjidl_core/nn-shobjidl_core-isearchfolderitemfactory) is a component that can create instances of the Search folder data source, which is a sort of "virtual" data source provided by the Shell that can execute queries over other data sources in the Shell namespace and enumerate results. It can do so either by using the indexer, or by manually enumerating and inspecting items in the specified scopes.

Third-party developers can create applications that consume the data in the index through programmatic queries, and can extend the data in the index for custom file and item types to be indexed by Windows Search. If you want to show query results in Windows Explorer, you must implement a Shell data source before you can create a protocol handler to extend the index. However, if all queries will be programmatic (through OLE DB for example) and interpreted by the application?s code rather than the Shell, then a Shell namespace is still preferred but not required. A protocol handler is required for Windows to obtain information about file contents, such as items in databases or custom file types. While Windows Search can index the name and properties of the file, Windows has no information about the content of the file. As a result, such items cannot be indexed or exposed in the Windows Shell. By implementing a custom protocol handler, you can expose these items. For a list of handlers identified by the developer scenario you are trying to achieve, see "Overview of Handlers" in [Windows Search as a Development Platform](../search/-search-3x-wds-development-ovr.md).

> [!Note]  
> A Shell data source is sometimes known as a Shell namespace extension. A handler is sometimes known as a Shell extension or a Shell extension handler.

 

## Note to Implementers

Due to potential difficulties that the indexer may have when consuming the property system's schema, it is critical that you define attributes carefully and strategically for the first release of the schema. Any changes to attributes (type, column width, whether indexible) will not be reflected in the database after a schema has been registered. The only ways to have these changes recognized after the schema has been registered once on a system would be either to rebuild the index and then register the new schema, or to register the schema and then create a new property for each subsequent release; for example `PKEY_GroupName_PropertyNameV2`, `PKEY_GroupName_PropertyNameV3`, and so forth. We do not recommend creating new properties in this manner, because multiple extraneous columns may impact system performance.

## Windows Property System Documentation

The remainder of this documentation contains the following sections:

-   [Windows Property System Developer's Guide](property-system-developer-s-guide.md)

    Describes in detail how to implement the main development scenarios using the Windows Property System.

-   [Property System Reference](property-system-reference.md)

    Documents the [Windows Properties](props.md), [Property Description Schema](property-description-schema.md), [Interfaces](interfaces.md), [Functions](functions.md), [Structures](structures.md), and [Constants, Enumerations, and Flags](constants--enumerations--and-flags.md) of the Windows Property System.

-   [Property System Code Samples](property-system-code-samples.md)

    Describes samples that demonstrate how to use the Windows Property System.

## Additional Resources

-   For information about reusing the In-Memory Property Store, see [Initializing Property Handlers](building-property-handlers-property-handlers.md) and [**PSCreateMemoryPropertyStore**](/windows/desktop/api/Propsys/nf-propsys-pscreatememorypropertystore).
-   For a specification of the Microsoft Property Store Binary File Format, see [\[MS\_PROPSTORE\]](/openspecs/windows_protocols/ms-propstore/39ea873f-7af5-44dd-92f9-bc1f293852cc).
-   The relationship between Windows Search and indexing, and how to extend the index, are explained in the following topics in Windows Search:
    -   [Developing Filter Handlers for Windows Search](../search/-search-ifilter-conceptual.md)
    -   [Developing Protocol Handlers for Windows Search](../search/-search-3x-wds-phaddins.md)
    -   [Developing Property Handlers for Windows Search](../search/-search-3x-wds-extidx-propertyhandlers.md)
    -   For the Windows 7 or updated Windows Vista SDK download, see the [Windows SDK](https://msdn.microsoft.com/windowsvista/bb980924.aspx).

## Related topics

<dl> <dt>

[Windows Property System Developer's Guide](property-system-developer-s-guide.md)
</dt> <dt>

[Property System Reference](property-system-reference.md)
</dt> <dt>

[Property System Code Samples](property-system-code-samples.md)
</dt> </dl>

 

 
