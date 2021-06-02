---
description: Glossary page
ROBOTS: NOINDEX, NOFOLLOW
title: Shell Glossary
ms.topic: article
ms.date: 05/31/2018
ms.assetid: 2F463941-A4BA-4b34-B391-7E599E87BEEA
api_name: 
api_type: 
api_location: 
topic_type: 
 - kbArticle

---

# Shell Glossary

## A

<dl> <dt>

**association**
</dt> <dd>

A mapping of a file name extension (for example, .mp3) or protocol (for example, http) to a programmatic identifier (ProgID). This mapping is stored in the registry as a per-user setting with a per-computer fallback. Applications that participate in the Default Programs system set the association mapping for the file name extension or protocol to point to the ProgID keys that they own.

</dd> <dt>

**association array**
</dt> <dd>

An ordered list of registry locations used to store information about an item type, including handlers, verbs, and other attributes like the icon and display name of the type. For example, a .jpg file has the following association array on a default Windows system: "HKCR\\jpgfile", "HKCR\\SystemFileAssociations\\.jpg", "HKCR\\SystemFileAssociations\\image", "HKCR\\\*", "HKCR\\AllFileSystemObjects".

</dd> </dl>

## B

<dl> <dt>

**bind**
</dt> <dd>

To load or associate code with data. For example, a handler may be associated with a Shell data source.

</dd> </dl>

## C

<dl> <dt>

**canonical name**
</dt> <dd>

The unique name of a resource. Canonical means "according to the rules." See also: canonical verb name.

</dd> <dt>

**canonical verb name**
</dt> <dd>

A language-neutral name that can be used programmatically to refer to a verb, regardless of the localized string in the user interface. See also: canonical name, verb.

</dd> <dt>

**container**
</dt> <dd>

A type of Shell item that can contain other items. Items in a container are exposed to the Shell namespace by using a Shell data source. Examples include folders, drives, network servers, and compressed files with a .zip file name extension. See also: Shell data source, folder, Shell item.

</dd> <dt>

**content**
</dt> <dd>

Text and properties associated with a Shell item or a content source that can be indexed.

</dd> <dt>

**content source**
</dt> <dd>

An item that can be accessed by the indexer. Content sources are addressable by a URL and are provided to the indexer by a protocol handler. Examples include: file system files and folders, Microsoft Outlook items and folders, database records, and Microsoft SharePoint stored items. A content source can be exposed as Shell items by implementing a Shell data source. See also: content, Shell item.

</dd> <dt>

**content view**
</dt> <dd>

A view in Windows Explorer (offered in Windows 7 and later) that displays the most relevant content for each item in the list based on its file name extension or Kind association. Content view uses a resizing logic that drops properties when the window size decreases to ensure that the most critical properties still have room to be clearly readable. See also: layout pattern, Kind, Kind association.

</dd> <dt>

**content view mode**
</dt> <dd>

See definition for: content view.

</dd> <dt>

**context menu**
</dt> <dd>

This term is sometimes used to mean shortcut menu. See definition for: shortcut menu.

</dd> <dt>

**context menu handler**
</dt> <dd>

This term is sometimes used to mean shortcut menu handler. See definition for: shortcut menu handler.

</dd> </dl>

## D

<dl> <dt>

**data object handler**
</dt> <dd>

A handler that provides additional clipboard formats for the data object (IDataObject) of an item. Data objects are used in drag-and-drop and copy/paste scenarios.

</dd> <dt>

**data source**
</dt> <dd>

This term is sometimes used to mean data store or Shell data source. See definition for: data store, Shell data source.

</dd> <dt>

**data store**
</dt> <dd>

A repository of data. A data store can be exposed to the Shell programming model as a container using a Shell data source. The items in a data store can be indexed by the Windows Search system using a protocol handler.

</dd> <dt>

**desktop composition**
</dt> <dd>

A Windows Vista feature that enables individual windows to be drawn to off-screen surfaces in video memory instead of the being drawn directly to the primary display device.

</dd> <dt>

**document**
</dt> <dd>

A Shell item that contains text, and for which the IFilter interface could be implemented.

</dd> <dt>

**drop handler**
</dt> <dd>

A handler that enables a particular item type to support drag-and-drop and copy/paste scenarios.

</dd> <dt>

**drop target**
</dt> <dd>

A data object that is dragged and dropped onto a file. See also: data handler, drop handler.

</dd> <dt>

**dynamic verb**
</dt> <dd>

A verb that depends on the state of a Shell item or of the system; the appearance of the item is state based and requires that the executing code determine whether the item should appear. See also: shortcut menu handler, static verb, verb.

</dd> </dl>

## E

<dl> <dt>

**Explorer command**
</dt> <dd>

An object that can be presented as a button near the top of the Windows Explorer window that provides functionality for items and containers in that window. A Shell data source provides the Windows Explorer command objects for a particular container item. Commands are sometimes used as verbs.

