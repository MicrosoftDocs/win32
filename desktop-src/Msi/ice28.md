---
description: ICE28 is commonly used to validate that the ForceReboot action is placed before or after, and never within, a specific group of actions in the action sequence tables. See the ForceReboot action topic to determine the actions that comprise this group.
ms.assetid: 746d907a-33e1-479a-bcb0-93e7fd5dd975
title: ICE28
ms.topic: article
ms.date: 05/31/2018
---

# ICE28

ICE28 is commonly used to validate that the ForceReboot action is placed before or after, and never within, a specific group of actions in the action sequence tables. See the [ForceReboot action](forcereboot-action.md) topic to determine the actions that comprise this group.

ICE28 validates actions in the following sequence tables:

[AdminUISequence table](adminuisequence-table.md)

[AdminExecuteSequence table](adminexecutesequence-table.md)

[InstallUISequence table](installuisequence-table.md)

[InstallExecuteSequence table](installexecutesequence-table.md)

## Result

ICE28 posts an error message if ForceReboot is sequenced within the specified action group.

## Example

For the example shown, ICE28 posts the following error message:

``` syntax
Action: 'ForceReboot' of table InstallExecuteSequence is not permitted in the range 5 to 15 because it cannot separate a set of actions contained in this range.
```

[InstallExecuteSequence Table](installexecutesequence-table.md)



| Action             | Sequence |
|--------------------|----------|
| ForceReboot        | 10       |
| RegisterMIMEInfo   |   5      |
| RegisterProgIdInfo | 15       |



 

The sequence number of 10 given to ForceReboot breaks generates the error, because it comes between the sequence numbers of RegisterMIMEInfo and RegisterProgIdInfo.

## Related topics

<dl> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



