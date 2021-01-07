---
description: Glossary page
ROBOTS: NOINDEX, NOFOLLOW
ms.assetid: 8e9b45de-c81b-4324-b00b-b11ee6749920
title: Windows Search Glossary
ms.topic: article
ms.date: 05/31/2018
---

# Windows Search Glossary

## \#

**.osd file**

OpenSearch Descriptor file.

**.osdx file**

An OpenSearch description XML file that describes available server connections and result formats for a specific web-based data source. It is used for interacting with the Windows Shell. See also: OpenSearch descriptor.

## A

**Advanced Query Syntax (AQS)**

The default query syntax used by Windows Search to query the index and to refine and narrow search parameters. AQS is primarily user facing, and can be used by users to build AQS queries, but can also be used programmatically. See also: Natural Query Syntax (NQS).

**AQS**

See definition for: Advanced Query Syntax (AQS).

**association**

A mapping of a file name extension (for example, .mp3) or protocol (for example, http) to a programmatic identifier (ProgID). This mapping is stored in the registry as a per-user setting with a per-computer fallback. Applications that participate in the Default Programs system set the association mapping for the file name extension or protocol to point to the ProgID keys that they own.

**association array**

An ordered list of registry locations used to store information about an item type, including handlers, verbs, and other attributes like the icon and display name of the type. For example, a .jpg file has the following association array on a default Windows system: "HKCR\\jpgfile", "HKCR\\SystemFileAssociations\\.jpg", "HKCR\\SystemFileAssociations\\image", "HKCR\\\*", "HKCR\\AllFileSystemObjects".

**Atom**

An XML schema used for web feeds and content distribution, developed as an alternative to Really Simple Syndication (RSS). The Atom syndication format was published as an IETF proposed standard in RFC 4287.

## B

**bind**

To load or associate code with data. For example, a handler may be associated with a Shell data source.

**binding**

A request in a search query for a column in a returned rowset. The binding specifies a property to be included in the search results.

**bookmark**

An indicator that uniquely identifies a row within a set of rows.

## C

**canonical name**

The unique name of a resource. Canonical means "according to the rules." See also: canonical verb name.

**canonical verb name**

A language-neutral name that can be used programmatically to refer to a verb, regardless of the localized string in the user interface. See also: canonical name, verb.

**catalog**

The highest-level unit of organization in Windows Search. A catalog represents a set of indexed documents that can be queried. A catalog consists of a properties table with the text or value and corresponding location stored in columns of the table. Each row of the table corresponds to a separate document in the scope of the catalog, and each column of the table corresponds to a property. See also: index, Windows Search service.

**category**

A hierarchical grouping of rows. For example, a query result that contains author and title columns can be categorized based on author. In this example, each group of rows that contains the same value for author constitutes a category.

**chapter**

A collection of rows within a set of rows. See also: catalog, category.

**column**

The container for a single type of information in a row. Columns map to property names and specify which properties are used for the search query's command tree elements. See also: category.

**command tree**

A combination of restrictions, categories, and sort orders that are specified for the search query. See also: category.

**container**

A type of Shell item that can contain other items. Items in a container are exposed to the Shell namespace by using a Shell data source. Examples include folders, drives, network servers, and compressed files with a .zip file name extension. See also: Shell data source, folder, Shell item.

**content**

Text and properties associated with a Shell item or a content source that can be indexed.

**content source**

An item that can be accessed by the indexer. Content sources are addressable by a URL and are provided to the indexer by a protocol handler. Examples include: file system files and folders, Microsoft Outlook items and folders, database records, and Microsoft SharePoint stored items. A content source can be exposed as Shell items by implementing a Shell data source. See also: content, Shell item.

**content view**

A view in Windows Explorer (offered in Windows 7 and later) that displays the most relevant content for each item in the list based on its file name extension or Kind association. Content view uses a resizing logic that drops properties when the window size decreases to ensure that the most critical properties still have room to be clearly readable. See also: layout pattern, Kind, Kind association.

**content view mode**

See definition for: content view.

**context menu**

This term is sometimes used to mean shortcut menu. See definition for: shortcut menu.

**context menu handler**

This term is sometimes used to mean shortcut menu handler. See definition for: shortcut menu handler.

**crawl**

To iterate over a crawl scope, identifying content sources that require indexing or re-indexing.

**crawl scope**

A collection of data stores (identifiable by URL) that represents content that the indexer crawls and indexes.

