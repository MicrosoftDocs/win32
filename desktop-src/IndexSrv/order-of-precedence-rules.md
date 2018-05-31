---
title: Order of Precedence Rules
description: Order of Precedence Rules
ms.assetid: 7e34f447-013e-4a07-a0cd-5fbf26cd2371
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Order of Precedence Rules

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The Boolean and proximity operators follow conventional precedence rules. The order of precedence is the following.

1.  **NOT**
2.  **AND** and **NEAR**
3.  **OR**

The proximity operator has the same precedence as **AND**. After precedence rules are applied, operators are processed left to right. You can add parentheses to nest expressions within a query to explicitly specify the precedence. Expressions within parentheses are evaluated first.

 

 




