---
title: Creating a Static Query Form
description: Creating a Static Query Form
ms.assetid: 2babe437-f8c5-4ca9-b55c-575e3a05432e
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Creating a Static Query Form

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Three files — an HTML file, an Internet Data Query (.idq) file, and an Extended HTML (.htx) file — interact to create a static query with Indexing Service. The HTML file creates the form, which posts user input as a query to the .idq file. The .idq file then sends the results of the query to the .htx file, which formats the results that are returned to the Web browser.

All three of these files must be in a virtual directory defined in Internet Service Manager. The .idq and .htx files must be in the /IisSamples/IsSamples virtual directory, which is physically located in C:\\InetPub\\IisSamples\\IsSamples, or in another virtual directory with both Read and Execute (or Script) permissions set.

This section contains the following topics:

-   [Internet Data Query Files](internet-data-query-files.md)
-   [Setting up the Form (.Htm File)](setting-up-the-form--htm-file-.md)
-   [Controlling the Search (.Idq File)](controlling-the-search--idq-file-.md)
-   [HTML Extension Files](html-extension-files.md)

 

 