**cursor**

In the context of the local index, a cursor is an indicator for working with one row or a small block of rows at a time in a set of data returned in a result set. After the cursor is positioned on a row, operations can be performed on that row or on a block of rows starting at that position.

## D

**Data Management, Exploration and Mining**

See definition for: Database Mining Extensions (DMX).

**data object handler**

A handler that provides additional clipboard formats for the data object (IDataObject) of an item. Data objects are used in drag-and-drop and copy/paste scenarios.

**data source**

This term is sometimes used to mean data store or Shell data source. See definition for: data store, Shell data source.

**data store**

A repository of data. A data store can be exposed to the Shell programming model as a container using a Shell data source. The items in a data store can be indexed by the Windows Search system using a protocol handler.

**Database Mining Extensions (DMX)**

A query language used to create and manipulate data mining. The administrative templates for Windows 7, Windows Search, and Windows Explorer are .admx files, and rely on DMX technology. The following templates can be customized through Group Policy: Search.admx, Explorer.admx, and WindowsExplorer.admx.

**DMX**

See definition for: Database Mining Extensions.

**document**

A Shell item that contains text, and for which the IFilter interface could be implemented.

**drop handler**

A handler that enables a particular item type to support drag-and-drop and copy/paste scenarios.

**drop target**

A data object that is dragged and dropped onto a file. See also: data handler, drop handler.

**dynamic verb**

A verb that depends on the state of a Shell item or of the system; the appearance of the item is state based and requires that the executing code determine whether the item should appear. See also: shortcut menu handler, static verb, verb.

## E

**Explorer command**

An object that can be presented as a button near the top of the Windows Explorer window that provides functionality for items and containers in that window. A Shell data source provides the Windows Explorer command objects for a particular container item. Commands are sometimes used as verbs.

## F

**federated search**

An extensibility model that enables searching data stores and representing the results as Shell items in Windows Explorer. See also: federated search provider, search connector, OpenSearch descriptor, OpenSearch standard.

**federated search connector**

See definition for: search connector.

**federated search provider**

A web service, implemented by a data store, that supports the protocols used by Windows 7 so that Windows 7 and later versions can search that data store remotely. See also: OpenSearch descriptor, OpenSearch standard.

**file association**

See definition for: file type association.

**file format**

A format for data stored in a file that has a documented format specification. Examples include OLE DocFile, OPC, XML, ZIP and other well known file format specifications. File type creators generally use an existing file format as the basis of a new file type. A file format can be simply a definition that is not instantiated as a file type.

**file format handler**

This term is a synonym for file type handler. See definition for: file type handler.

**file name extension**

See definition for: file name extension.

**file name extension**

The primary indicator of a file type for file system items, it is the portion of the file name that follows the final dot. The file name extension cannot contain spaces or non-ASCII characters and applies only to files (not folders). File name extensions are compared using a comparison function that is not sensitive to case or locale. See also: file format, file type.

**file type**

A particular file name extension value, like ".htm" or ".jpg", that defines a class of files that are of the same type and have a common set of associations. See also: Kind, file type association.

**file type association**

For a particular file name extension, the association array elements that define where handlers and other attributes can be registered. See also: association array, file type.

**file type customization**

An association that enables Shell to customize how Shell treats a file type. File type customizations include: specifying the application used to open the file when double-clicked, adding commands to the shortcut menu for a file type, specifying a custom icon, specifying a MIME content type to associate with a file type, specifying a perceived type, and specifying one or more applications associated by file type with the Open With dialog box. See also: PerceivedType.

**file type handler**

A handler registered for a file type. See also: handler.

**filter**

An implementation of the IFilter interface. It opens files of a particular file type, and filters properties and chunks of text for the indexer. Filters are associated with file types, as denoted by file name extensions, MIME types, or class identifiers (CLSIDs). Although one filter can handle multiple file types, each file type works with only one filter.

**folder**

See definition for: container.

## H

**handler**

A COM object that provides functionality for a Shell item. Most Shell data sources offer an extensible system for binding handlers to items. For example, the file system folder uses the association system to look up the handlers for a particular file type. See also: file association, file type, file type customization.

## I

**icon handler**

A handler that provides the information needed to generate and cache an icon for an item. The file system data store supports loading an icon handler for an item based on the file type, enabling that handler to provide an icon that is used for all instances of that file type.

**index**

