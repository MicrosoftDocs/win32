---
Description: 'Represents a column in a table in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'e2c219fb-9d5a-480c-a8bc-888bd64a2eef'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Column element
---

# Column element

Represents a column in a table in the report for a diagnostic test.

## Usage

``` syntax
<Column/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                               | Description                                                                                          |
|---------------------------------------|------------------------------------------------------------------------------------------------------|
| [**Columns**](columns.md)<br/> | Represents the set of columns in a table in the report for a diagnostic test.<br/> <br/> |



## Remarks

This element should appear in StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in StepResult XML for the PreStep stage.

The content of this element is the text that appears as the column heading in the table.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**Columns**](columns.md)
</dt> </dl>

 

 




