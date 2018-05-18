---
Description: 'Represents a row in a table in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '663ed9fd-8e43-47a9-b69d-51a121b1b638'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Row element
---

# Row element

Represents a row in a table in the report for a diagnostic test.

## Usage

``` syntax
<Row>
  child elements
</Row>
```

## Attributes

There are no attributes.

## Child elements



| Element                           | Description                                                                                           |
|-----------------------------------|-------------------------------------------------------------------------------------------------------|
| [**Items**](items.md)<br/> | Represents a single item in a bulleted list in a report for a diagnostic test.<br/> <br/> |



### Child element sequence

``` syntax
Items
```

## Parent elements



| Element                         | Description                                                                                     |
|---------------------------------|-------------------------------------------------------------------------------------------------|
| [**Rows**](rows.md)<br/> | Represents a set of rows in a table in the report for a diagnostic test.<br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**Rows**](rows.md)
</dt> </dl>

 

 




