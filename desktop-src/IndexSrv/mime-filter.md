---
title: MIME Filter
description: MIME Filter
ms.assetid: 3e0cbff4-adab-442b-b781-ebd93d69a2b9
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# MIME Filter

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The MIME implementation for the [IFilter](/windows/desktop/api/Filter/nn-filter-ifilter) interface (in mimefilt.dll) extracts text and property information from multipurpose Internet mail extension files with the extensions .eml and .nws. IIS includes a Network News Transfer Protocol (NNTP) server that saves files with the .nws extension. This filter enables indexing and querying NNTP messages with Indexing Service.

 

 




