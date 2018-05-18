---
Description: 'Represents a set of rows in a table in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '586b7e5e-50e8-47ad-bb8a-518721715dfd'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Rows element
---

# Rows element

Represents a set of rows in a table in the report for a diagnostic test.

## Usage

``` syntax
<Rows>
  child elements
</Rows>
```

## Attributes

There are no attributes.

## Child elements



| Element                       | Description                                                                              |
|-------------------------------|------------------------------------------------------------------------------------------|
| [**Row**](row.md)<br/> | Represents a row in a table in the report for a diagnostic test. <br/> <br/> |



### Child element sequence

``` syntax
Row+
```

## Parent elements



| Element                           | Description                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------|
| [**Table**](table.md)<br/> | Represents a table in the report for a diagnostic test. <br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**Table**](table.md)
</dt> </dl>

 

 




