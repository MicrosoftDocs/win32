---
title: HTML Extension Files
description: HTML Extension Files
ms.assetid: 'e1a9a456-0bdf-43bc-b110-b4ff94745805'
---

# HTML Extension Files

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

HTML extension (.htx) files for Indexing Service are similar to HTML extension files for the Internet Database Connector (IDC). There are some slight differences, however. For example, for Indexing Service, .idq files will reference .htx files, but for the IDC, .idc files will reference .htx files.

This section explains the features of Indexing Service extension files.

-   [Query Result Pages](query-result-pages.md): Describes the query results page, which is formatted in the .htx file.
-   [Syntax in HTML Extension Files](syntax-in-html-extension-files.md): Discusses the syntax in .htx files.
-   [Query Execution Parameters](query-execution-parameters.md): Describes built-in variables available to the .htx file to flag any unexpected query results.
-   [Formatting the Results (.Htx File)](formatting-the-results--htx-file-.md): Describes the format of the HTML extension (.htx) file.
-   [Record Numbers and Counts](record-numbers-and-counts.md): Discusses record-number and count built-in variables.
-   [Parameters from Internet Data Query Files](parameters-from-internet-data-query-files.md): Explains predefined parameters that can be set in .idq files.
-   [Navigating Between Pages in Query Results](navigating-between-pages-in-query-results.md): Tells how to add navigational aids to your results pages.
-   [HTTP Variables](http-variables.md): Lists and explains default HTML variables.
-   [Variables Affecting the Formatting of Results](variables-affecting-the-formatting-of-results.md): Describes variables that control how a results page will look.
-   [Error Pages](error-pages.md): Describes error types that can cause an error page to be displayed.

> [!Note]  
> All path names to .htx files must be either full virtual paths or full physical paths with no “.” or “..” components. This applies to .htx files referenced in [CiTemplate](variables-in-forms-and-in-idq-files.md#-idxs-citemplate-var) or as include files.

 

Do not put these files on a virtual root pointing to a remote Uniform Naming Convention (UNC) share.

 

 




