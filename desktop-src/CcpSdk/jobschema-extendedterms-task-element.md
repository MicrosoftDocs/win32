---
Description: 'Contains a collection of extended terms that are defined for the task.'
audience: developer
author: 'REDMOND\\danlep'
manager: 'REDMOND\\timlt'
ms.assetid: '5854cc36-16e5-4dcb-a4a6-0959350267e6'
ms.prod: 'windows-server-dev'
ms.technology: 'compute-cluster-pack'
ms.tgt_platform: multiple
title: 'ExtendedTerms (Task) Element'
---

# ExtendedTerms (Task) Element

Contains a collection of extended terms that are defined for the task. All HPC implementations should use [**CustomProperties**](jobschema-customproperties-task-element.md) instead.

**Microsoft Compute Cluster Server 2003 (CSS):** This is a CSS element included for backward compatibility.

``` syntax
<xs:element name="ExtendedTerms"
    type="NameValueCollection"
 />
```

The **ExtendedTerms** element is defined by the [**Task**](jobschema-task-complextype.md) complex type.

## Requirements



|                    |                                           |
|--------------------|-------------------------------------------|
| Product<br/> | HPC Pack 2008 Client Utilities<br/> |



## See also

<dl> <dt>

**Definition context of element in schema**
</dt> <dt>

[**Task**](jobschema-task-complextype.md)
</dt> <dt>

**Possible immediate parent element in schema instance**
</dt> <dt>

[**Task (ArrayOfTask)**](jobschema-task-arrayoftask-element.md)
</dt> </dl>

 

 




