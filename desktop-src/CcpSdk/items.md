---
Description: 'Represents the set of entries in a row in a table in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b7cf5ee6-e681-4b01-bfd3-f94e0566ce0c'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Items element
---

# Items element

Represents the set of entries in a row in a table in the report for a diagnostic test.

## Usage

``` syntax
<Items>
  child elements
</Items>
```

## Attributes

There are no attributes.

## Child elements



| Element                               | Description                                                                                                      |
|---------------------------------------|------------------------------------------------------------------------------------------------------------------|
| [**RowItem**](rowitem.md)<br/> | Specifies the text for an individual cell in a table in the report for a diagnostic test.<br/> <br/> |



### Child element sequence

``` syntax
RowItem+
```

## Parent elements



| Element                       | Description                                                                             |
|-------------------------------|-----------------------------------------------------------------------------------------|
| [**Row**](row.md)<br/> | Represents a row in a table in the report for a diagnostic test.<br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**Row**](row.md)
</dt> </dl>

 

 




