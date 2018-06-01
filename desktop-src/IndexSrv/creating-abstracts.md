---
Description: Creating Abstracts
ms.assetid: d77a705a-d897-41ca-b314-f4ebc4e2bc06
title: Creating Abstracts
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Creating Abstracts

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/windows/desktop/6da601c6-3742-40ad-99f2-8817f7f642b3) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The CiDaemon.exe process of Indexing Service can automatically generate a summary or abstract (also called a characterization) for each file. If the [GenerateCharacterization](generatecharacterization.md) registry entry is set to one, the abstract is generated. The maximum number of characters in the generated abstract is controlled by the [MaxCharacterization](maxcharacterization.md) registry entry.

If the abstract is set to be generated automatically, Indexing Service usually takes by default the first 320 characters of a document and copies that block of text for the summary. Alternatively, if a document has certain properties, such as DocTitle, they contribute more to the abstract than the first block of text in the file.

See [HTML Filter](html-filter.md) for a description of how you can override this feature for the HTML class of documents. You can use this description as a basis to generate an abstract of any type of documents.

 

 



