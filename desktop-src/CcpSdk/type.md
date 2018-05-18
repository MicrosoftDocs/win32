---
Description: 'Indicates the type of information contained in an item in a bulleted list in a report for a diagnostic test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '39d3cc99-b967-4c0a-8a25-9c689897a1d2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Type element
---

# Type element

Indicates the type of information contained in an item in a bulleted list in a report for a diagnostic test.

## Usage

``` syntax
<Type/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                       | Description                                                                                           |
|-----------------------------------------------|-------------------------------------------------------------------------------------------------------|
| [**Information**](information.md)<br/> | Represents a single item in a bulleted list in a report for a diagnostic test.<br/> <br/> |



## Remarks

The content of this element can be one of the following values:

-   Information

-   Failure

-   Warning

This element should appear in the StepResult XML only for the RunStep and PostStep stages of a diagnostic test. This element should not appear in the StepResult XML for the PreStep stage.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**Information**](information.md)
</dt> </dl>

 

 




