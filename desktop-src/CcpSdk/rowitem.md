---
Description: 'Specifies the text for an individual cell in a table in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '52467f7b-27dd-4542-91ae-0cc5d2ffb4f9'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: RowItem element
---

# RowItem element

Specifies the text for an individual cell in a table in the report for a diagnostic test.

## Usage

``` syntax
<RowItem/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                           | Description                                                                                                   |
|-----------------------------------|---------------------------------------------------------------------------------------------------------------|
| [**Items**](items.md)<br/> | Represents the set of entries in a row in a table in the report for a diagnostic test.<br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**Items**](items.md)
</dt> </dl>

 

 




