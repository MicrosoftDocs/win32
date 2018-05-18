---
Description: 'Indicates the nodes on which the RunStep stage of the diagnostic test should run.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'b46ac27f-5cce-470f-8a0f-a45bbda6aca2'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Nodes element
---

# Nodes element

Indicates the nodes on which the RunStep stage of the diagnostic test should run.

## Usage

``` syntax
<Nodes>
  child elements
</Nodes>
```

## Attributes

There are no attributes.

## Child elements



| Element                                 | Description                                                                                                                                          |
|-----------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Node**](node-element.md)<br/> | Represents a node on which the RunStep stage of a diagnostic test should run, or a node on which the diagnostic test failed. <br/> <br/> |



### Child element sequence

``` syntax
Node*
```

## Parent elements



| Element                                             | Description                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file. <br/> <br/> |



## Remarks

This element should contain child elements in the StepResult XML only for the PreStep stage of a diagnostic test. This element should not contain child elements in the StepResult XML for the RunStep and PostStep stages.

If you want the RunStep stage of the diagnostic test to run on all of the nodes that the user specified when starting the test, include in the PreStepResult.xml file a **Nodes** element that has child [**Node**](node-element.md) elements for all of the nodes that the user specified, or do not include the **Nodes** element at all. If you include an empty **Nodes** element, the test fails.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




