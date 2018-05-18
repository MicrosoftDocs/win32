---
title: Indexing Service
description: Indexing Service is a base service that extracts content from files and constructs an indexed catalog to facilitate efficient and rapid searching.
ms.assetid: '5c0b3646-eeec-4666-b4c7-451aba783030'
keywords: ["Indexing Service"]
---

# Indexing Service

\[Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.\]

## Purpose

Indexing Service is a base service that extracts content from files and constructs an indexed catalog to facilitate efficient and rapid searching.

Indexing Service can extract both text and property information from files on the local host and on remote, networked hosts. The files can be simply members of a selected file system or part of a virtual Web hosted by, for example, Internet Information Services (IIS).

Indexing Service extracts the content by filtering, using filter components that understand a file's format. The format could include multi-language features such as international languages and locales. A filter component implements the IFilter interface, which supplies methods to read a file to extract text and properties. Windows 2000 and Microsoft Windows XP supply filters for Microsoft Office files, Hypertext Markup Language (HTML) files, Multipurpose Internet Mail Extension (MIME) messages, and plain-text files.

Indexing Service then merges the extracted information into catalogs of indexes for efficient searches. Indexing is the overall process of filtering, creating index entries, and merging them into catalogs.

The final step in the indexing process is creation of a catalog that contains a master index (and any temporary word lists and shadow indexes) storing words and their locations within a set of indexed documents. Subsequently, searching, or querying, the catalogs for particular word combinations uses the master index as well as word lists and shadow indexes to execute queries quickly and efficiently.

## Developer audience

The Indexing Service application programming interface (API) provides additional versatile and flexible facilities for programmatically interacting with Indexing Service. These facilities include:

-   Admin and Query Helper objects and ActiveX Data Object (ADO) methods for use with Microsoft Visual Basic, Microsoft Visual Basic Scripting Edition (VBScript), Microsoft Visual J++ and Microsoft JScript development software.
-   ISAPI Extensions for use in .idq, .ida, and .htx files.
-   OLE DB Helper functions for use with Microsoft Visual C++ development system.
-   OLE DB Provider for Indexing Service interfaces for use with Visual C++.
-   IFilter interface for use with Visual C++.

## In this section

-   [About the Indexing Service](what-s-new-in-indexing-service.md)
-   [Getting Started](getting-started.md)
-   [Using Indexing Service with File Systems](using-indexing-service-with-file-systems.md)
-   [Using Indexing Service with Web Servers](using-indexing-service-with-web-servers.md)
-   [Using Custom Filters with Indexing Service](using-custom-filters-with-indexing-service.md)
-   [Extending Language Resources for Indexing Service](extending-language-resources-for-indexing-service.md)
-   [Troubleshooting Indexing Service](troubleshooting-the-indexing-service.md)
-   [Indexing Service Reference](indexing-service-reference.md)
-   [OLE DB Provider for Indexing Service](ole-db-provider-for-indexing-service.md)

 

 




