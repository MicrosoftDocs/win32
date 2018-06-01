---
Description: CiHiliteColor
ms.assetid: 0f71ace3-cd73-4ba0-b0d5-dcbb2f800bac
title: CiHiliteColor
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# CiHiliteColor

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Format1: **CiHiliteColor**=*24-bit color mask*

The mask takes the form 0x*HHHHHH*, where each *H* is a hexadecimal digit.

Format2: **CiHiliteColor**=*color*

where *color* is the name of any color {red, green, blue, yellow, black}. This parameter is optional. It specifies the color used to highlight the text matching the restriction. If it is not specified, or if the format used does not match either of the above, Webhits defaults to red.

 

 



