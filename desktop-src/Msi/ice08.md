---
description: ICE08 validates that the Component table contains no duplicate GUIDs. Every component must have a unique GUID. No validation is done if the Component table does not exist.
ms.assetid: c8ff53f3-6587-479d-afb8-b09d0df3b673
title: ICE08
ms.topic: article
ms.date: 05/31/2018
---

# ICE08

ICE08 validates that the [Component table](component-table.md) contains no duplicate [GUIDs](guid.md). Every component must have a unique GUID. No validation is done if the Component table does not exist.

## Result

ICE08 posts an error message if two or more entries in the ComponentId column of the Component table contain the same GUID.

## Example

For the following example, ICE08 would post a message stating that components Red and Green have duplicate GUIDs.

[Component Table](component-table.md) (partial)



| Component | ComponentId                            |
|-----------|----------------------------------------|
| Red       | {0000000A-0003-0000-0000-624474736554} |
| Blue      | {0000000A-0003-0000-0000-624474736354} |
| Green     | {0000000A-0003-0000-0000-624474736554} |



 

To fix this error, change either of the duplicate GUIDs.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



