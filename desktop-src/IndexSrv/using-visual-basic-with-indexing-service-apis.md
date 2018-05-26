---
title: Using Visual Basic with Indexing Service APIs
description: Using Visual Basic with Indexing Service APIs
ms.assetid: b0201244-2ce0-4f6f-9850-e8aefe52334b
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Using Visual Basic with Indexing Service APIs

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When you use Indexing Service APIs with Visual Basic, you can choose early binding or late binding of your application to the objects that implement the APIs. Early binding occurs at compile time and generally produces applications that execute faster. Early binding can also provide interactive development features such as object browsing and automatic class and member expansion. Late binding occurs at execution time and gives you greater flexibility in programmatically picking alternative object implementations when they are available. Late binding is also more closely compatible with the style of programming used with VBScript (see [Using Indexing Service APIs from Scripts](using-indexing-service-apis-from-scripts.md)).

Either binding method uses the prog ID of the objects in the API, and early binding can use references to type libraries. This section discusses the following topics concerning the use of early and late binding.

-   [Using Prog IDs of Objects](using-prog-ids-of-objects.md)
-   [Using References to Type Libraries](using-references-to-type-libraries.md)
-   [Creating Objects with Early and Late Binding](creating-objects-with-early-and-late-binding.md)

 

 




