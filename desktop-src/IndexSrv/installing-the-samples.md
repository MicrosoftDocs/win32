---
title: Installing the Samples
description: Installing the Samples
ms.assetid: 291995a0-8800-4df1-a646-f4a112a3743e
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Installing the Samples

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

To install the sample code for Indexing Service that comes with the Microsoft Platform SDK, select **Sample Code, Windows Base Samples, Indexing Service Samples** in the Platform SDK Setup Wizard during installation. The system installs the sample files in subdirectories of the mssdk\\samples\\winbase\\indexing directory.

The current topic alphabetically summarizes the Indexing Service samples. For an organization of the samples by task, language, API, and tool, see [Samples by Task, Language, API, and Tool](samples-by-task--language--api--and-tool.md).

The following table lists the samples for Indexing Service included in the Platform SDK and provides implementation language and a short description of each sample. Selecting the name of a sample takes you to a more detailed reference for that sample.



| Sample                                    | Language                                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                |
|-------------------------------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [AdvQuery](advquery-sample.md)           | C++                                       | A command-line application that executes a query using OLE DB Provider interfaces such as **ICommand** and [**ICommandTree**](/previous-versions/windows/desktop/api/cmdtree/nn-cmdtree-icommandtree). It shows how to specify a catalog, machine name, and scope. It can also display the OLE DB command tree for the query.                                                                                                                                                                    |
| [ChgState](chgstate-sample.md)           | C++                                       | A command-line application that can either report the current state of a catalog or change the state of the catalog using the [**SetCatalogState**](/windows/desktop/api/Ntquery/nf-ntquery-setcatalogstate) function of the OLE DB Helper API.                                                                                                                                                                                                                                |
| [DHtml (CiDHtml)](https://www.bing.com/search?q=DHtml (CiDHtml))  | Visual Basic Scripting Edition (VBScript) | A dynamic HTML (DHTML) application that creates a client-side query form to query an Indexing Service catalog. The sample uses the Query Helper API for the query and an ADO recordset to return the results.                                                                                                                                                                                                                              |
| [HtmlProp](htmlprop-sample.md)           | C++                                       | An example [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) implementation that specializes the Indexing Service HTML filter to extract value-type properties. It converts HTML meta properties to data types other than strings as specified by a configuration file.                                                                                                                                                                                           |
| [IFilter (HtmlFilt)](ifilter-sample.md)  | C++                                       | An example [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) implementation (HtmlFilt) for HTML files. It is more complex than a basic text filter, because it demonstrates techniques for extracting both text-type and value-type properties.                                                                                                                                                                                                                   |
| [IISAdmin](iisadmin-sample.md)           | VBScript, JScript, IDA+HTX                | A set of HTML and ASP forms that demonstrates how to use Internet Information Services (IIS) to administer Indexing Service. The forms retrieve indexing statistics, force a master merge, rescan paths, and check for documents that could not be filtered.                                                                                                                                                                               |
| [IISSearch](iissearch-sample.md)         | VBScript, JScript, IDQ+HTX                | A set of HTML and ASP forms that demonstrates how to use Internet Information Services (IIS) to query Indexing Service. The forms use Indexing Service Query Language queries and the Query Helper API, use SQL queries and the ADO and Query Helper APIs, and use IDQ+HTX and the ISAPI Extension API.                                                                                                                                    |
| [Simple (QSample)](simple-sample.md)     | C++                                       | A command-line application that executes a query using the OLE DB Helper API functions [**CICreateCommand**](/windows/desktop/api/Ntquery/nf-ntquery-cicreatecommand) and [**CITextToFullTree**](/windows/desktop/api/Ntquery/nf-ntquery-citexttofulltree) to simplify the coding needed to create a query to an Indexing Service catalog.                                                                                                                                                                         |
| [SmpFilt](smpfilt-sample.md)             | C++                                       | An example [**IFilter**](/windows/desktop/api/Filter/nn-filter-ifilter) implementation that reads an unformatted text file (with the extension .smp) using the ANSI code page of the current thread, and outputs UNICODE text for the current locale. It accepts as input only single-byte-character text files and not multibyte-character or UNICODE text files. It is the simplest example of an **IFilter** implementation included in the Indexing Service sample code. |
| [Lrsample](language-resource-samples.md) | C++                                       | An example [**IWordbreaker**](https://www.bing.com/search?q=**IWordbreaker**) and [**IStemmer**](https://www.bing.com/search?q=**IStemmer**) implementation that parses Unicode text on the occurrence of white space and generates inflected forms for words based on a small custom dictionary.                                                                                                                                                                                                      |
| [SQuery](squery-sample.md)               | VBScript, JScript                         | Three scripts that execute using Windows Script Host. VBSQuery is written in VBScript and performs a simple query. JSQuery is a translation of VBSQuery to JScript. QSample is written in VBScript and functions similarly to the C++ [Simple Sample](simple-sample.md) with managing and querying functionality.                                                                                                                         |
| [VBAdmin](vbadmin-sample.md)             | Visual Basic                              | A Windows application that illustrates how to administer Indexing Service using the [**AdminIndexServer**](iadminindexserver.md), [**CatAdm**](icatadm.md), and [**ScopeAdm**](iscopeadm.md) automation objects of the Admin Helper API.                                                                                                                                                                                                |
| [VBQuery](vbquery-sample.md)             | Visual Basic                              | A Windows application that illustrates how to query Indexing Service using the Indexing Service Query Language Dialects and the SQL language and the ADO and Query Helper APIs.                                                                                                                                                                                                                                                            |
| [VJQuery](vjquery-sample.md)             | Visual J++                                | A command-line application that illustrates how to query Indexing Service using the SQL query language and the ADO API.                                                                                                                                                                                                                                                                                                                    |



 

 

 