</dd> </dl>

## F

<dl> <dt>

**file association**
</dt> <dd>

See definition for: file type association.

</dd> <dt>

**file format**
</dt> <dd>

A format for data stored in a file that has a documented format specification. Examples include OLE DocFile, OPC, XML, ZIP and other well known file format specifications. File type creators generally use an existing file format as the basis of a new file type. A file format can be simply a definition that is not instantiated as a file type.

</dd> <dt>

**file format handler**
</dt> <dd>

This term is a synonym for file type handler. See definition for: file type handler.

</dd> <dt>

**file name extension**
</dt> <dd>

The primary indicator of a file type for file system items, it is the portion of the file name that follows the final dot. The file name extension cannot contain spaces or non-ASCII characters and applies only to files (not folders). File name extensions are compared using a comparison function that is not sensitive to case or locale. See also: file format, file type.

</dd> <dt>

**file type**
</dt> <dd>

A particular file name extension value, like ".htm" or ".jpg", that defines a class of files that are of the same type and have a common set of associations. See also: Kind, file type association.

</dd> <dt>

**file type association**
</dt> <dd>

For a particular file name extension, the association array elements that define where handlers and other attributes can be registered. See also: association array, file type.

</dd> <dt>

**file type customization**
</dt> <dd>

An association that enables Shell to customize how Shell treats a file type. File type customizations include: specifying the application used to open the file when double-clicked, adding commands to the shortcut menu for a file type, specifying a custom icon, specifying a MIME content type to associate with a file type, specifying a perceived type, and specifying one or more applications associated by file type with the Open With dialog box. See also: PerceivedType.

</dd> <dt>

**file type handler**
</dt> <dd>

A handler registered for a file type. See also: handler.

</dd> <dt>

**folder**
</dt> <dd>

See definition for: container.

</dd> <dt>

**full PIDL**
</dt> <dd>

A PIDL that uniquely describes an object relative to the desktop folder.

</dd> </dl>

## H

<dl> <dt>

**handler**
</dt> <dd>

A COM object that provides functionality for a Shell item. Most Shell data sources offer an extensible system for binding handlers to items. For example, the file system folder uses the association system to look up the handlers for a particular file type. See also: file association, file type, file type customization.

</dd> </dl>

## I

<dl> <dt>

**icon handler**
</dt> <dd>

A handler that provides the information needed to generate and cache an icon for an item. The file system data store supports loading an icon handler for an item based on the file type, enabling that handler to provide an icon that is used for all instances of that file type.

</dd> <dt>

**infotip handler**
</dt> <dd>

A handler that provides pop-up text when the user hovers the mouse pointer over a user interface object.

</dd> <dt>

**item**
</dt> <dd>

See definition for: Shell item.

</dd> <dt>

**item class**
</dt> <dd>

See definition for: file type.

</dd> <dt>

**item identifier list**
</dt> <dd>

Sequence of one or more SHITEMID structures that uniquely defines an object relative to some root object.

</dd> </dl>

## K

<dl> <dt>

**Kind**
</dt> <dd>

A property that provides a user-friendly Kind name, and can be associated with a list of properties and a layout pattern. Kind was introduced in Windows Vista to express a more end-user friendly notion of file type and it was defined to be a multi-value string property (canonical string values), thus you can have an "audio;video" or "link;document" Kind value. Some user-friendly Kind names are already associated with properties and layout patterns. For example, items associated with Kind.Picture and items associated with Kind.Document display different properties even when they are in the same view. Each item Kind can be associated with one of four unique layout patterns that define the number of properties displayed for each item and their layout. See also: Kind association, content view, layout pattern.

</dd> </dl>

## L

<dl> <dt>

**layout pattern**
</dt> <dd>

One of several arrangements for displaying properties. In Windows 7 and later, when you are registering a new file type, you can use the content view to register a custom property list and layout pattern for your file type. You can choose from four different layout patterns: Alpha (for document search results that contain code snippets), Beta (for email search results with code snippets), Gamma (similar to Alpha but with a two-line layout instead of four), and Delta (for showing many shorter properties, such as with music and pictures). See also: content view, Kind, Kind association.

</dd> </dl>

## M

<dl> <dt>

**metadata handler**
</dt> <dd>

This term is sometimes used to mean property handler. See definition for: property handler.

</dd> </dl>

## N

<dl> <dt>

**namespace extension**
</dt> <dd>

See definition for: Shell data source.

</dd> </dl>

## O

<dl> <dt>

**Object Linking and Embedding Database (OLE DB)**
</dt> <dd>

A standard set of interfaces that provides heterogeneous access to disparate sources of information located anywhere, such as file systems, email folders, and databases.

</dd> <dt>

**OLE DB**
</dt> <dd>

See definition for: Object Linking and Embedding Database.

</dd> </dl>

## P

<dl> <dt>

**PerceivedType**
</dt> <dd>

