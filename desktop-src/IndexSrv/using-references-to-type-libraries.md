---
Description: Using References to Type Libraries
ms.assetid: 3f4d6bd9-e977-4fc8-8346-65a421525b7e
title: Using References to Type Libraries
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Using References to Type Libraries

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

You can declare and create objects from the Indexing Service APIs using references to type libraries. To do this you need to select the appropriate libraries in the Visual Basic development environment. The following table lists the APIs and the reference and type library for each.



| API          | Reference                                                                                       | Library  |
|--------------|-------------------------------------------------------------------------------------------------|----------|
| Admin Helper | Indexing Service Administration Type Library 1.0                                                | CIODMLib |
| Query Helper | ixsso Control Library                                                                           | Cisso    |
| ADO          | ActiveX Data Objects (ADO) *version* Library, where *version* is one of the available versions. | ADODB    |



 

See [Creating Objects with Early and Late Binding](creating-objects-with-early-and-late-binding.md) for details on using this information.

 

 



