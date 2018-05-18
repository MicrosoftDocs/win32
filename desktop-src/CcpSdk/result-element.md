---
Description: 'Describes the result of a diagnostic test, such as whether the test completed, succeeded, or failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'fbd6cba6-f13b-41d5-8f31-3b900ec66966'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Result element
---

# Result element

Describes the result of a diagnostic test, such as whether the test completed, succeeded, or failed.

## Usage

``` syntax
<Result/>
```

## Attributes

There are no attributes.

## Child elements

There are no child elements.

## Parent elements



| Element                                             | Description                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file. <br/> <br/> |



## Remarks

The content of this element can be one of the following values:

-   NoResult

-   Success

-   Warning

-   Failure

-   Complete

You should use the default value of NoResult in the StepResult XML for the PreStep stage, and use an appropriate value in the StepResult XML for the RunStep and PostStep stages.

If the **NodeName** attribute of the [**StepResult**](stepresult-element.md) element that is a parent to the **Result** element is the name of a node, the result represents the result of the diagnostic test for that node.

If the **NodeName** attribute of the [**StepResult**](stepresult-element.md) element that is a parent to the **Result** element is Summary, the result represents the result of the entire diagnostic test across all of the nodes on which it ran.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