A broad category of file format types. PerceivedType was introduced in Windows XP, and supports a limited set of known file types (examples include Image, Text, Audio, and Compressed file types). File types, generally public file types, can also have a perceived type. For example, the image file types .bmp, .png, .jpg, and .gif are also of the perceived type, image. At the programming layer, PerceivedType is expressed as an integer. Because there is code that uses Kind and PerceivedType, file format owners must register both. For example "play all" depends on PerceivedType. See also: file type.

</dd> <dt>

**preview handler**
</dt> <dd>

A handler that quickly produces a read-only, simplified view of the Shell item to be displayed in the Windows Explorer preview pane.

</dd> <dt>

**property handler**
</dt> <dd>

A handler that translates data stored in a file into a structured schema that is recognized by and can be accessed by Windows Explorer, Windows Search, and other applications. These systems can then interact with the property handler to write and read properties to and from the file. The translated data includes details view, infotips, details pane, property pages, and so forth. Each property handler is associated with a particular file type, identified by the file name extension. See also: property system.

</dd> <dt>

**property sheet handler**
</dt> <dd>

A handler that is used to create custom property sheets with UI pictures and controls that permit custom interaction with a file type.

</dd> <dt>

**property system**
</dt> <dd>

An extensible read/write system of data definitions that uses properties implemented as name-value pairs. See also: property handler, Shell item.

</dd> <dt>

**property value**
</dt> <dd>

A value associated with a property name for a Shell item. For example, "Author", "Size", and "Date Taken" are properties. Property values are expressed as a PROPVARIANT structure.

</dd> <dt>

**protocol handler**
</dt> <dd>

A handler that accesses content sources and provides an IUrlAccessor object for a specified protocol and URL. Protocol handlers extend Windows Search functionality, and may provide change notifications to indexers. Different protocol handlers are required to index specific types of data stores. To provide a reasonable user experience, you must also provide a Shell data source for the data store in addition to implementing your protocol handler. The protocol handler exposes the items in the data store to the indexer, while the Shell data source exposes the items in the data store to the Shell.

</dd> </dl>

## R

<dl> <dt>

**relative PIDL**
</dt> <dd>

A PIDL that is relative to some root object in the shell namespace other than the desktop folder. This is commonly the parent folder of the item.

</dd> </dl>

## S

<dl> <dt>

**Shell data source**
</dt> <dd>

A component that is used to extend the Shell namespace and expose items in a data store. In the past, the Shell data source was referred to as the Shell namespace extension. See also: container, handler, Shell item.

</dd> <dt>

**Shell extension**
</dt> <dd>

This term is sometimes used to mean file type handler. See definition for: file type handler.

</dd> <dt>

**Shell extension handler**
</dt> <dd>

This term is sometimes used to mean file type handler. See definition for: file type handler.

</dd> <dt>

**Shell handler**
</dt> <dd>

This term is sometimes used to mean file type handler. See definition for: file type handler.

</dd> <dt>

**Shell item**
</dt> <dd>

A single piece of content. Some Shell items are content sources, and some are not. A folder is a content source, for example, but a .jpg file is not. File type handlers expose Shell items. In some contexts "item" is used to distinguish containers from noncontainers. See also: container, content source, file type handler.

</dd> <dt>

**Shell namespace extension**
</dt> <dd>

This term is sometimes used to mean Shell data source. See definition for: Shell data source.

</dd> <dt>

**shortcut menu**
</dt> <dd>

A user interface that is used to present a collection of verbs associated with a user interface element, such as a file or folder.

</dd> <dt>

**Shortcut menu handler**
</dt> <dd>

A handler that adds verbs for an item or items. These verbs are commonly displayed in a shortcut menu. See also: shortcut menu.

</dd> <dt>

**simple PIDL**
</dt> <dd>

A PIDL that is parsed without disk verification.

</dd> <dt>

**static verb**
</dt> <dd>

A verb that applies to a Shell item without needing to inspect the current state of an item or system. A static verb is based on a static registration of the associated elements of an item, and does not change.

</dd> </dl>

## T

<dl> <dt>

**thumbnail handler**
</dt> <dd>

A handler that provides a static image to represent a Shell item.

</dd> <dt>

**thumbnail provider**
</dt> <dd>

This term is sometimes used to mean thumbnail handler. See definition for: thumbnail handler.

</dd> </dl>

## U

<dl> <dt>

**user friendly kind name**
</dt> <dd>

See definition for: Kind.

</dd> </dl>

## V

<dl> <dt>

**verb**
</dt> <dd>

An individual action that can be called by a Shell item. Examples include open and print. Verbs are sometimes referred to as commands or tasks. See also: dynamic verb, shortcut menu handler, static verb.

</dd> <dt>

**verb handler**
</dt> <dd>

This term is sometimes used to mean shortcut menu handler. See definition for: shortcut menu handler.

</dd> </dl>

 

 



