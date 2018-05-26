---
title: HTML Filter
description: HTML Filter
ms.assetid: dd328ddc-6b3b-406c-bf72-e0dd08a6c8fb
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# HTML Filter

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The HTML implementation for the [**IFilter**](/windows/win32/Filter/nn-filter-ifilter?branch=master) interface (in nlhtml.dll) extracts text and property information from the class "htmlfiles" so that it can be indexed by Indexing Service. Indexing Service calls the methods on this **IFilter** interface implementation when indexing HTML files. For a description of the association between filter and file type, see [Finding the Filter DLL for a File](finding-the-filter-dll-for-a-file.md).

You can use the &lt;META&gt; tag feature of HTML documents to convey special handling requests to the HTML filter. &lt;META&gt; tags occur near the beginning of an html file within the &lt;HEAD&gt; ... &lt;/HEAD&gt; tags, as shown in the following example.


```
<head>
<META NAME="DESCRIPTION" CONTENT="This text will appear on the results page as the document's summary.">
</head>
```



Some HTML META tags are automatically mapped to [well-known property](filtering-well-known-properties.md) set and property ID values so that queries on these properties will search the mapped contents. Examples include the following.



| Property example                                      | Mapped to                                                               |
|-------------------------------------------------------|-------------------------------------------------------------------------|
| &lt;meta name="author" content="ruth"&gt;             | The author property in the Summary Information property set.            |
| &lt;meta name="subject" content="word processing"&gt; | The subject property in the Summary Information property set.           |
| &lt;meta name="keywords" content="fonts, serif"&gt;   | The keyword property in the Summary Information property set.           |
| &lt;meta name="ms.category" content="fiction"&gt;     | The category property in the document Summary Information property set. |



 

Here are some other special features of the HTML filter:

-   **Creating special abstracts from files**

    The filtering process can generate abstracts for each filtered file, which default to being a set of characters at the beginning of the file. As shown in the example at the beginning of this section, you can use the &lt;META NAME="DESCRIPTION" ..&gt; tag to instruct the filter to use the string following the **CONTENT** keyword as the document abstract.

-   **Preventing individual files from being filtered**

    Add the following meta tag to the file:

    &lt;meta name="robots" content="noindex"&gt;

-   **Setting the language code for a file to ensure the system chooses the correct language word breakers and noise word files**

    Add the following meta tag to the file, where the content field specifies the appropriate language code (in characters or using the locale value):

    &lt;meta name="ms.locale" content="EN"&gt; or

    &lt;meta name="ms.locale" content=1033&gt;

You can also define new new property names to filter. For additional information, see [Defining New Property Names for a Web Catalog](defining-new-property-names-for-a-web-catalog.md).

 

 




