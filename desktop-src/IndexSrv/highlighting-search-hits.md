---
title: Highlighting Search Hits
description: Highlighting Search Hits
ms.assetid: f0b2bcd2-d7e0-45d5-b3bf-ef9ab24b5fe4
ms.date: 05/31/2018
ms.topic: article
ms.author: windowssdkdev
ms.prod: windows
ms.technology: desktop
---

# Highlighting Search Hits

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

When you query a document with Indexing Service, the hit-highlighting feature shows the exact portions (if any) of the document that satisfy your query. The hit-highlighting feature generates an HTML page containing a list of the *hits*, with those words making up the hit emphasized (by default, displayed in red and italics). Each hit is displayed together with some of the text that surrounds it in the document. Also, for each document in which a hit is found, Indexing Service gives you a link to the full text of that document.

> [!Note]  
> CiBeginHilite and CiEndHilite are not supported in versions of Index Server later than 2.0, due to the potential security risk posed by allowing HTML tags to be passed as the arguments for these parameters.

 

This section contains:

-   [Hit-Highlighting Syntax:](hit-highlighting-syntax.md) Tells how to start the hit-highlighting application.
-   [Webhits Parameters](webhits-parameters.md) Provides parameters to help you fine-tune a query with Webhits.
-   [Formatting Considerations:](formatting-considerations.md) Gives details about the placement of Webhits parameters.
-   [Adding a Hit-Highlighting Link to a Results Page:](adding-a-hit-highlighting-link-to-a-results-page.md) Tells how to modify Query.htx file to add a link to Webhits in an existing page.
-   [Hit-Highlighting Examples:](hit-highlighting-examples.md) Shows an example of how to set up hit-highlighting in queries and gives examples of acceptable path names.

## Related topics

<dl> <dt>

[Hit-Highlighting Errors](hit-highlighting-errors.md)
</dt> <dt>

[Secure Code Practices](secure-code-practices.md)
</dt> </dl>

 

 




