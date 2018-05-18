---
Description: 'Contains a collection of application-defined extended task terms.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: 'c9ed1fea-3869-4071-88e7-e974e7028bd1'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ExtendedTerms (Task)'
---

# ExtendedTerms (Task)

Contains a collection of application-defined extended task terms.

``` syntax
<xs:element name="ExtendedTerms"
    type="NameValueCollection"
    maxOccurs="1"
    minOccurs="1"
    nillable="true"
 />
```

## Remarks

You must include this element as a child of the [**Task**](schema-task-arrayoftask-element.md) element but it does not have to have any children (you do not have to specify extended terms for the task).

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Job Schema Elements](schema-job-elements.md)
</dt> </dl>

 

 




