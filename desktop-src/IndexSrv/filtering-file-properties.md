---
title: Filtering File Properties
description: Filtering File Properties
ms.assetid: 060e9e96-915a-4ac5-8ab3-d86e613135ce
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Filtering File Properties

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The CiDaemon.exe process of Indexing Service filters file properties by calling the [**IFilter::GetChunk**](/windows/desktop/api/Filter/nf-filter-ifilter-getchunk) and [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) methods. Each chunk can have only one property. If the chunk is not ordinary text, it can originate from one of the following kinds of information:

-   Properties accessed through the Microsoft ActiveX [**IPropertyStorage**](https://www.bing.com/search?q=**IPropertyStorage**) and [**IPropertySetStorage**](https://www.bing.com/search?q=**IPropertySetStorage**) interfaces. For example, the properties you see displayed when you right-click on a Microsoft Office file in a Web browser, or using Microsoft Windows Explorer, are properties from the Office Summary Information property set. The [**IFILTER\_FLAGS\_OLE\_PROPERTIES**](/windows/desktop/api/Filter/ne-filter-tagifilter_flags) flag tells the filter that ActiveX properties exist and should not be returned through the filter.
-   Properties accessed as internal value-type properties from files that treat some internal fields as value-type properties. For example, fields within a spreadsheet can be tagged with property set and property ID values to make them available for later searching. The [**IFILTER\_INIT\_APPLY\_INDEX\_ATTRIBUTES**](/windows/desktop/api/Filter/nf-filter-ifilter-init) flag indicates that the client wants textual content retrieved as the values they are defined to represent. Examples of internal value-type properties are HTML tags like &lt;TITLE&gt; (which gets mapped into the "DocTitle" Office property set and property ID) and HTML anchor tags.

You can use the Microsoft Management Console (MMC) snap-in of Indexing Service to specify cached properties for the second category (internal, value-type properties). If this has been done, calls to the [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue) method produce properties that are saved in the property store for the catalog that indexes these files. Certain well-known properties are cached for performance reasons. Cached properties can be displayed in query result tables and you can search for these properties using relational or regular expression queries (see [Property-Value Queries](property-value-queries.md) for details).

You can also create file abstracts at this time if the [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface implementation supports creation of such a summary. (See [Creating Abstracts](creating-abstracts.md) for more information). You can adjust the property cache through the MMC by right-clicking **MyComputer** and choosing **Manage**, then **Server Applications**. Then select **Services** and **Indexing Service** on **Local Machine**. The globally unique identifier (GUID) for the property set is in the first column and the property ID, either a number or string, is in the second column. Right-click on the guide to display the property menu and set the **Cache** check box to cache the property.

An example showing how to expose additional HTML &lt;META&gt; tag properties, how to make these properties available for comparisons, and how to show them in the search results table can be found in the HTMLProp sample in the [code samples](installing-the-samples.md) directory under **IFilter**.

 

 




