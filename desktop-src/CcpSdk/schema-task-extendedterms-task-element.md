---
Description: 'Defines the application-defined extended task terms.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '429ad75c-984b-428f-bb48-49e8b6fff799'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ExtendedTerms (Task)'
---

# ExtendedTerms (Task)

Defines the application-defined extended task terms.

``` syntax
<xs:element name="ExtendedTerms"
    type="NameValueCollection1"
    maxOccurs="1"
    minOccurs="1"
    nillable="true"
 />
```

## Remarks

You must include this element as a child of the [**Task**](schema-task-element.md) element but it does not have to have any children (you do not have to specify extended terms for the task).

## Requirements



|                    |                                                  |
|--------------------|--------------------------------------------------|
| Product<br/> | Compute Cluster Pack Client Utilities<br/> |



## See also

<dl> <dt>

[Task Schema Elements](schema-task-elements.md)
</dt> </dl>

 

 




