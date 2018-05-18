---
Description: 'Indicates the nodes on which the diagnostic test failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'cecee1b6-a051-480d-887f-4b92146bfe23'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: FailedNodes element
---

# FailedNodes element

Indicates the nodes on which the diagnostic test failed.

## Usage

``` syntax
<FailedNodes>
  child elements
</FailedNodes>
```

## Attributes

There are no attributes.

## Child elements



| Element                                 | Description                                                                    |
|-----------------------------------------|--------------------------------------------------------------------------------|
| [**Node**](node-element.md)<br/> | Represents a node on which the diagnostic test failed. <br/> <br/> |



### Child element sequence

``` syntax
Node*
```

## Parent elements



| Element                                             | Description                                                                                                                            |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------|
| [**StepResult**](stepresult-element.md)<br/> | Represents the result of a stage in a diagnostic test and serves as the root element of a StepResult XML file. <br/> <br/> |



## Remarks

This element should include child elements in the StepResult XML only for the PostStep stage of a diagnostic test. This element should not include child elements in the StepResult XML for the PreStep and RunStep stages.

If the **FailedNodes** element in a PostStepResult.xml file contains failed nodes, the command to pivot to a failed node from a test result is available in **HPC Cluster Manager**.

## Element information



|              |     |
|--------------|-----|
| Can be empty | Yes |



## See also

<dl> <dt>

[**StepResult**](stepresult-element.md)
</dt> </dl>

 

 




