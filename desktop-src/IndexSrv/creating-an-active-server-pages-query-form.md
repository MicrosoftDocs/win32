---
title: Creating an Active Server Pages Query Form
description: Creating an Active Server Pages Query Form
ms.assetid: e735dea9-c397-42b9-9f80-e82767b2fc81
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating an Active Server Pages Query Form

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

This section walks you through the creation of a basic Active Server Page (.asp) file, demonstrating how to create a sample query form, how to control the search, and how to format the results. Although an .asp file is different from .htm, .idq, and .htx files, you will see similar elements in all of them. With Active Server Pages, instead of creating three separate files, you can combine all the information into one .asp file. Regardless of whether you create one file or multiple files, the processing that corresponds to .htm, .idq and .htx processing takes place in the .asp file.

This section contains the following topics:

-   [Setting up an Active Server Pages Form](setting-up-an-active-server-pages-form.md)
-   [Controlling an Active Server Pages Search](controlling-an-active-server-pages-search.md)
-   [Formatting Results in an Active Server Pages File](formatting-results-in-an-active-server-pages-file.md)

When you install Indexing Service, Ixtrasp.asp is installed with the sample files. This sample file shows the query form and query processing combined into one file, which this test drive annotates.

**To use the Ixtrasp.asp sample file**

1.  Copy the Ixtrasp.asp file to a virtual directory with the execute or script permission set.
2.  Change the AddScopeToQuery directory to the directory or directories you want to search. This example uses a hypothetical directory called Myfiles

**To create a basic .asp query form**

1.  Type your scripts and HTML code into a file.
2.  Save the file in HTML format. (Some lines are shown in bold for emphasis only.)

 

 




