---
Description: 'Represents a node on which the RunStep stage of a diagnostic test should run, or a node on which the diagnostic test failed.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '2b6776e7-4982-4e32-acdb-2865db6f4ea6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: Node element
---

# Node element

Represents a node on which the RunStep stage of a diagnostic test should run, or a node on which the diagnostic test failed.

## Usage

``` syntax
<Node>
  child elements
</Node>
```

## Attributes

There are no attributes.

## Child elements



| Element                                                          | Description                                                                                                    |
|------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| [**Parameters**](parameters--stepresult--element.md)<br/> | Specifies the set of parameters that you want to set for the RunStep stage on the node.<br/> <br/> |



### Child element sequence

``` syntax
Parameters
```

## Parent elements



| Element                                               | Description                                                                                              |
|-------------------------------------------------------|----------------------------------------------------------------------------------------------------------|
| [**FailedNodes**](failednodes-element.md)<br/> | Indicates the nodes on which the diagnostic test failed.<br/> <br/>                          |
| [**Nodes**](nodes-element.md)<br/>             | Indicates the nodes on which the RunStep stage of the diagnostic test should run.<br/> <br/> |



## Remarks

This element should appear as a child element of the [**Nodes**](nodes-element.md) element in the StepResult XML only for the PreStep stage of a diagnostic test. This element should not appear as a child element of the **Nodes** element in the StepResult XML for the RunStep and PostStep stages.

This element should appear as a child element of the [**FailedNodes**](failednodes-element.md) element in the StepResult XML only for the PostStep stage of a diagnostic test. This element should not appear as a child element of the **FailedNodes** element in the StepResult XML for the PreStep and RunStep stages.

## Element information



|              |     |
|--------------|-----|
| Can be empty | No  |



## See also

<dl> <dt>

[**FailedNodes**](failednodes-element.md)
</dt> <dt>

[**Nodes**](nodes-element.md)
</dt> </dl>

 

 




