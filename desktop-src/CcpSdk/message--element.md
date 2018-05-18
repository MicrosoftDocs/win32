---
Description: 'Contains the text of an item in a bulleted list.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'd3346e35-804e-4355-9e75-2eb5bf58e409'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Message element
---

# Message element

Contains the text of an item in a bulleted list.

## Usage

``` syntax
<Message/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                             | Description                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**Information**](information.md)<br/>       | Represents a single item in a bulleted list in a report for a diagnostic test.<br/> <br/>                                  |
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file. <br/> <br/> |



## Remarks

This element should appear as a child element of the [**Information**](information.md) element in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear as a child element of the **Information** element in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**Information**](information.md)
</dt> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




