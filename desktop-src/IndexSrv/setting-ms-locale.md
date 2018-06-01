---
Description: Setting MS.Locale
ms.assetid: 6f78509a-5e89-4dc9-95ad-de852fd8bd12
title: Setting MS.Locale
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Setting MS.Locale

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The **MS.Locale** meta tag specifies the language in which the document is written. This property also tells Indexing Service to use the correct locale-specific resources when processing the HTML page. You should set this variable when the HTML pages being indexed are on sites in different locales. If all the HTML pages being indexed are in the same locale as the server where Indexing Service is installed, then you do not have to include this property in your HTML files.

For example, to designate a locale of Japanese, set your **MS.Locale** meta tag as follows:


```
<META NAME="MS.LOCALE"   CONTENT="JA">
```



When you have included **MS.Locale** in your HTML files, clients can query for that property, as with any other meta tag property. For example, to see all the files in Japanese, send the following query:


```
@Locale JA
```



**Locale** is not a default property in Indexing Service. For the query @Locale JA to work, you must first define the **Locale** meta property. To define the meta property, see [Defining New Property Names for a Web Catalog](defining-new-property-names-for-a-web-catalog.md). To find a list of recognized locale codes, see [Valid Locale Identifiers](valid-locale-identifiers.md).

 

 



