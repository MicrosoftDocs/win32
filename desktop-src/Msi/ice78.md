---
description: ICE78 verifies that the AdvtUISequence table either does not exist or is empty. This is required because no user interface is allowed during advertising.
ms.assetid: 8ed1c68f-331d-42f9-80df-bdcb42962482
title: ICE78
ms.topic: article
ms.date: 05/31/2018
---

# ICE78

ICE78 verifies that the [AdvtUISequence table](advtuisequence-table.md) either does not exist or is empty. This is required because no user interface is allowed during advertising.

## Result

ICE78 posts an error if the AdvtUISequence table exists and is not empty.

## Example

ICE78 reports the following error for the example:

Action 'Action1' found in AdvtUISequence table. No UI is allowed during advertising. Therefore AdvtUISequence table must be empty or not present.

[AdvtUISequence table](advtuisequence-table.md)(partial)



| Action  | Condition | Sequence |
|---------|-----------|----------|
| Action1 | TRUE      | 1        |



 

To fix the error, either remove "Action1" from the table, or remove the table.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



