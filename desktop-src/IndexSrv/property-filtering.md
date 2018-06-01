---
Description: Property Filtering
ms.assetid: bb8884fb-ffe1-4e07-879e-9febe7dbbfab
title: Property Filtering
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Property Filtering

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Properties are extracted from documents by filters implemented for specific document types. Some value-type properties are obtained by other means; for example, by the property-storage interfaces. The implementer of a custom [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface can interpret the contents of a document type in any number of ways, and the descriptions here represent "best practices" for an implementation.

The [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) interface contains several methods that Indexing Service uses when filtering a document. The methods include:

-   [**IFilter::Init**](/windows/desktop/api/Filter/nf-filter-ifilter-init), which returns the [**IFILTER\_FLAGS**](/windows/desktop/api/Filter/ne-filter-tagifilter_flags) enumeration. If the IFILTER\_FLAGS\_OLE\_PROPERTIES member of this enumeration is set to one, Indexing Service uses the [**IPropertySetStorage**](https://www.bing.com/search?q=**IPropertySetStorage**) and [**IPropertyStorage**](https://www.bing.com/search?q=**IPropertyStorage**) interfaces to enumerate and access external value-type properties.
-   [**IFilter::GetChunk**](/windows/desktop/api/Filter/nf-filter-ifilter-getchunk), which returns information from a document in "chunks" with chunk type (text or value), name, and locale. A chunk contains one document property.
-   [**IFilter::GetText**](/windows/desktop/api/Filter/nf-filter-ifilter-gettext), which gets a text-type property from a chunk.
-   [**IFilter::GetValue**](/windows/desktop/api/Filter/nf-filter-ifilter-getvalue), which gets a value-type property from a chunk.

The following figure graphically represents an example document. The external value-type property DocTitle (obtained using methods of the [**IPropertySetStorage**](https://www.bing.com/search?q=**IPropertySetStorage**) and [**IPropertyStorage**](https://www.bing.com/search?q=**IPropertyStorage**) interfaces) and the internal value-type property Book (obtained as a result of a custom [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) implementation) describe the document as a whole. The text-type properties Contents and Chapter describe the content of the document. When processing this document, the **IFilter** implementation identifies and extracts these properties.

![](images/ixarch09.png)

 

 