n. A catalog that stores the content and properties of Shell items to enable fast searches. See also: catalog, indexer, indexing, inverted index. v. To access content sources, filter the sources for content and properties, and insert the extracted values into the index (for text) and the Windows Search property store (for properties). See also: content source, index, indexer, inverted index.

**indexer**

An application that does indexing or coordinates indexing. See also: index, indexing, inverted index.

**infotip handler**

A handler that provides pop-up text when the user hovers the mouse pointer over a user interface object.

**inverted index**

A persistent structure that contains the content pulled out of files by Windows Search. The text is organized into an index that maps from a word in a property to a list of the documents and locations within a document that contain that word. Hence, an inverted index is the inverse of the process of extracting the text and properties from the document and putting them into the indexer. See also: index, indexer, indexing.

**item**

See definition for: Shell item.

**item class**

See definition for: file type.

## K

**Kind**

A property that provides a user-friendly Kind name, and can be associated with a list of properties and a layout pattern. Kind was introduced in Windows Vista to express a more end-user friendly notion of file type and it was defined to be a multi-value string property (canonical string values), thus you can have an "audio;video" or "link;document" Kind value. Some user-friendly Kind names are already associated with properties and layout patterns. For example, items associated with Kind.Picture and items associated with Kind.Document display different properties even when they are in the same view. Each item Kind can be associated with one of four unique layout patterns that define the number of properties displayed for each item and their layout. See also: Kind association, content view, layout pattern.

**Kind association**

A property in the property system, called System.Kind, that determines which UX templates are displayed for a file. This property also provides a user-friendly name for the type of the item and is linked to the file name extension. See also: Kind.

## L

**layout pattern**

One of several arrangements for displaying properties. In Windows 7 and later, when you are registering a new file type, you can use the content view to register a custom property list and layout pattern for your file type. You can choose from four different layout patterns: Alpha (for document search results that contain code snippets), Beta (for email search results with code snippets), Gamma (similar to Alpha but with a two-line layout instead of four), and Delta (for showing many shorter properties, such as with music and pictures). See also: content view, Kind, Kind association.

## M

**metadata handler**

This term is sometimes used to mean property handler. See definition for: property handler.

## N

**namespace extension**

See definition for: Shell data source.

**namespace walk**

A helper process that traverses the namespace of a container or set of containers, discovering each item and possibly doing something with each. The INamespaceWalk interface can be used to walk any part of the Windows Explorer namespace or to discover the items referenced by a data object or view. Container verbs (like "play" on Artists containers) walk the namespace and discover the items.

**natural language query**

See definition for: Natural Query Syntax (NQS).

**Natural Query Syntax (NQS)**

A query syntax that is more relaxed than AQS and looks more like human language. NQS can be used by Windows Search to query the index if NQS is selected instead of the default, AQS. See also: Advanced Query Syntax (AQS).

**noise word**

A word that is ignored by Windows Search when it is present in the restrictions specified for the search query, because it has little discriminatory value. Examples include "and" and "the."

**NQS**

See definition for: Natural Query Syntax (NQS).

## O

**Object Linking and Embedding Database (OLE DB)**

A standard set of interfaces that provides heterogeneous access to disparate sources of information located anywhere, such as file systems, email folders, and databases.

**OLE DB**

See definition for: Object Linking and Embedding Database.

**OpenSearch descriptor**

An XML file that describes available server connections and result formats for a specific web-based data source. This file contains one or more URL templates, and uses an .osdx file name extension when interacting with the Windows Shell. An OpenSearch description is sometimes referred to as a search connector, although it is only the description portion of a connector. See also: search connector.

**OpenSearch standard**

