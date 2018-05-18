---
Description: 'Represents the set of columns in a table in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5696941f-e294-46f9-8456-f301b4beb29c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Columns element
---

# Columns element

Represents the set of columns in a table in the report for a diagnostic test.

## Usage

``` syntax
<Columns>
  child elements
</Columns>
```

## Attributes

There are no attributes.

## Child elements



| Element                             | Description                                                                                |
|-------------------------------------|--------------------------------------------------------------------------------------------|
| [**Column**](column.md)<br/> | Represents a column in a table in the report for a diagnostic test.<br/> <br/> |



### Child element sequence

``` syntax
Column
```

## Parent elements



| Element                           | Description                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------|
| [**Table**](table.md)<br/> | Represents a table in the report for a diagnostic test. <br/> <br/> |



## Remarks

This element should appear in StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**Table**](table.md)
</dt> </dl>

 

 




