---
description: The Billboard table lists the Billboard controls displayed in the full user interface.
ms.assetid: bb8c1d7c-aa1d-43cc-9fb4-3a0ad75c4615
title: Billboard Table
ms.topic: article
ms.date: 05/31/2018
---

# Billboard Table

The Billboard table lists the [Billboard controls](billboard-control.md) displayed in the full user interface.

The Billboard table has the following columns.



| Column    | Type                         | Key | Nullable |
|-----------|------------------------------|-----|----------|
| Billboard | [Identifier](identifier.md) | Y   | N        |
| Feature\_ | [Identifier](identifier.md) | N   | N        |
| Action    | [Identifier](identifier.md) | N   | Y        |
| Ordering  | [Integer](integer.md)       | N   | Y        |



 

## Columns

<dl> <dt>

<span id="Billboard"></span><span id="billboard"></span><span id="BILLBOARD"></span>Billboard
</dt> <dd>

Name of the [Billboard control](billboard-control.md).

</dd> <dt>

<span id="Feature_"></span><span id="feature_"></span><span id="FEATURE_"></span>Feature\_
</dt> <dd>

An external key to the first column of the [Feature table](feature-table.md). The billboard is displayed only if this feature is being installed.

</dd> <dt>

<span id="Action"></span><span id="action"></span><span id="ACTION"></span>Action
</dt> <dd>

The name of an action. The billboard is displayed during the progress messages received from this action.

</dd> <dt>

<span id="Ordering"></span><span id="ordering"></span><span id="ORDERING"></span>Ordering
</dt> <dd>

If there is more than one billboard corresponding to an action, then they are displayed in the order defined by this column. This number must be non-negative.

</dd> </dl>

## Validation

<dl>

[ICE03](ice03.md)  
[ICE06](ice06.md)  
[ICE32](ice32.md)  
[ICE95](ice95.md)  
</dl>

 

 



