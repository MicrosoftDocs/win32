---
title: Special Characters and Words
description: Special Characters and Words
ms.assetid: 36644bef-298a-45b8-8a29-2f5d46af8674
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Special Characters and Words

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

Special characters are characters such as "," "©," and "™". These characters are rarely used in queries. Word breakers should strip special characters during index creation and at query time.

It is recommended that word breakers recognize special words, such as "C++," "C#," ".NET," grades, and musical notation. Word breakers may use a language heuristic to identify a pattern for special words. Word breakers may also use a custom dictionary that contains recognized special words.

 

 




