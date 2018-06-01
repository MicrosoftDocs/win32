---
Description: Sample Query
ms.assetid: 9e943b8a-f384-4c79-9bf8-61551d75741a
title: Sample Query
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Sample Query

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Suppose, when putting together the information in the previous sections, that you want to search for the author of a document greater than 100 bytes in size, and the author’s name is George. To do this, send the following query:


```
@DocAuthor = George AND @size < 100
```



You want to aim your query at this document:

/InetPub/Docs/Ideas.doc

To choose default formatting, refer to a virtual directory with Execute or Script permission:

/*Path*/null.htw?

Before the query string can be passed to Webhits, it must be escaped, resulting in:


```
@DocAuthor%20%3D%20George%20AND%20@size%20%3E%20100
```



Now, to hit-highlight the document, issue the following command:


```
http://MyServer/Path/Null.htw?CiWebhitsFile=\vpath\Docs\Ideas.doc &amp;
CiRestriction=@DocAuthor%20%3D%20George%20AND%20@size%20%3E%20100
```



> [!Note]  
> Neither @size nor @DocAuthor are custom properties, so you do not need to specify an .idq file in this case.

 

 

 



