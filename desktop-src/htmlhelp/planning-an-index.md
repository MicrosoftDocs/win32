---
title: Planning an Index
description: Planning an Index
ms.assetid: F03C5DD1-638B-4c07-BF6A-A2A406EA2887
ms.technology: desktop
ms.prod: windows
ms.author: windowssdkdev
ms.topic: article
ms.date: 05/31/2018
---

# Planning an Index

[Adding an index](create-an-index-file.md) to a help system is one of the most important ways to get users quickly to the information they need. Usability studies have shown that users will more frequently use a well-planned index to locate topics than they will a table of contents or [full-text search](the-difference-between-the-index-tab-and-the-search-tab.md). Users click a keyword listed in the index and it either takes them directly to the topic containing the information they are looking for, or to a list of topics that contain the keyword.

The index contains keywords that you specify. It can contain terms for beginners and advanced users, synonyms for terms, terms that describe topics generally, and terms that describe topics specifically. The index provides users with many different ways to get to topics. The more ways you provide, the more likely it is that users will find the topic they need.

Traditionally an index is designed so that it contains first and second level entries. First-level entries describe a general category. Second-level entries are indented under the first-level entries and describe specific topics within that category. With HTML Help, you can use an unlimited number of index levels.

Items from the [accessibility word list](about-the-accessibility-word-list.md) can be added as index keywords so that disabled users can easily find the information they need about your software product.

## Tips for creating indexes

-   Plan some [guidelines for creating keywords](guidelines-for-writing-keywords.md) before you begin indexing.
-   If your index is being shipped with a software program, go through the user interface carefully and add index entries for every element. For example, include words or phrases that appear in tool tips, menu items, dialog boxes, and context-sensitive help topics.
-   Index entries should be short and concise, and should never wrap to a second line.
-   After you compile your help file, check your index keywords to make sure they look the way you want them to. Some keywords may be so similar that they could be consolidated.

## Related topics

<dl> <dt>

[Start a Help System Design](start-a-help-system-design.md)
</dt> </dl>

 

 




