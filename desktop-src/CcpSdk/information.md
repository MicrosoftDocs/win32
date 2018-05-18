---
Description: 'Represents a single item in a bulleted list in a report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '02de21e8-ec70-41f6-a17a-27fec4a5f81e'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Information element
---

# Information element

Represents a single item in a bulleted list in a report for a diagnostic test.

## Usage

``` syntax
<Information>
  child elements
</Information>
```

## Attributes

There are no attributes.

## Child elements



| Element                                        | Description                                                                                                                                 |
|------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------|
| [**Message**](message--element.md)<br/> | Contains the text of an item in a bulleted list. <br/> <br/>                                                                    |
| [**Type**](type.md)<br/>                | Indicates the type of information that is contained in an item in a bulleted list in a report for a diagnostic test.<br/> <br/> |



### Child element sequence

``` syntax
TypeMessage
```

## Parent elements



| Element                                                 | Description                                                                                             |
|---------------------------------------------------------|---------------------------------------------------------------------------------------------------------|
| [**BulletPoints**](bulletpoints-element.md)<br/> | Represents a set of items in a bulleted list in a report for a diagnostic test. <br/> <br/> |



## Remarks

This element should appear in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**BulletPoints**](bulletpoints-element.md)
</dt> </dl>

 

 




