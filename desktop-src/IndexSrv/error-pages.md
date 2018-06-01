---
Description: Error Pages
ms.assetid: b6846bf5-96f8-48d2-b880-a336dd17d200
title: Error Pages
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Error Pages

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Through registry settings, it is possible to configure .htx files to display in the event errors are encountered while executing a search. Any of the file's error types can cause an error page to be displayed:

<dl> <dt>

<span id="Query_error"></span><span id="query_error"></span><span id="QUERY_ERROR"></span>Query error
</dt> <dd>

An error in a query specification ([CiRestriction](https://www.bing.com/search?q=CiRestriction)). This is most likely a user error.

</dd> <dt>

<span id="Error_in_HTML_extension_file"></span><span id="error_in_html_extension_file"></span><span id="ERROR_IN_HTML_EXTENSION_FILE"></span>Error in HTML extension file
</dt> <dd>

An error was found while formatting the .htx file. This is probably a configuration error.

</dd> <dt>

<span id="Error_in_Internet_Data_Query__.idq__file"></span><span id="error_in_internet_data_query__.idq__file"></span><span id="ERROR_IN_INTERNET_DATA_QUERY__.IDQ__FILE"></span>Error in Internet Data Query (.idq) file
</dt> <dd>

An error was found in the query parameter file. This is probably a configuration error, although it might also occur due to unexpected data input from a form.

</dd> <dt>

<span id="Some_other_error"></span><span id="some_other_error"></span><span id="SOME_OTHER_ERROR"></span>Some other error
</dt> <dd>

An unspecified error occurred.

</dd> </dl>

Error pages have access to some of the variables available to .htx files. In addition, there is a variable [CiErrorMessage](https://www.bing.com/search?q=CiErrorMessage), which gives a message describing the error. See [.Idq File Errors](idq-file-errors.md) and [.Htx File Errors](htx-file-errors.md) for a list of the possible values of CiErrorMessage and [Error Messages and Error Pages](error-messages-and-error-pages.md) for details on Indexing Service error messages.

 

 



