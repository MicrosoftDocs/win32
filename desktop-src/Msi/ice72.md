---
description: ICE72 verifies that non-built-in custom actions are not used in the AdvtExecuteSequence table.
ms.assetid: b04227d5-5bd6-434a-860c-498d787a1f0a
title: ICE72
ms.topic: article
ms.date: 05/31/2018
---

# ICE72

ICE72 verifies that non-built-in custom actions are not used in the [AdvtExecuteSequence table](advtexecutesequence-table.md). Specifically, only type 19, type 35, and type 51 custom actions are allowed in the AdvtExecuteSequence table. If other custom actions are used, advertisement may not behave as expected.

## Result

ICE72 returns an error if the AdvExecuteSequence table uses custom actions other than type 35, type 51, and type 19.

## Example

ICE72 reports the following error for the example shown:

``` syntax
Custom Action 'CA1' in the AdvtExecuteSequence table is not allowed. Only built-in custom actions are allowed.
```

To fix the error, remove 'CA1' from the AdvtExecuteSequence table.

[AdvtExecuteSequence Table](advtexecutesequence-table.md) (partial)



| Action |
|--------|
| CA1    |
| CA35   |



 

[CustomAction Table](customaction-table.md) (partial)



| Action | Type |
|--------|------|
| CA1    | 1    |
| CA35   | 35   |



 

## Tables used during execution

[AdvtExecuteSequence Table](advtexecutesequence-table.md)

[CustomAction Table](customaction-table.md)

## Related topics

<dl> <dt>

[Custom Action Type 19](custom-action-type-19.md)
</dt> <dt>

[Custom Action Type 35](custom-action-type-35.md)
</dt> <dt>

[Custom Action Type 51](custom-action-type-51.md)
</dt> <dt>

[ICE Reference](ice-reference.md)
</dt> </dl>

 

 



