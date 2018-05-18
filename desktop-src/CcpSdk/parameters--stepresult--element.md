---
Description: 'Represents a set of parameters that you want to set for the RunStep stage of a diagnostic test, on one node or on all of the nodes in the test.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '05714b3b-4904-4ebf-8990-9da852a5632d'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Parameters element
---

# Parameters element

Represents a set of parameters that you want to set for the RunStep stage of a diagnostic test, on one node or on all of the nodes in the test.

## Usage

``` syntax
<Parameters>
  child elements
</Parameters>
```

## Attributes

There are no attributes.

## Child elements



| Element                                   | Description                                                                                                                                                  |
|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Parameter**](parameter.md)<br/> | Specifies the value to use for a parameter in the RunStep stage of a diagnostic test, on one node or on all of the nodes in the test.<br/> <br/> |



### Child element sequence

``` syntax
Parameter*
```

## Parent elements



| Element                                             | Description                                                                                                                                          |
|-----------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| [**Node**](node-element.md)<br/>             | Represents a node on which the RunStep stage of a diagnostic test should run, or a node on which the diagnostic test failed. <br/> <br/> |
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file. <br/> <br/>               |



## Remarks

This element should have child elements in the StepResult XML only for the PreStep stage of a diagnostic test. This element should not have child elements in the StepResult XML for the RunStep and PostStep stages.

If the **Parameters** element is a child element of a [**Node**](node-element.md) element, the parameter values that are specified by the [**Parameter**](parameter.md) elements that the **Parameters** element contains apply only to the node that corresponds to the **Node** element.

If the **Parameters** element is a child element of a [**StepResult**](stepresult-element.md) element, the parameter values that are specified by the [**Parameter**](parameter.md) elements that the **Parameters** element contains apply to all of the nodes in the test.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**Node**](node-element.md)
</dt> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




