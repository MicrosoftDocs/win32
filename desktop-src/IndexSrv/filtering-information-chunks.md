---
title: Filtering Information Chunks
description: Filtering Information Chunks
ms.assetid: '6e9c4d18-4cd1-42f5-9e7f-95ddb62ead1c'
---

# Filtering Information Chunks

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Chunks are the fundamental logical units of text processed by clients of filters. Chunks share the same properties and the same locale, so word breaking and noise-word removal from the text can be tailored to the appropriate native language. Two pieces of text that cannot share the same properties and the same locale must be in different chunks. Chunks may overlap, but a specific property is applied to a given character only once. Following are three examples of chunks.

-   You can represent a simple text file in one chunk of text.
-   With an HTML file, you need to represent each tag as a single chunk of text so that the tag &lt;TITLE&gt; for instance, can be mapped to a known property such as **DocTitle**.
-   Chunks in other types of files can include separate text boxes in a graphics file, labels and titles on charts, and possibly text in separate cells of a spreadsheet.

The CiDaemon.exe process of Indexing Service filters objects by making successive calls to the [**IFilter::GetChunk**](ifilter-getchunk.md) method to get a [**STAT\_CHUNK**](stat-chunk.md) structure that describes the chunks. All chunks of text use the Unicode representation, so single- and multibyte-characters are converted to Unicode when necessary.

In order for the appropriate word breaker to process the chunks, the file must have language-attribute information accessible to the filter. For example, Microsoft Word documents can tag text with a language tag using the **Tools/Language** menu. This information is stored with the text and is then available for the Word filter to process it accordingly.

The filter gives each chunk a unique, **ULONG** identifier (ID) greater than zero. These identifiers are guaranteed to remain constant until the [**IFilter**](ifilter.md) interface is released. Calling an **IFilter** method on an object with the same parameters for the [**IFilter::Init**](ifilter-init.md) method produces the same set of chunks. If, however, you change the **Init** method parameters for repeated calls to the **IFilter** interface, you may get a different set of chunks. Most significantly, changing the set of properties requested from an object by changing the attribute array in the **IFilter::Init** method may re-partition the chunks of an object.

Calls to the [**IFilter::GetChunk**](ifilter-getchunk.md) method do not reveal the original source of the chunk (that is, whether it was embedded, linked, or in a top-level container).

 

 




