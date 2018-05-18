---
title: Other Usage Rules
description: Other Usage Rules
ms.assetid: '42e24aed-8bf3-4d22-98e2-a03e6e1e44fe'
---

# Other Usage Rules

> [!Note]  
> Indexing Service is no longer supported as of Windows XP and is unavailable for use as of Windows 8. Instead, use [Windows Search](https://msdn.microsoft.com/library/windows/desktop/aa965362) for client side search and [Microsoft Search Server Express]( http://go.microsoft.com/fwlink/p/?linkid=258445) for server side search.

 

The following rules also apply to the use of the Boolean and proximity operators.

-   Use double quotes (") to indicate that a Boolean or proximity operator keyword should be ignored in your query. For example, "Jack and Jill" will match documents with that exact phrase, not documents that match the Boolean expression. (In addition to being an operator, the word *and* is a noise word in English.)
-   The **NEAR** operator is similar to the **AND** operator in that **NEAR** returns a match if both words being sought are in the same document. However, the **NEAR** operator differs from **AND** because the rank assigned by **NEAR** depends on the proximity of words. That is, the rank of a document in which the sought words are closer together is higher than or equal to the rank of a document in which the words are farther apart. If these words are more than 50 words apart, they are not considered near enough to be related, and the document is assigned a rank of zero.
-   The **NOT** operator can be used only after an **AND** operator in content (text-type) queries; it can be used only to exclude documents that match a previous content restriction. For value-type property queries, the **NOT** operator can be used apart from the **AND** operator.
-   The symbols (&, \|, !, ~) and the English keywords **AND**, **OR**, **NOT**, and **NEAR** work the same way in all languages supported by Indexing Service.
-   The **NEAR** operator can be applied only to words or phrases.

 

 




