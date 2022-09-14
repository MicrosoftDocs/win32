---
description: Registry values must be set for verbs to handle situations where a user can select a single item, multiple items, or a selection from an item. A verb requires separate registry values for each of these three situations that the verb supports.
ms.assetid: B6D4C879-3E52-4010-9B2E-3BCD81BB6C93
title: How to Employ the Verb Selection Model
ms.topic: article
ms.date: 05/31/2018
---

# How to Employ the Verb Selection Model

Registry values must be set for verbs to handle situations where a user can select a single item, multiple items, or a selection from an item. A verb requires separate registry values for each of these three situations that the verb supports.

## Instructions


Specify the MultiSelectModel value for all verbs. If the MultiSelectModel value is not specified, it is inferred from the type of verb implementation you have chosen. For COM-based methods (such as DropTarget and ExecuteCommand) **Player** is assumed, and for the other methods **Document** is assumed.

The possible values for the verb selection model are as follows:

1.  Specify **Single** for verbs that support only a single selection.
2.  Specify **Player** for verbs that support any number of items.
3.  Specify **Document** for verbs that create a top-level window for each item. Doing so limits the number of items that are activated and helps avoid running out of system resources if the user opens too many windows.

## Remarks

When the number of items selected does not match the verb selection model or is greater than the default limits outlined in the following table, the verb fails to appear.



| Type of verb implementation | Document | Player    |
|-----------------------------|----------|-----------|
| Legacy                      | 15 items | 100 items |
| COM                         | 15 items | No limit  |



 

The following are example registry entries that use the MultiSelectModel value.

```
HKEY_CLASSES_ROOT
   Folder
      shell
         open
             = MultiSelectModel = Document
```

```
HKEY_CLASSES_ROOT
   ProgID
      shell
         verb
             = MultiSelectModel = Single | Document | Player
```

 

 



