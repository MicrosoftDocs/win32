---
title: Querying a Site in a Different Locale
description: Querying a Site in a Different Locale
ms.assetid: '94402bf1-64de-4a99-a2ac-937242117971'
---

# Querying a Site in a Different Locale

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When querying a site for documents in different languages, you can send a [CiCodepage](variables-in-forms-and-in-idq-files.md#-idxs-cicodepage-var) variable in the URL to override the codepage character setting on the server and in the HTTP\_ACCEPT\_LANGUAGE variable in your browser. For example, suppose a client by the name of Yukio from Japan wants to query a site in the United States that contains documents in American English. Yukio wants a list of all documents containing the word *cache*. By appending the CiCodepage variable to his query, he can override the HTTP\_ACCEPT\_LANGUAGE setting in his browser, making sure the query results will be returned in English.

In the following example, Yukio is querying a server called **Example**, located at **example.microsoft.com**, and a virtual directory called **Software**.


```
http://example.microsoft.com/software/[form.htm]
```



In the search form, Yukio then types:


```
Cache&amp;CiLocale=EN&amp;CiCodepage=Windows-1252
```



 

 




