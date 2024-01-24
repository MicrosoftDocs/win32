---
description: Introduces the Search Connector Description schema that is used by Windows Explorer libraries and federated search providers.
ms.assetid: b85a04c6-9398-4cc7-a894-881216600203
title: Search Connector Description Schema
ms.topic: article
ms.date: 05/31/2018
---

# Search Connector Description Schema

Introduces the Search Connector Description schema that is used by Windows Explorer libraries and federated search providers. The schema specifies the structure and requirements for Search Connector Description files (\*.searchConnector-ms) and for **searchConnectorDescriptionType** elements of the Shell Library Description (\*.library-ms) files.

This topic describes the schema as it relates to federated search connectors. For more information about libraries and the Library Description schema, see [Library Description Schema](../shell/library-schema-entry.md).

This topic includes the following sections:

-   [What Are Search Connectors?](#what-are-search-connectors)
-   [How Do Search Connector Description Files Work?](#search-connector-description-schema)
-   [What Is the Search Connector Description Schema?](#what-is-the-search-connector-description-schema)
-   [What Are the Major Parts of the Schema?](#what-are-the-major-parts-of-the-schema)
-   [Examples of Search Connector Description Files](#examples-of-search-connector-description-files)
-   [Additional Resources](#additional-resources)
-   [Related topics](#related-topics)

## What Are Search Connectors?

Search connectors connect users with data stored in web services or remote storage locations. With Windows 7, users can install search connectors for locations, like web services, so that they search those locations directly from Windows Explorer. Search connectors are Search Connector Description files (\*.searchConnector-ms) that specify how to connect to, send queries to, and receive results from the location.

In addition to web services, search connectors can be used to search local index scopes created by protocol handlers. For example, users can search email indexed locally with the MAPI protocol handler by using a search connector for that email store.

## How Do Search Connector Description Files Work?

When Search Connector Description files are installed on users' systems, users can open Windows Explorer, click the search connector in the navigation pane, and enter a search query. Windows Explorer sends the query using information from the Search Connector Description file, such as which provider to use and the scope of the search. The results are returned as RSS or Atom feed items and displayed to users as if they were regular Shell items.

How you deploy your Search Connector Description file depends on the type of location the search connector supports:

-   In an OpenSearch configuration (\*.osdx) file for your web service
-   As part of your protocol handler installation

You should ensure that the following things happen when a user opens the .osdx file or installs the protocol handler:

-   The .searchconnector-ms file is created in the users' **Windows Searches** folder (%userprofile%/Searches).
-   A shortcut to the .searchconnector-ms file is created in the users' **Links** folder (%userprofile%/Links).

## What Is the Search Connector Description Schema?

The Search Connector Description schema is an XML schema that defines the structure of Search Connector Description files (\*.searchConnector-ms). Each search connector must have a Search Connector Description file that specifies how to connect to, send queries to, and receive results from the location.

## What Are the Major Parts of the Schema?

The following table lists the major parts of the schema.



| Child elements                                                                         | Description                                                                                                                                                                             |
|----------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [isSearchOnlyItem](search-schema-sconn-issearchonlyitem.md)                           | Identifies whether the locations supported by the search connector are search-only or search and browse.                                                                                |
| [isDefaultSaveLocation](search-schema-sconn-isdefaultsavelocation.md)                 | For library use only.                                                                                                                                                                   |
| [isDefaultNonOwnerSaveLocation](search-schema-sconn-isdefaultnonownersavelocation.md) | For library use only.                                                                                                                                                                   |
| [description](search-schema-sconn-description.md)                                     | Describes the search connector.                                                                                                                                                         |
| [iconReference](search-schema-sconn-iconreference.md)                                 | Identifies the location of a custom icon for the search connector.                                                                                                                      |
| [imageLink](search-schema-sconn-imagelink.md)                                         | Identifies the location of a custom thumbnail for the search connector.                                                                                                                 |
| [author](search-schema-sconn-author.md)                                               | Identifies the author of the search connector.                                                                                                                                          |
| [dateCreated](search-schema-sconn-datecreated.md)                                     | Identifies the date that the search connector was created.                                                                                                                              |
| [templateInfo](search-schema-sconn-templateinfo.md)                                   | Specifies a folder type for the search connector.                                                                                                                                       |
| [locationProvider](search-schema-sconn-locationprovider.md)                           | Specifies the search provider to be used by this search connector.                                                                                                                      |
| [scope](search-schema-sconn-scope.md)                                                 | Specifies the locations to include in and exclude from the search scope.                                                                                                                |
| [propertyStore](search-schema-sconn-propertystore.md)                                 | Specifies the location of an XML-based [**IPropertyStore**](/windows/win32/api/propsys/nn-propsys-ipropertystore) for this search connector. The **IPropertyStore** supports the search connector's open metadata. |
| [includeInStartMenuScope](search-schema-sconn-includeinstartmenuscope.md)             | Specifies whether the location represented by the search connector should be included in the Start menu's search scope.                                                                 |
| [domain](search-schema-sconn-domain.md)                                               | Identifies the search connector's top-level domain.                                                                                                                                     |
| [supportsAdvancedQuerySyntax](search-schema-sconn-supportsadvancedquerysyntax.md)     | Specifies whether the search connector supports Advanced Query Syntax (AQS).                                                                                                            |
| [isIndexed](search-schema-sconn-isindexed.md)                                         | Specifies whether the location represented by the search connector is indexed.                                                                                                          |



 

## Examples of Search Connector Description Files

The following is an example of a Search Connector Description file for a federated search web service.


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
  <description>Search MSDN. Powered by live.com</description>
  <isSearchOnlyItem>true</isSearchOnlyItem>
  <domain>https://social.msdn.microsoft.com</domain>
  <supportsAdvancedQuerySyntax>false</supportsAdvancedQuerySyntax>
  <templateInfo>
    <folderType>{8FAF9629-1980-46FF-8023-9DCEAB9C3EE3}</folderType>
  </templateInfo>
  <propertyStore>
    <property name="OpenSearchHTMLRolloverTemplate">https://social.msdn.microsoft.com/Search/?Query={searchTerms}</property>
  </propertyStore>
  <locationProvider clsid="{48E277F6-4E74-4cd6-BA6F-FA4F42898223}">
    <propertyBag>
      <property name="OpenSearchShortName">MSDN</property>
      <property name="OpenSearchQueryTemplate">https://social.msdn.microsoft.com/Search/Feed.aspx?locale=en-US&Query={searchTerms}&format=RSS&StartIndex={startIndex}</property>
      <property name="MaximumResultCount" type="uint32">100</property>
    </propertyBag>
  </locationProvider>
</searchConnectorDescription>
```



The following is an example of a Search Connector Description file for a MAPI protocol handler.


```
<?xml version="1.0" encoding="UTF-8"?>
<searchConnectorDescription xmlns="http://schemas.microsoft.com/windows/2009/searchConnector">
    <description>Microsoft Outlook</description>
    <isSearchOnlyItem>true</isSearchOnlyItem>
    <includeInStartMenuScope>true</includeInStartMenuScope>
    <templateInfo>
        <folderType>{91475FE5-586B-4EBA-8D75-D17434B8CDF6}</folderType>
    </templateInfo>
    <simpleLocation>
        <url>mapi://{S-1-5-21-2127521184-1604012920-1887927527-2779359}/</url>
    </simpleLocation>
</searchConnectorDescription>
```



## Additional Resources

-   For more information about the Library Description schema, see [Library Description Schema](../shell/library-schema-entry.md).
-   For more information on installing a search connector, see [Federated Search in Windows](-search-federated-search-overview.md).

## Related topics

<dl> <dt>

**Reference**
</dt> <dt>

[searchConnectorDescriptionType Element (Search Connector Schema)](search-schema-searchconnectordescription.md)
</dt> <dt>

**Other Resources**
</dt> <dt>

[OpenSearch](https://www.opensearch.org)
</dt> <dt>

[Microsoft Download Center](https://www.microsoft.com/DOWNLOADS/en/default.aspx)
</dt> </dl>

 

 
