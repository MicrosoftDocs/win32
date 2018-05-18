---
Description: 'Represents the set of tables in the report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '3864f4ac-5f20-48b4-afe2-41c941a7a6b8'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Tables element
---

# Tables element

Represents the set of tables in the report for a diagnostic test.

## Usage

``` syntax
<Tables>
  child elements
</Tables>
```

## Attributes

There are no attributes.

## Child elements



| Element                           | Description                                                                     |
|-----------------------------------|---------------------------------------------------------------------------------|
| [**Table**](table.md)<br/> | Represents a table in the report for a diagnostic test. <br/> <br/> |



### Child element sequence

``` syntax
Table*
```

## Parent elements



| Element                                             | Description                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file. <br/> <br/> |



## Remarks

This element should have child elements in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not have child elements in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




