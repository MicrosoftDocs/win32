---
description: Categories help you organize events so Event Viewer can filter them. Each event source can define its own numbered categories and the text strings to which they are mapped.
ms.assetid: ddba8066-b6b9-42a6-b49f-cbae8f97ef6d
title: Event Categories
ms.topic: article
ms.date: 05/31/2018
---

# Event Categories

Categories help you organize events so Event Viewer can filter them. Each [event source](event-sources.md) can define its own numbered categories and the text strings to which they are mapped.

The categories must be numbered consecutively, beginning with the number 1. The categories themselves are defined in a message file. For example, use the following syntax to declare three event categories. In Event Viewer, the events that use these categories will have Category 1, Category 2, or Category 3 displayed in the **Category** column.

``` syntax
MessageId=0x1
SymbolicName=CATEGORY_1
Language=English
Category 1
.

MessageId=0x2
SymbolicName=CATEGORY_2
Language=English
Category 2
.

MessageId=0x3
SymbolicName=CATEGORY_3
Language=English
Category 3
.
```

Categories can be stored in a separate message file, or in a file that contains messages of other types. If you create a single message file, be sure that the categories are the first messages in the file. For more information on creating and using message files, see [Message Files](message-files.md).

The total number of categories is stored in the **CategoryCount** value for the event source.

 

 



