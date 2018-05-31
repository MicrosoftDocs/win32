---
title: Hit-Highlighting Syntax
description: Hit-Highlighting Syntax
ms.assetid: 30662363-9cf1-4bba-96f0-803eb46124ae
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Hit-Highlighting Syntax

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The hit highlighter (Webhits.dll) is an Internet Server API (ISAPI) application that you invoke from your browser by referring to an .htw template file.

If you want the minimum formatting to appear in your results set, choose the default formatting in Webhits.dll. To choose the default formatting, specify Null.htw as the template file. This file need not exist.

Sample template files for Webhits output formatting are included in the installed samples as:

/Iissamples/Issamples/Oop/Qfullhit.htw

/Iissamples/Issamples/Oop/Qsumrhit.htw

 

 




