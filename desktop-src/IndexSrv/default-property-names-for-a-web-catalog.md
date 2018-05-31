---
title: Default Property Names for a Web Catalog
description: Default Property Names for a Web Catalog
ms.assetid: 7285d091-e15b-481b-9a46-eb836005689e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Default Property Names for a Web Catalog

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This list of properties includes all properties in the property store exposed by system [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) implementations. Additional properties can be indexed by using custom property features, if available, documented in each **IFilter** implementation or by installing additional **IFilter** implementations that expose additional properties.



| Friendly Name         | Datatype                      | Property                                                                                                                                                                                          |
|-----------------------|-------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| A\_HRef               | DBTYPE\_WSTR \| DBTYPE\_BYREF | Text of HTML HREF. This property name was created for Microsoft Site Server and corresponds to the Indexing Service property name **HtmlHRef**. Can be queried but not retrieved.                 |
| Access                | VT\_FILETIME                  | Last time file was accessed.                                                                                                                                                                      |
| All                   | (not applicable)              | Searches every property for a string. Can be queried but not retrieved.                                                                                                                           |
| AllocSize             | DBTYPE\_I8                    | Size of disk allocation for file.                                                                                                                                                                 |
| Attrib                | DBTYPE\_UI4                   | File attributes.                                                                                                                                                                                  |
| ClassId               | DBTYPE\_GUID                  | Class ID of object; for example, Corel WordPerfect, Microsoft Word, and so on.                                                                                                                    |
| Characterization      | DBTYPE\_WSTR \| DBTYPE\_BYREF | Characterization, or abstract, of document. Computed by Indexing Service.                                                                                                                         |
| Contents              | (not applicable)              | Main contents of file. Can be queried but not retrieved.                                                                                                                                          |
| Create                | VT\_FILETIME                  | Time file was created.                                                                                                                                                                            |
| Directory             | DBTYPE\_WSTR \| DBTYPE\_BYREF | Physical path to the file, not including the file name.                                                                                                                                           |
| DocAppName            | DBTYPE\_WSTR \| DBTYPE\_BYREF | Name of application that created the file.                                                                                                                                                        |
| DocAuthor             | DBTYPE\_WSTR \| DBTYPE\_BYREF | Author of document.                                                                                                                                                                               |
| DocByteCount          | DBTYPE\_14                    | Number of bytes in a document.                                                                                                                                                                    |
| DocCategory           | DBTYPE\_STR \| DBTYPE\_BYREF  | Type of document such as a memo, schedule, or white paper.                                                                                                                                        |
| DocCharCount          | DBTYPE\_I4                    | Number of characters in document.                                                                                                                                                                 |
| DocComments           | DBTYPE\_WSTR \| DBTYPE\_BYREF | Comments about document.                                                                                                                                                                          |
| DocCompany            | DBTYPE\_STR \| DBTYPE\_BYREF  | Name of the company for which the document was written.                                                                                                                                           |
| DocCreatedTm          | VT\_FILETIME                  | Time document was created.                                                                                                                                                                        |
| DocEditTime           | VT\_FILETIME                  | Total time spent editing document.                                                                                                                                                                |
| DocHiddenCount        | DBTYPE\_14                    | Number of hidden slides in a Microsoft PowerPoint document.                                                                                                                                       |
| DocKeywords           | DBTYPE\_WSTR \| DBTYPE\_BYREF | Document keywords.                                                                                                                                                                                |
| DocLastAuthor         | DBTYPE\_WSTR \| DBTYPE\_BYREF | Most recent user to edit document.                                                                                                                                                                |
| DocLastPrinted        | VT\_FILETIME                  | Time document was last printed.                                                                                                                                                                   |
| DocLastSavedTm        | VT\_FILETIME                  | Time document was last saved.                                                                                                                                                                     |
| DocLineCount          | DBTYPE\_14                    | Number of lines contained in a document.                                                                                                                                                          |
| DocManager            | DBTYPE\_STR \| DBTYPE\_BYREF  | Name of the manager of the document’s author.                                                                                                                                                     |
| DocNoteCount          | DBTYPE\_14                    | Number of pages with notes in a PowerPoint document.                                                                                                                                              |
| DocPageCount          | DBTYPE\_I4                    | Number of pages in document.                                                                                                                                                                      |
| DocParaCount          | DBTYPE\_14                    | Number of paragraphs in a document.                                                                                                                                                               |
| DocPartTitles         | DBTYPE\_STR \| DBTYPE\_VECTOR | Names of document parts. For example, in Microsoft Excel, part titles are the names of spreadsheets; in PowerPoint, slide titles; and in Word, the names of the documents in the master document. |
| DocPresentationTarget | DBTYPE\_STR\|DBTYPE\_BYREF    | Target format (35mm, printer, video, and so on) for a presentation in PowerPoint.                                                                                                                 |
| DocRevNumber          | DBTYPE\_WSTR \| DBTYPE\_BYREF | Current version number of document.                                                                                                                                                               |
| DocSecurity           | DBTYPE\_14                    | Control permissions.                                                                                                                                                                              |
| DocSlideCount         | DBTYPE\_14                    | Number of slides in a PowerPoint document.                                                                                                                                                        |
| DocSubject            | DBTYPE\_WSTR \| DBTYPE\_BYREF | Subject of document.                                                                                                                                                                              |
| DocTemplate           | DBTYPE\_WSTR \| DBTYPE\_BYREF | Name of template for document.                                                                                                                                                                    |
| DocThumbnail          | VT\_CF                        | Thumbnail                                                                                                                                                                                         |
| DocTitle              | DBTYPE\_WSTR \| DBTYPE\_BYREF | Title of document.                                                                                                                                                                                |
| DocWordCount          | DBTYPE\_I4                    | Number of words in document.                                                                                                                                                                      |
| FileIndex             | DBTYPE\_I8                    | Unique ID of file.                                                                                                                                                                                |
| FileName              | DBTYPE\_WSTR \| DBTYPE\_BYREF | Name of file.                                                                                                                                                                                     |
| Img\_Alt              | DBTYPE\_WSTR \| DBTYPE\_BYREF | Alternate text for &lt;IMG&gt; tags. Can be queried but not retrieved.                                                                                                                            |
| Path                  | DBTYPE\_WSTR \| DBTYPE\_BYREF | Full physical path to file, including file name.                                                                                                                                                  |
| ShortFileName         | DBTYPE\_WSTR \| DBTYPE\_BYREF | Short (8.3) file name.                                                                                                                                                                            |
| Size                  | DBTYPE\_I8                    | Size of file, in bytes.                                                                                                                                                                           |
| USN                   | DBTYPE\_I8                    | Update Sequence Number (USN). NTFS file system drives only.                                                                                                                                       |
| Write                 | VT\_FILETIME                  | Last time file was written.                                                                                                                                                                       |



 

 

 




