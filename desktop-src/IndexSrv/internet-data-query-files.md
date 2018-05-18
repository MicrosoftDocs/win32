---
title: Internet Data Query Files
description: Internet Data Query Files
ms.assetid: '9e4eb914-3d1f-4821-b8aa-95bf5408f584'
---

# Internet Data Query Files

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Internet Data Query files (files with an .idq extension) for Indexing Service, together with the form parameters, specify the query that Indexing Service will run. The .idq file is divided into two sections: the names section (which is optional and need not be supplied for standard queries) and the query section.

This part of the documentation contains the following topics:

-   [Names Section of .Idq Files](names-section-of-idq-files.md): Defines nonstandard column names in an .idq file that can be referred to in a query.
-   [Defining Friendly Names](defining-friendly-names.md): Examples of defining friendly names for properties.
-   [Defining Custom Properties](defining-custom-properties.md): Examples of custom properties from various [**IFilter**](ifilter.md) implementations, including Microsoft Office and HTML.
-   [Query Section of .Idq Files](query-section-of-idq-files.md): Explains the parameters that can be used in a query.
-   [Effect of Parameters on Query Performance](effect-of-parameters-on-query-performance.md): Tells how to set parameters for the best performance.
-   [Sequential vs. Nonsequential Execution](sequential-and-nonsequential-execution.md): Describes the two ways to execute a query.
-   [Enumerated vs. Indexed Resolution](enumerated-and-indexed-resolution.md). Describes conditions under which queries are enumerated against the system disk rather than the Content Index.
-   [Deferring Nonindexed Trimming](deferring-nonindexed-trimming.md). Describes how to defer the trimming of records returned from certain queries.

> [!Note]  
> All paths to .idq files must be the full path name from a virtual root, not a relative path or a physical path. In other words, all paths must start with a forward slash and cannot contain "." or ".." components. See the following examples:

 

**Valid Paths**

-   /scripts/myquery.idq

-   /iissamples/issamples/query.idq

**Invalid Paths**

-   c:\\iissrv\\scripts\\myquery.idq

-   scripts/query.idq

-   /samples/../scripts/example.idq

You must put the .idq files into a virtual directory with Execute or Script permission. You cannot put .idq files into a virtual directory pointing to a remote Universal Naming Convention (UNC) share.

> [!Note]  
> Indexing Service does not support physical paths longer than the Microsoft Windows 2000 shell limit (260 characters).

 

 

 




