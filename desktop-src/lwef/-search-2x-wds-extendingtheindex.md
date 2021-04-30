---
title: Extending the Index (Legacy Windows Environment Features)
description: The use of and development for the 2.x versions of Microsoft Windows Desktop Search (WDS) is strongly discouraged in favor of Windows Search.
ms.assetid: 'vs|search|~\search\wds2x\extending_index_ovr.htm'
ms.topic: article
ms.date: 05/31/2018
---

# Extending the Index (Legacy Windows Environment Features)

> [!NOTE]
> Windows Desktop Search 2.x is an obsolete technology that was originally available as an add-in for Windows XP and Windows Server 2003. On later releases, use [Windows Search](../search/-search-3x-wds-overview.md) instead.

The use of and development for the 2.x versions of Microsoft Windows Desktop Search (WDS) is strongly discouraged in favor of [Windows Search](../search/-search-3x-wds-overview.md).

WDS can be extended to index the contents of new file types and data stores. Currently, WDS 2.x contains filters for over 200 types of items (including plaintext items such as HTML, XML, and source code files) and uses the same [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)and protocol handler technology as SharePoint Services. If you already have filter implementations installed for your new file types, WDS can use the existing filter interfaces to index this data.

WDS 2.x add-ins enable the index to traverse and parse new data and data structures for information to add to the searchable catalog. These add-ins can also extend the Windows Shell to associate icons and context-menu handlers with the new file types and data stores. To include new file types in the WDS catalog, an add-in must implement the [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface. To include new data stores, an add-in must be a protocol handler. If the new data store includes embedded files or new file types itself, you will also need to write an appropriate filter as well.

> [!Note]
>
> Filters and protocol handlers must be written in native code due to potential CLR versioning issues with the process all add-ins run in.

 

## Adding File Types to the Index

Add-ins can extend WDS to index new or proprietary file types and to associate each new file type with a file-specific icon or context menu. To do this, you can build and register an add-in that:

1.  Implements an [**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)interface for each file type so WDS can access and index the file type's text and metadata.
2.  Implements the **IExtractIcon** and **IContextMenu** interfaces to add icons and context menus for greater integration and usability.

For a discussion on implementing filters, see [Developing IFilter Add-ins](-search-2x-wds-ifilteraddins.md).

## Adding Data Stores to the Index

Add-ins can extend WDS to index new data stores and to associate files with a file-specific icon or context menu. To do this, you can build and register a protocol handler that:

1.  Implements the **ISearchProtocol** and **IUrlAccessor** interfaces to process and bind individual items in the content source. WDS uses URLs to uniquely identify items, whether those items are in the file system, inside a database-like store, or on the Web.
2.  Implements the **IPersistFolder** interface and portions of the **IShellFolder** interface to add icons and context menus for greater integration and usability.

For a discussion on implementing protocol handlers, see [Developing Protocol Handlers](-search-2x-wds-phaddins.md).

## Add-in Installer Guidelines

Installation of an add-in should follow the following guidelines:

-   The installer must use either EXE or MSI installer.
-   Release notes must be provided.
-   An **Add/Remove Programs** entry must be created for each add-in installed.
-   The installer must take over all registry settings for the particular file type or store that the current add-in understands.
-   If a previous add-in is being overwritten, the installer should notify the user.
-   If a newer add-in has overwritten the previous add-in, there should be the ability to restore the previous add-in's functionality and make it the default add-in for that file type or store again.

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[Developing IFilter Add-ins](-search-2x-wds-ifilteraddins.md)
</dt> <dt>

[Developing Protocol Handlers](-search-2x-wds-phaddins.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[**IFilter**](/windows/desktop/api/filter/nn-filter-ifilter)
</dt> </dl>

 

 