A collection of simple formats and protocols used for sharing search results. For more information, see the OpenSearch website (https://github.com/dewitt/opensearch).

## P

**PerceivedType**

A broad category of file format types. PerceivedType was introduced in Windows XP, and supports a limited set of known file types (examples include Image, Text, Audio, and Compressed file types). File types, generally public file types, can also have a perceived type. For example, the image file types .bmp, .png, .jpg, and .gif are also of the perceived type, image. At the programming layer, PerceivedType is expressed as an integer. Because there is code that uses Kind and PerceivedType, file format owners must register both. For example "play all" depends on PerceivedType. See also: file type.

**preview handler**

A handler that quickly produces a read-only, simplified view of the Shell item to be displayed in the Windows Explorer preview pane.

**previewer**

This term is sometimes used to mean preview handler. See definition for: preview handler.

**property handler**

A handler that translates data stored in a file into a structured schema that is recognized by and can be accessed by Windows Explorer, Windows Search, and other applications. These systems can then interact with the property handler to write and read properties to and from the file. The translated data includes details view, infotips, details pane, property pages, and so forth. Each property handler is associated with a particular file type, identified by the file name extension. See also: property system.

**property sheet handler**

A handler that is used to create custom property sheets with UI pictures and controls that permit custom interaction with a file type.

**property system**

An extensible read/write system of data definitions that uses properties implemented as name-value pairs. See also: property handler, Shell item.

**property value**

A value associated with a property name for a Shell item. For example, "Author", "Size", and "Date Taken" are properties. Property values are expressed as a PROPVARIANT structure.

**protocol handler**

A handler that accesses content sources and provides an IUrlAccessor object for a specified protocol and URL. Protocol handlers extend Windows Search functionality, and may provide change notifications to indexers. Different protocol handlers are required to index specific types of data stores. To provide a reasonable user experience, you must also provide a Shell data source for the data store in addition to implementing your protocol handler. The protocol handler exposes the items in the data store to the indexer, while the Shell data source exposes the items in the data store to the Shell.

## R

**restriction**

A condition that a file must meet to be included in the search results that are returned by Windows Search.

**row**

The columns that contain the property values that describe a single result from the set of objects that matched the restrictions specified in a search query.

**rowset**

A set of rows returned in the search results.

## S

**search connector**

An XML file that contains information about a data store. Search connectors are deployed for federated search.

**search consumer**

A component or application that queries the index.

**search federation**

See definition for: federated search provider.

**search provider**

A component or application that provides data to Windows Search.

**search scope**

This term is sometimes used to mean crawl scope. See definition for: crawl scope.

**Shell data source**

A component that is used to extend the Shell namespace and expose items in a data store. In the past, the Shell data source was referred to as the Shell namespace extension. See also: container, handler, Shell item.

**Shell extension**

This term is sometimes used to mean file type handler. See definition for: file type handler.

**Shell extension handler**

This term is sometimes used to mean file type handler. See definition for: file type handler.

**Shell handler**

This term is sometimes used to mean file type handler. See definition for: file type handler.

**Shell item**

A single piece of content. Some Shell items are content sources, and some are not. A folder is a content source, for example, but a .jpg file is not. File type handlers expose Shell items. In some contexts "item" is used to distinguish containers from noncontainers. See also: container, content source, file type handler.

**Shell namespace extension**

This term is sometimes used to mean Shell data source. See definition for: Shell data source.

**shortcut menu**

A user interface that is used to present a collection of verbs associated with a user interface element, such as a file or folder.

**Shortcut menu handler**

A handler that adds verbs for an item or items. These verbs are commonly displayed in a shortcut menu. See also: shortcut menu.

**static verb**

A verb that applies to a Shell item without needing to inspect the current state of an item or system. A static verb is based on a static registration of the associated elements of an item, and does not change.

## T

**thumbnail handler**

A handler that provides a static image to represent a Shell item.

**thumbnail provider**

This term is sometimes used to mean thumbnail handler. See definition for: thumbnail handler.

## U

**URL template**

A URL-based connection string that is used to query a web server for search results. The template looks like a URL, but contains several placeholder values (such as {searchTerms}) that the client must replace with data about the results it wants to retrieve. The definition of URL templates is key to implementing the federated search and OpenSearch standards.

**user friendly kind name**

See definition for: Kind.

## V

**verb**

An individual action that can be called by a Shell item. Examples include open and print. Verbs are sometimes referred to as commands or tasks. See also: dynamic verb, shortcut menu handler, static verb.

**verb handler**

This term is sometimes used to mean shortcut menu handler. See definition for: shortcut menu handler.

## W

**walk**

See definition for: namespace walk.

**Windows Search**

See definition for: Windows Search service.

**Windows Search property store**

The cache of property values used in the implementation of the Windows Search service. These property values can be programmatically queried by using the Windows Search OLE DB provider. The Windows Search property store collects and stores properties emitted by filter handlers or property handlers when an item such as a Word document is indexed. This store is discarded and rebuilt when the index is rebuilt.

**Windows Search service**

Refers to Windows Search 3.0 and above. This service analyzes a set of documents, extracts useful information, and then organizes the extracted information so that properties of those documents can be efficiently returned in response to queries. See also: catalog.
