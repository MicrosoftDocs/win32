---
Description: 'Represents a set of items in a bulleted list in a report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'acbbb04d-9d9d-4952-9b27-a4a84f0c17fa'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: BulletPoints element
---

# BulletPoints element

Represents a set of items in a bulleted list in a report for a diagnostic test.

## Usage

``` syntax
<BulletPoints>
  child elements
</BulletPoints>
```

## Attributes

There are no attributes.

## Child elements



| Element                                       | Description                                                                                           |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**Information**](information.md)<br/> | Represents a single item in a bulleted list in a report for a diagnostic test.<br/> <br/> |



### Child element sequence

``` syntax
Information*
```

## Parent elements



| Element                                             | Description                                                                                                                           |
|-----------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------|
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file.<br/> <br/> |



## Remarks

This element should have child elements only for the RunStep and PostStep stages of a diagnostic test. This element should not have child elements for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




